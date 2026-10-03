(()=>{"use strict";const B="حجاج",T=/\b(frappe|erpnext)\b/i,G=/\b(frappe|erpnext)\b/gi,SKIP=new Set(["SCRIPT","STYLE","TEXTAREA","INPUT","CODE","PRE"]),ATTRS=["title","placeholder","alt","aria-label"];
const fix=s=>s.replace(G,B);
const run=()=>{
if(T.test(document.title))document.title=fix(document.title);
const w=document.createTreeWalker(document.body||document.documentElement,NodeFilter.SHOW_TEXT);
let n;while((n=w.nextNode())){const p=n.parentNode;if(p&&!SKIP.has(p.nodeName)&&T.test(n.nodeValue))n.nodeValue=fix(n.nodeValue)}
ATTRS.forEach(a=>document.querySelectorAll("["+a+"]").forEach(el=>{const v=el.getAttribute(a);if(v&&T.test(v))el.setAttribute(a,fix(v))}))};
let q=false;const sched=()=>{if(q)return;q=true;requestAnimationFrame(()=>{q=false;run()})};
const start=()=>{run();new MutationObserver(sched).observe(document.documentElement,{childList:true,subtree:true,characterData:true})};
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",start,{once:true});else start()})();
