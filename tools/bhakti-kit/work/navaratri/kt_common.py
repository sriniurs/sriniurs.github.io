import sys
import pages as PG
from pages import foreword,glance,reading,story,cards,end,sources,build,covart,verse
from fig import strip
from fig2 import panel, fig_row
from tfig import *
from dnfig import cracked, rock, greens, bees, kaludipa
L=lambda u,t: f'<a href="{u}">{t}</a>'
KT_PARTS=[('hampi-virupaksha','Hampi Virūpākṣa','Pampāpati of the Vijayanagara Kings'),
 ('belur-halebidu','Belūr and Haḷebīḍu','The Hoysaḷa Temples of Stone Lace'),
 ('savadatti-yellamma','Savadatti Yellamma','Reṇukā on the Hill of Yallammanagudda'),
 ('ganagapura-dattatreya','Gāṇagāpura Dattātreya','The Guru’s Seat on the Bhīmā'),
 ('banashankari','Banaśaṅkarī','Śākambharī of the Tilakāraṇya Forest')]
PG.configure('/temples-of-india/karnataka/',KT_PARTS,'navy','Temples of Karnataka','Lord','Temples of Karnataka')
PG.CFG.update(backurl='/temples-of-india/karnataka/',backname='Temples of Karnataka')
PG.OUT='outk/temples-of-india/karnataka/'
def finish(i,*a):
    build(i,*a)
    p=PG.OUT+KT_PARTS[i][0]+'/index.html'
    s=open(p).read().replace('src="/assets/brand/logo-clear.png"','src="https://bhakti.srinipresents.com/assets/brand/logo-clear.png"')
    open(p,'w').write(s); print(KT_PARTS[i][0],'pages',s.count('<section class="page'))
