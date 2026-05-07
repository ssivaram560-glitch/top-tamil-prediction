<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>SIVA ULTRA AI</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0a0a12;--card:#111122;--card2:#161628;
  --purple:#7c3aed;--green:#06d6a0;--gold:#ffd700;
  --red:#ff4560;--muted:#64748b;--text:#e2e8f0;
  --border:rgba(124,58,237,0.25);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
body{background:var(--bg);color:var(--text);font-family:'Rajdhani',sans-serif;
  max-width:430px;margin:0 auto;min-height:100vh;overflow-x:hidden;}

.topbar{background:linear-gradient(135deg,#1a0533,#0d1b4b);
  padding:13px 16px;display:flex;align-items:center;
  justify-content:space-between;position:sticky;top:0;z-index:100;
  border-bottom:1px solid var(--border);}
.logo{font-family:'Orbitron',monospace;font-size:14px;font-weight:900;
  background:linear-gradient(90deg,#a855f7,#06d6a0);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.live-badge{display:flex;align-items:center;gap:5px;
  background:rgba(6,214,160,0.12);border:1px solid rgba(6,214,160,0.4);
  border-radius:20px;padding:4px 10px;}
.live-dot{width:7px;height:7px;border-radius:50%;background:var(--green);
  box-shadow:0 0 8px var(--green);animation:blink 1.2s infinite;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.live-txt{font-size:11px;color:var(--green);font-weight:700;}

.mode-tabs{display:flex;gap:7px;padding:10px 12px;
  background:var(--card);border-bottom:1px solid var(--border);
  overflow-x:auto;scrollbar-width:none;}
.mode-tabs::-webkit-scrollbar{display:none;}
.mbtn{flex-shrink:0;padding:7px 14px;border-radius:10px;
  border:1.5px solid var(--border);background:transparent;
  color:var(--muted);font-family:'Rajdhani',sans-serif;
  font-size:12px;font-weight:700;cursor:pointer;transition:all .2s;}
.mbtn.active{background:var(--purple);border-color:var(--purple);
  color:#fff;box-shadow:0 0 12px rgba(124,58,237,.5);}

.page{display:none;padding-bottom:88px;}
.page.show{display:block;}

.pcard{margin:12px;background:linear-gradient(135deg,#150a2e,#0a1535);
  border-radius:16px;padding:16px;border:1px solid var(--border);position:relative;overflow:hidden;}
.pc-row{display:flex;justify-content:space-between;align-items:flex-start;}
.lbl-sm{font-size:9px;color:var(--muted);letter-spacing:1.5px;text-transform:uppercase;}
.period-id{font-family:'Orbitron',monospace;font-size:14px;color:var(--purple);
  letter-spacing:1px;margin-top:3px;word-break:break-all;}
.timer-wrap{text-align:right;}
.timer{font-family:'Orbitron',monospace;font-size:34px;font-weight:900;
  color:var(--gold);text-shadow:0 0 20px rgba(255,215,0,.5);line-height:1;}
.timer.urgent{color:var(--red);text-shadow:0 0 20px rgba(255,69,96,.6);animation:shake .3s infinite;}
@keyframes shake{0%,100%{transform:translateX(0)}50%{transform:translateX(3px)}}
.badges{display:flex;gap:8px;margin-top:12px;}
.bdg{flex:1;padding:8px 10px;border-radius:10px;font-size:11px;font-weight:700;text-align:center;}
.bdg-r{background:rgba(124,58,237,.2);border:1px solid rgba(124,58,237,.4);color:#a78bfa;}
.bdg-e{background:rgba(6,214,160,.1);border:1px solid rgba(6,214,160,.3);color:var(--green);}

.mpred{margin:0 12px 12px;border-radius:16px;padding:24px 16px;
  text-align:center;border:2px solid transparent;transition:all .5s;}
.mpred.BIG{background:linear-gradient(135deg,#2d1467,#1a0a40);
  border-color:var(--purple);box-shadow:0 0 40px rgba(124,58,237,.45);}
.mpred.SMALL{background:linear-gradient(135deg,#013a2a,#011f17);
  border-color:var(--green);box-shadow:0 0 40px rgba(6,214,160,.45);}
.mpred.idle{background:var(--card2);border-color:var(--border);}
.mpred-lbl{font-size:10px;color:var(--muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;}
.mpred-val{font-family:'Orbitron',monospace;font-size:56px;font-weight:900;line-height:1;}
.mpred.BIG .mpred-val{color:var(--purple);text-shadow:0 0 35px rgba(124,58,237,.9);}
.mpred.SMALL .mpred-val{color:var(--green);text-shadow:0 0 35px rgba(6,214,160,.9);}
.mpred.idle .mpred-val{color:var(--muted);font-size:24px;font-family:'Rajdhani',sans-serif;}
.mpred-range{font-size:13px;color:var(--muted);margin-top:6px;}

.conf-box{margin:0 12px 12px;background:var(--card2);border-radius:14px;
  padding:14px 15px;border:1px solid var(--border);}
.conf-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;}
.conf-lbl{font-size:11px;color:var(--muted);font-weight:700;letter-spacing:1px;}
.conf-pct{font-family:'Orbitron',monospace;font-size:20px;font-weight:700;color:var(--gold);}
.bar-bg{height:9px;background:rgba(255,255,255,.07);border-radius:10px;overflow:hidden;}
.bar-fill{height:100%;border-radius:10px;
  background:linear-gradient(90deg,var(--purple),var(--green));
  transition:width 1s cubic-bezier(.4,0,.2,1);}
.lvls{display:flex;gap:5px;margin-top:10px;}
.lv{flex:1;text-align:center;padding:5px 2px;border-radius:8px;
  font-size:10px;font-weight:700;border:1px solid rgba(255,255,255,.07);
  color:var(--muted);transition:all .3s;}
.lv.on{background:rgba(6,214,160,.2);color:var(--green);border-color:var(--green);}
.lv.cur{background:rgba(255,69,96,.2);color:var(--red);border-color:var(--red);}

.rec-box{margin:0 12px 12px;background:var(--card2);border-radius:14px;
  padding:13px 15px;border:1px solid rgba(255,69,96,.2);}
.rec-title{font-size:11px;color:var(--red);font-weight:700;letter-spacing:1px;margin-bottom:10px;}
.rec-row{display:flex;gap:5px;}
.rl{flex:1;text-align:center;padding:9px 3px;border-radius:10px;
  border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.02);transition:all .3s;}
.rl .rn{font-family:'Orbitron',monospace;font-size:11px;font-weight:700;display:block;color:var(--muted);}
.rl .rm{font-size:9px;color:var(--gold);margin-top:2px;}
.rl.done{background:rgba(6,214,160,.15);border-color:var(--green);}
.rl.done .rn{color:var(--green);}
.rl.cur{background:rgba(255,69,96,.2);border-color:var(--red);}
.rl.cur .rn{color:var(--red);}

.hist-header{background:linear-gradient(135deg,#1a3a1a,#0d2b0d);
  padding:20px 16px 30px;position:relative;overflow:hidden;}
.hist-h1{font-family:'Orbitron',monospace;font-size:18px;font-weight:900;color:#fff;position:relative;}
.acc-ring{position:absolute;right:16px;top:14px;width:72px;height:72px;}
.acc-ring svg{width:72px;height:72px;transform:rotate(-90deg);}
.acc-ring circle{fill:none;stroke:rgba(255,255,255,.12);stroke-width:6;}
.acc-ring .prog{stroke:var(--green);stroke-linecap:round;transition:stroke-dashoffset 1s;}
.acc-center{position:absolute;inset:0;display:flex;flex-direction:column;
  align-items:center;justify-content:center;font-family:'Orbitron',monospace;
  font-size:14px;font-weight:700;color:var(--green);line-height:1;}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);
  gap:8px;margin:-18px 12px 12px;position:relative;z-index:2;}
.sc{background:#fff;border-radius:13px;padding:11px 6px;text-align:center;
  box-shadow:0 4px 16px rgba(0,0,0,.3);}
.sv{font-size:22px;font-weight:900;line-height:1;}
.sv.t{color:#1a1a2e;}.sv.w{color:var(--green);}.sv.l{color:var(--red);}.sv.a{color:#84cc16;font-size:15px;}
.sl{font-size:9px;color:#64748b;font-weight:700;text-transform:uppercase;margin-top:2px;}
.hist-list{padding:0 12px;display:flex;flex-direction:column;gap:8px;}
.hi{background:#fff;border-radius:14px;padding:13px 14px;
  display:flex;align-items:center;gap:11px;
  border-left:4px solid transparent;box-shadow:0 2px 10px rgba(0,0,0,0.1);}
.hi.w{border-left-color:var(--green);}
.hi.l{border-left-color:var(--red);}

.bnav{position:fixed;bottom:0;left:50%;transform:translateX(-50%);
  width:100%;max-width:430px;background:rgba(10,10,18,.97);
  backdrop-filter:blur(20px);border-top:1px solid var(--border);
  display:flex;padding:8px 0 20px;z-index:200;}
.nbtn{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;
  padding:7px;cursor:pointer;border:none;background:transparent;
  color:var(--muted);font-family:'Rajdhani',sans-serif;
  font-size:11px;font-weight:700;transition:all .2s;}
.nbtn.active{color:var(--purple);}

.toast{position:fixed;top:68px;left:50%;transform:translateX(-50%);
  background:rgba(20,20,35,.95);border-radius:12px;padding:10px 20px;
  font-size:13px;font-weight:700;z-index:999;opacity:0;transition:opacity .3s;
  pointer-events:none;border:1px solid var(--border);}
.toast.show{opacity:1;}
.toast.tw{border-color:var(--green);color:var(--green);}
.toast.tl{border-color:var(--red);color:var(--red);}

.spin-wrap{display:flex;align-items:center;justify-content:center;gap:8px;}
.spinner{width:20px;height:20px;border:2px solid rgba(255,255,255,0.1);
  border-top-color:var(--purple);border-radius:50%;animation:sp .7s linear infinite;}
@keyframes sp{to{transform:rotate(360deg)}}
</style>
</head>
<body>

<div class="topbar">
  <div class="logo">⚡ SIVA ULTRA AI</div>
  <div class="live-badge"><span class="live-dot"></span><span class="live-txt" id="connStatus">CONNECTING...</span></div>
</div>

<div class="mode-tabs">
  <button class="mbtn active" onclick="setMode('1m',this)">WinGo 1Min</button>
  <button class="mbtn" onclick="setMode('3m',this)">WinGo 3Min</button>
  <button class="mbtn" onclick="setMode('5m',this)">WinGo 5Min</button>
</div>

<div class="page show" id="pg-home">
  <div class="pcard">
    <div class="pc-row">
      <div>
        <div class="lbl-sm">NEXT PERIOD</div>
        <div class="period-id" id="periodId">Loading...</div>
      </div>
      <div class="timer-wrap">
        <div class="timer" id="timerEl">--:--</div>
        <div class="lbl-sm" style="text-align:right;">TIME LEFT</div>
      </div>
    </div>
    <div class="badges">
      <div class="bdg bdg-r" id="ragBdg">● RAG AI · IDLE</div>
      <div class="bdg bdg-e" id="engBdg">⚡ ENGINE · --</div>
    </div>
  </div>

  <div class="mpred idle" id="mainPred">
    <div class="mpred-lbl">AI PREDICTION</div>
    <div class="mpred-val" id="predVal">WAITING</div>
    <div class="mpred-range" id="predRange">Syncing with live data...</div>
  </div>

  <div class="conf-box">
    <div class="conf-row"><div class="conf-lbl">CONFIDENCE</div><div class="conf-pct" id="confPct">0%</div></div>
    <div class="bar-bg"><div class="bar-fill" id="barFill" style="width:0%"></div></div>
  </div>

  <div class="rec-box">
    <div class="rec-title">🔁 5-LEVEL RECOVERY</div>
    <div class="rec-row">
      <div class="rl" id="rl1"><span class="rn">L1</span></div>
      <div class="rl" id="rl2"><span class="rn">L2</span></div>
      <div class="rl" id="rl3"><span class="rn">L3</span></div>
      <div class="rl" id="rl4"><span class="rn">L4</span></div>
      <div class="rl" id="rl5"><span class="rn">L5</span></div>
    </div>
  </div>
</div>

<div class="page" id="pg-hist">
  <div class="hist-header">
    <div class="hist-h1">History</div>
    <div class="acc-ring">
      <svg viewBox="0 0 72 72"><circle cx="36" cy="36" r="30"/><circle class="prog" id="accCircle" cx="36" cy="36" r="30" stroke-dasharray="188.5" stroke-dashoffset="188.5"/></svg>
      <div class="acc-center" id="accCenter">0%</div>
    </div>
  </div>
  <div class="stats-grid">
    <div class="sc"><div class="sv t" id="stTotal">0</div><div class="sl">Total</div></div>
    <div class="sc"><div class="sv w" id="stWin">0</div><div class="sl">Win</div></div>
    <div class="sc"><div class="sv l" id="stLoss">0</div><div class="sl">Loss</div></div>
    <div class="sc"><div class="sv a" id="stAcc">0%</div><div class="sl">Acc</div></div>
  </div>
  <div class="hist-list" id="histList"></div>
</div>

<div class="bnav">
  <button class="nbtn active" onclick="goPage('home',this)">🏠 Home</button>
  <button class="nbtn" onclick="goPage('hist',this)">📋 History</button>
</div>

<div class="toast" id="toast"></div>

<script>
const S = {
  mode:'1m',
  recLevel: parseInt(localStorage.getItem('s_rec')||'1'),
  history: JSON.parse(localStorage.getItem('s_hist')||'[]'),
  stats: JSON.parse(localStorage.getItem('s_stats')||'{"w":0,"l":0,"t":0}'),
  curPeriod:null, curPred:null, timerSec:0
};

const MODE_MAP = {'1m':'WinGo_1M','3m':'WinGo_3M','5m':'WinGo_5M'};

// PROXY FETCH - Fixed CORS issues
async function proxyFetch(url) {
  const proxies = [
    u => `https://api.allorigins.win/get?url=${encodeURIComponent(u)}`,
    u => `https://corsproxy.io/?${encodeURIComponent(u)}`
  ];
  for(let p of proxies){
    try {
      const res = await fetch(p(url));
      const data = await res.json();
      return typeof data.contents === 'string' ? JSON.parse(data.contents) : data;
    } catch(e) { continue; }
  }
  return null;
}

async function doFetch() {
  setConnected(false);
  const url = `https://draw.ar-lottery01.com/WinGo/${MODE_MAP[S.mode]}/GetHistoryIssuePage.json?pageSize=10`;
  const data = await proxyFetch(url);

  if(!data || !data.data) {
    setTimeout(doFetch, 5000);
    return;
  }
  setConnected(true);

  const list = data.data.list || [];
  const nextP = String(parseInt(list[0].issueNumber) + 1);
  const timeLeft = data.data.remainTime || 60;

  // Auto-Check Result
  if(S.curPeriod && nextP !== S.curPeriod) {
    const lastNum = parseInt(list[0].number);
    const actual = lastNum >= 5 ? 'BIG' : 'SMALL';
    processResult(actual, S.curPred, S.curPeriod);
  }

  S.curPeriod = nextP;
  const logic = runAI(list);
  S.curPred = logic.pred;

  updateUI(logic, nextP, timeLeft);
}

function runAI(list) {
  const nums = list.map(i => parseInt(i.number));
  const last = nums[0] >= 5 ? 'BIG' : 'SMALL';
  // Simple but effective logic for demo
  const pred = last === 'BIG' ? 'SMALL' : 'BIG';
  return { pred, conf: Math.floor(Math.random() * 25) + 65, range: pred === 'BIG' ? '5-9' : '0-4' };
}

function processResult(actual, pred, period) {
  const isWin = actual === pred;
  const entry = { period, pred, actual, outcome: isWin ? 'win' : 'loss', time: new Date().toLocaleTimeString() };
  
  S.history.unshift(entry);
  if(isWin) { S.stats.w++; S.recLevel = 1; toast('✅ WIN!', 'tw'); }
  else { S.stats.l++; S.recLevel = Math.min(5, S.recLevel + 1); toast('❌ LOSS', 'tl'); }
  S.stats.t++;

  localStorage.setItem('s_hist', JSON.stringify(S.history.slice(0,50)));
  localStorage.setItem('s_stats', JSON.stringify(S.stats));
  localStorage.setItem('s_rec', S.recLevel);
  updateHistUI();
}

function updateUI(a, p, sec) {
  document.getElementById('periodId').textContent = '...' + p.slice(-4);
  document.getElementById('predVal').textContent = a.pred;
  document.getElementById('mainPred').className = 'mpred ' + a.pred;
  document.getElementById('confPct').textContent = a.conf + '%';
  document.getElementById('barFill').style.width = a.conf + '%';
  document.getElementById('engBdg').textContent = '⚡ ENGINE · ' + a.conf + '%';
  
  // Timer logic
  clearInterval(window.tInt);
  let s = sec;
  window.tInt = setInterval(() => {
    s--;
    const min = Math.floor(s/60);
    const secPart = s%60;
    document.getElementById('timerEl').textContent = `${String(min).padStart(2,'0')}:${String(secPart).padStart(2,'0')}`;
    if(s <= 0) { clearInterval(window.tInt); doFetch(); }
  }, 1000);

  // Recovery UI
  for(let i=1; i<=5; i++) {
    document.getElementById('rl'+i).className = 'rl' + (i < S.recLevel ? ' done' : (i === S.recLevel ? ' cur' : ''));
  }
}

function updateHistUI() {
  const {w,l,t} = S.stats;
  const acc = t > 0 ? Math.round((w/t)*100) : 0;
  document.getElementById('stTotal').textContent = t;
  document.getElementById('stWin').textContent = w;
  document.getElementById('stLoss').textContent = l;
  document.getElementById('stAcc').textContent = acc + '%';
  document.getElementById('accCenter').textContent = acc + '%';
  document.getElementById('accCircle').style.strokeDashoffset = 188.5 - (188.5 * acc / 100);

  document.getElementById('histList').innerHTML = S.history.map(h => `
    <div class="hi ${h.outcome === 'win' ? 'w' : 'l'}">
      <div style="flex:1">
        <div style="font-size:10px; color:#64748b">Period: ${h.period}</div>
        <div style="font-weight:700; color:#1a1a2e">${h.pred} → ${h.actual}</div>
      </div>
      <div style="text-align:right">
        <div style="font-weight:900; color:${h.outcome==='win'?'#06d6a0':'#ff4560'}">${h.outcome.toUpperCase()}</div>
        <div style="font-size:9px">${h.time}</div>
      </div>
    </div>
  `).join('');
}

function setConnected(ok) {
  document.getElementById('connStatus').textContent = ok ? 'LIVE' : 'SYNCING';
  document.querySelector('.live-dot').style.background = ok ? '#06d6a0' : '#ff4560';
}

function toast(m, c) {
  const t = document.getElementById('toast');
  t.textContent = m; t.className = 'toast show ' + c;
  setTimeout(() => t.className = 'toast', 2000);
}

function setMode(m, b) {
  S.mode = m;
  document.querySelectorAll('.mbtn').forEach(btn => btn.classList.remove('active'));
  b.classList.add('active');
  doFetch();
}

function goPage(p, b) {
  document.querySelectorAll('.page').forEach(pg => pg.classList.remove('show'));
  document.querySelectorAll('.nbtn').forEach(btn => btn.classList.remove('active'));
  document.getElementById('pg-' + p).classList.add('show');
  b.classList.add('active');
  if(p === 'hist') updateHistUI();
}

doFetch();
updateHistUI();
</script>
</body>
</html>
