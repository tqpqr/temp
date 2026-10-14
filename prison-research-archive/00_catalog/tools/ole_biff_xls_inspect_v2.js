/* OLE Compound File / BIFF XLS forensic metadata decoder v2.
   Pure JS. Read-only; recognizes OLE 512/4096 sectors, DIFAT and FAT chains.
   BIFF sheet metadata and first 32 labelled cells per sheet.
   No claims of numerical accuracy or complete formats. */
(function(){
const alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
function b64(s){let a=[],v=0,n=0;for(let c of s.replace(/\s/g,"")){if(c==="=")break;let k=alphabet.indexOf(c);if(k<0)throw Error("invalid base64");v=v<<6|k;n+=6;if(n>=8){n-=8;a.push((v>>n)&255)}}return Uint8Array.from(a)}
const u16=(b,i)=>b[i]|b[i+1]<<8, u32=(b,i)=>(b[i]|b[i+1]<<8|b[i+2]<<16|b[i+3]<<24)>>>0;
function cp(s,codepage=1251){
 let out="";for(let i=0;i<s.length;i++){let x=s[i];if(x<128)out+=String.fromCharCode(x);
 else if(codepage===1251){let dict={168:1025,184:1105,170:1028,186:1108,175:1031,191:1111,178:1030,179:1110,165:1168,180:1169,161:1038,162:1118};out+=String.fromCharCode(dict[x]|| (x>=192?x+(x<224?848:848):x));}
 else out+=String.fromCharCode(x);
 }return out}
function unicode(b,start,len){let s="";for(let i=0;i<len;i++)s+=String.fromCharCode(u16(b,start+i*2));return s}
function ole(bytes){
 const hdr=bytes;if(u32(hdr,0)!==0xe011cfd0||u32(hdr,4)!==0xe11ab1a1)throw Error("not OLE compound");
 const secSize=2**u16(hdr,30),miniSize=2**u16(hdr,32),fatNum=u32(hdr,44),dirStart=u32(hdr,48);
 if(secSize!==512&&secSize!==4096)throw Error("sector size");
 const sectors=id=>bytes.slice(512+id*secSize,512+(id+1)*secSize);
 let difat=[];for(let i=0;i<109;i++){let j=u32(hdr,76+4*i);if(j!==0xffffffff)difat.push(j)}
 let ext=u32(hdr,68),more=u32(hdr,72);
 for(let i=0;i<more&&ext!==0xfffffffe&&ext!==0xffffffff;i++){
 let a=sectors(ext);for(let j=0;j<secSize/4-1;j++){let n=u32(a,j*4);if(n!==0xffffffff)difat.push(n)}ext=u32(a,secSize-4);
 } if(difat.length<fatNum)throw Error("DIFAT underspecified");
 let fat=[];for(let j of difat.slice(0,fatNum)){let s=sectors(j);for(let i=0;i<secSize;i+=4)fat.push(u32(s,i))}
 function chain(start){let ids=[],cur=start,seen=new Set();while(cur!==0xfffffffe&&cur!==0xffffffff){if(cur>=fat.length||seen.has(cur)||ids.length>100000)throw Error("FAT chain invalid");seen.add(cur);ids.push(cur);cur=fat[cur]}return ids}
 function readStream(start,n){let list=chain(start),out=new Uint8Array(Math.min(n,list.length*secSize));let p=0;for(let id of list){let s=sectors(id);out.set(s.slice(0,Math.min(s.length,out.length-p)),p);p+=Math.min(s.length,out.length-p);if(p>=out.length)break}return out}
 const directory=readStream(dirStart,500000), entries=[];
 for(let i=0;i+128<=directory.length;i+=128){let len=u16(directory,i+64),type=directory[i+66];if(!type||len<2)continue;
 let name=unicode(directory,i,(len-2)/2),start=u32(directory,i+116),size=u32(directory,i+120);
 entries.push({name,type,start,size});}
 const workbook=entries.find(x=>/^(Workbook|Book)$/i.test(x.name));
 if(!workbook)throw Error("no Workbook directory stream; entries: "+entries.map(x=>x.name).join(","));
 if(workbook.size<4096)throw Error("mini workbook stream not implemented");
 return {stream:readStream(workbook.start,workbook.size),entries,secSize,miniSize}
}
function extract(b,limit=30){
const ol=ole(b),d=ol.stream,sheets=[],statistics={records:0,globalRecordTypes:{},sheetRecordTypes:{}},boundaries=[];
let pos=0,codepage=1251,sst=[],records=[];
while(pos+4<=d.length){const typ=u16(d,pos),len=u16(d,pos+2),start=pos+4,end=start+len;if(end>d.length)break;
 records.push({type:typ,off:pos,p:start,q:end});
 statistics.records++;
 if(typ===0x0042&&len>=2)codepage=u16(d,start);
 if(typ===0x0085&&len>=8){let off=u32(d,start),st=d[start+5],n=d[start+6],flags=d[start+7],nm=flags&1?unicode(d,start+8,n):cp(d.slice(start+8,start+8+n),codepage);sheets.push({name:nm,offset:off,sheetType:st,rows:0,usedMinRow:null,usedMaxRow:null,labels:[],seenCells:0});}
 pos=end;
}
 // Simple BIFF8 SST decoder. Most source strings are compact, may span CONTINUE records;
 // link continuous raw payloads only when strings are intact.
const srIndex=records.findIndex(x=>x.type===0x00fc);
let expectedSST=null;
if(srIndex>=0){
 let pieces=[d.slice(records[srIndex].p,records[srIndex].q)];
 for(let j=srIndex+1;j<records.length&&records[j].type===0x003c;j++)pieces.push(d.slice(records[j].p,records[j].q));
 let seg=0,off=0;
 function next(){if(++seg>=pieces.length)throw Error("SST continuation exhausted");off=0}
 function one(){if(off>=pieces[seg].length)next();return pieces[seg][off++]}
 function two(){let a=one();return a|one()<<8}
 function four(){let a=two();return (a|two()<<16)>>>0}
 function skip(n){while(n--){one()}}
 function getChars(n,wide){
  let s="";
  while(n>0){
   if(off>=pieces[seg].length){next();wide=(one()&1)!==0}
   let avail=pieces[seg].length-off;
   if(wide){
    let take=Math.min(n,Math.floor(avail/2));
    if(!take){next();wide=(one()&1)!==0;continue}
    for(let j=0;j<take;j++)s+=String.fromCharCode(two());n-=take;
   }else{
    let take=Math.min(n,avail);
    for(let j=0;j<take;j++)s+=cp([one()],codepage);n-=take;
   }
  }
  return s;
 }
 try{
 let total=four();expectedSST=four();
 for(let i=0;i<expectedSST;i++){
  let n=two(),flag=one(),rich=(flag&8)!==0,ext=(flag&4)!==0,wide=(flag&1)!==0;
  let runs=rich?two():0,extra=ext?four():0;
  let value=getChars(n,wide);
  skip(runs*4+extra);sst.push(value);
 }
 }catch(error){statistics.sstParseError=String(error)}
}
for(const sheet of sheets){
let end=d.length;for(const o of sheets)if(o.offset>sheet.offset&&o.offset<end)end=o.offset;
let p=sheet.offset,kindCount={},firstHead=[];
while(p+4<=end){let typ=u16(d,p),len=u16(d,p+2),at=p+4,stop=at+len;if(stop>end)break;
kindCount[typ]=(kindCount[typ]||0)+1;
let row=null,col=null,label=null;
if((typ===0x00fd||typ===0x0204||typ===0x027e||typ===0x0203||typ===0x0006)&&len>=6){row=u16(d,at);col=u16(d,at+2);sheet.seenCells++;
if(typ===0x00fd&&len>=10)label=sst[u32(d,at+6)]??null;
if(typ===0x0204&&len>=8){let sl=u16(d,at+6);label=cp(d.slice(at+8,at+8+sl),codepage);}
if(row!==null){sheet.usedMinRow=sheet.usedMinRow===null?row:Math.min(sheet.usedMinRow,row);sheet.usedMaxRow=sheet.usedMaxRow===null?row:Math.max(sheet.usedMaxRow,row);}
if(label&&String(label).trim()&&sheet.labels.length<limit)sheet.labels.push({cellRow:row+1,cellCol:col+1,text:String(label).slice(0,180)});
}
if(typ===0x000a)break;
p=stop;
}
sheet.recordTypes=Object.entries(kindCount).sort((a,b)=>b[1]-a[1]).slice(0,9).map(([k,n])=>[Number(k).toString(16),n]);
}
return {sheets,codepage,cfbEntries:ol.entries.map(x=>({name:x.name,size:x.size})),sstDecoded:sst.length,sstExpected:expectedSST,parseWarning:statistics.sstParseError||"",totalRecordCount:records.length,workbookBytes:d.length}
}
return {version:"ole_biff_xls_inspect_v2",b64,ole,extract};
})()