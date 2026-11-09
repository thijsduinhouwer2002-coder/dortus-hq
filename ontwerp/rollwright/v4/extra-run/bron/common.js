const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ease=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const out=x=>{x=cl(x);return 1-Math.pow(1-x,3)};
const back=x=>{x=cl(x);const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ph=(t,a,b)=>cl((t-a)/(b-a));
let seed=11;const rnd=()=>(seed=(seed*16807)%2147483647)/2147483647;
const EMB=[...Array(80)].map(()=>({x:rnd()*1280,y:rnd()*720,s:.6+rnd()*2.2,v:12+rnd()*40,w:rnd()*6.28,a:.25+rnd()*.6}));
const BUR=[...Array(60)].map(()=>({ang:rnd()*6.28,sp:200+rnd()*520,s:1+rnd()*2.8}));
// frame for label at time since click (s); before click -> 'voor'
function fr(label,since){const L=FR[label];if(since<0)return L[0][1];let f=L[0][1];for(const [m,n] of L){if(m>=0&&m<=since*1000)f=n}return f}
function embers(c,t,warm){for(const e of EMB){const y=((e.y-e.v*t*1.4)%760+760)%760-20;const x=e.x+Math.sin(t*.8+e.w)*14;
 c.fillStyle=`rgba(255,${170+e.s*20|0},90,${e.a*(.5+.5*Math.sin(t*3+e.w))*warm})`;c.beginPath();c.arc(x,y,e.s,0,7);c.fill()}}
function burst(c,t,t0,cx,cy){const d=t-t0;if(d<0||d>2.4)return;for(const b of BUR){const r=b.sp*d*(1-d*.17);
 c.fillStyle=`rgba(255,${200+b.s*15|0},110,${cl(1-d/2.4)})`;c.beginPath();c.arc(cx+Math.cos(b.ang)*r*1.5,cy+Math.sin(b.ang)*r*.85,b.s*(1.3-d*.35),0,7);c.fill()}}
function setImg(el,src){if(el.getAttribute('src')!==src)el.setAttribute('src',src)}
