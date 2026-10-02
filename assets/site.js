/* AMP Insurance Assistance - shared site script.
   Pages set window.SITE (contact config) and window.I18N (en/es strings) before this file loads. */
(function(){
  "use strict";
  const SITE = window.SITE || {}, I18N = window.I18N || {en:{},es:{}};
  let lang = "en";
  const $ = (s,c=document)=>c.querySelector(s);
  const $$ = (s,c=document)=>Array.from(c.querySelectorAll(s));
  const t = k => (I18N[lang] && I18N[lang][k] !== undefined) ? I18N[lang][k] : (I18N.en[k] !== undefined ? I18N.en[k] : "");
  const esc = s => String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const todayISO = (()=>{ const d=new Date(); d.setMinutes(d.getMinutes()-d.getTimezoneOffset()); return d.toISOString().slice(0,10); })();
  const thisYear = +todayISO.slice(0,4);

  /* ---------------- Contact config ---------------- */
  function applyConfig(){
    $$(".js-phone").forEach(el=> el.textContent = SITE.phoneDisplay);
    $$(".js-email").forEach(el=> el.textContent = SITE.email);
    $$(".js-tel").forEach(a=> a.href = "tel:"+String(SITE.phoneDisplay).replace(/[^\d+]/g,""));
    $$(".js-mail").forEach(a=> a.href = "mailto:"+SITE.email);
    $$(".js-ig").forEach(a=> a.href = "https://instagram.com/"+SITE.instagram);
    $$(".js-year").forEach(el=> el.textContent = new Date().getFullYear());
  }

  /* ---------------- Language ---------------- */
  function setLang(next){
    lang = I18N[next] ? next : "en";
    document.documentElement.lang = lang;
    $$("[data-i18n]").forEach(el=>{
      const v = t(el.getAttribute("data-i18n"));
      if(el.hasAttribute("data-html")) el.innerHTML = v; else el.textContent = v;
    });
    $$("[data-i18n-ph]").forEach(el=> el.setAttribute("placeholder", t(el.getAttribute("data-i18n-ph"))));
    $$("[data-i18n-aria]").forEach(el=> el.setAttribute("aria-label", t(el.getAttribute("data-i18n-aria"))));
    $$("[data-i18n-alt]").forEach(el=> el.setAttribute("alt", t(el.getAttribute("data-i18n-alt"))));
    $$("[data-lang-block]").forEach(el=> el.hidden = el.getAttribute("data-lang-block") !== lang);
    $$(".lang button").forEach(b=> b.setAttribute("aria-pressed", String(b.dataset.lang===lang)));
    if(t("meta_title")) document.title = t("meta_title");
    buildFaq(); relabelReps(); refreshWaLinks();
    if(successEl && successEl.classList.contains("show")) renderSuccess();
    try{ localStorage.setItem("amp_lang", lang); }catch(e){}
  }

  function buildFaq(){
    const list = $("#faqList"); if(!list) return;
    const open = $$("details",list).map(d=>d.open);
    list.innerHTML = "";
    (t("faq") || []).forEach((item,i)=>{
      const d = document.createElement("details"); d.className = "faq-item"; if(open[i]) d.open = true;
      d.innerHTML = '<summary>'+esc(item.q)+'<i class="ph ph-caret-down" aria-hidden="true"></i></summary><div class="ans">'+esc(item.a)+'</div>';
      list.appendChild(d);
    });
  }

  /* ---------------- Mobile menu ---------------- */
  const menuBtn = $("#menuBtn"), menuPanel = $("#menuPanel");
  function setMenu(open){
    if(!menuBtn) return;
    menuBtn.setAttribute("aria-expanded", String(open));
    menuPanel.hidden = !open;
    menuBtn.querySelector(".ph").className = "ph " + (open ? "ph-x" : "ph-list");
    menuBtn.setAttribute("data-i18n-aria", open ? "menu_close" : "menu_open");
    menuBtn.setAttribute("aria-label", t(open ? "menu_close" : "menu_open"));
  }
  if(menuBtn){
    menuBtn.addEventListener("click", ()=> setMenu(menuBtn.getAttribute("aria-expanded") !== "true"));
    $$("a", menuPanel).forEach(a=> a.addEventListener("click", ()=> setMenu(false)));
    document.addEventListener("keydown", e=>{ if(e.key==="Escape" && menuBtn.getAttribute("aria-expanded")==="true"){ setMenu(false); menuBtn.focus(); } });
    document.addEventListener("click", e=>{ if(menuBtn.getAttribute("aria-expanded")==="true" && !e.target.closest("#menuPanel,#menuBtn")) setMenu(false); });
  }

  /* ---------------- WhatsApp ---------------- */
  const waUrl = txt => "https://wa.me/"+String(SITE.whatsapp).replace(/\D/g,"")+"?text="+encodeURIComponent(txt);
  function refreshWaLinks(){ const u = waUrl(t("wa_greeting")); $$("[data-wa-link]").forEach(a=> a.href = u); }

  /* ================= QUOTE FORM ================= */
  const form = $("#quoteForm"), successEl = $("#success");

  /* ---- Repeaters (travelers, drivers, vehicles) ---- */
  let repUid = 0;
  function addRepItem(rep, focus){
    const list = $(".rep-list", rep), max = +rep.dataset.max || 10;
    if(list.children.length >= max) return;
    const id = rep.dataset.rep + "-" + (++repUid);
    const item = document.createElement("div"); item.className = "rep-item";
    item.innerHTML =
      '<div class="rep-head"><b class="rep-title"></b><button type="button" class="rep-rm"><i class="ph ph-x" aria-hidden="true"></i><span></span></button></div>' +
      $("template", rep).innerHTML.split("__ID__").join(id);
    list.appendChild(item);
    $$("[data-max-today]", item).forEach(i=> i.max = todayISO);
    applyI18nTo(item);
    item.querySelector(".rep-rm").addEventListener("click", ()=>{
      const next = item.nextElementSibling || item.previousElementSibling;
      item.remove(); relabelReps();
      if(next) next.querySelector("input").focus();
    });
    relabelReps();
    if(focus) item.querySelector("input").focus();
  }
  function applyI18nTo(root){
    $$("[data-i18n]", root).forEach(el=> el.textContent = t(el.getAttribute("data-i18n")));
    $$("[data-i18n-ph]", root).forEach(el=> el.setAttribute("placeholder", t(el.getAttribute("data-i18n-ph"))));
  }
  function relabelReps(){
    $$(".rep").forEach(rep=>{
      const items = $$(".rep-item", rep), max = +rep.dataset.max || 10;
      items.forEach((item,i)=>{
        const n = i+1;
        item.querySelector(".rep-title").textContent = t(rep.dataset.title)+" "+n;
        const rm = item.querySelector(".rep-rm");
        rm.querySelector("span").textContent = t("remove");
        rm.setAttribute("aria-label", t("remove")+": "+t(rep.dataset.title)+" "+n);
        rm.hidden = items.length === 1;
        applyI18nTo(item);
        $$(".err[data-k]", item).forEach(e=> e.textContent = t(e.dataset.k));
      });
      $(".rep-add", rep).hidden = items.length >= max;
    });
  }

  /* ---- Insurance type switching ---- */
  function currentType(){ const r = form && $('input[name="qtype"]:checked', form); return r ? r.value : ""; }
  function showType(type){
    $$(".qsec", form).forEach(sec=>{
      const on = sec.dataset.for === type;
      sec.hidden = !on; sec.disabled = !on;
    });
    $("#qcontact").hidden = !type; $("#qcontact").disabled = !type;
    $("#qsubmit").hidden = !type;
    $("#typeErr").classList.remove("show");
  }

  /* ---- Validation ---- */
  function errOf(input){ const f = input.closest(".field"); return f ? $(".err", f) : null; }
  function showErr(input, on, key){
    input.setAttribute("aria-invalid", on ? "true" : "false");
    const e = errOf(input); if(!e) return;
    if(key){ e.dataset.k = key; e.textContent = t(key); }
    e.classList.toggle("show", on);
    if(!e.id) e.id = input.id + "-err";
    if(on) input.setAttribute("aria-describedby", e.id); else input.removeAttribute("aria-describedby");
  }
  const RX = { zip:/^\d{5}$/, email:/^[^\s@]+@[^\s@]+\.[^\s@]+$/, year:/^\d{4}$/ };
  function checkInput(el){
    const v = el.value.trim(), base = el.dataset.err || "err_required";
    if(el.required && !v) return base;
    if(!v) return null;
    switch(el.dataset.v){
      case "zip": return RX.zip.test(v) ? null : "err_zip";
      case "email": return RX.email.test(v) ? null : "err_email";
      case "year": return (RX.year.test(v) && +v >= 1900 && +v <= thisYear + 1) ? null : "err_year";
      case "dob": return v > todayISO ? "err_dob_future" : (v < "1900-01-01" ? base : null);
      case "after": { const other = document.getElementById(el.dataset.after); return (other && other.value && v < other.value) ? "err_ret" : null; }
    }
    return null;
  }
  function validate(){
    let first = null;
    const mark = (el, key)=>{ showErr(el, !!key, key); if(key && !first) first = el; };
    if(!currentType()){
      $("#typeErr").classList.add("show"); first = $('input[name="qtype"]', form);
    }
    $$("input", form).forEach(el=>{
      if(el.closest("fieldset:disabled") || el.type === "radio" || el.type === "checkbox") return;
      if(el.closest(".field")) mark(el, checkInput(el));
    });
    $$(".chip-group[data-required]", form).forEach(g=>{
      if(g.closest("fieldset:disabled")) return;
      const bad = !$("input:checked", g);
      $(".err", g).classList.toggle("show", bad);
      if(bad && !first) first = $("input", g);
    });
    const c = $("#consent");
    if(!$("#qcontact").disabled){
      $("#consentErr").classList.toggle("show", !c.checked);
      if(!c.checked && !first) first = c;
    }
    if(first){ first.focus({preventScroll:true}); first.scrollIntoView({behavior:"smooth", block:"center"}); }
    return !first;
  }

  /* ---- WhatsApp message ---- */
  const fmtDate = v=>{ if(!v) return ""; const [y,m,d] = v.split("-"); return lang==="es" ? d+"/"+m+"/"+y : m+"/"+d+"/"+y; };
  const ageOn = iso=>{ const [y,m,d] = iso.split("-").map(Number), [ty,tm,td] = todayISO.split("-").map(Number);
    return ty - y - ((tm < m || (tm === m && td < d)) ? 1 : 0); };
  function valueText(el){
    const v = el.value.trim(); if(!v) return "";
    if(el.type === "date") return el.dataset.v === "dob" ? fmtDate(v)+", "+t("wa_age")+" "+ageOn(v) : fmtDate(v);
    return v;
  }
  function buildMessage(){
    const type = currentType();
    const lines = ["*"+t("wa_title_"+type)+"*", ""];
    const secs = [$('.qsec[data-for="'+type+'"]', form), $("#qcontact")];
    secs.forEach((sec, si)=>{
      if(si === 1) lines.push("");
      $$("[data-wa]", sec).forEach(node=>{
        if(node.closest(".rep-item") && !node.classList.contains("rep")) return; // handled by its repeater
        const label = t(node.dataset.wa);
        if(node.classList.contains("rep")){
          lines.push("*"+label+":*");
          $$(".rep-item", node).forEach((item,i)=>{
            const vals = $$("input", item).map(valueText).filter(Boolean);
            const txt = node.dataset.join === "space" ? vals.join(" ") : vals[0] + (vals.length > 1 ? " ("+$$("input", item).slice(1).map(inp=>{ const vt = valueText(inp); return vt ? t(inp.dataset.waLabel || "")+": "+vt : ""; }).filter(Boolean).join(", ")+")" : "");
            lines.push((i+1)+". "+txt);
          });
          lines.push("");
        } else if(node.classList.contains("chip-group")){
          const picked = $$("input:checked", node).map(i=> i.closest(".chip").textContent.trim());
          if(picked.length) lines.push("*"+label+":* "+picked.join(", "));
        } else if(node.tagName === "INPUT"){
          const vt = valueText(node);
          if(vt) lines.push("*"+label+":* "+vt);
        }
      });
    });
    return lines.join("\n").replace(/\n{3,}/g,"\n\n").trim();
  }

  function renderSuccess(){
    const msg = buildMessage();
    $("#copyBox").textContent = msg.replace(/\*/g,"");
    $("#successWa").href = waUrl(msg);
    return msg;
  }

  function initForm(){
    if(!form) return;
    $$(".rep", form).forEach(rep=>{
      $(".rep-add", rep).addEventListener("click", ()=> addRepItem(rep, true));
      addRepItem(rep, false);
    });
    $$('input[name="qtype"]', form).forEach(r=> r.addEventListener("change", ()=> showType(r.value)));
    const params = new URLSearchParams(location.search);
    const preset = params.get("type") || form.dataset.preset || "";
    const pr = preset && $('input[name="qtype"][value="'+preset+'"]', form);
    if(pr) pr.checked = true;
    showType(currentType());
    $$("[data-min-today]", form).forEach(i=> i.min = todayISO);

    form.addEventListener("input", e=>{
      const el = e.target;
      if(el.dataset && el.dataset.digits) el.value = el.value.replace(/\D/g,"").slice(0, +el.dataset.digits);
      if(el.getAttribute && el.getAttribute("aria-invalid")==="true" && !checkInput(el)) showErr(el, false);
    });
    form.addEventListener("change", e=>{
      const el = e.target;
      if(el.id === "consent" && el.checked) $("#consentErr").classList.remove("show");
      const g = el.closest(".chip-group"), ge = g && $(".err", g);
      if(ge && $("input:checked", g)) ge.classList.remove("show");
      if(el.id === "depart"){ const r = $("#ret"); if(r) r.min = el.value || todayISO; }
      if(el.type === "date" && el.getAttribute("aria-invalid")==="true" && !checkInput(el)) showErr(el, false);
    });
    form.addEventListener("submit", e=>{
      e.preventDefault();
      if(!validate()) return;
      const msg = renderSuccess();
      form.hidden = true; successEl.classList.add("show");
      successEl.scrollIntoView({behavior:"smooth", block:"start"});
      successEl.focus({preventScroll:true});
      window.open(waUrl(msg), "_blank", "noopener");
    });
    $("#editBtn").addEventListener("click", ()=>{
      successEl.classList.remove("show"); form.hidden = false;
      form.scrollIntoView({behavior:"smooth", block:"start"});
    });
    $("#copyBtn").addEventListener("click", ()=>{
      const txt = $("#copyBox").textContent, lbl = $("#copyBtn span");
      const done = ()=>{ lbl.textContent = t("s_copied"); setTimeout(()=> lbl.textContent = t("s_copy"), 1800); };
      if(navigator.clipboard && window.isSecureContext){ navigator.clipboard.writeText(txt).then(done).catch(()=>{}); }
      else { const r = document.createRange(); r.selectNodeContents($("#copyBox")); const s = getSelection(); s.removeAllRanges(); s.addRange(r); try{ document.execCommand("copy"); done(); }catch(err){} }
    });
    $$("[data-ac]", form).forEach(inp=> attachAutocomplete(inp, inp.dataset.ac === "countries" ? COUNTRIES : PLACES));
  }

  /* ---------------- Observers (no scroll listeners) ---------------- */
  function initObservers(){
    const nav = $("#nav"), mbar = $("#mbar"), heroCta = $(".hero-cta"), quote = $("#quote");
    if(!("IntersectionObserver" in window)){ $$("[data-reveal]").forEach(el=> el.classList.add("in")); return; }
    if(nav && $("#top-sentinel")) new IntersectionObserver(([e])=> nav.classList.toggle("scrolled", !e.isIntersecting)).observe($("#top-sentinel"));
    if(mbar){
      const st = { hero: !!heroCta, quote:false };
      const upd = ()=>{ const show = !st.hero && !st.quote; mbar.classList.toggle("show", show); mbar.setAttribute("aria-hidden", String(!show)); $$("a", mbar).forEach(a=> a.tabIndex = show ? 0 : -1); };
      if(heroCta) new IntersectionObserver(([e])=>{ st.hero = e.isIntersecting; upd(); }).observe(heroCta);
      if(quote) new IntersectionObserver(([e])=>{ st.quote = e.isIntersecting; upd(); }, {rootMargin:"-10% 0px -10% 0px"}).observe(quote);
      upd();
    }
    if(window.matchMedia("(prefers-reduced-motion: reduce)").matches){ $$("[data-reveal]").forEach(el=> el.classList.add("in")); return; }
    const io = new IntersectionObserver(entries=>{
      entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } });
    }, {threshold:0.12, rootMargin:"0px 0px -6% 0px"});
    $$("[data-reveal]").forEach(el=> io.observe(el));
  }

  /* ---------------- Location autocomplete (travel) ---------------- */
  const COUNTRIES = ["United States","Colombia","Venezuela","Mexico","Canada","Argentina","Peru","Chile","Ecuador","Panama","Costa Rica","Dominican Republic","Guatemala","Honduras","El Salvador","Nicaragua","Cuba","Puerto Rico","Bolivia","Paraguay","Uruguay","Brazil","Spain","Portugal","France","United Kingdom","Italy","Germany","Netherlands","Switzerland","Austria","Belgium","Ireland","Greece","Turkey","Croatia","Czech Republic","Poland","Sweden","Norway","Denmark","Iceland","Finland","Russia","Morocco","Egypt","South Africa","Kenya","Nigeria","United Arab Emirates","Qatar","Saudi Arabia","Israel","India","China","Japan","South Korea","Thailand","Vietnam","Singapore","Malaysia","Indonesia","Philippines","Australia","New Zealand","Jamaica","Bahamas","Barbados","Trinidad and Tobago","Aruba","Curaçao","Belize"];
  const CITIES = ["Miami, United States","Orlando, United States","Fort Lauderdale, United States","Tampa, United States","Jacksonville, United States","New York, United States","Los Angeles, United States","Chicago, United States","Houston, United States","Dallas, United States","Atlanta, United States","Boston, United States","Washington, United States","Las Vegas, United States","San Francisco, United States","Seattle, United States","Philadelphia, United States","Phoenix, United States","Denver, United States","San Diego, United States","Bogotá, Colombia","Medellín, Colombia","Cali, Colombia","Cartagena, Colombia","Barranquilla, Colombia","Bucaramanga, Colombia","Pereira, Colombia","Santa Marta, Colombia","Cúcuta, Colombia","Caracas, Venezuela","Maracaibo, Venezuela","Valencia, Venezuela","Barquisimeto, Venezuela","Mexico City, Mexico","Cancún, Mexico","Guadalajara, Mexico","Monterrey, Mexico","Tijuana, Mexico","Playa del Carmen, Mexico","Puerto Vallarta, Mexico","Lima, Peru","Cusco, Peru","Arequipa, Peru","Buenos Aires, Argentina","Córdoba, Argentina","Mendoza, Argentina","Santiago, Chile","Valparaíso, Chile","Quito, Ecuador","Guayaquil, Ecuador","Cuenca, Ecuador","Panama City, Panama","San José, Costa Rica","Santo Domingo, Dominican Republic","Punta Cana, Dominican Republic","Puerto Plata, Dominican Republic","Guatemala City, Guatemala","San Salvador, El Salvador","Tegucigalpa, Honduras","Managua, Nicaragua","La Paz, Bolivia","Santa Cruz, Bolivia","Asunción, Paraguay","Montevideo, Uruguay","São Paulo, Brazil","Rio de Janeiro, Brazil","Brasília, Brazil","Havana, Cuba","San Juan, Puerto Rico","Nassau, Bahamas","Montego Bay, Jamaica","Kingston, Jamaica","Oranjestad, Aruba","Madrid, Spain","Barcelona, Spain","Valencia, Spain","Seville, Spain","Málaga, Spain","Lisbon, Portugal","Porto, Portugal","Paris, France","London, United Kingdom","Rome, Italy","Milan, Italy","Venice, Italy","Amsterdam, Netherlands","Berlin, Germany","Munich, Germany","Zurich, Switzerland","Vienna, Austria","Athens, Greece","Istanbul, Turkey","Dublin, Ireland","Toronto, Canada","Vancouver, Canada","Montreal, Canada","Dubai, United Arab Emirates","Doha, Qatar","Tel Aviv, Israel","Tokyo, Japan","Seoul, South Korea","Bangkok, Thailand","Singapore","Sydney, Australia","Auckland, New Zealand"];
  const PLACES = CITIES.concat(COUNTRIES);
  const acNorm = s => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"");
  function attachAutocomplete(input, source){
    const wrap = document.createElement("div"); wrap.className = "ac-wrap";
    input.parentNode.insertBefore(wrap, input); wrap.appendChild(input);
    const list = document.createElement("ul"); list.className = "ac-list"; list.id = "ac-"+input.id; list.setAttribute("role","listbox");
    wrap.appendChild(list);
    input.setAttribute("role","combobox"); input.setAttribute("aria-autocomplete","list");
    input.setAttribute("aria-expanded","false"); input.setAttribute("aria-controls", list.id); input.setAttribute("autocomplete","off");
    let items = [], active = -1, open = false;
    function render(q){
      const nq = acNorm(q.trim()); if(!nq){ close(); return; }
      const starts = [], incl = [];
      for(const p of source){ const i = acNorm(p).indexOf(nq); if(i===0) starts.push(p); else if(i>0) incl.push(p); }
      items = starts.concat(incl).slice(0,6);
      if(!items.length || (items.length===1 && items[0]===q.trim())){ close(); return; }
      list.innerHTML = items.map((p,idx)=>{
        const i = acNorm(p).indexOf(nq), n = nq.length;
        return '<li role="option" id="'+list.id+'-'+idx+'" data-v="'+esc(p)+'"><i class="ph ph-map-pin" aria-hidden="true"></i><span>'+esc(p.slice(0,i))+'<b>'+esc(p.slice(i,i+n))+'</b>'+esc(p.slice(i+n))+'</span></li>';
      }).join("");
      active = -1; open = true; list.classList.add("show"); input.setAttribute("aria-expanded","true");
    }
    function close(){ open = false; list.classList.remove("show"); list.innerHTML = ""; active = -1; input.setAttribute("aria-expanded","false"); input.removeAttribute("aria-activedescendant"); }
    function highlight(){
      const lis = $$("li", list);
      lis.forEach((li,idx)=> li.classList.toggle("active", idx===active));
      if(active>=0){ input.setAttribute("aria-activedescendant", lis[active].id); lis[active].scrollIntoView({block:"nearest"}); }
    }
    function choose(v){ input.value = v; close(); if(input.getAttribute("aria-invalid")==="true") showErr(input,false); }
    input.addEventListener("input", ()=> render(input.value));
    input.addEventListener("keydown", e=>{
      if(!open) return;
      if(e.key==="ArrowDown"){ e.preventDefault(); active = Math.min(active+1, items.length-1); highlight(); }
      else if(e.key==="ArrowUp"){ e.preventDefault(); active = Math.max(active-1, 0); highlight(); }
      else if(e.key==="Enter" && active>=0){ e.preventDefault(); choose(items[active]); }
      else if(e.key==="Escape"){ close(); }
    });
    list.addEventListener("mousedown", e=>{ const li = e.target.closest("li"); if(li){ e.preventDefault(); choose(li.getAttribute("data-v")); } });
    input.addEventListener("blur", ()=> setTimeout(close, 150));
  }

  /* ---------------- Init ---------------- */
  $$(".lang button").forEach(b=> b.addEventListener("click", ()=> setLang(b.dataset.lang)));
  applyConfig();
  initForm();
  initObservers();
  let saved = "";
  try{ saved = localStorage.getItem("amp_lang") || ""; }catch(e){}
  if(!saved) saved = (navigator.language||"en").toLowerCase().startsWith("es") ? "es" : "en";
  setLang(saved);
})();
