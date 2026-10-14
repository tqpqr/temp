/* Pure-JS ODS parser, v1. This file is code-as-data; use only when source SHA verified.
 * No network, dependencies, Date assumptions, or JS runtime APIs except Uint8Array.
 * Eval as expression in a trusted ECMAScript environment: const parser = eval(source).
 */
(function() {
const alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
function fromBase64(s){let a=[],v=0,n=0;for(let c of s.replace(/\s/g,"")){if(c==="=")break;let x=alphabet.indexOf(c);if(x<0)throw Error("invalid base64");v=v<<6|x;n+=6;if(n>=8){n-=8;a.push(v>>n&255)}}return Uint8Array.from(a)}
function zipXML(d){let u=i=>d[i]|d[i+1]<<8,w=i=>(d[i]|d[i+1]<<8|d[i+2]<<16|d[i+3]<<24)>>>0;for(let i=d.length-22;i>=0;i--)if(w(i)===0x06054b50){let p=w(i+16);for(let j=0;j<u(i+10);j++){let len=w(p+20),nm=u(p+28),ex=u(p+30),co=u(p+32),o=w(p+42),name=String.fromCharCode(...d.slice(p+46,p+46+nm));if(name==="content.xml"){let st=o+30+u(o+26)+u(o+28);return{method:u(p+10),size:w(p+24),data:d.slice(st,st+len)}}p+=46+nm+ex+co}}throw Error("No content.xml")}
function inflate(src){let bit=0,out=[],rd=n=>{let x=0;for(let j=0;j<n;j++)x|=(src[bit>>3]>>(bit&7)&1)<<j,bit++;return x};function huffman(ls){let count=Array(16).fill(0),code=Array(16).fill(0),m=new Map();for(let z of ls)if(z)count[z]++;let x=0;for(let l=1;l<16;l++)x=(x+count[l-1])*2,code[l]=x;for(let i=0;i<ls.length;i++){let l=ls[i];if(!l)continue;let k=code[l]++,reverse=0;for(let j=0;j<l;j++)reverse=reverse<<1|(k>>j&1);m.set(l*65536+reverse,i)}return()=>{let x=0;for(let l=1;l<16;l++){x|=rd(1)<<(l-1);let y=m.get(l*65536+x);if(y!==undefined)return y}throw Error("invalid huffman")}}const BL=[3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258],EL=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0],BD=[1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577],ED=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13];let done=0;while(!done){done=rd(1);let type=rd(2),L,D;if(type===0){bit=(bit+7)&~7;let n=rd(16);rd(16);while(n--)out.push(rd(8));continue}if(type===1){L=Array(288).fill(8);for(let i=144;i<256;i++)L[i]=9;for(let i=256;i<280;i++)L[i]=7;for(let i=280;i<288;i++)L[i]=8;D=Array(32).fill(5)}else if(type===2){let h=rd(5)+257,d=rd(5)+1,k=rd(4)+4,order=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15],lengths=Array(19).fill(0);for(let i=0;i<k;i++)lengths[order[i]]=rd(3);let ct=huffman(lengths),v=[];while(v.length<h+d){let z=ct();if(z<16)v.push(z);else{let n=z===16?rd(2)+3:z===17?rd(3)+3:rd(7)+11,val=z===16?v.at(-1):0;while(n--)v.push(val)}}L=v.slice(0,h);D=v.slice(h)}else throw Error("reserved DEFLATE block");let lt=huffman(L),dt=huffman(D);for(;;){let z=lt();if(z<256){out.push(z);continue}if(z===256)break;let j=z-257,n=BL[j]+rd(EL[j]),k=dt(),dist=BD[k]+rd(ED[k]);if(dist>out.length)throw Error("invalid DEFLATE distance");while(n--)out.push(out[out.length-dist])}}let s="";for(let i=0;i<out.length;i+=20000)s+=String.fromCharCode(...out.slice(i,i+20000));return s}
function decode(base64){let z=zipXML(fromBase64(base64));if(z.method!==8&&z.method!==0)throw Error("unsupported zip compression");let s=z.method===8?inflate(z.data):String.fromCharCode(...z.data);if(s.length!==z.size)throw Error("uncompressed size mismatch "+s.length+" vs "+z.size);return s}
function cells(s,max=30){let a=[];for(let m of s.matchAll(/<table:table-cell\b([^>]*?)(?:\/>|>([\s\S]*?)<\/table:table-cell>)/g)){let n=+(m[1].match(/table:number-columns-repeated="(\d+)"/)?.[1]||1),v=m[1].match(/office:value="([^"]+)"/)?.[1]??[...(m[2]||"").matchAll(/<text:p[^>]*>([\s\S]*?)<\/text:p>/g)].map(x=>x[1].replace(/<[^>]+>/g,"")).join(" ");for(let i=0;i<Math.min(n,max-a.length);i++)a.push(v);if(a.length>=max)break}return a}
function tables(xml){return [...xml.matchAll(/<table:table\b[^>]*table:name="([^"]+)"/g)].map(m=>({name:m[1],start:m.index}))}
function rows(xml,name){let ts=tables(xml),tab=ts.find(x=>x.name===name);if(!tab)throw Error("missing table "+name);let part=xml.slice(tab.start,xml.indexOf("</table:table>",tab.start));return[...part.matchAll(/<table:table-row\b[^>]*>([\s\S]*?)<\/table:table-row>/g)].map((m,i)=>({number:i+1,c:cells(m[1])}))}
function prisonPopulation(xml,path){let ts=tables(xml),r=rows(xml,ts[0].name);let head=r.findIndex(x=>x.c[0]==="Prison Name"&&x.c[1]?.includes("CNA"));if(head<0)throw Error("missing prison name/CNA header");let dt=r.slice(0,head).map(x=>x.c[0]).join(" ").match(/Report Date\s*:\s*(\d{1,2})\/(\d{1,2})\/(\d{4})/i);if(!dt)throw Error("missing report date");let date=dt[3]+"-"+dt[2].padStart(2,"0")+"-"+dt[1].padStart(2,"0");let out=[];for(let x of r.slice(head+1)){let c=x.c,n=c[0]?.trim();if(!n||/^(total|all prisons|male|female|prison name|establishments)/i.test(n))continue;if(!/^\d+(\.\d+)?$/.test(c[1]||"")||!/^\d+(\.\d+)?$/.test(c[3]||""))continue;out.push([date,path,x.number,n,c[1],c[2],c[3],c[4]??""])}return out}

function zipParts(base64,names) {
const d=fromBase64(base64),want=new Set(names||[]),res={};let u=i=>d[i]|d[i+1]<<8,w=i=>(d[i]|d[i+1]<<8|d[i+2]<<16|d[i+3]<<24)>>>0;
for(let i=d.length-22;i>=0;i--){if(w(i)!==0x06054b50)continue;let at=w(i+16);
for(let j=0;j<u(i+10);j++){let method=u(at+10),z=w(at+20),plain=w(at+24),ln=u(at+28),ex=u(at+30),cm=u(at+32),off=w(at+42),name=String.fromCharCode(...d.slice(at+46,at+46+ln));at+=46+ln+ex+cm;
if(names&&!want.has(name))continue;
let begin=off+30+u(off+26)+u(off+28),slice=d.slice(begin,begin+z);
let value=method===8?inflate(slice):method===0?(()=>{let s="";for(let k=0;k<slice.length;k+=20000)s+=String.fromCharCode(...slice.slice(k,k+20000));return s})():null;
if(value===null)throw Error("unsupported ZIP method");
if(value.length!==plain)throw Error("ZIP size mismatch for "+name);
res[name]=value;
}break}return res}
function xlsxRows(worksheetXml,sharedStrings) {
let output=[];
for(let m of worksheetXml.matchAll(/<row\b([^>]*?)>([\s\S]*?)<\/row>/g)){
let at=m[1],rowNumber=+(at.match(/\br="(\d+)"/)?.[1]||0),v=[];
for(let c of m[2].matchAll(/<c\b([^>]*?)(?:\/>|>([\s\S]*?)<\/c>)/g)){
let ca=c[1],ref=ca.match(/\br="([A-Z]+)\d+"/)?.[1]||"",col=0;for(let t of ref)col=col*26+t.charCodeAt(0)-64;col--;if(col<0||col>1000)continue;
let type=ca.match(/\bt="([^"]+)"/)?.[1],raw=c[2]||"",z=raw.match(/<v>([\s\S]*?)<\/v>/)?.[1]??raw.match(/<t[^>]*>([\s\S]*?)<\/t>/)?.[1]??"";
if(type==="s")z=sharedStrings[+z]??"";v[col]=z;
}output.push({number:rowNumber,c:Array.from({length:Math.max(0,v.length)},(_,i)=>v[i]??"")})}
return output}
return{decode,tables,rows,cells,prisonPopulation,zipParts,xlsxRows,version:"uk_statistical_zip_parser_v2"};
})()