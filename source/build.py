"""Construit l'application.
python3 build.py                -> rapport-du-culte.html (version web / artifact, librairies PDF via CDN)
python3 build.py <dossier www>  -> <www>/index.html + <www>/lib/* (version Android/iOS, hors ligne)
"""
import sys, os, shutil
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'app.src.html')).read()
reg=open(os.path.join(here,'reglement.json')).read()
def opt(f,d):
    f=os.path.join(here,'i18n',f)
    return open(f).read() if os.path.exists(f) else d
app=(src.replace('/*__REGLEMENT__*/[]',reg)
        .replace('/*__REGLEMENT_PT__*/[]',opt('reglement.pt.json','[]'))
        .replace('/*__REGLEMENT_EN__*/[]',opt('reglement.en.json','[]'))
        .replace('/*__I18N__*/{}',opt('ui.json','{}')))
CDN=('<script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"></script>\n'
     '<script src="https://cdn.jsdelivr.net/npm/jspdf-autotable@3.8.2/dist/jspdf.plugin.autotable.min.js"></script>')
LOCAL=('<script src="lib/jspdf.umd.min.js"></script>\n<script src="lib/jspdf.plugin.autotable.min.js"></script>')
open(os.path.join(here,'rapport-du-culte.html'),'w').write(app.replace('<!--__PDFLIBS__-->',CDN))
if len(sys.argv)>1:
    www=sys.argv[1]; os.makedirs(os.path.join(www,'lib'),exist_ok=True)
    for f in ('jspdf.umd.min.js','jspdf.plugin.autotable.min.js'):
        shutil.copy(os.path.join(here,'lib',f),os.path.join(www,'lib',f))
    head=('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n'
          '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover">\n'
          '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n')
    nat=app.replace('<!--__PDFLIBS__-->',LOCAL)
    te=nat.index('</title>')+8
    body_start=nat.index('<div class="splash"')
    out=head+nat[:te]+nat[te:body_start]+'</head>\n<body>\n'+nat[body_start:]+'\n</body>\n</html>\n'
    open(os.path.join(www,'index.html'),'w').write(out)
