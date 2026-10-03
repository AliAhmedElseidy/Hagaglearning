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
const P="/api/method/hagag_learning.private.";
const api=(m,a)=>fetch(P+m,{method:"POST",headers:{"Content-Type":"application/json","X-Frappe-CSRF-Token":window.csrf_token||""},credentials:"same-origin",body:JSON.stringify(a||{})}).then(r=>r.json());
const err=x=>{try{return JSON.parse(JSON.parse(x._server_messages)[0]).message}catch(e){return "حصل خطأ"}};
const esc=s=>String(s==null?"":s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const B="padding:8px 14px;border:0;border-radius:10px;cursor:pointer;font-weight:600;";
const on=B+"background:#f76b1c;color:#fff;",off=B+"background:#e8ecf1;color:#333;",red=B+"background:#fde8e8;color:#c0392b;";
let cur=null,btn=null,box=null;
const course=()=>{const m=location.pathname.match(/^\/lms\/courses\/([^\/]+)/);return m&&m[1]!=="new"?decodeURIComponent(m[1]):null};
const close=()=>{if(box){box.remove();box=null}};
const draw=async()=>{
const c=cur;if(!c||!box)return;
const [s,l]=await Promise.all([api("get_settings",{course:c}),api("get_students",{course:c})]);
if(!box||!s.message)return;
const st=s.message,rows=l.message||[];
box.firstChild.innerHTML=
'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px"><b style="font-size:17px">إدارة الكورس</b><button data-a="x" style="'+off+'">إغلاق</button></div>'+
'<div style="margin-bottom:10px">الظهور: <button data-a="vis" data-v="0" style="'+(st.is_private?off:on)+'">عام</button> <button data-a="vis" data-v="1" style="'+(st.is_private?on:off)+'">خاص</button></div>'+
(st.can_publish?'<div style="margin-bottom:10px">النشر: <button data-a="pub" data-v="1" style="'+(st.published?on:off)+'">منشور</button> <button data-a="pub" data-v="0" style="'+(st.published?off:on)+'">غير منشور</button></div>':'')+
'<div style="margin:14px 0 6px"><b>الطلاب ('+rows.length+')</b></div>'+
'<div style="max-height:220px;overflow:auto">'+(rows.map(r=>'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #eee"><span>'+esc(r.full_name||"")+' <small style="color:#777">'+esc(r.member)+'</small></span><button data-a="rm" data-e="'+esc(r.member)+'" style="'+red+'">إزالة</button></div>').join("")||'<div style="color:#777">لا يوجد طلاب</div>')+'</div>'+
'<div style="display:flex;gap:6px;margin-top:12px"><input id="hg-e" placeholder="إيميل الطالب" style="flex:1;padding:8px;border:1px solid #ccd;border-radius:10px"><button data-a="add" style="'+on+'">إضافة</button></div>';
};
const open=()=>{
box=document.createElement("div");
box.style.cssText="position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;padding:16px";
const card=document.createElement("div");
card.dir="rtl";
card.style.cssText="background:#fff;border-radius:18px;padding:18px;width:100%;max-width:420px;max-height:90vh;overflow:auto;color:#111";
box.appendChild(card);
box.onclick=async e=>{
if(e.target===box)return close();
const t=e.target.closest("[data-a]");if(!t)return;
const a=t.dataset.a,c=cur;let x;
if(a==="x")return close();
if(a==="vis")x=await api("set_visibility",{course:c,is_private:+t.dataset.v});
else if(a==="pub")x=await api("set_published",{course:c,published:+t.dataset.v});
else if(a==="rm"){if(!confirm("إزالة "+t.dataset.e+" من الكورس؟"))return;x=await api("remove_student",{course:c,email:t.dataset.e})}
else if(a==="add"){const v=(document.getElementById("hg-e").value||"").trim();if(!v)return;x=await api("add_student",{course:c,email:v})}
if(x&&!x.message)alert(err(x));
draw()};
document.body.appendChild(box);draw()};
const tick=async()=>{const c=course();if(c===cur)return;cur=c;close();if(btn){btn.remove();btn=null}if(!c)return;
try{const r=await api("can_manage",{course:c});if(!r.message||course()!==c)return;
btn=document.createElement("button");btn.textContent="إدارة الكورس";
btn.style.cssText="position:fixed;bottom:18px;left:18px;z-index:9999;padding:12px 18px;border:0;border-radius:12px;background:linear-gradient(135deg,#f5a623,#f76b1c);color:#fff;font-weight:600;box-shadow:0 6px 20px rgba(0,0,0,.3);cursor:pointer";
btn.onclick=open;document.body.appendChild(btn)}catch(e){}};
setInterval(tick,1000)})();
