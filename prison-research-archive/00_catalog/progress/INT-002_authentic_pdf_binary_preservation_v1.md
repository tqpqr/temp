# INT-002 — Authentic RISE seven-page decision PDF is now preserved as original binary

**SUCCESS: true publisher PDF stored in repository, original fake PDF retained unchanged.** Completed 14 October 2026 via GitHub Actions, not by copying extracted text or re-generating a PDF.

## Authenticated source
- Issuer: Rikosseuraamuslaitos (RISE), decision `Päätös vankipaikkojen valtakunnallisesta jakautumisesta`, dated **22 November 2021**, docket **12/280/2021**.
- Public original binary URL: https://www.sttinfo.fi/data/attachments/00037/3fe38edf-552e-428d-a53c-31b19201c702.pdf . It is attached by RISE to its announcement of 1 Dec 2021 at https://www.sttinfo.fi/tiedote/69926272/vankipaikkauudistuksella-vaikutuksia-laajasti-kaikkiin-vankiloihin-erityisryhmille-perustetaan-uusia-osastoja?publisherId=2090 .

## New preserved archival original — exact bytes
- Repo path: `prison-research-archive/03_international/Finland/original_sources/RISE_Dnro_12-280-2021_decision_2021-11-22.pdf`
- **Git blob SHA-1 `8431f59ce96bfeeed99fc50a75a8e94e78a717c1`** (verified by GitHub fetch_file after writer committed).
- **File size 134230 bytes** (GitHub Contents PUT created status 201 and reported exact size).
- **SHA-256 `5937807ed705f3bf522f986e31efa753afbf093f5346ad2d5560da3a1e8aff69`** (computed by `sha256sum` on downloaded original).
- GitHub Actions run **38625475056**, result `success`: https://github.com/tqpqr/temp/actions/runs/38625475056 . The runner issued `curl --fail --location` directly to STT publisher URL, verified leading `%PDF-`, used `pypdf.PdfReader(strict=True)`, confirmed **7** original PDF pages and docket `12/280/2021` present in extracted document text. It then created the original binary in the repository via authenticated GitHub Contents PUT.
- Prior first attempt Actions run `38625323818` did download original PDF but verification stopped at missing `pdfinfo` executable; run **38625475056** fixed validation with pypdf and succeeded. Never claim failed run archived a file.

## Data custody / original source issue
- Different old repo path `space-archive/extra/stp8/Finland_Paatos_vankipaikkojen_jakautumisesta_22.11.2021.pdf` Git SHA-1 `7007835861b6ee8a6dcae8ef6624cdb5bb8c8288` is **154203-byte HTML 404 page**, NOT this true PDF. Preserved untouched as an integrity incident MB-035, now **mitigated with independently verified authentic new copy**; do not overwrite or re-label 404 as a PDF.
- Decision is a **planned prison-place allocation** founded on expected counts and 90% occupancy, **NOT observed facility capacities** (MB-036). Decision p7 lists separately named Annex 2 full capacity table, not present in the preserved seven-page main decision; recovery remains separate INT-003 dependency.

**This is direct authenticated publisher binary preservation, not a regenerated approximation.**
