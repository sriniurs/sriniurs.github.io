from pages import *
from fig import *
OFFER={1:'ghee',2:'sugar',3:'milk or kheer',4:'malpuā (sweet pancakes)',5:'bananas',6:'honey',7:'jaggery',8:'coconut',9:'sesame'}
CAKRA={1:'mūlādhāra, the root centre',2:'svādhiṣṭhāna, the sacral centre',3:'maṇipūra, the navel centre',4:'anāhata, the heart centre',5:'viśuddha, the throat centre',6:'ājñā, the brow centre',7:'sahasrāra, the crown (in some lists)',8:'the crown and beyond (lists differ)',9:'the crown and beyond (lists differ)'}
def make(d):
    i=d['idx']; n=i-2  # night number
    nm=d['name']
    DV=lambda s=1: devi(skin=d.get('skin','#f2c79b'),sari=d['sari'],items=d['items'],**d.get('dk',{}))
    mount=d.get('mount')
    def hero(x,y,s):
        o=''
        if mount: o+=g(x-10*s,y,s*.95,beast(mount))
        o+=g(x,y-(30*s if mount else 0),s*.9,DV())
        return o
    COV=covart(d['covlabel'],d.get('covbg','')+hero(220,200,1.35)+d.get('covextra',''))
    pages=[foreword(i,d['fw'],d['fwt']),
     glance([('Night','The '+['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth'][n-1]+' night of Navarātri (Devī Kavaca order)'),('Name',d['gl_name']),('Mount',d['gl_mount']),('Holds',d['gl_holds']),('Story',d['gl_story']),('Known for',d['gl_known']),('Her verse','Navadurgā Stotra, verse '+str(n))],
       svg(560,170,d['covlabel'],hero(280,165,1.05)),[('z',d['glq']),('b',d['gla'])]),
     reading('name',d['name_title'],d['name_sub'],svg(560,190,d['name_fig_label'],d['name_fig']),d['name_p'],d['name_t'],d['name_k']),
     story('story',d['story_title'],d['story_sub'],strip(d['strip_label'],d['strip'],d['strip_caps']),d['story_lead'],d['steps'],d['story_t'],d['story_k']),
     cards('form','HER FORM AND SYMBOLS','What the image teaches',svg(560,200,'The form of '+nm+' with labels for what she holds and rides',hero(280,195,1.3)+''.join(lab(x,y,t) for x,y,t in d['form_labels'])),d['form_cards'],d['form_t'],d['form_k']),
     verse('verse',f'NAVADURGĀ STOTRA {n}','HER MEDITATION VERSE (DHYĀNA)',d['vlines'],svg(220,160,'The form of '+nm+' as the verse describes her',hero(110,155,.85),cls=''),d['vmean'],d['vwords'],d['vinsight'],None,d['vkey'],'Text as in the Navadurgā Stotra (shlokam.org transliteration).'+d.get('vnote','')),
     reading('worship',d.get('w_title','WORSHIP ON HER NIGHT'),'How devotees keep night '+str(n),svg(560,180,'A small altar for '+nm+' with a lamp, flowers and an offering of '+OFFER[n],ground(560,180,160,'#e9d6c0')+'<rect x="200" y="100" width="160" height="60" fill="#e8c06a" stroke="#111" stroke-width="2.5"/>'+g(280,104,.7,DV())+g(160,160,1,lamp())+g(400,150,.9,pot('#e0a800'))+g(230,100,.6,lotus())+g(330,100,.6,lotus())+lab(400,176,'offering: '+OFFER[n].split(' (')[0])),
       d['w_p']+['<b>Offerings and colours.</b> A widely followed North Indian custom offers <b>'+OFFER[n]+'</b> on this night; lists differ between families and regions. Many cities also publish a “colour of the day” for each night, but that colour is set each year by the weekday, so we do not fix one here.'],d['w_t'],d['w_k']),
     reading('inner','THE INNER READING','What many teachers see in her',svg(560,180,'A seated meditator with a glowing point at the '+CAKRA[n].split(',')[0]+', and the goddess’s emblem beside',g(200,170,1.4,person('#7a3fa0',seat=True))+f'<circle cx="200" cy="{[0,166,150,134,118,100,84,70,58,58][n]}" r="9" fill="#ffd60a" stroke="#c0392b" stroke-width="3"/>'+g(400,160,1,d.get('emblem',lotus()))+lab(400,175,d['emblem_label'])),
       d['in_p']+['<b>The yogic map.</b> A modern yogic reading links each night to a centre of the subtle body; for '+nm+' it is <b>'+CAKRA[n]+'</b>. This mapping is popular but recent, and teachers differ; take it as a meditation aid, not scripture.'],d['in_t'],d['in_k']),
     end(i,d['end_lines'],d['next'],nm),
     sources([('Verse:','Navadurgā Stotra verse '+str(n)+' (shlokam.org transliteration); order of the nine from Devī Kavaca 3–5.')]+d['src'],d['unver'],'Navadurgā Stotra numbered by goddess, Śailaputrī = 1.')]
    build(i,f'PART {i+1} OF 16 · NIGHT {n} · '+d['kick'],COV,d['cap'],d['how'],d['desc'],pages)
