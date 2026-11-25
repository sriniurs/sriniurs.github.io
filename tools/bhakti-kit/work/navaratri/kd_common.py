import sys
import pages as PG
from pages import foreword,glance,reading,story,cards,end,sources,build,covart,verse
from fig import strip
from fig2 import panel, fig_row
from tfig import *
from dnfig import cracked, rock, greens, bees, kaludipa
L=lambda u,t: f'<a href="{u}">{t}</a>'
KD_PARTS=[('kodavas','The Kodavas','People of the Hills and the Kāverī'),
 ('puttari','Puttari','The Festival of New Rice'),
 ('kailpodh','Kailpoḷd','The Festival of Arms'),
 ('kaveri-sankramana','Kāverī Saṅkramaṇa','The River Mother Rises at Talakāverī'),
 ('igguthappa','Igguthappa','The God of Rain and Rice at Pāḍi'),
 ('mand-and-dances','The Mand and Its Dances','Kōlāṭ, Bōlakāṭ, Ummattāṭ and the Village Green'),
 ('ainmane','The Ainmane','The Ancestral House and Its Lamp'),
 ('life-rites','Kodava Life Rites','Birth, Marriage and Death'),
 ('village-deities','Village Deities of Kodagu','Bhagavatī, Bhadrakāḷī and the Kōlas'),
 ('temples','Temples of Kodagu','Omkāreśvara, Bhāgamaṇḍala, Iruppu and More'),
 ('kodava-year','The Kodava Year and Its Food','Months, Kakkaḍa Padinett and Festival Dishes'),
 ('communities','Kodagu’s Many Communities','Gowdas, Airis, Meda and Others')]
PG.configure('/kodagu/',KD_PARTS,'navy','Kodagu: Culture and Festivals','Kāverī Amma','Kodagu')
PG.CFG.update(backurl='/kodagu/',backname='Kodagu')
PG.OUT='outd2/kodagu/'
def finish(i,*a):
    build(i,*a)
    p=PG.OUT+KD_PARTS[i][0]+'/index.html'
    s=open(p).read().replace('src="/assets/brand/logo-clear.png"','src="https://bhakti.srinipresents.com/assets/brand/logo-clear.png"')
    open(p,'w').write(s); print(KD_PARTS[i][0],'pages',s.count('<section class="page'))
# Kodagu figures
def kodava_man(c='#1b1b1b'):
    """Man in kupya (long black coat), red-gold chele sash, white turban (mande tuni), with oḍi kathi at the waist."""
    o=f'<path d="M-16 0 l4 -60 h24 l4 60z" fill="{c}"/><path d="M-12 -40 h24" stroke="#c0392b" stroke-width="5"/><path d="M-12 -40 h24" stroke="#e0a800" stroke-width="1.5"/>'
    o+='<path d="M8 -38 l10 18" stroke="#9a9a9a" stroke-width="4"/>'+'<circle cy="-70" r="10" fill="#c98a5a"/><path d="M-11 -76 q11 -12 22 0 q-11 -4 -22 0z" fill="#f4f1ea"/>'
    return o
def kodava_woman(c='#c0392b'):
    """Woman in the Kodava sari style (pleats at the back, pallu over the shoulder), head scarf."""
    o=f'<path d="M-18 0 q4 -40 6 -60 h24 q2 20 6 60z" fill="{c}"/><path d="M6 -58 q10 10 12 30" stroke="#e0a800" stroke-width="4" fill="none"/>'
    o+='<circle cy="-70" r="10" fill="#c98a5a"/><path d="M-12 -72 q12 -16 24 0 l2 10 q-14 -6 -28 0z" fill="#f4f1ea"/>'
    return o
def gun(l=60): return f'<path d="M0 0 l{l} -{l*.25:.0f}" stroke="#5a3a1a" stroke-width="5"/><path d="M{l*.6:.0f} -{l*.15:.0f} l{l*.4:.0f} -{l*.1:.0f}" stroke="#555" stroke-width="3"/>'
def kutti(): return '<path d="M-8 0 v-30 h16 v30z" fill="#c9a36b"/><path d="M-8 -10 h16 M-8 -20 h16" stroke="#8a6a3a" stroke-width="1.5"/>'
def nere(): return '<path d="M0 0 q-8 -10 -4 -22 M0 0 q8 -10 4 -22 M0 0 v-24" stroke="#2f7a3a" stroke-width="3" fill="none"/><path d="M-6 -6 h12" stroke="#8a6a3a" stroke-width="3"/>'
def paddy(n=8,w=200,h=40): return ''.join(f'<path d="M{-w/2+k*w/(n-1):.0f} 0 q-4 {-h*.6:.0f} 6 {-h:.0f} M{-w/2+k*w/(n-1):.0f} 0 q4 {-h*.5:.0f} -6 {-h*.9:.0f}" fill="none" stroke="#b8860b" stroke-width="3"/>' for k in range(n))
def hills(w=560,y=150,c='#3a7a4a'): return f'<path d="M0 {y} q70 -60 140 -10 q70 -60 140 0 q70 -70 140 -6 q70 -50 140 6 V{y+80} H0z" fill="{c}" stroke="none"/>'
def coffee(): return '<path d="M0 0 v-30" stroke="#5a3a1a" stroke-width="3"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="4" fill="#2f7a3a"/>' for x,y in [(-8,-12),(8,-16),(-6,-24),(6,-28)])+''.join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#c0392b"/>' for x,y in [(2,-10),(-2,-18),(3,-22)])
def kola_dancer(c='#1b1b1b',flip=False):
    o=kodava_man(c)+'<path d="M-10 -50 l-16 -16 M10 -50 l16 -16" stroke="#8a6a3a" stroke-width="3"/>'
    return f'<g transform="scale(-1 1)">{o}</g>' if flip else o
def dudi(): return '<path d="M-10 -14 q10 8 20 0 v28 q-10 -8 -20 0z" fill="#a0522d"/><ellipse cy="-14" rx="10" ry="4" fill="#e9d6c0"/><ellipse cy="14" rx="10" ry="4" fill="#e9d6c0"/>'
def ainmane(w=180):
    h=w*.35
    o=f'<rect x="{-w/2}" y="{-h}" width="{w}" height="{h}" fill="#e9d6c0"/><rect x="-14" y="{-h*.8}" width="28" height="{h*.8}" fill="#5a3a1a"/>'
    o+=''.join(f'<rect x="{x}" y="{-h*.7}" width="14" height="14" fill="#5a3a1a"/>' for x in (-w/2+16,w/2-30))
    o+=f'<path d="M{-w/2-16} {-h} L0 {-h-44} L{w/2+16} {-h}z" fill="#7a3b1f"/><path d="M{-w/4} {-h-22} h{w/2}" stroke="#5a2a10" stroke-width="2"/>'
    return o
def hanging_lamp(): return '<path d="M0 -60 v40" stroke="#b8860b" stroke-width="2"/><path d="M-14 -20 q14 14 28 0z" fill="#d8a520"/>'+g(0,-20,.6,flame(1))
