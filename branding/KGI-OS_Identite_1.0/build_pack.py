#!/usr/bin/env python3
"""Exports fidèles des sources. Dépendances : Pillow, Inkscape (accueil PNG)."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
import base64, json, shutil, subprocess, hashlib
from html import escape

ROOT = Path(__file__).resolve().parent
SRC = ROOT / '00-visuels-originaux'
BG = '#00130F'
RESOLUTIONS = [(1366,768),(1920,1080),(1920,1200),(1600,1200)]
manifest = []

def write(rel, content):
    path = ROOT/rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

def canvas(source, size):
    im = Image.open(SRC/source).convert('RGBA')
    scaled = ImageOps.contain(im, size, Image.Resampling.LANCZOS)
    out = Image.new('RGBA', size, BG)
    out.alpha_composite(scaled, ((size[0]-scaled.width)//2,(size[1]-scaled.height)//2))
    return out.convert('RGB')

def wrapper(source, w, h, title, extra=''):
    data = base64.b64encode((SRC/source).read_bytes()).decode()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{escape(title)}</title><rect width="100%" height="100%" fill="{BG}"/><image x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{data}"/>{extra}</svg>'''

def export(folder, stem, source, resolutions=RESOLUTIONS, svg_sizes=()):
    d=ROOT/folder; d.mkdir(parents=True,exist_ok=True)
    for w,h in resolutions:
        p=d/f'{stem}-{w}x{h}.png'
        canvas(source,(w,h)).save(p, optimize=True)
        manifest.append(dict(file=str(p.relative_to(ROOT)),source='00-visuels-originaux/'+source,width=w,height=h,fit='contain',crop=False))
        if (w,h) in svg_sizes:
            write(str(p.relative_to(ROOT).with_suffix('.svg')),wrapper(source,w,h,stem))
    shutil.copy2(d/f'{stem}-1920x1080.png',d/f'{stem}.png')

export('02-plymouth','kgi-demarrage','logo kgi ecran de veille.png',svg_sizes=[(1920,1080)])
export('03-connexion','kgi-connexion','logo KGI.png',svg_sizes=[(1920,1080),(1920,1200),(1600,1200)])
export('06-fond-ecran','kgi-bureau','Logo KGI 03.png',svg_sizes=[(1920,1080)])
export('07-ecran-veille','kgi-veille','logo kgi ecran de veille.png')

# The complete original is preserved; small Plymouth images are opaque panels,
# not extracted logos. No asset is incorrectly called "transparent".
for w in [256,512,1024]:
    h=round(w*941/1672)
    p=ROOT/'02-plymouth/png'/f'kgi-visuel-{w}.png';p.parent.mkdir(exist_ok=True)
    canvas('logo kgi ecran de veille.png',(w,h)).save(p)
    manifest.append(dict(file=str(p.relative_to(ROOT)),source='00-visuels-originaux/logo kgi ecran de veille.png',width=w,height=h,fit='contain',crop=False))

# Real brand icon, resized only; no substitute or redrawn emblem.
for size in [16,24,32,48,64,128,256,512]:
    im=Image.open(SRC/'kapa-greenit-icone-dark.png').convert('RGBA').resize((size,size),Image.Resampling.LANCZOS)
    for stem in ['kgi-os','kgi-install-usb','kgi-a-propos']:
        rel=f'04-icones/png/{stem}-{size}.png';(ROOT/rel).parent.mkdir(parents=True,exist_ok=True);im.save(ROOT/rel)
        manifest.append(dict(file=rel,source='00-visuels-originaux/kapa-greenit-icone-dark.png',width=size,height=size,fit='resize',crop=False))
for stem in ['kgi-os','kgi-install-usb','kgi-a-propos']:
    write(f'04-icones/{stem}.svg',wrapper('kapa-greenit-icone-dark.png',512,512,stem).replace(f'<rect width="100%" height="100%" fill="{BG}"/>',''))

# Installer: source artwork intact underneath actual editable presentation text.
lines=[(58,'Bienvenue dans KGI-OS',25,True),(86,'Un système Linux léger pour prolonger',13,False),(105,'la vie des ordinateurs.',13,False),
       (149,'Essentiel',18,True),(173,'Internet, messagerie, documents',13,False),(192,'et démarches du quotidien.',13,False),
       (231,'Éducation',18,True),(255,'Apprentissage, outils scolaires',13,False),(274,'et ressources pédagogiques.',13,False),
       (313,'Professionnel / Association',17,True),(337,'Bureautique, activités associatives',13,False),(356,'et travail collaboratif.',13,False),
       (393,'Choix du profil à l’étape dédiée.',12,False)]
for w,h in [(752,448),(960,600)]:
    scale=min(w/752,h/448)
    text='<g transform="scale('+str(scale)+')"><rect x="22" y="24" width="335" height="385" rx="14" fill="#00130F" fill-opacity="0.88"/>'
    for y,label,size,bold in lines:
        text+=f'<text x="38" y="{y}" fill="'+('#34E99B' if bold and y>58 else '#F5FAF7')+f'" font-family="DejaVu Sans" font-size="{size}" font-weight="'+('bold' if bold else 'normal')+'">'+escape(label)+'</text>'
    text+='</g>'
    rel=f'01-installateur/kgi-bienvenue-{w}x{h}.svg'
    write(rel,wrapper('Logo KGI 03.png',w,h,'Bienvenue dans KGI-OS',text))
    subprocess.run(['inkscape',str(ROOT/rel),'--export-type=png','--export-filename='+str((ROOT/rel).with_suffix('.png'))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    manifest.append(dict(file=rel.replace('.svg','.png'),source='00-visuels-originaux/Logo KGI 03.png',width=w,height=h,fit='contain',crop=False,overlay='Présentation des profils dans la zone libre à gauche'))

write('01-installateur/profils-fr.json',json.dumps({'Essentiel':'Internet, messagerie, documents et démarches du quotidien.','Éducation':'Apprentissage, outils scolaires et ressources pédagogiques.','Professionnel / Association':'Bureautique, activités associatives et travail collaboratif.','note':'Le choix du profil se fait dans un écran interactif séparé.'},ensure_ascii=False,indent=2))
write('INTEGRATION.json',json.dumps({'version':'1.0-visuels-originaux','status':'assets_prepared_not_installed','scale':'contain_no_crop_no_stretch','defaults':{'installateur':'01-installateur/kgi-bienvenue-752x448.png','plymouth':'02-plymouth/kgi-demarrage.png','connexion':'03-connexion/kgi-connexion.png','icone':'04-icones/png/kgi-os-64.png','bureau':'06-fond-ecran/kgi-bureau.png','veille':'07-ecran-veille/kgi-veille.png','animation':'08-fond-anime/kgi-bureau-anime-1920x1080.mp4'},'login_form':{'side':'left','recommended_box_fraction':[0.06,0.20,0.40,0.55],'opaque_panel_required':True},'animated_wallpaper_default':False,'exports':manifest},ensure_ascii=False,indent=2))

# A contact sheet of the actual exported files, not substitute artwork.
out=Image.new('RGB',(1400,1060),'#E8EFEC');d=ImageDraw.Draw(out)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
bold=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',28)
d.text((30,20),'KGI-OS · Vos visuels intégrés',font=bold,fill='#062019')
items=[('Accueil et profils','01-installateur/kgi-bienvenue-752x448.png'),('Démarrage / arrêt','02-plymouth/kgi-demarrage.png'),('Fond de bureau','06-fond-ecran/kgi-bureau.png'),('Écran de veille','07-ecran-veille/kgi-veille.png'),('Connexion · saisie prévue à gauche','03-connexion/kgi-connexion.png')]
for i,(label,rel) in enumerate(items):
    x=30+(i%2)*695;y=80+(i//2)*320
    d.text((x,y),label,font=font,fill='#062019')
    im=ImageOps.contain(Image.open(ROOT/rel).convert('RGB'),(650,272),Image.Resampling.LANCZOS)
    out.paste(im,(x,y+37))
d.text((725,720),'Icônes · logo original',font=font,fill='#062019')
for i,s in enumerate([32,64,128]):
    im=Image.open(ROOT/f'04-icones/png/kgi-os-{s}.png');out.paste(im,(750+i*165,790),im)
out.save(ROOT/'APERCU_KGI-OS.png')
print('Exports générés :',len(manifest))
