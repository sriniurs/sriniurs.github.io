import re,sys
CY='#ffd60a';CO='#ff9f1c';CB='#4dabf7';CG='#69db7c';CP='#f783ac';CW='#fff8e7';CR='#e03131';CV='#9775fa';CK='#495057'
def badge(n): return f'<circle cx="84" cy="16" r="12" fill="#7a1020"/><text x="84" y="21" text-anchor="middle" font-size="{14 if n<10 else 12}" font-weight="bold" fill="#fff" stroke="none" font-family="Georgia,serif">{n}</text>'
SHIELD=f'<path d="M50 14 l28 10 v22 c0 20 -14 32 -28 38 c-14 -6 -28 -18 -28 -38 v-22z" fill="{CR}"/>'
IC={
1:SHIELD+f'<path d="M50 28 v38 M38 32 v8 q0 8 12 8 q12 0 12 -8 v-8" fill="none" stroke="{CY}" stroke-width="5"/>',
2:SHIELD+f'<circle cx="50" cy="44" r="12" fill="{CY}"/><path d="M38 66 h24"/>',
3:f'<rect x="20" y="40" width="60" height="44" rx="4" fill="{CO}"/><path d="M20 40 l30 -24 30 24"/><path d="M50 40 v44" /><path d="M30 62 h40" stroke-width="6"/>',
4:f'<path d="M32 60 l40 -40 8 8 -40 40z" fill="{CY}"/><circle cx="30" cy="70" r="14" fill="{CO}"/><circle cx="30" cy="70" r="5" fill="{CW}"/>',
5:f'<path d="M50 80 v-34" stroke-width="5" stroke="#8d5524"/><circle cx="50" cy="36" r="22" fill="{CG}"/><circle cx="30" cy="80" r="6" fill="{CW}"/><circle cx="70" cy="80" r="6" fill="{CW}"/><path d="M24 92 h52"/>',
6:f'<path d="M24 76 q26 12 52 0 q-26 -6 -52 0z" fill="{CB}"/><path d="M50 72 c-8 -8 -8 -22 0 -32 c8 10 8 24 0 32z" fill="{CP}"/><circle cx="50" cy="28" r="9" fill="{CY}"/>',
7:f'<circle cx="50" cy="50" r="12" fill="{CY}"/><path d="M50 14 v18 M50 68 v18 M14 50 h18 M68 50 h18 M25 25 l13 13 M62 62 l13 13 M75 25 l-13 13 M38 62 l-13 13" stroke="{CO}" stroke-width="5"/><path d="M50 14 v18 M50 68 v18 M14 50 h18 M68 50 h18"/>',
8:f'<path d="M18 46 q-4 -20 12 -24 M82 46 q4 -20 -12 -24" fill="none" stroke-width="5"/><ellipse cx="50" cy="56" rx="30" ry="24" fill="{CK}"/><circle cx="40" cy="52" r="4" fill="{CR}"/><circle cx="60" cy="52" r="4" fill="{CR}"/><path d="M50 12 l6 74" stroke="{CY}" stroke-width="5"/>',
9:f'<path d="M30 80 l-4 -30 q0 -16 24 -18 q24 2 24 18 l-4 30z" fill="{CW}"/><path d="M50 32 v48"/><circle cx="50" cy="20" r="7" fill="{CO}"/>',
10:f'<circle cx="50" cy="50" r="10" fill="{CY}"/><circle cx="50" cy="22" r="8" fill="{CP}"/><circle cx="76" cy="40" r="8" fill="{CP}"/><circle cx="68" cy="72" r="8" fill="{CP}"/><circle cx="32" cy="72" r="8" fill="{CP}"/><circle cx="24" cy="40" r="8" fill="{CP}"/>',
11:f'<path d="M20 70 q10 -30 30 -10 q20 -30 30 10z" fill="#adb5bd"/><path d="M24 54 q8 -20 20 -16 M56 40 q14 -6 20 14" fill="none"/><path d="M40 84 l20 -20" stroke="{CO}" stroke-width="6"/>',
12:f'<path d="M50 16 c-18 6 -24 26 -14 46 l14 20 14 -20 c10 -20 4 -40 -14 -46z" fill="{CK}"/><circle cx="43" cy="44" r="4" fill="{CR}"/><circle cx="57" cy="44" r="4" fill="{CR}"/><path d="M42 60 h16" stroke="{CW}"/>',
13:f'<path d="M50 12 c-10 16 -14 24 -14 32 a14 14 0 0 0 28 0 c0 -8 -4 -16 -14 -32z" fill="{CR}"/><circle cx="26" cy="74" r="7" fill="{CR}"/><circle cx="50" cy="82" r="5" fill="{CR}"/><circle cx="74" cy="72" r="6" fill="{CR}"/>',
14:f'<path d="M20 80 l60 -60" stroke-width="5"/><path d="M80 20 l-14 4 10 10z" fill="{CK}"/><circle cx="36" cy="40" r="14" fill="{CY}"/><path d="M36 26 v28 M22 40 h28" />',
15:f'<path d="M50 12 v54" stroke-width="5"/><path d="M50 12 l-12 14 h24z" fill="{CY}"/><path d="M36 26 q-12 10 -4 22 M64 26 q12 10 4 22" fill="none" stroke-width="5"/><path d="M30 84 h40 l-6 -18 h-28z" fill="{CR}"/>',
16:f'<circle cx="50" cy="44" r="26" fill="{CY}"/><path d="M50 28 l5 10 11 2 -8 8 2 11 -10 -5 -10 5 2 -11 -8 -8 11 -2z" fill="{CR}"/><path d="M30 84 h40"/>',
17:f'<path d="M20 30 q16 -8 30 0 v48 q-14 -8 -30 0z" fill="{CW}"/><path d="M80 30 q-16 -8 -30 0 v48 q14 -8 30 0z" fill="{CW}"/><path d="M50 12 l3 6 6 1 -5 4 1 6 -5 -3 -5 3 1 -6 -5 -4 6 -1z" fill="{CY}"/>',
18:f'<path d="M50 18 c-10 0 -18 8 -18 20 v6 h36 v-6 c0 -12 -8 -20 -18 -20z" fill="{CY}"/><rect x="28" y="44" width="44" height="10" rx="3" fill="{CR}"/><path d="M34 76 q16 -16 32 0 q-16 12 -32 0z" fill="{CP}"/>',
19:f'<path d="M28 82 h44 l-6 -16 h-32z" fill="{CO}"/><path d="M50 64 c-12 0 -14 -14 -6 -22 c0 6 6 6 6 2 c0 -8 6 -14 8 -18 c0 10 8 14 8 22 c0 10 -6 16 -16 16z" fill="{CY}"/><circle cx="50" cy="14" r="5" fill="{CR}"/>',
}
f=sys.argv[1]; h=open(f).read()
pat=re.compile(r'(<div class="tile-art" style="background:[^"]+"><svg class="ill"[^>]*><g [^>]*>)(.*?)(</g></svg></div><div class="tile-copy"><strong class="label">Part (\d+) of 19)',re.S)
h,k=pat.subn(lambda m:m.group(1)+IC[int(m.group(4))]+badge(int(m.group(4)))+m.group(3),h)
open(f,'w').write(h); print('replaced',k)
