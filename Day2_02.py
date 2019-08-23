import collections
import re
import itertools

data = """fonbsmjyqugrapsczckghtvdxl
fonpsmjyquwrnpeczikghtvdxw
fonbsmdymuwrapexzikghtvdxl
fonwsmjyquwrapeczikghttdpl
fonbsmjkquwrapeczjkghtvdxx
yonbsmjyquwrapecgikghtvdxc
donbsmjyquqrapeczikghtadxl
monbsmjyquprgpeczikghtvdxl
fonbsmjyquwvapecqgkghtvdxl
fonbsmjyquwrkphczikghsvdxl
fonbomjyeuwvapeczikghtvdxl
fonwsmjyjuwrapoczikghtvdxl
foybsmjyquwcapeczikghsvdxl
fonbsmjyquwrtaeczikgptvdxl
ponbsmpyquwjapeczikghtvdxl
flnbcmjyquwrqpeczikghtvdxl
fonbsmjyquwrapegzikvbtvdxl
fonbjmjyqgwrazeczikghtvdxl
zoabsmjyquwkapeczikghtvdxl
fonbsmjyquwrapecziktxkvdxl
fonbsxjyrpwrapeczikghtvdxl
fonbsmjbquwqapeciikghtvdxl
lonbsmjyquwraphczikghtvdul
ftnbsmjyquwrapcczikghtxdxl
fonbsmjyqgwrapeczikghtldxc
fonbsmjsquwmapeyzikghtvdxl
fonbsmjyqfwrapecziqghtgdxl
yonbsmjyquwraveczikgftvdxl
fovbsmjyquwrapeczikggkvdxl
fonbsmjyquwrapezzikghbvdvl
fonzsmxyquwrapeczukghtvdxl
fonbemjyquwrapevzikghtvrxl
conbsxjxquwrapeczikghtvdxl
fonbsmjsmewrapeczikghtvdxl
folbsmjyqhwrapqczikghtvdxl
fonbsmjyquwrzneczikghtvdxn
fonbsmjyquirapeczikjhtvdll
fontsmgyquwrgpeczikghtvdxl
fonbsmjyauwrapeczbfghtvdxl
ftnbsmjyquwrapecpifghtvdxl
fonvsmjyqewrapeczikghlvdxl
fonbsljyquwrapecziklhtvdxw
fonbbmjyquwrapeczikghvadxl
ponbsmjyquwrspeczikghivdxl
fonbsmjcquwrapeccikghtvuxl
fonbsmjnquwrapetzikghtvlxl
fonbsmjymuwrapeczieghtvdxr
ffnbsxnyquwrapeczikghtvdxl
fonbsmjytuwrajeczzkghtvdxl
fonssmjyquwhapeczikghkvdxl
fonbsajyuuwrapeczikghlvdxl
fonbsmjyquwrapeczihghtcixl
fohbsmjyquwrapzczirghtvdxl
fonbsmjyquwrapecjqnghtvdxl
fonbsmjytuhrapeczihghtvdxl
foabumjyquwrapeczikghtvdxz
conbsmjyqtwrapeczikggtvdxl
fonbsmjyiqwrapeczokghtvdxl
fondsmjypuwrapeczikghtvjxl
fonbswjyquwrapeczikgvtydxl
fonbsmjyqqwrapeczikkhtvdbl
fonbsmjyquwrapemzitghtvdsl
fonbsmjyquwrspecziegxtvdxl
fonbsmpyquwrgpeczikghtwdxl
fodbsmjqquwrapeczmkghtvdxl
fonbsmjkquwrapeczikghpvdxr
fonbsmjyquwrapeczikshzvmxl
fznbsmjyqulrapeczikghkvdxl
fonbsmjyquwripeczikghtbdjl
fcnbsmjyquzrapecyikghtvdxl
ronbxmjyquwrapeczikghgvdxl
fonbsmuyvuwrgpeczikghtvdxl
fonbsmjyyuwraplczikghtudxl
poxbsmjyqewrapeczikghtvdxl
foabsmjyquwrapecziqghtvpxl
ponbsmjrquwrapeczikchtvdxl
fonzzmjyquwrapeczikghtvdxs
wonbsmjyquwghpeczikghtvdxl
fofbsejyquwrapeczikgctvdxl
ponbsmjyquwrayegzikghtvdxl
fonbumjyquwripeczikghtvdxf
fonbsmqyquwrapeczikgftvdxv
qonbsmjyquwraplczitghtvdxl
fmnbsajdquwrapeczikghtvdxl
fonbsrjyquwrapempikghtvdxl
fonbsmjyquwrapeczikgotudxw
fonbsmtyquwrapeflikghtvdxl
fzqbsmjyquwrapecjikghtvdxl
fdnbsmjyquwraqeclikghtvdxl
fvnbsijyquwrapechikghtvdxl
fovbsmjyquwsapeczikghqvdxl
ffjbsmjyqgwrapeczikghtvdxl
fonbsmjyquwrapeczvkhhivdxl
forbamjjquwrapeczikghtvdxl
fonbwmjyquwtapeyzikghtvdxl
fonvsmjyquwrapeczikglnvdxl
fonnsmjyguwrapeczikghtvxxl
fopbsmjyquwrapeczikghtvaxz
fonbsmjyquwiapeczikrhavdxl
fonbsujyquwrapeczikthtvdjl
fonpsmkyeuwrapeczikghtvdxl
fonbsmjyquwrapeczqkgttvdxk
fonbsmjyqzwrapeczikgrtddxl
fokbsmjiquwrapeczikgltvdxl
fonbsmjyqbwrapeczikghttdxo
fonbsejyquwrapeczikghbvdal
fonblmjyquwyaveczikghtvdxl
fonbsmjyquwlzpepzikghtvdxl
fonbsmjyqulrapbczigghtvdxl
fonbsmjyxuwrapecziyghtvsxl
fonbyjjyquwrapeczikghtvdxn
fonbhmjyquwrapeczikghtjhxl
fonbspjykuwraieczikghtvdxl
aonbsmjyquwwapeczikchtvdxl
fombsmjyquwyapeczikghtvdll
fonbsmjynuwrapeczivgbtvdxl
xonbsmjfquwrapeczikghqvdxl
fonbyzjyquwzapeczikghtvdxl
fbnbsmjyquwrapeczimgvtvdxl
qonbsmjyquwraoeczikgftvdxl
fonbsrjyquwrapeczikghtvjxm
fonbsmjyquwrapxjzykghtvdxl
fonbwgjyquwrapecziklhtvdxl
fonjcmjyouwrapeczikghtvdxl
fonbsmjyquwrapefzisuhtvdxl
fonbsmjyqywrspeczikghtvnxl
qonbsmjyquwrapeczlkuhtvdxl
fonbsmjyqlprapeczikghtvdbl
fonbsmjzquwrapedzikfhtvdxl
fonbsmjyquwrapeczizghtvjxq
fonbsmxyquwrrpeczikghtvcxl
fonpsmjyquwoapeczikghjvdxl
fonbshkyauwrapeczikghtvdxl
fonbsmjysuwrapeczilghpvdxl
fovwsxjyquwrapeczikghtvdxl
fonbsmjyquwrppecnikghmvdxl
fonbkmjyiuwrrpeczikghtvdxl
gonbsmjyquwrapeczikphtudxl
foncsmjyqlwrapeczimghtvdxl
fonbsmjhquwrtpeczikghtvdxg
fogbsmjyquarapeczikghtvdil
fonbsmjyquwraperzekghwvdxl
fonbstjyquwrapeczicghtedxl
fonbsmjoquhrapeczikgotvdxl
fonbsmjykuwrareczikgdtvdxl
fonbsmjyvuwrayeczivghtvdxl
fonbzmgyquwraptczikghtvdxl
fonbsmjyqubrapeczikgftvdxb
fonbgmjyjuwrapeczikghtvdul
fonbsmjzqurrapeczikghtvfxl
fonbsmjyiuwrapeczikgstvtxl
fpnbstjyquwrapeczikghtvdcl
fonbpmjyquwrapeczivghtndxl
fonbsmjyquwrapeczilgptvvxl
fonbsmjyqdwripecbikghtvdxl
fonbsmjytuwgapnczikghtvdxl
fonbsejyquwrapedzikghtvdml
fonbsojyqdwrapeczikghtgdxl
fonbsmjykuwrayeczicghtvdxl
foubsmtyquwrapeczikchtvdxl
fonbqmjyqukrapeyzikghtvdxl
fonbsmjyquwaapenzikghtvdwl
fonbsmeyquwrapeyzixghtvdxl
fonusmjyquhrapeczikgytvdxl
fonbsmjyquwrapwazikqhtvdxl
fonwsmeyquwrapeczikghhvdxl
fonmsmjyquxrspeczikghtvdxl
fonqsmjyqxwrapeczikghtvdml
fonfsmjyquwrapeuzikgatvdxl
fonvsmjyquwrapeczikgrtvdul
fonbsmayquwrapeczikihtvdxm
fonbsmnyquwrapecdifghtvdxl
fonbsmjyeuwraseczikghtvdxo
fonbvvjyquwrapeczikghtvdxi
fonbsmjyquwrapeczbkghtorxl
tonbsmjyqvwrapeczikghtvdcl
fonbsmjyquwrapeczhkgbtvdkl
fonqsmjyquwrapenzibghtvdxl
fontsmeyqudrapeczikghtvdxl
qonbsmjyauwrapeczikghtvdbl
fynbsmjyluwrapeczekghtvdxl
fonbsmjhquwrappczikghtvdxt
conbsmjyquwrapeczikahtvdxz
fonbsmjyquorapeczikvftvdxl
fonbsriyquwrapeczikchtvdxl
yonfsmjyquwrapeczikghtvdxq
fonaomjyquwrapecziwghtvdxl
fonbsxsyqdwrapeczikghtvdxl
fonbsqjyouwrapeczikgltvdxl
fonbstsyquwraleczikghtvdxl
fonbsmjyquwraoecztkghtvdsl
fonbsmjyquwrapezzjkghmvdxl
fonbwmjyqnwrapecpikghtvdxl
fonbsmvyqbwrapeczikghtvdsl
fonbsijyquwrazeczikghtvdwl
fonbsmjyouwrapewzikghtldxl
xonbsmjyqcwrapeczikghtvdul
fonbgmjxquwrajeczikghtvdxl
fokbsmjyquwrapechikghtrdxl
fonbqmjyqawrapeczikghtrdxl
fonbwmjzquwtapeyzikghtvdxl
fonbsmjyquwrapecdikgatvdnl
fonbsmjyqowrkpeczikghtvdxj
fonbsmjyquwkapejzikuhtvdxl
fonbsmjyquwrabeozikghtmdxl
fonbsijyeuwrapeczikghtvdxh
fonbsmjhquprapeczizghtvdxl
fonesmjyquwrapcczikghtvdxh
fonbamjyquwrapeczifrhtvdxl
foabsmjyquwpapeczikghtvdxs
fonbsmjyquwrapeczukghivdxh
fonbsejyoulrapeczikghtvdxl
fonbsmjyquwraceczikgdmvdxl
eonbsmjyquerppeczikghtvdxl
ffnzsmjyquwgapeczikghtvdxl
donbsmyyquwrapeczirghtvdxl
fjnbsmjyqufrapeczikghtwdxl
fonfsmjyquwrareczigghtvdxl
fonusmjyquwrapeczikgetvexl
tonbsmjyqpwrapeczikghtjdxl
fonbsmjhqukkapeczikghtvdxl
fonbsmjyqusraseczikghtvzxl
fonbsmjyquygapeczxkghtvdxl
folbsmjyquwraqeczikghjvdxl
fonbsmjyquwrppecjinghtvdxl
fonbsmjyquwraepczhkghtvdxl
fonbfmjyquwrapeczisghtrdxl
fsnbsmjwqubrapeczikghtvdxl
fonbspjyquwrapjczikghtedxl
fowbsmjyquwrapeczikghtbdbl
fonbymjyquwrapeczikghlvdrl
fonbsmjyruwrapecbikghtvixl
fonyqmjyqufrapeczikghtvdxl
focbscjyquwrapeczmkghtvdxl
fonbsmjyqtwnkpeczikghtvdxl
eonbsmjyquwrameczizghtvdxl
zonbsmjyqcwrapeczikghtvhxl
foubsmjyquwrapehzikghtvnxl
ffnbsmjyquwrapetzikghtjdxl
fonbjgjyquwrapkczikghtvdxl
fonbwmjyquwqapeczdkghtvdxl
forbsmjyquwrapeczikkhtvdml
fonbsmjyiuwrapeczivghevdxl
fonbsmjyquwrapeglikghwvdxl
fopgsmjyquwrapegzikghtvdxl
fonbsmjyqzwrajeczikghtldxl
fonbsmjyruwrapexzmkghtvdxl
fonbsmjyquwrdpeczikxstvdxl
fonbsmjyquwrapeezivghtvdql
fonbdmjyqujsapeczikghtvdxl"""
import time
start = time.time()
test = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""
from collections import Counter

class Found(Exception):
    pass
def run(data):
    final = []
    two = 0
    three = 0
    lines = [i for i in data.split('\n')]
    for line in lines:
        found2 = []
        found3 = []
        c = Counter(line)
        for i in c.values():
            if i == 2:
                found2.append(2)
            elif i == 3:
                found3.append(3)
        two += len(set(found2))
        three += len(set(found3))
        final.append(line)
    try:
        for i in final:
            for j in final:
                if len([i[b] for b in range(len(i)) if i[b] not in j[b]]) == 1:
                    print("found", i, j)
                    f = i
                    f2 = j
                    raise Found
    except Found:
        ans = ""
        for m in range(len(f)):
            if f[m] == f2[m]:
                ans += f[m]
        print(ans)

a = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

run(data)
print(time.time()-start)