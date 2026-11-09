import json,collections,statistics as st,re,sys
T={'shader':'シェーダー|shader|Shader|マテリアル','aai':'撫で|なでなで|なで|nade|pat','face':'表情|FaceEmo|Face|まばたき|Blink|blendshape|ブレンドシェイプ|シェイプキー',
'opt':'軽量化|最適化|Optimiz|Compress|ポリゴン削減|Simplif','outfit':'衣装|着せ替え|きせ|Kise|服|フィット|fit|変換','camera':'カメラ|撮影|Lens|Camera|写真|自撮り',
'sleep':'睡眠|sleep|寝','hair':'髪|hair|Hair','phys':'胸|揺れ|PhysBone|PB|物理','sound':'音|Sound|SFX|ボイス|声','pose':'ポーズ|Pose|pose|姿勢',
'world':'Udon|ワールド|World|world','osc':'OSC','mesh':'メッシュ|Mesh|mesh','color':'色|カラー|Color|color|テクスチャ|Texture','eye':'目|アイ|Eye|瞳',
'dance':'ダンス|Dance|dance|踊','weapon':'銃|武器|剣|Gun|gun|Sword','light':'ライト|Light|light|ライティング','move':'移動|飛行|飛|グライダー|Fly|fly|ワープ|Loco',
'contact':'ハグ|だっこ|抱っこ|キス|Kiss|Hug|つかめる|掴|Grab|握手','menu':'メニュー|Menu|menu|ExMenu','particle':'パーティクル|Particle|エフェクト|Effect|effect',
'ma':'Modular|MA前提|MA対応|NDMF|非破壊','quest':'Quest|Android|iOS|モバイル|PC/Quest','body':'体型|身長|足|手|指|Hand|Foot','tail':'尻尾|しっぽ|耳|ケモ'}
def themes(d):
    s=d['name']+' '+' '.join(d['tags'])
    return [k for k,v in T.items() if re.search(v,s)]
def minp(d):
    pr=[p for p in d['prices'] if p is not None]; return min(pr) if pr else 0
if __name__=='__main__':
    N=[json.loads(l) for l in open('platformen/verkenner/data/booth-tools-2026-05tot09-2026-11-07.jsonl')]
    N=[d for d in N if d.get('ok') and d['published']<'2026-09']
    L=[json.loads(l) for l in open('platformen/verkenner/data/booth-top1500-likes-2026-11-09.jsonl')]
    print('nieuw (mei-aug) betaald:',sum(minp(d)>0 for d in N))
    rows=[]
    for k in T:
        nn=[d for d in N if k in themes(d) and minp(d)>0]
        if len(nn)<5: continue
        lk=[d['likes'] for d in nn]
        tp=[d for d in L if k in themes(d)]
        top=tp[0] if tp else None
        shops=len(set(d['shop'] for d in nn))
        rows.append((st.median(lk),k,len(nn),shops,sum(x>=500 for x in lk),round(st.median([minp(d) for d in nn])),len(tp), (top['likes'],top['published'][:7],minp(top),top['name'][:30]) if top else None))
    for r in sorted(rows,reverse=True): print(r)
