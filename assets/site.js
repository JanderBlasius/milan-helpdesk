(function(){
  var b=document.body, t=document.getElementById('menuToggle'), o=document.getElementById('overlay');
  function set(open){b.classList.toggle('nav-open',open); if(t) t.setAttribute('aria-expanded',open?'true':'false');}
  if(t) t.addEventListener('click',function(){set(!b.classList.contains('nav-open'));});
  if(o) o.addEventListener('click',function(){set(false);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){set(false);lb.classList.remove('open');}});
  // aktiven Menüpunkt in Sicht rollen
  var sb=document.getElementById('sidebar'), act=document.querySelector('.nav-list a.active'); if(sb&&act){sb.scrollTop=Math.max(0,act.offsetTop-sb.clientHeight/3);}
  // Bild vergrößern
  var lb=document.createElement('div'); lb.className='lightbox'; lb.setAttribute('role','dialog'); lb.setAttribute('aria-label','Vergrößerte Ansicht');
  var li=document.createElement('img'); lb.appendChild(li); document.body.appendChild(lb);
  lb.addEventListener('click',function(){lb.classList.remove('open');});
  document.querySelectorAll('figure.shot img').forEach(function(im){
    im.addEventListener('click',function(){li.src=im.src; li.alt=im.alt; lb.classList.add('open');});
  });
  // Suche (Index kommt aus search-index.js)
  var inp=document.getElementById('navSearch'), list=document.getElementById('navList'), res=document.getElementById('searchResults');
  if(inp && window.MILAN_INDEX){
    function norm(s){return s.toLowerCase().replace(/ä/g,'ae').replace(/ö/g,'oe').replace(/ü/g,'ue').replace(/ß/g,'ss');}
    inp.addEventListener('input',function(){
      var q=norm(inp.value.trim()); if(!q){res.hidden=true;res.innerHTML='';list.hidden=false;return;}
      var words=q.split(/\s+/), hits=[];
      window.MILAN_INDEX.forEach(function(e){
        var hay=norm(e.t+' '+e.k), ok=words.every(function(w){return hay.indexOf(w)>-1;});
        if(ok){hits.push(e);}
      });
      list.hidden=true; res.hidden=false; res.innerHTML='';
      if(!hits.length){var li2=document.createElement('li');li2.textContent='Nichts gefunden. Versuch ein anderes Wort.';li2.style.cssText='padding:8px;font-size:14px;color:#5A6B80';res.appendChild(li2);return;}
      hits.slice(0,12).forEach(function(e){var l=document.createElement('li'),a=document.createElement('a');a.href=(document.body.getAttribute('data-root')||'')+e.u;a.textContent=e.n+' '+e.t;l.appendChild(a);res.appendChild(l);});
    });
  }
})();
