(()=>{"use strict";const B="Hagag",T=/\b(frappe|erpnext)\b/i,G=/\b(frappe|erpnext)\b/gi,SKIP=new Set(["SCRIPT","STYLE","TEXTAREA","INPUT","CODE","PRE"]),ATTRS=["title","placeholder","alt","aria-label"];
const fix=s=>s.replace(G,B);
const run=()=>{
if(T.test(document.title))document.title=fix(document.title);
const w=document.createTreeWalker(document.body||document.documentElement,NodeFilter.SHOW_TEXT);
let n;while((n=w.nextNode())){const p=n.parentNode;if(p&&!SKIP.has(p.nodeName)&&T.test(n.nodeValue))n.nodeValue=fix(n.nodeValue)}
ATTRS.forEach(a=>document.querySelectorAll("["+a+"]").forEach(el=>{const v=el.getAttribute(a);if(v&&T.test(v))el.setAttribute(a,fix(v))}))};
let q=false;const sched=()=>{if(q)return;q=true;requestAnimationFrame(()=>{q=false;run()})};
const start=()=>{run();new MutationObserver(sched).observe(document.documentElement,{childList:true,subtree:true,characterData:true})};
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",start,{once:true});else start()})();

(()=>{"use strict";
const api=(m,a)=>fetch("/api/method/hagag_learning.private."+m,{method:"POST",headers:{"Content-Type":"application/json","X-Frappe-CSRF-Token":window.csrf_token||""},credentials:"same-origin",body:JSON.stringify(a)}).then(r=>r.json());
let cur=null,btn=null;
const course=()=>{const m=location.pathname.match(/^\/lms\/courses\/([^\/]+)/);return m&&m[1]!=="new"?decodeURIComponent(m[1]):null};
const tick=async()=>{const c=course();if(c===cur)return;cur=c;if(btn){btn.remove();btn=null}if(!c)return;
try{const r=await api("can_manage",{course:c});if(!r.message||course()!==c)return;
btn=document.createElement("button");btn.textContent="فتح الكورس لطالب";
btn.style.cssText="position:fixed;bottom:18px;left:18px;z-index:9999;padding:12px 18px;border:0;border-radius:12px;background:linear-gradient(135deg,#f5a623,#f76b1c);color:#fff;font-weight:600;box-shadow:0 6px 20px rgba(0,0,0,.3);cursor:pointer";
btn.onclick=async()=>{const e=prompt("إيميل الطالب:");if(!e)return;const x=await api("add_student",{course:c,email:e.trim()});alert(x.message?"تم فتح الكورس للطالب":(x.exception||x._server_messages||"حصل خطأ"))};
document.body.appendChild(btn)}catch(_){}};
setInterval(tick,1000)})();
