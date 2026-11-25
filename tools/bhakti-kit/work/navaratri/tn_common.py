import sys
import pages as PG
from pages import foreword,glance,reading,story,cards,end,sources,build,covart,verse
from fig import strip
from fig2 import panel, fig_row
from tfig import *
from dnfig import cracked, rock, greens, bees, kaludipa
L=lambda u,t: f'<a href="{u}">{t}</a>'
TN_PARTS=[('tulu-year','The Tuḷu Year','Twelve Solar Months of the Coast'),
 ('mangaluru-dasara','Maṅgaḷūru Dasarā','Navadurgā and Śāradā at Kudroḷi'),
 ('udupi-festivals','Uḍupi Festivals','Chariots, Kṛṣṇa’s Birth and the Paryāya'),
 ('laksha-deepotsava','Lakṣa Dīpotsava','A Hundred Thousand Lamps at Dharmasthaḷa'),
 ('polali-jatre','Poḷali Jātre','The Month-Long Fair and the Ball Game'),
 ('katil-festivals','Kaṭīl Festivals','The Island Goddess Through the Year'),
 ('kodi-habba','Koḍi Habba','The Sugarcane Chariot of Kōṭeśvara'),
 ('bappanadu-jatre','Bappanāḍu Jātre','The Drums of the River Goddess'),
 ('siri-jatre','Siri Jātre','The Gathering of the Siri Women')]
PG.configure('/tulunadu/festivals/',TN_PARTS,'navy','Festivals of Tulu Nadu','Lord','Tulu Nadu Festivals')
PG.CFG.update(backurl='/tulunadu/festivals/',backname='Festivals of Tulu Nadu')
PG.OUT='outt/tulunadu/festivals/'
def finish(i,*a):
    html=build(i,*a)
    p=PG.OUT+TN_PARTS[i][0]+'/index.html'
    s=open(p).read().replace('src="/assets/brand/logo-clear.png"','src="https://bhakti.srinipresents.com/assets/brand/logo-clear.png"')
    open(p,'w').write(s); print(TN_PARTS[i][0],'pages',s.count('<section class="page'))
