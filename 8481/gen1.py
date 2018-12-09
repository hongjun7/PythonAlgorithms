__import__('sys').stdout = open('res1.txt', 'w')

import base64, zlib
def decipher(s): return zlib.decompress(base64.b85decode(s)).decode('utf-8')
god = "Godzilla terrorizes Bajtoly lower again. Every day a monster comes out of the ocean, slow movement of marching through the city to some of the skyscrapers and eats it with people who are in it. Eating one skyscraper takes the whole day, at dusk, it returns to its hiding place hidden in the depths. To make matters worse, going through the city, Godzilla wags its tail and destroys towers, near the passes. The prospect of becoming a meal for an underwater monster, to discourage some residents spent in uncomfort- tion in the city. During the night of each tower is derived as a resident and flees to the countryside. In Bajtogrodzie skyscrapers were built only at street crossings. At each intersection there is exactly one building. Junctions are connected by two-way streets. In addition, a the junction is just above the ocean, this is where Godzilla begins its destructive journey through the city. During the investigation, the monster moves only in the streets. Godzilla noted that he must hurry up with the consumption of residents and carefully choose the skyscrapers devouring and streets, which reaches them. Of course, choosing never previously consumed or destroyed- wanego skyscraper. What is the maximum number of people who can eat before the city completely desolate? Entrance The first line of standard input contains two integers him (1 n 100 000, 0 500 000 m) respectively denoting the number of intersections in the city and the number of connecting streets. Crossroads numbers are numbered from 1 to n, junction 1 is located on the shores of the ocean. Next row contains a sequence of integers n s (0 s 100 000) to describe population skyscrapers at various intersections. In each of the next m rows are the two integers ai and bi (1 ai, bi n, ai = bi), which means that there is a road junction connecting ai and bi. The crossing number One can reach any other intersection in the city. Exit Write to stdout the number of people who eat Godzilla for the optimum choice of meals and roads through the city every day. Example For input: the result is correct: 5 5 11 1 3 2 4 7 1 2 1 3 2 3 2 4 3 5"  

class gen1:
    def gen(_):
        Z = b'c${rj+iu%N5dD>Ti~(AZk{AU76h+dyLHf|V6v*?6J0jO6ci6p%R=&Pxb}3qf3mXP4?arJzm*H2jKix1GN*sa&_md-iF;7W`3k@=JAk!J=cl3DXa3O0hWM~v0ah_Tkaa?jDIZ^7Fq-En9inxhGXCB#???w~a-uVuPg5<6*hg+8}l!PLxTnohKOKgLgI7Bku5}OpsC7NC8X=0fMrnwg~fysG%17Id;W%0MSDVb+L(~>xjO90-GNn~?;ZnR?Hl!K27z@bO)tX7!@)3W|!*=qwWV0lV?+|fURIi4ARQc`@ggvbqb@_&Oh^!3W@Y`R!_B;$rMmF1X%T(mhDjtzM>p<JCzjI6!%IY^wiEd(AJTx%bY&t{;LKp0QiTMn~PEf!509mu-aN)D#uN^aojFc2W1AQW+W69rKv-BWV1&Z^LN^hXYLCMNH?z93-J_7yL=hzWu_vn2zW*79Yx)4*I<E#)Np6fXMpj=uTotS%@sTdh%+>6qPsULMwiQlN-AQ41C#(14WBsiJUR`3Ex!9BtGKk@&^530Kt!T1oZX(O(!;&&6VyR=meO06)Tdv)s?{b8Qq0Kx3`b<M2uu;Ay$84W4quh)3A^*6XRqSNNR^j#cy{cg|PYi`p4waPbMUc)q-`%Z793&$!|`Q<3OL*TiY4Vx?$NY(>Ae_M!u(9vtdTMcwCs@aC!Js4C-Q9;Y%J)O~e`YS@CSQy$Qy?L{KLiKgYVRJ?k8fzW^h2YG^uRKqv!==(`sP?A!L=_SutCh#|(o#d!(3L2n>t(S1Hy+?99cXHEtM?Z8dSCc)O7dPgSd>)UehcRw8M2mP}dq4=doL?6XY>y*}(G{I!KzM$mN4V5@BwurPasiYL&X=te6Gk+_g6|274oDGW-5awMBX-J1??!reAWw(=p7#5FLwkCtk2KyXyBcH|pmc>mYrIzIx2BG_aV!*X&n`CBBCGtrYfgd~8<&IC@%0(Zo`Q^Y&|tz+tE~^p<shw5%gExW9)!isO5f4n{DPf{wZ0NyDDuCVm9+(ap~6$7cYFL<sJJT&i6NjnVyDTJhvMt)s!wz_LCvt`p=7dTenI0E#;8E*c>38!3F8W1N2hui*XWa`+0n0fyt{f7OH?&fGp!2*iwyL=a&yD-TD5NG>rT2#@*P%DzZK`>B$kj?-7c!lhJAd&E9ggXiOU->S$&CaMZWQ}`go1EuKpqn!mI8_s$A7T-wZXt)dz20wtRhuD*&T8pg$#4XMZZkAbcK5z*-3b$Uo5oehvpX<paH^kMs+k-Y@^vPd?DYf5}SqqW'
        Z = decipher(Z)
        rep = [2932]; s = ''
        for i in range(2117): rep.append((rep[-1] - (2*len(rep)-1) - 1) % 2932 + 1)
        for i in range(2118): s+= Z[i]*rep[i]
        print(s)

q = gen1()
q.gen()

assert open('gen1.out').read().rstrip() == open('res1.txt').read().rstrip()