/* Reproducible, read-only catalogue of original MoJ/HMPPS prison-cost spreadsheet tables.
 * Pass existing verified ZIP/ODS helper as parser. Do not follow formula links or external sheets. */
(function(){
 function utf(s){let o="";for(let i=0;i<s.length;){let b=s.charCodeAt(i++),n;if(b<128)n=b;else if(b<224)n=(b&31)<<6|(s.charCodeAt(i++)&63);else if(b<240)n=(b&15)<<12|(s.charCodeAt(i++)&63)<<6|(s.charCodeAt(i++)&63);else n=(b&7)<<18|(s.charCodeAt(i++)&63)<<12|(s.charCodeAt(i++)&63)<<6|(s.charCodeAt(i++)&63);o+=String.fromCodePoint(n)}return o;}
 function plain(s){return s.replace(/&amp;/g,"&").replace(/&lt;/g,"<").replace(/&gt;/g,">").replace(/&quot;/g,'"').replace(/&apos;/g,"'").replace(/\s+/g," ").trim();}
 function rowSummary(rows){
 let first=rows.filter(r=>r.c.some(v=>String(v||"").trim()));
 const title=first[0]?.c.filter(x=>String(x||"").trim()).slice(0,2).map(plain).join(" | ")||"";
 let head=first.find(r=>r.c.some(x=>/Cost per|Certified Normal|Average Population|Expenditure|Function|Establishment|Table \d|Definition/i.test(String(x))))||first[1]||first[0];
 let firstNumeric=first.find(r=>r.c.filter(x=>/^\s*-?\d+(\.\d+)?\s*$/.test(String(x))).length>=2);
 return{n:rows.length,title:title.slice(0,260),header:head?.c.filter(x=>String(x).trim()).slice(0,13).map(plain).join(" | ").slice(0,550)||"",headerRow:head?.number||"",numericSample:firstNumeric?.c.filter(x=>String(x).trim()).slice(0,13).map(plain).join(" | ").slice(0,350)||"",numericSampleRow:firstNumeric?.number||""};
 }
 function index(base64,format,parser,sourcePath,sha,fy){
 const out=[];
 if(format==="ods"){
  const xml=parser.decode(base64),ts=parser.tables(xml);
  let skipped=0;
  for(let i=0;i<ts.length;i++){const t=ts[i];if(t.name.length>130||/^['"]?(?:https?:|file:|\\\\)/i.test(t.name)){skipped++;continue;}
   let rows=parser.rows(xml,t.name);if(rows.length<=1&&rows.every(r=>r.c.every(z=>!String(z).trim()))){skipped++;continue;}
   let x=rowSummary(rows);out.push({source_path:sourcePath,git_sha1:sha,fiscal_year_from_filename:fy,file_format:"ods",source_tab_no:i+1,actual_tab_name:t.name,source_rows:x.n,observed_title:x.title,observed_header:x.header,header_original_row:x.headerRow,first_numeric_record:x.numericSample,first_numeric_original_row:x.numericSampleRow,content_verified:"actual_original_sheet_XML_and_source_rows",limitations:"No formulas recalculated; external references never followed; fiscal year must match own cover and official release."});
  }
  return{rows:out,externalReferencesSkipped:skipped,totalListed:ts.length};
 }
 const names=["xl/workbook.xml","xl/sharedStrings.xml",...Array.from({length:15},(_,i)=>"xl/worksheets/sheet"+(i+1)+".xml")];
 const z=parser.zipParts(base64,names),book=utf(z["xl/workbook.xml"]||""),
  sheets=[...book.matchAll(/<sheet\b[^>]*name="([^"]+)"[^>]*>/g)].map(x=>x[1]),
  shared=utf(z["xl/sharedStrings.xml"]||""),
  stringTable=[...shared.matchAll(/<si>([\s\S]*?)<\/si>/g)].map(m=>[...m[1].matchAll(/<t[^>]*>([\s\S]*?)<\/t>/g)].map(x=>x[1]).join(""));
 for(let i=1;i<=15;i++){
  let raw=z["xl/worksheets/sheet"+i+".xml"];if(!raw)continue;
  let rows=parser.xlsxRows(utf(raw),stringTable),x=rowSummary(rows),name=sheets[i-1]||"sheet"+i;
  out.push({source_path:sourcePath,git_sha1:sha,fiscal_year_from_filename:fy,file_format:"xlsx",source_tab_no:i,actual_tab_name:name,source_rows:x.n,observed_title:x.title,observed_header:x.header,header_original_row:x.headerRow,first_numeric_record:x.numericSample,first_numeric_original_row:x.numericSampleRow,content_verified:"actual_original_sheet_XML_and_source_rows",limitations:"No formulas recalculated; external references never followed; fiscal year must match own cover and official release."});
 }
 return{rows:out,externalReferencesSkipped:0,totalListed:sheets.length}
 }
 return {index,version:"gb_cost_spreadsheet_catalog_v1"};
})()