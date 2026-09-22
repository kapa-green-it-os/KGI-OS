#!/usr/bin/env python3
"""Vidéo décorative à boucle mathématique de 12 s. Pillow, numpy, FFmpeg."""
from pathlib import Path
import math, subprocess
import numpy as np
from PIL import Image, ImageOps
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'08-fond-anime'; OUT.mkdir(exist_ok=True)
W,H,FPS,DURATION=1920,1080,24,12
src=Image.open(ROOT/'00-visuels-originaux/Logo KGI 03.png').convert('RGB')
base=Image.new('RGB',(W,H),'#00130F')
scaled=ImageOps.contain(src,(W,H),Image.Resampling.LANCZOS)
base.paste(scaled,((W-scaled.width)//2,(H-scaled.height)//2))
base=np.array(base)
# Overlay stays entirely to the left of the logo/text. The source is fixed.
cw,ch=480,270
x,y=np.meshgrid(np.linspace(0,1,cw,dtype=np.float32),np.linspace(0,1,ch,dtype=np.float32))
mask=np.clip((0.57-x)/0.14,0,1)*np.clip((x-0.015)/0.09,0,1)*np.sin(np.pi*y)**2
target=OUT/'kgi-bureau-anime-1920x1080.mp4'
cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','21','-pix_fmt','yuv420p','-movflags','+faststart',str(target)]
process=subprocess.Popen(cmd,stdin=subprocess.PIPE)
def frame(index):
    t=2*math.pi*index/(FPS*DURATION)
    wave_y=0.52+0.12*np.sin(x*7+t)
    ribbon=np.exp(-((y-wave_y)/0.018)**2)*(0.7+0.3*np.sin(x*11-t)**2)
    mist=np.exp(-((y-0.49-0.14*np.sin(x*5+t))/0.19)**2)*(0.45+0.35*np.sin(t+x*4)**2)
    lum=(ribbon*12+mist*8)*mask
    for k in range(8):
        px=0.1+0.38*((k/8+t/(2*math.pi))%1)
        py=0.35+0.26*math.sin(t+k*1.7)
        pulse=(math.sin(t+k)+1)*0.5
        lum+=np.exp(-((x-px)**2+(y-py)**2)/0.000018)*22*pulse*mask
    overlay=np.stack([lum*0.08,lum,lum*0.58],axis=2)
    up=np.asarray(Image.fromarray(np.clip(overlay,0,255).astype('uint8')).resize((W,H),Image.Resampling.BILINEAR))
    return np.clip(base.astype('uint16')+up,0,255).astype('uint8')
for n in range(FPS*DURATION):
    process.stdin.write(frame(n).tobytes())
process.stdin.close()
assert process.wait()==0
assert np.array_equal(frame(0),frame(FPS*DURATION)), 'Loop mismatch'
assert np.array_equal(frame(100)[:,int(W*.6):],base[:,int(W*.6):]), 'Brand area changed'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(target),'-vf','scale=1280:720','-an','-c:v','libx264','-preset','fast','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart',str(OUT/'kgi-bureau-anime-1280x720.mp4')],check=True)
Image.fromarray(frame(FPS*3)).save(OUT/'apercu-animation.png')
(OUT/'preview.html').write_text('''<!doctype html><html lang="fr"><meta charset="utf-8"><title>KGI-OS · Fond animé</title><style>html,body{margin:0;height:100%;background:#00130f;color:#fff;font:16px sans-serif}video{width:100%;height:100%;object-fit:contain}button{position:fixed;bottom:24px;left:24px;padding:12px 20px;border:1px solid #20d58c;border-radius:8px;background:#00130f;color:#fff}</style><video id="wallpaper" loop muted playsinline controls poster="../06-fond-ecran/kgi-bureau.png"><source src="kgi-bureau-anime-1920x1080.mp4" type="video/mp4"></video><button id="play" type="button">Lire / Mettre en pause</button><script>const v=document.getElementById('wallpaper');document.getElementById('play').addEventListener('click',()=>{if(v.paused){v.play().catch(()=>{});}else{v.pause();}});document.addEventListener('visibilitychange',()=>{if(document.hidden)v.pause();});</script></html>''',encoding='utf-8')
print('Animation : 12 s, 24 i/s, boucle vérifiée, logo fixe, 1080p + 720p')
