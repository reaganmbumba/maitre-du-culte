#!/usr/bin/env python3
"""Approuver ou retirer un téléphone pour une paroisse dans config.json.

  python3 tools/approuver.py "Paroisse de Pika" A7K2-9QX4 [--ville Kikwit]
  python3 tools/approuver.py "Paroisse de Pika" A7K2-9QX4 --retirer
  python3 tools/approuver.py "Paroisse de Pika" --suspendre | --reactiver
  python3 tools/approuver.py "Paroisse de Pika" --whatsapp "+243 8.."
  python3 tools/approuver.py --liste
"""
import argparse, hashlib, json, os, re, sys

CFG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')

def tel_hash(dev):
    return hashlib.sha256(('mdc-tel:' + dev.strip().upper()).encode()).hexdigest()[:24]

def same(a, b):
    return a.strip().lower() == b.strip().lower()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('paroisse', nargs='?')
    ap.add_argument('telephone', nargs='?')
    ap.add_argument('--ville', default='')
    ap.add_argument('--whatsapp', help='numéro qui reçoit les rapports de cette paroisse')
    ap.add_argument('--retirer', action='store_true')
    ap.add_argument('--suspendre', action='store_true')
    ap.add_argument('--reactiver', action='store_true')
    ap.add_argument('--liste', action='store_true')
    a = ap.parse_args()

    c = json.load(open(CFG, encoding='utf-8'))
    ps = c.setdefault('paroisses', [])

    if a.liste:
        print('activation:', c.get('activation'))
        for p in ps:
            print(f"- {p['nom']} ({p.get('ville','')}) : {len(p.get('tel', []))} tél.{' · suspendue' if p.get('actif') is False else ''}")
        return

    if not a.paroisse:
        sys.exit('Indiquez la paroisse.')
    e = next((p for p in ps if same(p['nom'], a.paroisse)), None)

    if a.whatsapp and not a.telephone:
        if not e:
            sys.exit('Paroisse introuvable.')
        e['whatsapp'] = a.whatsapp.strip()
    elif a.suspendre or a.reactiver:
        if not e:
            sys.exit('Paroisse introuvable.')
        e['actif'] = bool(a.reactiver)
    else:
        dev = (a.telephone or '').strip().upper()
        if not re.fullmatch(r'[A-Z0-9]{4}-[A-Z0-9]{4}', dev):
            sys.exit('Identifiant attendu sous la forme A7K2-9QX4.')
        h = tel_hash(dev)
        if a.retirer:
            if not e or h not in e.get('tel', []):
                sys.exit("Ce téléphone n'est pas approuvé pour cette paroisse.")
            e['tel'].remove(h)
        else:
            if not e:
                e = {'nom': a.paroisse.strip(), 'ville': a.ville.strip(), 'actif': True, 'tel': []}
                ps.append(e)
            elif a.ville and not e.get('ville'):
                e['ville'] = a.ville.strip()
            e.setdefault('tel', [])
            if h not in e['tel']:
                e['tel'].append(h)
            c['activation'] = True

    order = ['demandes', 'whatsapp', 'email', 'cc', 'activation', 'paroisses']
    out = {k: c[k] for k in order if k in c}
    out.update({k: v for k, v in c.items() if k not in out})
    open(CFG, 'w', encoding='utf-8').write(json.dumps(out, indent=2, ensure_ascii=False) + '\n')
    print('config.json mis à jour.')

if __name__ == '__main__':
    main()
