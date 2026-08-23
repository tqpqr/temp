import argparse
from pathlib import Path
from dataclasses import dataclass, field

import cv2
import fitz
import numpy as np
import pytesseract
from pytesseract import Output


# ============================================================
# CONFIG
# ============================================================

DPI = 300

OCR_LANG = "rus+eng"
OCR_PSM = 6

MIN_HORIZONTAL_LINE = 80
MIN_VERTICAL_LINE = 80

LINE_DILATE = 2
POSITION_MERGE_TOLERANCE = 8
TABLE_COMPONENT_GAP = 20

MIN_TABLE_WIDTH = 200
MIN_TABLE_HEIGHT = 100

MIN_CELL_WIDTH = 20
MIN_CELL_HEIGHT = 15

CELL_PADDING = 5

BOUNDARY_TOLERANCE = 8
CELL_ROW_TOLERANCE = 18


# ============================================================
# DATA STRUCTURES
# ============================================================

@dataclass
class HorizontalLine:
    x1: int
    x2: int
    y: float

    @property
    def width(self):
        return self.x2 - self.x1


@dataclass
class VerticalLine:
    x: float
    y1: int
    y2: int

    @property
    def height(self):
        return self.y2 - self.y1


@dataclass
class Cell:
    row: int
    column: int

    x1: int
    y1: int
    x2: int
    y2: int

    rowspan: int = 1
    colspan: int = 1

    text: str = ""
    words: list = field(default_factory=list)


@dataclass
class Table:
    id: int

    x1: int
    y1: int
    x2: int
    y2: int

    horizontal_lines: list = field(default_factory=list)
    vertical_lines: list = field(default_factory=list)

    cells: list = field(default_factory=list)


# ============================================================
# RENDER
# ============================================================

def render_page(page):

    zoom = DPI / 72.0

    pix = page.get_pixmap(
        matrix=fitz.Matrix(zoom, zoom),
        colorspace=fitz.csRGB,
        alpha=False
    )

    img = np.frombuffer(
        pix.samples,
        dtype=np.uint8
    ).reshape(
        pix.height,
        pix.width,
        3
    )

    return cv2.cvtColor(
        img,
        cv2.COLOR_RGB2BGR
    )


# ============================================================
# LINE DETECTION
# ============================================================

def threshold_image(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    return cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )[1]


def detect_line_masks(img):

    bw = threshold_image(img)

    horizontal_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (
            MIN_HORIZONTAL_LINE,
            1
        )
    )

    vertical_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (
            1,
            MIN_VERTICAL_LINE
        )
    )

    horizontal = cv2.morphologyEx(
        bw,
        cv2.MORPH_OPEN,
        horizontal_kernel
    )

    vertical = cv2.morphologyEx(
        bw,
        cv2.MORPH_OPEN,
        vertical_kernel
    )

    if LINE_DILATE > 1:

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (
                LINE_DILATE,
                LINE_DILATE
            )
        )

        horizontal = cv2.dilate(
            horizontal,
            kernel
        )

        vertical = cv2.dilate(
            vertical,
            kernel
        )

    return horizontal, vertical


def extract_horizontal_lines(mask):

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    lines = []

    for contour in contours:

        x, y, w, h = cv2.boundingRect(
            contour
        )

        if w < MIN_HORIZONTAL_LINE:
            continue

        if h > max(
            15,
            w // 10
        ):
            continue

        lines.append(
            HorizontalLine(
                x1=x,
                x2=x + w,
                y=y + h / 2
            )
        )

    lines.sort(
        key=lambda line: (
            line.y,
            line.x1
        )
    )

    return lines


def extract_vertical_lines(mask):

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    lines = []

    for contour in contours:

        x, y, w, h = cv2.boundingRect(
            contour
        )

        if h < MIN_VERTICAL_LINE:
            continue

        if w > max(
            15,
            h // 10
        ):
            continue

        lines.append(
            VerticalLine(
                x=x + w / 2,
                y1=y,
                y2=y + h
            )
        )

    lines.sort(
        key=lambda line: (
            line.x,
            line.y1
        )
    )

    return lines


def merge_horizontal_lines(lines):

    if not lines:
        return []

    lines = sorted(
        lines,
        key=lambda line: (
            line.y,
            line.x1
        )
    )

    result = []

    for line in lines:

        if not result:
            result.append(line)
            continue

        previous = result[-1]

        same_y = (
            abs(
                line.y -
                previous.y
            )
            <= POSITION_MERGE_TOLERANCE
        )

        overlap = (
            min(
                line.x2,
                previous.x2
            )
            >=
            max(
                line.x1,
                previous.x1
            )
            - TABLE_COMPONENT_GAP
        )

        if same_y and overlap:

            result[-1] = HorizontalLine(
                x1=min(
                    previous.x1,
                    line.x1
                ),
                x2=max(
                    previous.x2,
                    line.x2
                ),
                y=(
                    previous.y +
                    line.y
                ) / 2
            )

        else:

            result.append(line)

    return result


def merge_vertical_lines(lines):

    if not lines:
        return []

    lines = sorted(
        lines,
        key=lambda line: (
            line.x,
            line.y1
        )
    )

    result = []

    for line in lines:

        if not result:
            result.append(line)
            continue

        previous = result[-1]

        same_x = (
            abs(
                line.x -
                previous.x
            )
            <= POSITION_MERGE_TOLERANCE
        )

        overlap = (
            min(
                line.y2,
                previous.y2
            )
            >=
            max(
                line.y1,
                previous.y1
            )
            - TABLE_COMPONENT_GAP
        )

        if same_x and overlap:

            result[-1] = VerticalLine(
                x=(
                    previous.x +
                    line.x
                ) / 2,
                y1=min(
                    previous.y1,
                    line.y1
                ),
                y2=max(
                    previous.y2,
                    line.y2
                )
            )

        else:

            result.append(line)

    return result


# ============================================================
# TABLE DETECTION
# ============================================================

def line_bbox_horizontal(line):

    return (
        line.x1,
        line.y - 2,
        line.x2,
        line.y + 2
    )


def line_bbox_vertical(line):

    return (
        line.x - 2,
        line.y1,
        line.x + 2,
        line.y2
    )


def boxes_close(a, b, gap):

    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b

    return not (
        ax2 + gap < bx1
        or
        bx2 + gap < ax1
        or
        ay2 + gap < by1
        or
        by2 + gap < ay1
    )


def union_find_components(
    items,
    boxes,
    gap
):

    n = len(items)

    parent = list(
        range(n)
    )

    def find(x):

        while parent[x] != x:

            parent[x] = parent[
                parent[x]
            ]

            x = parent[x]

        return x

    def union(a, b):

        ra = find(a)
        rb = find(b)

        if ra != rb:
            parent[rb] = ra

    for i in range(n):

        for j in range(
            i + 1,
            n
        ):

            if boxes_close(
                boxes[i],
                boxes[j],
                gap
            ):

                union(i, j)

    groups = {}

    for i in range(n):

        root = find(i)

        groups.setdefault(
            root,
            []
        ).append(i)

    return list(
        groups.values()
    )


def detect_table_components(
    horizontal_lines,
    vertical_lines
):

    objects = []
    boxes = []

    for line in horizontal_lines:

        objects.append(
            ("h", line)
        )

        boxes.append(
            line_bbox_horizontal(line)
        )

    for line in vertical_lines:

        objects.append(
            ("v", line)
        )

        boxes.append(
            line_bbox_vertical(line)
        )

    if not objects:
        return []

    groups = union_find_components(
        objects,
        boxes,
        TABLE_COMPONENT_GAP
    )

    tables = []

    for group in groups:

        horizontal = []
        vertical = []

        for index in group:

            kind, obj = objects[index]

            if kind == "h":
                horizontal.append(obj)
            else:
                vertical.append(obj)

        if not horizontal or not vertical:
            continue

        x1 = min(
            [
                line.x1
                for line in horizontal
            ]
            +
            [
                line.x
                for line in vertical
            ]
        )

        x2 = max(
            [
                line.x2
                for line in horizontal
            ]
            +
            [
                line.x
                for line in vertical
            ]
        )

        y1 = min(
            [
                line.y
                for line in horizontal
            ]
            +
            [
                line.y1
                for line in vertical
            ]
        )

        y2 = max(
            [
                line.y
                for line in horizontal
            ]
            +
            [
                line.y2
                for line in vertical
            ]
        )

        if (
            x2 - x1 < MIN_TABLE_WIDTH
            or
            y2 - y1 < MIN_TABLE_HEIGHT
        ):
            continue

        tables.append(
            Table(
                id=0,
                x1=int(round(x1)),
                y1=int(round(y1)),
                x2=int(round(x2)),
                y2=int(round(y2)),
                horizontal_lines=sorted(
                    horizontal,
                    key=lambda line: line.y
                ),
                vertical_lines=sorted(
                    vertical,
                    key=lambda line: line.x
                )
            )
        )

    tables.sort(
        key=lambda table: (
            table.y1,
            table.x1
        )
    )

    for number, table in enumerate(
        tables,
        1
    ):
        table.id = number

    return tables


# ============================================================
# GRID / MERGED CELLS
# ============================================================

def unique_horizontal_positions(lines):

    positions = []

    for line in sorted(
        lines,
        key=lambda line: line.y
    ):

        if not positions:

            positions.append(
                line.y
            )

        elif abs(
            line.y -
            positions[-1]
        ) > POSITION_MERGE_TOLERANCE:

            positions.append(
                line.y
            )

        else:

            positions[-1] = (
                positions[-1] +
                line.y
            ) / 2

    return positions


def unique_vertical_positions(lines):

    positions = []

    for line in sorted(
        lines,
        key=lambda line: line.x
    ):

        if not positions:

            positions.append(
                line.x
            )

        elif abs(
            line.x -
            positions[-1]
        ) > POSITION_MERGE_TOLERANCE:

            positions.append(
                line.x
            )

        else:

            positions[-1] = (
                positions[-1] +
                line.x
            ) / 2

    return positions


@dataclass
class AtomicCell:
    row: int
    column: int
    x1: int
    y1: int
    x2: int
    y2: int
    top: bool
    bottom: bool
    left: bool
    right: bool


def horizontal_covers(
    line,
    x1,
    x2
):

    return (
        line.x1
        <=
        x1 + BOUNDARY_TOLERANCE
        and
        line.x2
        >=
        x2 - BOUNDARY_TOLERANCE
    )


def vertical_covers(
    line,
    y1,
    y2
):

    return (
        line.y1
        <=
        y1 + BOUNDARY_TOLERANCE
        and
        line.y2
        >=
        y2 - BOUNDARY_TOLERANCE
    )


def has_horizontal_boundary(
    lines,
    y,
    x1,
    x2
):

    for line in lines:

        if abs(
            line.y - y
        ) <= POSITION_MERGE_TOLERANCE:

            if horizontal_covers(
                line,
                x1,
                x2
            ):
                return True

    return False


def has_vertical_boundary(
    lines,
    x,
    y1,
    y2
):

    for line in lines:

        if abs(
            line.x - x
        ) <= POSITION_MERGE_TOLERANCE:

            if vertical_covers(
                line,
                y1,
                y2
            ):
                return True

    return False


def build_atomic_grid(table):

    xs = unique_vertical_positions(
        table.vertical_lines
    )

    ys = unique_horizontal_positions(
        table.horizontal_lines
    )

    cells = []

    for row in range(
        len(ys) - 1
    ):

        y1 = int(
            round(ys[row])
        )

        y2 = int(
            round(ys[row + 1])
        )

        if y2 - y1 < MIN_CELL_HEIGHT:
            continue

        for column in range(
            len(xs) - 1
        ):

            x1 = int(
                round(xs[column])
            )

            x2 = int(
                round(xs[column + 1])
            )

            if x2 - x1 < MIN_CELL_WIDTH:
                continue

            cells.append(
                AtomicCell(
                    row=row,
                    column=column,
                    x1=x1,
                    y1=y1,
                    x2=x2,
                    y2=y2,
                    top=has_horizontal_boundary(
                        table.horizontal_lines,
                        ys[row],
                        x1,
                        x2
                    ),
                    bottom=has_horizontal_boundary(
                        table.horizontal_lines,
                        ys[row + 1],
                        x1,
                        x2
                    ),
                    left=has_vertical_boundary(
                        table.vertical_lines,
                        xs[column],
                        y1,
                        y2
                    ),
                    right=has_vertical_boundary(
                        table.vertical_lines,
                        xs[column + 1],
                        y1,
                        y2
                    )
                )
            )

    return cells


def connected_components_atomic(
    cells
):

    if not cells:
        return []

    lookup = {
        (
            cell.row,
            cell.column
        ): cell
        for cell in cells
    }

    visited = set()
    components = []

    for start in cells:

        start_key = (
            start.row,
            start.column
        )

        if start_key in visited:
            continue

        stack = [start]
        visited.add(start_key)

        component = []

        while stack:

            current = stack.pop()

            component.append(
                current
            )

            r = current.row
            c = current.column

            neighbours = [
                (
                    r,
                    c + 1,
                    not current.right
                ),
                (
                    r,
                    c - 1,
                    not current.left
                ),
                (
                    r + 1,
                    c,
                    not current.bottom
                ),
                (
                    r - 1,
                    c,
                    not current.top
                ),
            ]

            for nr, nc, can_join in neighbours:

                if not can_join:
                    continue

                neighbour = lookup.get(
                    (
                        nr,
                        nc
                    )
                )

                if neighbour is None:
                    continue

                key = (
                    nr,
                    nc
                )

                if key in visited:
                    continue

                visited.add(key)
                stack.append(neighbour)

        components.append(
            component
        )

    return components


def build_real_cells(table):

    atomic_cells = build_atomic_grid(
        table
    )

    components = connected_components_atomic(
        atomic_cells
    )

    components.sort(
        key=lambda component: (
            min(
                c.row
                for c in component
            ),
            min(
                c.column
                for c in component
            )
        )
    )

    real_cells = []

    for component in components:

        min_row = min(
            c.row
            for c in component
        )

        max_row = max(
            c.row
            for c in component
        )

        min_col = min(
            c.column
            for c in component
        )

        max_col = max(
            c.column
            for c in component
        )

        real_cells.append(
            Cell(
                row=min_row + 1,
                column=min_col + 1,
                x1=min(
                    c.x1
                    for c in component
                ),
                y1=min(
                    c.y1
                    for c in component
                ),
                x2=max(
                    c.x2
                    for c in component
                ),
                y2=max(
                    c.y2
                    for c in component
                ),
                rowspan=(
                    max_row -
                    min_row +
                    1
                ),
                colspan=(
                    max_col -
                    min_col +
                    1
                )
            )
        )

    real_cells.sort(
        key=lambda cell: (
            cell.y1,
            cell.x1
        )
    )

    # Renumber visual rows / columns.
    current_row_y = None
    row_number = 0
    rows = {}

    for cell in real_cells:

        if (
            current_row_y is None
            or
            abs(
                cell.y1 -
                current_row_y
            ) > POSITION_MERGE_TOLERANCE
        ):

            row_number += 1
            current_row_y = cell.y1

        cell.row = row_number

        rows.setdefault(
            row_number,
            []
        ).append(cell)

    for row_cells in rows.values():

        row_cells.sort(
            key=lambda cell:
            cell.x1
        )

        for col_number, cell in enumerate(
            row_cells,
            1
        ):

            cell.column = col_number

    table.cells = real_cells

    return table


# ============================================================
# CELL OCR
# ============================================================

def clean_cell_image(
    cell_img
):

    gray = cv2.cvtColor(
        cell_img,
        cv2.COLOR_BGR2GRAY
    )

    bw = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY_INV +
        cv2.THRESH_OTSU
    )[1]

    h_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (
            max(
                20,
                cell_img.shape[1] // 4
            ),
            1
        )
    )

    v_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (
            1,
            max(
                20,
                cell_img.shape[0] // 4
            )
        )
    )

    h_lines = cv2.morphologyEx(
        bw,
        cv2.MORPH_OPEN,
        h_kernel
    )

    v_lines = cv2.morphologyEx(
        bw,
        cv2.MORPH_OPEN,
        v_kernel
    )

    lines = cv2.bitwise_or(
        h_lines,
        v_lines
    )

    result = cell_img.copy()

    result[
        lines > 0
    ] = 255

    return result


def ocr_cell(
    cell_img
):

    if cell_img.size == 0:

        return "", []

    cleaned = clean_cell_image(
        cell_img
    )

    data = pytesseract.image_to_data(
        cleaned,
        lang=OCR_LANG,
        config=(
            "--oem 3 "
            f"--psm {OCR_PSM}"
        ),
        output_type=Output.DICT
    )

    words = []

    for i in range(
        len(data["text"])
    ):

        text = (
            data["text"][i]
            .strip()
        )

        if not text:
            continue

        try:
            conf = float(
                data["conf"][i]
            )
        except Exception:
            conf = -1

        words.append(
            {
                "text": text,
                "x": int(
                    data["left"][i]
                ),
                "y": int(
                    data["top"][i]
                ),
                "w": int(
                    data["width"][i]
                ),
                "h": int(
                    data["height"][i]
                ),
                "conf": conf
            }
        )

    words.sort(
        key=lambda word: (
            word["y"] +
            word["h"] / 2,
            word["x"]
        )
    )

    lines = []

    for word in words:

        cy = (
            word["y"] +
            word["h"] / 2
        )

        found = None

        for line in lines:

            if abs(
                cy -
                line["center"]
            ) <= CELL_ROW_TOLERANCE:

                found = line
                break

        if found is None:

            lines.append({
                "center": cy,
                "words": [word]
            })

        else:

            found["words"].append(
                word
            )

            centers = [
                w["y"] +
                w["h"] / 2
                for w in found["words"]
            ]

            found["center"] = (
                sum(centers)
                /
                len(centers)
            )

    lines.sort(
        key=lambda line:
        line["center"]
    )

    text_lines = []

    for line in lines:

        line["words"].sort(
            key=lambda word:
            word["x"]
        )

        text_lines.append(
            " ".join(
                word["text"]
                for word in line["words"]
            )
        )

    return (
        "\n".join(
            text_lines
        ).strip(),
        words
    )


def ocr_table(
    img,
    table
):

    height, width = img.shape[:2]

    for cell in table.cells:

        x1 = max(
            0,
            cell.x1 + CELL_PADDING
        )

        y1 = max(
            0,
            cell.y1 + CELL_PADDING
        )

        x2 = min(
            width,
            cell.x2 - CELL_PADDING
        )

        y2 = min(
            height,
            cell.y2 - CELL_PADDING
        )

        if (
            x2 <= x1
            or
            y2 <= y1
        ):
            continue

        crop = img[
            y1:y2,
            x1:x2
        ]

        cell.text, cell.words = ocr_cell(
            crop
        )

    return table


# ============================================================
# PLAIN PAGE OCR
# ============================================================

def ocr_plain_page(img):

    data = pytesseract.image_to_data(
        img,
        lang=OCR_LANG,
        config=(
            "--oem 3 "
            f"--psm {OCR_PSM}"
        ),
        output_type=Output.DICT
    )

    words = []

    for i in range(
        len(data["text"])
    ):

        text = (
            data["text"][i]
            .strip()
        )

        if not text:
            continue

        try:
            conf = float(
                data["conf"][i]
            )
        except Exception:
            conf = -1

        words.append(
            {
                "text": text,
                "x": int(
                    data["left"][i]
                ),
                "y": int(
                    data["top"][i]
                ),
                "w": int(
                    data["width"][i]
                ),
                "h": int(
                    data["height"][i]
                ),
                "conf": conf
            }
        )

    words.sort(
        key=lambda word: (
            word["y"] +
            word["h"] / 2,
            word["x"]
        )
    )

    lines = []

    for word in words:

        cy = (
            word["y"] +
            word["h"] / 2
        )

        found = None

        for line in lines:

            if abs(
                cy -
                line["center"]
            ) <= CELL_ROW_TOLERANCE:

                found = line
                break

        if found is None:

            lines.append({
                "center": cy,
                "words": [word]
            })

        else:

            found["words"].append(
                word
            )

            centers = [
                w["y"] +
                w["h"] / 2
                for w in found["words"]
            ]

            found["center"] = (
                sum(centers)
                /
                len(centers)
            )

    lines.sort(
        key=lambda line:
        line["center"]
    )

    result = []

    for line in lines:

        line["words"].sort(
            key=lambda word:
            word["x"]
        )

        text = " ".join(
            word["text"]
            for word in line["words"]
        )

        if text.strip():
            result.append(
                text.strip()
            )

    return "\n".join(
        result
    ).strip()


# ============================================================
# DEBUG IMAGE
# ============================================================

def draw_debug_image(
    img,
    tables
):

    debug = img.copy()

    for table in tables:

        cv2.rectangle(
            debug,
            (
                table.x1,
                table.y1
            ),
            (
                table.x2,
                table.y2
            ),
            (0, 0, 255),
            4
        )

        cv2.putText(
            debug,
            f"T{table.id}",
            (
                table.x1 + 5,
                max(
                    25,
                    table.y1 - 8
                )
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )

        for cell in table.cells:

            cv2.rectangle(
                debug,
                (
                    cell.x1,
                    cell.y1
                ),
                (
                    cell.x2,
                    cell.y2
                ),
                (255, 0, 0),
                2
            )

            label = (
                f"{cell.row},"
                f"{cell.column}"
            )

            if (
                cell.rowspan > 1
                or
                cell.colspan > 1
            ):

                label += (
                    f" rs{cell.rowspan}"
                    f"xcs{cell.colspan}"
                )

            cv2.putText(
                debug,
                label,
                (
                    cell.x1 + 3,
                    cell.y1 + 20
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 0, 0),
                1,
                cv2.LINE_AA
            )

    return debug


# ============================================================
# PAGE MARKDOWN
# ============================================================

def save_table_markdown(
    f,
    table
):

    f.write(
        f"### Table {table.id}\n\n"
    )

    f.write(
        f"Geometry: "
        f"`{table.x1}, "
        f"{table.y1}, "
        f"{table.x2}, "
        f"{table.y2}`\n\n"
    )

    for cell in table.cells:

        f.write(
            f"#### Cell "
            f"{cell.row},"
            f"{cell.column}\n\n"
        )

        f.write(
            f"- bbox: "
            f"`{cell.x1}, "
            f"{cell.y1}, "
            f"{cell.x2}, "
            f"{cell.y2}`\n"
        )

        f.write(
            f"- rowspan: "
            f"{cell.rowspan}\n"
        )

        f.write(
            f"- colspan: "
            f"{cell.colspan}\n\n"
        )

        if cell.text:

            f.write(
                "```text\n"
            )

            f.write(
                cell.text
            )

            f.write(
                "\n```\n\n"
            )

        else:

            f.write(
                "_Пустая ячейка._\n\n"
            )


def build_page_markdown(
    page_number,
    tables,
    plain_text
):

    lines = []

    lines.append(
        f"## Страница {page_number}"
    )

    lines.append("")

    if not tables:

        lines.append(
            "### Текст"
        )

        lines.append("")

        if plain_text:

            lines.append(
                plain_text
            )

        else:

            lines.append(
                "_Текст не распознан._"
            )

        lines.append("")

        return "\n".join(
            lines
        )

    for table in tables:

        table_lines = []

        from io import StringIO

        buffer = StringIO()

        save_table_markdown(
            buffer,
            table
        )

        table_lines.append(
            buffer.getvalue().rstrip()
        )

        lines.extend(
            table_lines
        )

        lines.append("")

    return "\n".join(
        lines
    )


def save_markdown(
    path,
    page_number,
    tables,
    plain_text
):

    content = build_page_markdown(
        page_number,
        tables,
        plain_text
    )

    with open(
        path,
        "w",
        encoding="utf-8",
        newline="\n"
    ) as f:

        f.write(
            f"# Page {page_number}\n\n"
        )

        f.write(
            content
        )

        f.write(
            "\n"
        )


# ============================================================
# DOCUMENT MARKDOWN
# ============================================================

def append_page_to_document(
    document_file,
    page_number,
    tables,
    plain_text
):
    """
    Append one processed page to the single document.md.

    Page boundaries are deliberately preserved.
    This is important for tables continuing on the next page.
    """

    document_file.write(
        f"## Страница {page_number}\n\n"
    )

    if not tables:

        document_file.write(
            "### Текст\n\n"
        )

        if plain_text:

            document_file.write(
                plain_text
            )

            document_file.write(
                "\n\n"
            )

        else:

            document_file.write(
                "_Текст не распознан._\n\n"
            )

    else:

        for table in tables:

            save_table_markdown(
                document_file,
                table
            )

            document_file.write(
                "\n"
            )

    document_file.write(
        "---\n\n"
    )


# ============================================================
# DEBUG TEXT
# ============================================================

def save_debug_text(
    path,
    page_number,
    horizontal_lines,
    vertical_lines,
    tables,
    plain_text_used
):

    with open(
        path,
        "w",
        encoding="utf-8",
        newline="\n"
    ) as f:

        f.write(
            f"PAGE {page_number}\n"
        )

        f.write(
            "=" * 70 +
            "\n\n"
        )

        f.write(
            "HORIZONTAL LINES\n"
        )

        f.write(
            "----------------\n"
        )

        for i, line in enumerate(
            horizontal_lines,
            1
        ):

            f.write(
                f"{i:03d}: "
                f"x={line.x1}..{line.x2} "
                f"y={line.y:.1f}\n"
            )

        f.write(
            "\n"
        )

        f.write(
            "VERTICAL LINES\n"
        )

        f.write(
            "--------------\n"
        )

        for i, line in enumerate(
            vertical_lines,
            1
        ):

            f.write(
                f"{i:03d}: "
                f"x={line.x:.1f} "
                f"y={line.y1}..{line.y2}\n"
            )

        f.write(
            "\n"
        )

        f.write(
            "TABLES\n"
        )

        f.write(
            "------\n"
        )

        f.write(
            f"Detected tables: "
            f"{len(tables)}\n"
        )

        f.write(
            f"Plain OCR used: "
            f"{plain_text_used}\n\n"
        )

        for table in tables:

            f.write(
                f"TABLE {table.id}\n"
            )

            f.write(
                f"  BBOX: "
                f"{table.x1},"
                f"{table.y1},"
                f"{table.x2},"
                f"{table.y2}\n"
            )

            f.write(
                f"  CELLS: "
                f"{len(table.cells)}\n"
            )

            for cell in table.cells:

                preview = (
                    cell.text
                    .replace(
                        "\n",
                        " / "
                    )
                    .strip()
                )

                f.write(
                    f"    CELL "
                    f"{cell.row},"
                    f"{cell.column} "
                    f"bbox="
                    f"{cell.x1},"
                    f"{cell.y1},"
                    f"{cell.x2},"
                    f"{cell.y2} "
                    f"rowspan="
                    f"{cell.rowspan} "
                    f"colspan="
                    f"{cell.colspan}"
                )

                if preview:

                    f.write(
                        f" text={preview}"
                    )

                f.write(
                    "\n"
                )


# ============================================================
# PROCESS PAGE
# ============================================================

def process_page(
    page,
    page_number,
    outdir
):

    print()
    print(
        "=" * 70
    )

    print(
        f"PAGE {page_number}"
    )

    print(
        "=" * 70
    )

    # --------------------------------------------------------
    # Render
    # --------------------------------------------------------

    print(
        "Rendering..."
    )

    img = render_page(
        page
    )

    print(
        f"Image: "
        f"{img.shape[1]} x "
        f"{img.shape[0]}"
    )

    # --------------------------------------------------------
    # Detect lines
    # --------------------------------------------------------

    print(
        "Detecting lines..."
    )

    horizontal_mask, vertical_mask = (
        detect_line_masks(
            img
        )
    )

    horizontal_lines = (
        extract_horizontal_lines(
            horizontal_mask
        )
    )

    vertical_lines = (
        extract_vertical_lines(
            vertical_mask
        )
    )

    horizontal_lines = (
        merge_horizontal_lines(
            horizontal_lines
        )
    )

    vertical_lines = (
        merge_vertical_lines(
            vertical_lines
        )
    )

    print(
        f"Horizontal lines: "
        f"{len(horizontal_lines)}"
    )

    print(
        f"Vertical lines: "
        f"{len(vertical_lines)}"
    )

    # --------------------------------------------------------
    # Detect tables
    # --------------------------------------------------------

    print(
        "Detecting tables..."
    )

    tables = detect_table_components(
        horizontal_lines,
        vertical_lines
    )

    print(
        f"Tables: {len(tables)}"
    )

    page_dir = (
        outdir
        /
        f"page_{page_number:04d}"
    )

    page_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # NO TABLES
    # --------------------------------------------------------

    plain_text = None
    plain_text_used = False

    if not tables:

        print(
            "No tables detected."
        )

        print(
            "Running ordinary page OCR..."
        )

        plain_text = ocr_plain_page(
            img
        )

        plain_text_used = True

        print(
            f"OCR characters: "
            f"{len(plain_text)}"
        )

    # --------------------------------------------------------
    # TABLES
    # --------------------------------------------------------

    else:

        print(
            "Reconstructing merged cells..."
        )

        for table in tables:

            build_real_cells(
                table
            )

            print(
                f"  Table {table.id}: "
                f"{len(table.cells)} cells"
            )

        print(
            "OCR cells..."
        )

        for table in tables:

            ocr_table(
                img,
                table
            )

    # --------------------------------------------------------
    # DEBUG IMAGE
    # --------------------------------------------------------

    if tables:

        debug_image = draw_debug_image(
            img,
            tables
        )

    else:

        debug_image = img.copy()

    debug_image_path = (
        page_dir /
        "debug.png"
    )

    cv2.imwrite(
        str(debug_image_path),
        debug_image
    )

    # --------------------------------------------------------
    # CLEANED IMAGE
    # --------------------------------------------------------

    if tables:

        line_mask = cv2.bitwise_or(
            horizontal_mask,
            vertical_mask
        )

        cleaned = img.copy()

        cleaned[
            line_mask > 0
        ] = 255

    else:

        cleaned = img.copy()

    cleaned_path = (
        page_dir /
        "cleaned.png"
    )

    cv2.imwrite(
        str(cleaned_path),
        cleaned
    )

    # --------------------------------------------------------
    # PAGE MARKDOWN
    # --------------------------------------------------------

    markdown_path = (
        page_dir /
        "page.md"
    )

    save_markdown(
        markdown_path,
        page_number,
        tables,
        plain_text
    )

    # --------------------------------------------------------
    # DEBUG TEXT
    # --------------------------------------------------------

    debug_text_path = (
        page_dir /
        "debug.txt"
    )

    save_debug_text(
        debug_text_path,
        page_number,
        horizontal_lines,
        vertical_lines,
        tables,
        plain_text_used
    )

    print(
        f"Output: {page_dir}"
    )

    return {
        "page": page_number,
        "tables": tables,
        "plain_text": plain_text
    }


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Universal PDF OCR with "
            "geometric table reconstruction "
            "and plain-text OCR."
        )
    )

    parser.add_argument(
        "input",
        help="Input PDF"
    )

    parser.add_argument(
        "--page",
        type=int,
        default=None,
        help=(
            "Process one page only "
            "for testing."
        )
    )

    parser.add_argument(
        "--outdir",
        default="ocr_output",
        help="Output directory"
    )

    args = parser.parse_args()

    input_path = Path(
        args.input
    ).resolve()

    outdir = Path(
        args.outdir
    ).resolve()

    outdir.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        "=" * 70
    )

    print(
        "UNIVERSAL PDF OCR"
    )

    print(
        "=" * 70
    )

    print(
        f"Input : {input_path}"
    )

    print(
        f"Output: {outdir}"
    )

    if args.page is None:

        print(
            "Mode  : entire PDF"
        )

    else:

        print(
            f"Mode  : page {args.page}"
        )

    print()

    if not input_path.exists():

        raise FileNotFoundError(
            f"Input file not found:\n"
            f"{input_path}"
        )

    doc = fitz.open(
        str(input_path)
    )

    # --------------------------------------------------------
    # MAIN DOCUMENT MARKDOWN
    # --------------------------------------------------------

    document_md_path = (
        outdir /
        "document.md"
    )

    document_md = open(
        document_md_path,
        "w",
        encoding="utf-8",
        newline="\n"
    )

    try:

        document_md.write(
            "# OCR-документ\n\n"
        )

        document_md.write(
            f"> Страниц в PDF: "
            f"{len(doc)}\n\n"
        )

        document_md.write(
            "---\n\n"
        )

        page_count = len(
            doc
        )

        print(
            f"PDF pages: "
            f"{page_count}"
        )

        # ----------------------------------------------------
        # Page selection
        # ----------------------------------------------------

        if args.page is not None:

            if (
                args.page < 1
                or
                args.page > page_count
            ):

                raise ValueError(
                    f"Page {args.page} "
                    f"outside 1.."
                    f"{page_count}"
                )

            page_numbers = [
                args.page
            ]

        else:

            page_numbers = range(
                1,
                page_count + 1
            )

        # ----------------------------------------------------
        # Process
        # ----------------------------------------------------

        processed_pages = 0
        total_tables = 0
        total_cells = 0
        plain_pages = 0

        for page_number in page_numbers:

            result = process_page(
                doc[
                    page_number - 1
                ],
                page_number,
                outdir
            )

            processed_pages += 1

            tables = result[
                "tables"
            ]

            plain_text = result[
                "plain_text"
            ]

            total_tables += len(
                tables
            )

            total_cells += sum(
                len(
                    table.cells
                )
                for table in tables
            )

            if not tables:

                plain_pages += 1

            # --------------------------------------------
            # Append this page to the ONE document.md
            # --------------------------------------------

            append_page_to_document(
                document_md,
                page_number,
                tables,
                plain_text
            )

            # Flush periodically.
            if (
                processed_pages % 10
                == 0
            ):

                document_md.flush()

        document_md.flush()

        # ----------------------------------------------------
        # Summary
        # ----------------------------------------------------

        print()
        print(
            "=" * 70
        )

        print(
            "FINISHED"
        )

        print(
            "=" * 70
        )

        print(
            f"Processed pages : "
            f"{processed_pages}"
        )

        print(
            f"Plain-text pages: "
            f"{plain_pages}"
        )

        print(
            f"Tables detected : "
            f"{total_tables}"
        )

        print(
            f"Cells detected  : "
            f"{total_cells}"
        )

        print(
            f"Document MD     : "
            f"{document_md_path}"
        )

        print(
            f"Output          : "
            f"{outdir}"
        )

    finally:

        document_md.close()
        doc.close()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()