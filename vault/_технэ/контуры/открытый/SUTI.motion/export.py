#!/usr/bin/env python3
"""Export the supported SUTI.motion subset. Standard library only."""
import html
import json
import pathlib
import sys
import shutil

ROOT = pathlib.Path(__file__).resolve().parent

def check(value, schema, path='$'):
    if 'const' in schema and value != schema['const']:
        raise ValueError(path + ': unsupported version')
    kind = schema.get('type')
    if kind:
        types = {'object': dict, 'array': list, 'string': str, 'integer': int, 'boolean': bool}
        if not isinstance(value, types[kind]) or (kind == 'integer' and isinstance(value, bool)):
            raise ValueError(path + ': incorrect type')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(path + ': unsupported value')
    if kind == 'object':
        missing = set(schema.get('required', [])) - value.keys()
        extra = value.keys() - schema.get('properties', {}).keys()
        if missing or (schema.get('additionalProperties') is False and extra):
            raise ValueError(path + ': missing or unknown fields')
        for key, item in value.items():
            check(item, schema['properties'][key], path + '.' + key)
    if kind == 'array':
        if not schema.get('minItems', 0) <= len(value) <= schema.get('maxItems', float('inf')):
            raise ValueError(path + ': array size')
        for i, item in enumerate(value):
            check(item, schema['items'], f'{path}[{i}]')
    if kind == 'integer' and not schema.get('minimum', -float('inf')) <= value <= schema.get('maximum', float('inf')):
        raise ValueError(path + ': numeric range')
    if kind == 'string':
        import re
        if not schema.get('minLength', 0) <= len(value) <= schema.get('maxLength', float('inf')):
            raise ValueError(path + ': text length')
        if 'pattern' in schema and re.search(schema['pattern'], value) is None:
            raise ValueError(path + ': invalid pattern')

def validate(data):
    schema = json.loads((ROOT / 'scene.schema.json').read_text())
    check(data, schema)
    cursor, ids = 0, set()
    for scene in data['scenes']:
        if scene['id'] in ids or scene['start_ms'] != cursor:
            raise ValueError('Scenes must have unique ids and contiguous timing')
        ids.add(scene['id'])
        if scene['motion']['duration_ms'] > scene['duration_ms'] / 2:
            raise ValueError('Transition exceeds half scene duration')
        cursor += scene['duration_ms']
    if cursor != data['duration_ms']:
        raise ValueError('Scene duration total differs from document duration')

TEMPLATE = '''<!doctype html>
<html lang="__LANG__"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;background:__BG__;color:__FG__;font-family:__FONT__}
main{width:100%;max-width:1280px;margin:auto}.stage{position:relative;aspect-ratio:__RATIO__;overflow:hidden}
.scene{position:absolute;inset:0;padding:8%;display:flex;flex-direction:column;justify-content:center;opacity:0;visibility:hidden}
.label{color:__ACCENT__;font-size:clamp(12px,2vw,24px);margin:0 0 1.5em}
h1{font-size:clamp(22px,5vw,62px);font-weight:500;line-height:1.15;max-width:20ch;margin:0 0 .65em;overflow-wrap:anywhere}
p{font-size:clamp(14px,2.3vw,28px);line-height:1.4;margin:0;max-width:45ch}
.controls{display:flex;gap:12px;padding:16px 8%}button{font:inherit;border:1px solid currentColor;border-radius:24px;background:transparent;color:inherit;padding:10px 18px;cursor:pointer}
button:focus-visible{outline:3px solid __ACCENT__;outline-offset:4px}.track{height:3px;background:__ACCENT__;transform-origin:left;transform:scaleX(0)}
.static .stage{aspect-ratio:auto}.static .scene{position:relative;opacity:1!important;visibility:visible!important;transform:none!important;border-bottom:1px solid currentColor}
.static .controls,.static .track{display:none}
@media(prefers-reduced-motion:reduce){.stage{aspect-ratio:auto}.scene{position:relative;opacity:1!important;visibility:visible!important;transform:none!important}.controls,.track{display:none}}
</style>
<main class="static" id="motion"><div class="stage" aria-label="__TITLE__">__SCENES__</div>
<div class="track" aria-hidden="true"></div><nav class="controls" aria-label="__CONTROLS__">
<button id="pause" type="button">__PAUSE__</button><button id="replay" type="button">__REPLAY__</button></nav></main>
<script type="application/json" id="scene-data">__JSON__</script>
<script>
(()=>{'use strict';
const data=JSON.parse(document.getElementById('scene-data').textContent);
const root=document.getElementById('motion'), cards=[...root.querySelectorAll('.scene')];
const pause=document.getElementById('pause'), replay=document.getElementById('replay');
const track=root.querySelector('.track'), preference=matchMedia('(prefers-reduced-motion: reduce)');
let elapsed=0,last=0,running=true,frame=0;
function paint(){
 const index=Math.max(0,data.scenes.findIndex((s,i)=>elapsed<s.start_ms+s.duration_ms||i===data.scenes.length-1));
 cards.forEach((card,i)=>{
  const s=data.scenes[i], active=i===index, local=elapsed-s.start_ms;
  const progress=s.motion.type==='none'||s.motion.duration_ms===0?1:Math.min(1,Math.max(0,local/s.motion.duration_ms));
  const eased=1-Math.pow(1-progress,3);
  card.style.visibility=active?'visible':'hidden';card.setAttribute('aria-hidden',String(!active));
  card.style.opacity=active?eased:0;card.style.transform=s.motion.type==='rise'?`translateY(${(1-eased)*16}px)`:'none';
 });track.style.transform=`scaleX(${elapsed/data.duration_ms})`;
}
function tick(now){
 if(!running||preference.matches)return;
 if(last)elapsed+=now-last;last=now;
 if(elapsed>=data.duration_ms){if(data.loop)elapsed%=data.duration_ms;else{elapsed=data.duration_ms;running=false;pause.textContent='продолжить';}}
 paint();if(running)frame=requestAnimationFrame(tick);
}
function start(){cancelAnimationFrame(frame);last=0;if(running&&!preference.matches)frame=requestAnimationFrame(tick);}
function mode(){
 root.classList.toggle('static',preference.matches);
 if(preference.matches){cancelAnimationFrame(frame);cards.forEach(c=>c.removeAttribute('aria-hidden'));}
 else{paint();start();}
}
pause.addEventListener('click',()=>{if(elapsed>=data.duration_ms)elapsed=0;running=!running;pause.textContent=running?'пауза':'продолжить';cancelAnimationFrame(frame);start();});
replay.addEventListener('click',()=>{elapsed=0;running=true;pause.textContent='пауза';start();});
document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(frame);last=0;}else start();});
preference.addEventListener('change',mode);mode();
})();
</script></html>'''

def export(source, destination):
    data = json.loads(source.read_text())
    validate(data)
    destination.mkdir(parents=True, exist_ok=True)
    esc = html.escape
    scenes = ''.join('<section class="scene"><p class="label">'+esc(s['label'])+'</p><h1>'+esc(s['headline'])+'</h1><p>'+esc(s['support'])+'</p></section>' for s in data['scenes'])
    style = data['style']
    labels = {
        'ru': ('управление анимацией', 'пауза', 'сначала'),
        'en': ('animation controls', 'pause', 'replay'),
        'es': ('controles de animación', 'pausar', 'repetir'),
        'pt': ('controles de animação', 'pausar', 'repetir'),
        'pt-BR': ('controles de animação', 'pausar', 'repetir'),
    }
    controls = labels.get(data['language'], labels['ru'])
    tokens = {'LANG':esc(data['language'],quote=True),'TITLE':esc(data['purpose'],quote=True),'BG':style['background'],'FG':style['foreground'],'ACCENT':style['accent'],'FONT':style['font_family'],'RATIO':f"{data['canvas']['width']} / {data['canvas']['height']}",'SCENES':scenes,'JSON':json.dumps(data,ensure_ascii=False).replace('<','\\u003c'),'CONTROLS':esc(controls[0],quote=True),'PAUSE':esc(controls[1]),'REPLAY':esc(controls[2])}
    import re
    output = re.sub(r'__([A-Z]+)__',lambda m:tokens[m.group(1)],TEMPLATE)
    (destination/'index.html').write_text(output)
    shutil.copyfile(ROOT/'scene.schema.json',destination/'scene.schema.json')
    (destination/'scene.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    s=data['scenes'][0]
    width, height = data['canvas']['width'], data['canvas']['height']
    scale = min(width / 1280, height / 720)
    poster=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{esc(data['purpose'])}</title><rect width="100%" height="100%" fill="{style['background']}"/><g transform="scale({scale:.6f})" font-family="{style['font_family']}" fill="{style['foreground']}"><text x="100" y="220" font-size="28" fill="{style['accent']}">{esc(s['label'])}</text><text x="100" y="330" font-size="38">{esc(s['headline'])}</text><text x="100" y="410" font-size="28">{esc(s['support'])}</text></g></svg>'''
    # Poster has fixed layout: reject long strings rather than silently overflow.
    if len(s['headline'])>45 or len(s['support'])>60 or len(s['label'])>32:
        raise ValueError('Poster text exceeds this template; adapt poster layout')
    (destination/'poster.svg').write_text(poster)
    manifest=json.loads((ROOT/'export.template.json').read_text())
    manifest.update(artifact_id=data['id'],status='rendered_html_svg')
    manifest['embedding']['aspect_ratio']=tokens['RATIO']
    manifest['embedding']['title']=data['purpose']
    manifest['canvas']=data['canvas']
    manifest['files']=[{'path':name,'media_type':mime} for name,mime in [('index.html','text/html'),('poster.svg','image/svg+xml'),('scene.json','application/json'),('scene.schema.json','application/schema+json'),('embed.html','text/html')]]
    (destination/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (destination/'embed.html').write_text('<iframe src="./index.html" title="'+esc(data['purpose'],quote=True)+'" loading="lazy" sandbox="allow-scripts" style="display:block;width:100%;height:100%;min-height:560px;border:0"></iframe>\n')
    print('Exported HTML, SVG, manifest, embed snippet:',destination)

if __name__=='__main__':
    export(pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'scene.json',pathlib.Path(sys.argv[2]) if len(sys.argv)>2 else ROOT/'export')
