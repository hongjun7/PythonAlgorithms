__import__('sys').stdout = open('res10.txt', 'w')
import base64, zlib
def decipher(s): return zlib.decompress(base64.b85decode(s)).decode('utf-8')
match = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#"

class gen10:
    def __init__(_): _.si = 0; _.seq = ''
    def read(_, x):
        s = ' '.join(_.seq[_.si:_.si+x]); _.si+= x
        return s
    def gen(_):
        s = "a_i = a_{i-1} . a_{i-2}\n\n"; a = [[1], [0]]
        for i in range(1, 16):
            s+= f"a_{i} = "; l = len(a[i%2])
            for j in range(l):
                s+= str(a[i%2][j])
                if j%40 == 39: s+= ' \n' + ' '*(5+len(str(i)))
                elif j != l-1: s+= ' '
            s+= '\n\n'; a[(i+1)%2] = a[i%2]+a[(i+1)%2]
        s+= '\n(A_i)^n = B_i (mod 2)\n\n'
        for i in range(16, 20): a[i%2]+a[(i+1)%2]
        
        Z = b'c%1CL=eDCrvn~2847~te@DuL@2pN$0hZEk&f#B&cNElVss_*tWyYJrTjB$HZmzE%tjEtBuBQi2sg+io5f*cAr@ymfJCu~xg2c6iEX^*T@A*Db%rlya~X(_=;IX-S_$DueO?a0`R*@AYFIK(K?aKa)LpJWL17x~~8vzwNFl{8GzF3vlO92bu`Kk1YjP@LOeqj(TZIS@`8(0Tt4LQV)`4hYf&2*3Xa!I<i=#$-T~e*b{A$`b{XQtX2aPXQ$yD<_rDv{P9zds6vC&r^{xow()WLBd{8njF5QoDdIE^G?e<asQ>C3Ptx{$l*&rI82i?8dEgUciNPCDsXm8<7E5(MsZpB`NlJ3JbX)O-0q)tJnFre-u%troeY8d21wuR;O?B5&3YjOAWkXl(ThRsdwEK3m|Q<!Dtz)zian^gn-f!glXo}XIqG(t3KgC51fr60denjbYDM!-A-Q_WKU0Z!t{EMt;{8PZllHO`GpEBfrkFvoykhSuo@_vrcW#?UKdgO;-Yu$_+9bxOMasK|jnWR87@rosLQ}hce1E;yD}9O6;rgdV-=+Wh`QyaH-+e<61be0TKlfkyzk5mhzlZyMv;RW-{$~{T`<sjx!W5rWJk>wK#r(cQ1a;S#COr`96}-Pzy?G;G(}RV2u9f~72?$<O+OKbF|GZk<_ifj&Q~xs?o_Z4{#s1un0NxKfGLFitlhUrhP`zvv;PpC9Us``7?bxL4d$N4jV=3;0U4Ms-a=(|1t*e$M!-KTy1#CAi)IV;6=xr~jL_GV6DZZ!m;u7~quStTgHoa7pRrc7W@EhF=NACUgV7|k?>W8wS*6N2cvaVM|k)3)=(jY###^)pb;Uk_t_#Zw7=lksgo<3;u&yRHaaDMpUhmS#)%TwI+lcRg6^eT^g<k<Z~aSvJdx)l&m>ur<TmNEb{=_sw2l-MMP-ce|A4K;n227E&^IS41S{|tfz?Yp-2rS7{H2j--I1|25p(YvHqJasg^0XR^@?fWkE^R^khv|vs~-&HTNU>t2g4^|H7N}DTZ4@$nvc~32ImUb>b7(yqM0cnRjvhN?v!Ku=BazghBll_2&z8$QP;Hu;eq*4L+po5&gu>*X)8#CDcf=9G5fF$poyf-l}T=IU5!p*t?y&0if!x&!c_E#zS0NOpVICqBbdaO|Jp&3Axoh4vU){8y@J=Ul;A_qm#=)-M=VImPh4c&_J)(onaPfzXNYd^T*K#c$O_U(pb-(Gt-Kf}RFos?%itvU&Kt$Uu~-R^Y|dNq;7wpa~H_B-k@7>?VBaW-g(fgo^jF!p(3+u@m|&&9)#5en8lUy}vUs`fxgyDWK<!!yIpjvSteY*?@FK-YeK9%S5?kWTeKynx4RKt)U{_+b#wIWv!;LsDzz04+y|l)>M558~}Xh)tIH=Fp<P0mvW?rMYW%psnb6vfhIn(Q25gQ*5sOc@Ts2F>DAx>4{S>L*Ixv$lTC(<2<1^2$Tf0&Au<$<oZBdJ<(j40f~-9fJN5#6+mCthS@$Z^0uc8ihs49kxmi}eed<jZe|GvBUnHQ4ASFB73zcbWB+s=`i3lK54=i=lzMp%_CRbdBqs?5RpeRh?uI@>tLVjB2i+R(hUbR0eTD}qyApid2lEF$e%KCLNK8k53>t0rPZ8k<E^saCJ+&OrAG<+d)>8b{Ah?8e$ZJqYXez7qFu6wGAJ>CiLK7p=puEUo_U?a@r<WtI*XP4Olcy&dYj?r_l;=G}h25gTJJJntkq7g~4T9m`AQ_A0@u?lgmw18BhtU{>r1tNCb>$3kP$IS3a78{edg+!&ybVdmPaho=f!u;ded}D-=wiTw2#fG79ppV8>WlH#Rt93~pc^g#i)Ju9e|ltfIW%%EmqYZP!d>ZLY_MZal)5&kDWKbA@D`e2NrtJ0`N4X`WrKDrDwFY{5y5wZCk;I9rRBi7&ONJKWoQ)Zj4)&y?`iOFzZ&5EX&%3C4By^2hY1e&rQa9d3VUCC-+T-BzBxRC1INhlY4LvGaFck0d-yYsGK~3->chA9b7x`RH|M7B*5jD{-|w66C%$hEE#EhVxAlh6mlp3y3^!YPn#VG;X|CyeFme)xnr}v%=g!ZE7L20^H~Y;nx0JEp9?YV#a(vH<>;wSMho|M{L5_^~0A#d3@o!d8wD94*EzJ5291TMzthzo2Z$!La^2ZIM8cSVZ5Q5=6&Wr|YN0AwT%wP{z&B<f*&c4=Bqz8kdXh_@<Z}bx#gA>Yo21@Xxj{~p>@lIg$Fj`(VQ7yfJ$X44k_I8s^Yed4^yE1tHM&dZ%H-<IPpa!<*L%&g6{BQGR?+z2$Z~nadE)%^qyV0|Uqz^*V_J&#Q-+Jw|z*OEwxM6GSM8C02g+BTk=AP^lJ!;<SKNQ}sjNcIi&Q;`1qa0gGJ80?smNq@SfLHeJLkKr``!=NjJhsJ~_!wEz75t6J-RZQi-d24uKD>H!Q>=E?OMXKgB4cg!8IisM>;RQi+BA{%W_!NAnH&2(BA6*kNDd>04^i#)IOOj<ibTXG&>^u&y#XxmwtkMj5tw>G^mbtfZVpENMsTi0fMUM;MBDS})4RR%a8kX01a7q&R&Sn@QqymTc{@p<rR%phI?rY!4+(0I1?`+3y*G?6CrEo;-%#EnP*}d1OBAo!BmL|1<MeVS%=7=k^WQ&~v4=tb!t;Aa-#vF6_0OMweg6m_uDMVC`uzBIKSdb7Jpb*51cGDq_00^_p7*cWn?sZ4mDm#eMwZ5Mx7>VNpS@xi`^^rndq7ul`=*J912d;Lt0sz_6^A#Ia2<awSLAoM9u}?+pk@6=KBY*-wtD9cu}Y$x`5`ujEa>7RIkUqL#)sx`2|2IZ?{07J-mX*WtDEzguvBW|+cwS#J<{--`sl23E}J)rCN~o~%I^vD8)a=@hP*Y-s^^m>zq`G?`~*LJ@D1qLFm~tsLw#ks1;ckYx_DGC?Ja^!C6##maHL`hTK3)T&D&(#uUFoRisO>`tkZgKWys#XZ!(x$3@rR<kuELX5`S8}^}4i(rxxT_i*#v0Pc7o5Mf&0LcZ*L@nOme&3ukHZzW!<Pp5fAhoLanXHnwn<7V*@A{A%&J{%-N<Ik#}87WC4B{Aw}82I;nkPS<x&ouYW}O-Q`QlTJdsr<L@JWJ>=`>)qm=QpLsbf@iGx9=+SGyeIyVT40@F4KzHkV<An6$H`cx{zyNu5WizEB7fxDppgPt?}t;Vxu&R(9lJ{hsMoiOWzl1M|9I;MbSTzkKI;Ih=KZ7fp1jk&Kq`md_$Ic9)WGj?2uMq=RQu8K)9TFP!?CHwY#{oR2FvMQ)INI7^D-;P9Hnl~RbGFTcqz`>v3y?+%~;(DAI$~#HEt3go7}`6@8KtlsMM4QcJIqjXkI1b1CA)6o^kYnqX+c-^SOL5#1~+H%n1tdU3uqLamNGHp?gR4R0vQwDnAAYTn?(<K|O8Om@j-Xp5C{F3;mpOimt!%xemVn`^dQWPq?;u&)WI?{O`3NWINa8r91t%x98t?pZ{L_L4?oG|1It5^`(@|6ZY}f=j+fNn9qZ5SbX!E(P1S92>G`|q@o$M&#Om|SkmH1_@ua$qwZkvL#t7JwVx0B!|hyPi>dhGiD#1|s8@YB0bTLuSN?%KTVm1)|5!k&I&*s)xhEpE^~V0NMY_Fvy7-&m{f(?$MG|HGA-I$5W!E2<?*BmWK3r}>j;Q3n3jU!G)?Ob;_@4-VetTtdeU?Fj{Aa=GRBS6d|GVICQvgA_R+V1_|8T<^iKU(TF?JI^5WRsut+t%hT)WTD;);jza`Ood=<bM$yK!NF)kn&sKC6x>CN79fzkiMu2gvZ){8%h>k*x=P_{}9-GP&G8tRM1<Ew|uDxjW9%>eD;4#f4`xyR|pQ8rYMMUG`B>KzU^_EZm3O#fjEj8-6sJY8zdP!p~G#)LKdXlJA{?XRox``=6<BG?-o5_9On0dOW31Hp}<xM>veNPr6YxDR#SmevWmBN!sKSkl5&mfoJ(MEw8DlBc*?)vWlInelb4Ndc|OU(LbuMr4YD!BU{>Tzf?JxW85#8>JERV<qC(EL6px_g7AtWp7E=N29br3MjD9!!$K*CuER42ep@K|+)?SLkcisHQ*8%BnDG3G>*pg~)70@3+7UlgLpc9f)q&e6lCB?!JX~(A()nkWYrXZ1bMP7G0jc$IkA0#X)~`|w(tkgh+J;8_7~;t==M|<Q7T|wkzPNtbE{cAv#Mq4|Q{l(_B#)6qxc?~K5q!UnK7o=1FX%A~+fN#hVkSecKUppv;f?^3*(aO0dm+m@&?n~XJuW`c(MRhmXR{I>=aH!0OA~76j}qnWL9>}LWx*bY@RWZRV-5z|_inZSMS@TE<dct`y8WaAbOi*5TQvgWa`JWxPyaiLcOKpP29*2%J;lEREXx$;J^#!nDR2{KpP%%EXN;;Pit+<+X-n?8&E=!t@R)L23;W!mJ<r)h4{&0?6KJl_pNTtJbBbj4lg*|s<acqce1=Nbg_7-#ACwA-2BXjs{V1O|aynC(&rpSiuB>?d0R|Nww5@kRKSODrzUdz_CQwKF3FYEPUpXB_7LbfWtTLR9J^M41tUM#r(|?`sXDAV25k@)xHs3dO@2{pP0M%!x{b{{sE$%ba&9Jm*n*1`~52d6RR3x$}_;tSTp+qrV@7C(b9dOF#1S<SF-;}LxS$#cGzs~o=1>RnSh)=;G&LvmoxcfM(z44&*&irG(J@q5EmfTRz_k2I`FMe4}m4k;dQ_)qoSHbx+ZgHm`u@IOa^z0pNy;ttPHGKO}1Y!b_?mvkhrFC3&RYvM^Vq^<v_fJD7I{LsBVfY^!5?*@U3&<F&vWtxQ^=q7qrHS_1U_VwM_V%gmr02&eGJ41HOgd_w1=K`j^bb4<hTBrD8~oC6grs&P;zxY@wc$rs#i6rY;D~+rY1bLrDcgQrn1H>`^W+i9u@f4!wWt4VNO8N!at<#1Yr_xUG&Wtm4(vy%+?84TkF7K6N_t(u9NT?p!IJm_%hw-WanJ_1x~e|r0ap4*tn5EE`~-`BNy>-k)h9DZfu;*zN;?KSa4Ups3m+F@r?b&M+;Q;*kS$H`o3X;z?GKgPJIi;&j~ua#nV|bJ#^qv{5+{4*qaS#;&mvF@aul-hyRAioqY^kX3&OM;btf4iQm(euND3I6non*-Q;Ub@sV2rH-zDCyHmec3v<Dsz+nYKrDcAX3j=RUFa6(^D);zN3aSG(h(OzfP`VgEKA6?hfM)$uN^?GA%;Bg&`KUA+K;LmI;%1t1W8L^zwhEvc}*|q-`58pmIyX6SW9A)@}-~6?D9JA}Vd<{3b=34MrxUJ97?SQO)*Wjl#?8FcU5Y#XF9IdAiE(s&Y-}L#521j%=nnU*U`b~o$#7T<5Bb9Fcroj)F-Yxq0fcRhZ`H7}{(4Ow6lXd-7pC1iEcUQz4%=%2Xx>Hfp((SJr{NS-zTlp2f!@p>7s$1iw8=>nFXNjsLS{H9WQuBB7q$p}Kwv?c)K-C;LM$`Qsg7joGXB^=yc0HG4k^CZRsp@0=M^8K`ULm>KjxaoAHLxur_+!G*&k&X^_aFPZ1QV`oC>hZeq6S^T&BqpTt12g`U61of(ktmn@@t$)CZCm_$tD$F9}ZE)+*meenL1=1n{m$C%Y}FhpRjj*iF*SZC&_Urk^^2iW^}@yOKyNT#=!h=zRIiHbDZ--pwmdeN3`EaEk*cdOtIQVqKF4SA~TaS%Gd)_j_yF<ZquPt^**h19d@Fzu76L-%!|P>Tpb(yeB*$L*QNT=y0|uyvN`Mnip97e@i<()Y<oiglVQi&PGLKC+OGaz4Evr*a8`Fnd$4{t?0Y5<0~-;v|4)V;Gaud-(qf(9pVZ!o+%D=Q^f@Ip1n#(<%8YCmMl>$HeC*RzWOiuqR6fha;qXbZ*R8@EyW;yhbGWmkF+)-EW$~qqQ=yN|HAQdj*mVWMO}I(N%!d*zP2R%Sv99${WSs)`V;D{iVh5mzG%o2#S|>`5#Yc`1UbmoVcxY7Topo=V4U8Jgb@CkCMDz0;8sx8c;03p1*PV6jxE0Hfp@=^^1ql^n*Ba>;i1c=>6Vm}iL^juqFiCRF3-OCJb`@bB1KD{iERTSF_R6raq~}CsRaT=LIr%-~bTBi<);lRdp$-_6pwM^%G2M+T?Nn0gCwn}ZV^`OO$SRb^uI!$V?ho%ej*2Qi9;lHuc2%2_Q!a2dE}S7ez3QkjdYy7hL({V4ks?yRzPbEeAG_Wv{r1rBBPYU&y5B3fHFhmphz}!$9M`^Q(1Bn(oOb<05kGh&KX%<)2PZk*^bz-AR~*A&JE}0lUmV03;e<2)NZ}}`jWW;}eA?1RJHlfVtYSdEYa@W&mNb1~Gw#Kaq2yAD(M@iWGg_+(H-B{7M)EKD5osp#h{5w1GR$aKx6iK5gcpv;OTY`cgJkKWn0}?cId4?K8(qH5d^GX6V8kUKtU&*P9>(dqX~M55Y0N|TbmQ!5C_ayXPbvR=5#wf@FKqx1<bFtgoG(oXo1MrY=ilf1kt1ZTB^n^+Z}X+6!Z8dznKb=vzRr{utf=t**p5xJho%9iH2Pz{Z#kNMfjodN8C_VAayL3V?kKV!HVzl=;4wnQ%<JOQg7D{j-)L>!Xk)LY3ON;+Hzti9Kh2lwW9=$Mxl{DReEa)Z^0LcIIwrvBi_oMOgqc6imnW2*K{rVD+k7Wa6;}D(x<S9qcZ6sd*YpK=kYkj0L?QK`WIM7QnV%A6eHHhkW_w+%s-UNkQ4Zu$9YHl6mytB8T+j5DZKth(C(%A5;yIbA&(@L^8;_HU1&c<CwiHIyW{Poo?FG9Xo8PZ{@Dy<P=y%~Ee}W!{kCupBW<%c1BR~3w%t+WlIZgBrkwCgKjfwZf`odY2DvWs*eUpRZL)es~(OFz>f~^3JF2Ei%HK{k7i7aAM)QjNhjJCN|BJ?;Z_U{@T@paf*0dsf8iU673oMW;njA_?I6U(0Fn=udO?eiTyoK9nDg7z(dt|C+%A;j#jYVka6Mu(z;J>KrbLq58_d<Ht6g~id*8LlhnX=jglZ48)?mEms2!mLx*Ysd$H)o8oqx#9CPa>f*fl)$}zd}{ItDnx#9^3~prwi8ke1SAg6Mk0tL@fFzhSh`6!N>SVJ$s7}2wkuANwY`nuH$8|}Mx(JZn)(L%-E%G7ChVWetDA2gW8Ue|P<Rm?Xxz5qGdm?Jft_sUp6J6We4mngOV)hK)!-Nf;_)jqHYdjK=xEHT`KSeF{0dG9+4vP6pEfn0Lfh2*UwIn&+taA2`S`SOYCb-GYCb+~Y7UK0o0^YRd3tI-ZL3Yq$EQur(f?nO|0gOEngZj&wt-cB*pIif&GR7L_H;A4p7{RipC12C`<_KohR}y|xBnCEdx6XM4JZE>+Q0Mpas1tXfBTQX!;#`fEy4fx_8)=CO*tscZvU(8$5oi1@#Wrkar^)C_9K3(YvxeoS)X!{(m++&?H*$Z!-@SZq3%{rG@UhIKnfA~tes94)S^YxRa;t<1xb08sU|+978ws*u<~48#y}Z!D`SH;uHB9Ubk5OFt-Cr6Ky`QB^J|?NGlJAGHVqR-+i`%jLsubHfWQ?0==fIe?m_e#2cQY0wM2>R#sMhdV!IjvugZz<vXF3}5HuNyudb*BbR9DeK>NOXBq{VhMMd&%X9>r;$0>75_<LKP&hC7^LOPYO2f0%U=_EVy^`uUvGwtN1Fnnmja8h%~NBfk4gK2pc3&e@PpUGg-0)Xk2vORgz0L2YJBi=S<HM18nJh~@p93Va3tOpJ^w`pzq%D_fGq9{CSfflF}+G#IjQnPvDbxLL~6H+#>J9CqOEjnr8vCq)GO6(>zS6j;nV89%!lk_FIqt5FpmZO?^P}*EMH`m7j_$wc1#JLQoyz!z{0emoVb1If>la4s7Kz>ql-5nC@cG*u^Q&>uPh24#5fW$aJFqaGaNzGo}bs@D@g;5I$gr8bOF0gTc<eVps3`EMLW(r2bpz*YJLbEC0FVEWUCoSME#6*QZ*(s)9ro|<U<WGixr9$qK_K=OK9C^fB^3~jdsRJBpD?^f?sf3X3ci=5znB&;NiE#d4Me92`b|7=sRMeKddlMe}_1gB4<UTwinw7Yh95pF89~HW7$&Kb?Qy6gaH7mS=t7?q4aj$!}1vAl@I*8Jxx-~^Lxn;a*+=yNa@U-SjZYd<=*IP5ygTND{-AM_ZRur^YCH+c1ZfD)`+=1~B@H7cg1>wHC9_Qsd8Ergfg&LVLRp4OtE}h$mpFsP%ZL$~-H@m5Xsi-!sKo4rl;7J5gP4B@(6A0HVwS`ykV_L{irW&glxgv#;zze$d3F8a`6R47$ryiAEO$gvA6S?|g!?aUA1Br)Z=bhIRNM4dfYbb+EDTw22)ItJQ1wG|gByqd*dzhV`DSCkCf&JQb;;82{@!T`HpE`tSV4OE5c$kF9@dGJgiZGw}T5nzu|4bf}zp@at_hr32O{?P&-#jkqR((v~vwqyG&2e*`+(SHW>c-x1`~*CXddWIlI*$p=CzSEeM{93R{<Ph7C&bv@>1lC)g4DaVmxBq+<?YU>xg|{K&zRJU2=)R`4iW|E?)G|)2g7<BpnfFKk0_k-HI4@Do1}{uVUj|o+MPl3Pjupmyxe=~jc+Dp#rqIa10+Z0iHJs}``tw`N1XI(iZc)!&IOO!2yMzZ-N0Qn!I|0@dS0y<crsdJyH2kmcOsM6wZ%gNt)?<&OviiotYgR9WFvRuhQ7ss(Ih#=)4I!D`C>l0%^qNbmcnMT8ilRcXWiWFi5}cwAE<y_u=-TDLF^C=VbIAYJD#5P;e2~x`sAx&`RdbJS)MXvGIfpH6-AOs@|0E_+P-GQ<nBaZRuG{cgsIYylBZfpfLm)!lD8G<g%JPQ!Flgx1q7L)<%#;)P(7J4G-PuGPyI7P4Ugp-^Q044&GG++p(fCI+NF8s$Wi~Bp_1pp5VX^&hJQ9xZ%U(&@Ec&&>i@`4>Dy44y7#h%!~O+B?MBH7<B?tv?CD(pVknwqR!7l0oV=e6HPo4{kOYKN4o)Rt-jn_2A+#Mfk@*wrYU4~L)25A+m?!&QM65pL52=YK>>Wyr=adg{JKn|~hm4)mD3EihJB+B4=^QJmH+^Q5`4cf#SNQ>AFU6nImh_b4Xl2Xb96z}tr!N9j9Vhd`(%!*hYs*c6hU7#<IrkbMr|?GaBl@oQq&(qFuwX11Ub%`V&Nee0cV#L;r<i%;j`7t9x^VLE0(>zxfg;Rgoal_*FNvTzvu3y5j=9RuH9nb3kcAy$D@Hvzh2RnTfpRqkn_?OdKIt4xooZ5TxzD;JW^eJRl(-N$&!j*hn2<z4)vH2QJ8mj1(HP+olGZTX1QQYhJ2_jU?zD(@x?-2TeE&Wb9%G@j*>zoY*33q_v4{48<4sVakGa1}^x@#dw0FmDcG?4<d};8uDtM?^^f0HV<f7=HwnHhCY8$vwB9*vITWYDu`@nhA(CN%2w6HV49G`YlX{UlD-gz}(KIbE^$2A2wjGY%E&bH(-R}7}KpHixT-C<fMOrhQBvy*J=J}#3>IwD789t7~w<WC7*5T&w@yeVIxmF`7~q2<F9Hz=v~7-m^cs$Hv@Y6l`J&TJ7}@=Dkp@71i@y_jD1rwEwVC@t$93A(*sCU0RV$jVA6<Y(1(Rqp%FL!LuHVw&xSYZGz8wR0s)zRQUSp8B{CAVhYhV9t!{C@<@!Ck127CWDe2`Pde7VVB2~^W%|L-kkDqK;4~Jw8>5d8;UYou2$)MI_4PDbrf80)oo2rF2tZB0J^f6&*Xi0=6+g9SAM<{!+r}UTsFUploq0a9b55J9~`d00nynt9?S&i-ow<CFGV&d5q^tC-9C?aW7_7xq3l?|PYs*{y7vN(@sm%031pI_sOVj+ftg%2sl!l-O_YfhGPtI0C?QCX$!_^Bd?{w$9LV{Kv3lI@b}CORwHP3-4BvIz*VHCWWlG5Q>}A3onJ{W-U@J17uRJ+nvm;T(ny&ckt?=5&D`qNN)1VAq4p>*{li$!?#p(B25vEKu?V?u^SFc(VCJ)ubja2~o^E7cqb}*Sr-<!;oYsN96acAB>;FI~|dly_z$gZ;I%tfeZ?flZTnd=fH!%*Mdsk4g)&{_wBB7RO}!FeF`V(+eZotT+KTl@mGE;mI@8oO<~`{uTpS3eZ+EJcf;ENk)%*0pYOpEOdFkH&|Z0`1&Uq6zkKBZVz=q>g{O#zfXmM6K3Eh9|`2EUsfZ@zoAr%|COE&y|<6YT(m#_k(LpS7eS~NgLq(7Qtthl>%=emZ=xi)VGreJnUpTMMUwp_$7wC96#q3*C7`bAbIS7Sw8Sy60ibYsM!~uFobC4F}qLGOjqLWu-gLaW?njA(p^=W9PIug&meSu&aM`Jdtm=eo)KMFFG1oJ7ZH;@e6m^TH!>(L|5%=3a!itVXRu=LKgly4I-p41tey!w2mY;b18&h}pUk+$T^l^1C8_>nd4`AMtRMD~e7*Zgo@obUubqLsmWsd2LwS%6QHHuE{;@p6!(T8+;TGBmKgcsh81t!akQcpI{wfbmZf~rTu)}-XKg#nSUkq+^-AdARGAUn~-YKZrr29dh$tRtDDIB%@=M~`}<#A#_J=BJF+V6gr=dF)!6B$_$$lHG;&qQErNmfng39cp;I+2X)9*sx!%${{did){k2|vs8*+#v#Lc7b#>pzlbA_>a!?gEpv^z1uPheck8U)p(fpO#vh5L$Pf{WQb94As37m?`VGZqBdW(m%RQGyCc`Z9x9sE&jC|^+z}Uk8aMd-O@k0&0%TjHpj%@y2ZbCqyFeNE<(S$javDmoAYb8^p9?Dv3~6q|JsfEquXSZrQ2kb-@7@#c1!>0HfrU&Tl{M`>W^+SCgyI!jEP^nIlp#G|L8Uu<*VChls~$~zjmYk=*Iui&H1%k`bW1J6HB)_H2l^r{<RzRN4HTcU)`p>?e}iZuier=y1m8vwOjmaH|mdWlTns#Gq?QV-LVv23-3rm_AFA#-(OC~2cHvx@2=4<AXhs$@@D}O+R{r+0oljgD7^7nsz3=?E$L28pbA5oel_dTmb7OP7tTT+jRRthq*D0ONQ}TXC!Ys?T3N=FFQXprH9j{7NJ-A*@YT-{U$8^mUI(>IckrwPNy8J6dZ@vSlnbuFgnEEle0GB}Ye2?giQ8N=adYztE3cC2W>uA}XBqJGzPwcG_<k1g$Xf2uSqt|fKU{7#fXt1ahZVEixgC(s1(-{)@!+P2&)8BIzitl&Atjd?b`@r~lFhGiY*y8y;1BGBQ@t5vc|e<o<7snT&Dr9HpePm6wikOwVsZt@GeF<m+07U<-K?JU8CU{*o4n+kV6=`kt4h)nz<-pjH?O?8D7zD6*Do7q7s6!kSsrE1Uije#$b0^}ZlOh0I~nLo7v8)UHrO0_E%xi|ILBf@m!KP)w6{6!j!T-2W2=+N8N_)YMC)Vnz~&NZeAN(}(Dv(iR#oUSXoAVt3qGr=g0`!grVfBSbDfCd^frLQdS1CQPC@jxNW|UTNWLbQ7~N8$JiDm*lo;>UkcaDBKf$eg<~FH{&ko72b;#xUAjxM{y@btyg^_wXKREneq6R8mkA#?+TO1?om&%1~J!e(XE9ejhDGM#DL^r#oMDNVdLX$0ie4KI24`)@~yogfC^&MFn9dXvt^Gg-ZjGtpANGiOJYx9)5%lV)i*`wxWo*-HP3Gn!Ev}S^h*BAD3px_dp0aLhSELSpdBWKRt^d3Q50pUI7<$;or4_R>F7@X&ff@|ymWL6%`tmk#>*Uj0z3~koCg(oY|)t$?-pF{!VO%ifjy3b{T`!T$$D~Y7$A~Ih+s3QVJFQuKs)7pPHwGKhpyepB?TWpgZ^9&AW_@TGvptUAd=yQM|S31$0nWwp!EDu^hUTLK`Pcc0JUP3>#%kwp7wT2~Zj+=m%h}l3{#^26R4BhaVuqp)FQT7Fa=Sl;0Xs-bil|kUoPOfDzdhFIla{P;h-de;U#=?QK^VDaGjF0Df&1O&h^{0jIvt^-OEakv$UtZ_1KqlAnNgT;&E>-kH5>yYv1DyR}p~<qbsEXlDudq;>AqN?{Z8*5S+t1EI<a_U`4pqpXEHnXZk9m!~+JzTsCfr+fIFbCF+|Si)GRZqX<WJpApDlY~kd5Q9);^kp%*i$~C%cuUIj_r(-qR!ORqd!VB|%6in@6y$Ckyq{MofdPOgWE!w9qKNsGRRFRK$z9s_c}e2x2d~;)QvgwYDX4w+EH1{n<hvEy`NK!9h=<-b{JWnz2d?Q#Z<-f_TpWyygg{>wmG(TZ>ZS9`RV)OVPZXpcK+FE$1krKUioEl6mn;tq%7u^Y#sm+%yzAHof*|>QIK$K;Cd7XcoeWq9eDzVC%0;Oqy;6^Yf7;=J{*pJIs<oNjg*I>DH;16+&FmULOFNbS|OA%a}6}xx+anWVoKqqM042btUd0b9tI~Cmk%S?83ktc*BP&H-nnTptupO6m!s7v?0pI2Gz#ltc|ZR7uBXu$M3Z0D^p#@oV8sHhfH>M_tfU{?)R884wx$O5T~O3Su}ATGo3{{4qw&bMA$4^P^w<Jhq~oBw-ZkrXw(w#-CnO5?deQ8ix%~YZ~z*L7rqd6l0;>)SHL3L*O)Vt^#<?CbFY9UV$5UC<#KxXy#aRJE1+DG;$_UGgvg{@ut!5O#|LK_a~5qu!jj>BjXA?=M&BY@4>Gz}FVD=dqS6@&vuNiwj@&pVN$4+#e_wQ&9%O#gE4}(ph=243-xPxa=D6`S<}6ypfd&NP4HEq`#8<OuUt|7^_))ak%l<?>wnXh^%)cQ1eR1)!{~F@o7xOFVgCW!_U>=ij@5VumD*bDP7z=K`31y<JjM<*KM}om&uL9<LDZQ8F9)9t6W8Pn*<QiWQ5x}cyI|J7fuRRS&`z<}|!wFJzkAP++OY@~XQ`tz%3SoM$ZBQkC_YTVQs;%csly@-vt668wvT5tdE0Ba^)Z?a_KJDD`h-hAqlqqK7jJe1<D%Q(7MN6$^?;N1r-c^m|k_YV6EJqHIF&D8&PZSZ%TVc?=A4C>y81GX3tevts<h3$cflk}r$@vo1>S)Itx1?^*$t<Vd4w6h!SMY1?7{D3HAEm^c^Q;&pcIBPqfo-$cFy9>vSPv|ynzE|YI1{)J9qIfvU*fIXRg7~K^sU*C{Q8UouiZ*~tLZb3?1_<jL`d)grZl+v^)uOV#+(DDjl4~22xHwZ=Di%kwHT&ovz{-JrAmRP`i7jC*~e2<P3bVt*6p+p?ZmtD?fhC>EELZ`r#Iauvuc-8cQa#fX2O;pLNj}P2B)LM5aQG)jau-kR_gX?nj(6iFNNDW+=;ZEgY#k}mBUt3nO(46&v@nVJiZ@QZ;LWBUY*xkY)`^kl$U+5q7?7zqTC?iQh>XghXBXf*VT8Hh{6fvDpptWypc^mNyyC-ce|FCHHl-;6eu{PO3ip3PD|{JG+V{XDz<|*PkkRp9Q;)q3{^D8u#3vfmx!>-UMj<$0(ilz;ZQ5^>EQGEC^AXZrZm=VcAa;N<5!6RXi042X2I)jrQWP{0Vv%Pva@5#l4z@v!BVvXu9f)^9n_l-z{M33?y$`(0GDD%x_W?5846?Yv82dY08pU%3W_D<#fPg7w40jL(PhEK#jlO;H{Elo7Di|xo>-~%kqHwNe}(n5YEEvxU&1B9K83(q-FDJ-*89bH)b*>46+@Uk8_YBWLAT8goDVxvd`Fv*w)WkNIp?=8sC^xAj^8BaoIfifMncIAP3ncPo0Gm$?#Q7MvzhB<6f+wIbRYZ0wQHWgU~Oh=m&F-xERq*Tc-KDWeLUw0siGqzdu!PtA`7H`q@qQo$GMWg6Ht>r^CM)gr}xBC8tD!%6;#QToX-@{YvkhaS3e+5%d)vKbQ0$6j1b8m=R4*7N+syY$#0=zDWYtS2DL?7!YgKCjHSoT^#L1A_vugbooOYGuvob8cc?<=`PTdMSvprw)>!J%(KEU7uY!b{C8UNTyIv*MRVm?_^N@RTy_kjJK*C?<`vHuoS%pn%e3vb`@n(hHvqw%{&*tpT?4y05>&h@Y`sewMfZ-^=J)@fE9H#d@`M87|5H+*Vlol4rYGx-OhvC=D%~X&DZhLp6G>PVeUgY!A&^Qy>Zm~cztZAUIS0v5NCm(p!Z*>uQ+{guzv=;%ja(>;A;5q{amVB;G3G6^tf0^%RdaTuyt#MQvWUkl5JV(fZO0L{xPcG(R{d{MH{CQb8__lF^15U-PGK=gasb0&ld%OrsT&}YOJ3tntu9g}=R*HN?Qy0}-c0BTnRg;hW+=4&OcV3D@Sdc@6@=}s{6PONwK8MZWc6(V^ZPUjtM4;jB$N8Fbq+^fC>(Gx`m%AT)dWK&dT4$7v8*ZOIXRHzJ<8f~-5>2BeOR`Sq)vabb(VqR%Dfp9NJ5QEh&Ja=Di@Z{%V^B^w112>@C+ycJ5`Ucuiws+jVAB_|r=lg?Q>u~Xcn7QcjI3A;895JS7+yA@c?ZF?q~yE;TT*T+*g&MgIX=B!>`AaiK`3p6p$ne`%IdN|m`7`s&Df`{r+tZ8-b(Eyf)a7g2eC}T%RW5qJ32)ssp#Z0Z^tRo!Q_sJeIA_+>QtVOVK46UtHejS1%nhb$_*QNSxd!@c2D=igqB4kiHK_aaNw?r7B_Cm-A;EoDvI#gXA^O=wPoNLd=B@19{FT9iNRY>dO710w<s+nlo*HnQvXVNgTU#|(dorf^poBchHT}-2IE}+OpqulubzuI%R)<rue%C12sdBWMuS28c9;<QKZmfHZwtO(Ot?>)FLwX8B5d;U%*yRLKJeGf{%=Fr_{duTiRDW=uKoY>5jLOHPif<U?l*gWySmOxeV)(~wZt*<qRr<d`=QTNed%s1&3-I&T)8w&K2{qmU8p>E^jC2u-PFVu=<v<4zTnNu^6Uj;y-fsv&BQIYB>W+<A?qUqoq2XKj0j3)he*26$%}FsFgk^|ZcT{rY=xvYUF6~=R_HC7ltH`W4hFIZUQ2*YCD6qi9YmJxOebQxt4H8@R;o)v+jzvodX=EHUluRqJ@NFQB%M_-A1mv_p9I5|9jV0pE=8Pn7Ra+rl)YGBp>*69o`!^|^l6@qlL16n*pRV;>LrR%^!2zBQ!Z(rOBLlVxULWhWw(UhxQLA8y1KF#TU@GV9d?15GNo4Qc43N}9-RSyvs&+#ZK8})@{~RRD?VP_ix3^`!BKKT<qOmp<aIt@krlVyEtu?Cf-|0#<8%wG!1he98g#8Q%h5qcg0<EQwvG_YXEkH?j74=so-@*({fqWjl;oYY3lHiGta<|mT^(L-*4M^gtb)=NA;4e>GCY3uIkl;(tb=Eci~IG*LBJYBT>L$yHE&Cp4JDpW%SytJdjqn&HP|qVb6+@^c|ur@*Gn!!-S+$`RxfZN&no9{s^9?zzjBe|0{%D?J3x+K0l6e2yv|7qkMnI{EwFm5BVV+I`)WTIpPblB&p7molk;=gAmKOUdVAcj&ULXA`Knr{RI<B7@p5b}Z6z+-xA88Bs)hW@V7=A23(#E_@b|3ZbdgDMg16L6VOK8zFsz+wNv8$X#R>J~3EXL^QrBvR*(j@}tg(Rq0L1Ecivkp~z{(9TrRCe8z2UyV?}D(#c@1bSDyOa?DMyvA;k$(s2?Sn0xf~4SB?83-y7f8+jyGF*0sqeJ4Opjl7+w~H1kgCu5zWeKwdgz(4sy-!<p%~Vs!RwPQ?~ae(@%@*gwmc^-{W(mJ{Hjv>4<RF({%RT0@cDvwL5fXU`$;QNDT!#2!axpTXJja4Eh9)sO7O)EY4^Jp*lChWx?5Z(iZLx$LI)g>}$cgkZf5}=Yws-E{c<y;&t|P^eU<gWfAV0z3v-&orw$n{mVrpDdTXtGmG=NHY7fjjk>e<3*G{hx2g+qKl0Q9_J|91ESI-X`&_b#+%ZMvew6CKTsSL3dF&RT_cW3g%w$jtiL`+o_sSCKqox)46^^W*?2<TU_=%Rww5*=H1t71IqW5;jf~(u&YOn2KpRNzk>9Oq5rd=fl2_|m}`wQB%zzH^#Gs@))v7*)+?!NM`l{N=HN}+ABMX%8vCcdhM2)kLg4VtFU1)ffqt~Rj%?e_NK=ocLb_reAy4%dZcNZ^h>`Qof)%L#fuiG0@zAM5>vUxGzu9AlhVS68lFDoV+EjUe$kaSVSU=hXG0%~54@eYH48R6x&{uuEwipCKPdtJC=^uC)piz5={!W}DrS*(<9V^6@J}z;1^XOng~5g`x%f*tKQ(eLP62RJkG{3NWdqATJ#-ie-{Y)SnCFm3#i+V)JA#TNE*UIr{eyyGSNIza8I0afO*eyV`@W5HItjZl{0{%ECJ?6|3}SKc4K1N?u=d`hTr!{{hASao7F`b>It?F)!5ivQ(3J@VYi^`&PowC5fk`NLdBGVQ|fnUNQwhY&RL&#7w>LMNHot8NrEIGIz^R*Y$%1q$ik#UkVlUO5;h%N8ft^lTL2NQ!JGFa!ZzyO5DQg_Mwu^0fPQ2|LAqn`6aJ+c5?EUiZ#{T%)NBF8CT9-hN1<64P{O=pI_CgFZuUh@@tMPWj5~-z><`UCmXu0SFc!k?7mdRUxTv}rzbr48Y;c+RVmCG<7=Uo2s=n2jZ;5|Y8lEq5cvhJWgxHqCjU4TYXUYws3Iew%YJ_xUth*;%f_w{EJLMnU2hGlQzHI9%0F!M`47-sT@6!z{w)7IR2XgCz1Z$o3GwBntMXCY#1$k`O9_T*z1`aIWQ&%*0KjU}xo`z7)TO1G6zBaq*CX-XqvIdtUy?=Qq`V$D_B!%t_BZ)QRVmE_iJ`+WcrXifM2bh<qwRVR?3a_8<eE9fTM|6IRBiD|U-d7@;Q*m>`B(YJp-#uVU2o{(Ftb$uQB%8Xt5<j{e64t013V#?zU$nth)2azf<M}9EwjNgl$=>N&0kk5==>M?=b;oP%Q^&L&O)@P3Ub3E$}5TxCd*I^q~57Z#9D$J|0ntTt2f(xHE<=kEbz1ZUn%^hp;#6o>f-+8>jyLE6XysYAInhD^9j&fmp!$}LUiP_U$2+qm6y-ZG8B4;FZoRh$p`nN{7c>&i;s&aq$M2Q_J5IoQk83hn@e$S;mh=@+;CNTG%E*#6ggPpbIdy&EaJIa67-TCB+uIkPwt)`p1#f{Xqvgh4@Fd$;=<GpxuK2Q4PO_ix9F<z{nyiMjTm)=#euHJ`nin}#kTo{m9m|>&&ckuHji`3YgpMIpMtxFi(^JD@qEvFXB><Vr<3%R%Ycx|S<;JXp)UwiPyB9|uQRI?^U-LEhpgCe^|j%K?pM+lHn&>tkVqD=C3=(i1Lf*-c@8(rPDtEU#bbMuTUx8WEZbpS=7}=qtIG;M?)Vp9T?zI`+spagK6Qexs_LUAKfglU3$ihf$j(`5V78ocpq-6RpR2vaWzn)97q_=vqSr6#0ezX4q&wd~91nq^J--Nl-B>Rwd|U)>DX{YoI}vlZRs#iGve_&_;9M<bo#ehw$`OnvYAX70q<q;4i6!FYc6U%XGs{thel@nzx2M{X#eDvq4rE-&@--08MkQ{Sgn{=t-@fp{VY6?)lEU@=XgEfFK%g(xdiUoel6OY2cfOcN(CG}9Zz-KwOL*dtq%4$DMqjY-l?Ij3h6bWnx?+|!E&aIrbX?jR@bs57KlYw$q199xz^X;HzK~p?29*Kev}|L>uWRBqj{QQL<B~-3>lb^;iJCmO%i((`Y40v>QZ6j(UrBu_%jueqH~wAu^2Ugbob?L7psu}8wBzp6EN?k%{0FN(Dl4^empG>=xr2*pIjg+pc}oIhy}bY7q(;a{9ufuD=hu!56oqhY$v6liUnD7Rs~UeO0+xOSX)%+TUAN8Js$FV<aaC@U2jFjIuUN8cJ~{?mg{~7zSPo!0MV(r^hCL%<gDo^w0Z*jR*Cyeu7M71m>3Y6H>sZ8IOYX$wtd<d{%0<^-3+jsL4tq36H+S$$wWnL&2`eAJo|oNjC%GbZVkPp)=IF2J!80L2<%$Wmi)#Bd3!B~^kKttYQq2}5K8wVBM`q9E42gr=j}UVcN=CS^is&A_nKe~r7gJeiDr_y$OG<~6@~`}@TfZz$x|8)QUuY`1Qd_lz+<K!d$8~Av{sOX~q;Ib_`f5unY`@^T%AsQ|CNGfZ6^F0uBOo`k1TkGGR;APym@>;jvXqlyY^`T4QXiHh12iegcbUVFt9qX=JQM2sMz&=@G^ORtU|bO5U4t#KNzgBMVo=gl5^k#n%S)sEJsfqdMg_wIEH9-n2SDtuRQ9CEv<n)OH4RsKKvI_ru<&)U!d^NhQ2RstRXnAX?pkx2lar@~mS}QUuuv0g#^&~QW{o`Uag6Ldj6UZJM4}zAZt)h|blq|~A*OS<LAbN)GC;F{jM=$mR4IZ?BIE*S;#AjnisC}<?*GL?Gv6iM2DQ;<tp>ccSctV5YHLZ6N;~QoV^aR{+%M0ZTTL%0bMy8Xfpn-!g8oGeRw;-KkihE)ypT|SAcKHBHJO?dU-<9T5;32hR8rZ`7IMDqX&up3^L#aSJVTO9(#E5k<aRcauL@{><XLcaJRi>3abcn1muSeYt`%F9|KgUbASzC{?w6lmTV9T}37_4@d#x$!XA3Q1E`2cW8MJJkyxsq1p}AOWStobJs;`QVmY^Il+iu+p5wp1UHDUAO+K-oeKX6~w2g<QDbwx+^T|Ix*w`_#Y)|^&zEcBy=v@Z+QwboQEe%W1vg-OyaSLN$aQcJL00s{M5A8!aP@(%BR1)6vl-6eXHseJVpkDURW7{=AC*qgmQSwCB7$!=&h2cy+RHlvFEn}w#<?(<Z#7eG)27+8|jFuER|j|-udXJwgiYHc=k_VnA_ULcv$l(r72XA;!ozb^M_4JHq>KxoNpumzID!KHUHE)iZQ{MABJYZWx>O&LFx##;iDSZ;KAeY2muRQ*ew`iF&<=Mosu-mxQPbhqlukG-91#rf7b(%{$LfKz1~o(QY8B$W$*>BFn`Vj47L>;45lj=aUk6RVU^{goLrMni2`E-ROJ&WGF@Qfw^e<hU}6FRg7+S8i|Oeq~x;;XFP7LR4u?arE=ArGP-N5|(ZgRE8J)Iq>1QrS4v&81UD+IV}soaP)2$pTEukxFHMJKq24obFw6ie3`pgku!pHA;>Qfqp7g14d1l&ud|B08DDv8b+&gJvSf^OfR?F&>-gFLzre;Dq>eP0ak2$;u@kkg{fJ>V=VL&BW#01INpd1yOW_M%v`l9m-xLL3A!m32K)TzmQp`WD&zI^;%e5aqbUiZYGy9diM_V>j*}#0M7w8LFD+s+Dcvssn&eswq+SEk5lR@yPe0jO+Z*X0!4KW)2vFmw2nIJvW!ty|&76Rfg&#kfrBi@3f<<u7?lIRNDU2G&YmLq~GW#(5?x)jeBA%6MIegoeCH5c!XV0lL%Zlp)ou%Msb!>`OfvysGjR=j61Uk3<dsm(}H){7G!!;6;VEB0h=>Y7s@%Lynljxa|$*vPZKw_nWvY|d_)hvjzTewCEst#qn<jTfMLw`kc7?*P@XTwBoGLRkC-JMi@7(OskVE8!)2Y_BsnU#ChrKbGQrId9JZuRrGZL54fvR;TVcniC9Ud}%p!cS5(eUl1XErBx_^idqQlE=v8yZ-=v(r?p8WNBb+irHdBQc$?s^kLBG@C)saGrY4^;-+o65Xox3I(kJ%&Wp~I){1~8UNms}aT3jUdfx{N(bgN0e*QSr-5N|`@eX?KMat@puN?@KCurL=QBA}arXE-c2kiRe|9o{xkCb%i{%)ZKj8{a%Mr&<$l%=s$~lUD+j-zyqGvah<c)siPD^9;=msYT0;40z@mL2ok1EJTz_r(mDluh*vdIvf!j<Z4sXr(D~h%LxD{(H>Tn9LhaaDqlg*;VJdpT%nB$d==!MDI+{LtIOjae$`c@3%BEvdh3O+-9kjp1HLy$=n<^0uP=+lh-}|m7g(E+`Q?+EuI~JrFjl2WEquYK$r=Yr=v<dyZtaAjw+Vdx45$RQ=#xJycE70Bh!apO=kQ|MGgi)3Jcl52{i2tr604T&nC_}Tzo<_uSNg%Ty6sW=s{H1G_<Ui9y<)EOZ)ng0vT5<_Ezp<u{!_YPPToNaSV>LdZ>9{xU9RIWn15~E^N~yL_7rhvOZuxwK}X#wLl_*9Ic+&7=R`)hfg|E!gBG!*Z#)TX&nve;FW&0<MMp`_=@lMa6H=Vt!0cBb<Pnp>u()5*^H;FM9}(hRujXMJe69Xdn_rz|&}6}<@s(nPtq-4K*f59)`|^3OA>hIXz;GWf?}0ffW?$+sDUL7<e3en0>Oh1r&)py1=_@?9b>nvz3|^5J;ENa4)W{&#mma0FyevYKck9I7vK1FAkFNkmZ$;%P7r@IIEA^ul%aA?;)k7D(<y;_5Y&CtSY`ud~ofhHJ?vB_+sH-befxfKB_~A+uQtYzD7tf-E_-+7+uvcqx`4vU|qfUh{QAOKWHvQ#Afd%Bp+kwT{$5#?AQcqFZ_$?mk-U6|hBVN31gfU5>(O1Ch2<OQ7D~XLLW3eLD^GQLps}~SH7l_68yW}T@?qBvn^<_l~)%q|B*6aOp)VBXX5qJ1~JQoRuzWA<oH=(of;$TIaUwK91Uvx%Tp&-dDXSrimq@-XIEAeWleKEp4zntZ5z?}h?_@c*7IB?O!7L{oC^#WT_U7OSK#V}h*`67yvRJQ&(;ZGj=^&SK5rl_AuucpC-FLFy`{qf-8HMu9NFQQ0GU>BON=5+PKuLS3Tx+)c~>o91)h$60~)kW{~rtM|_MHJ{x@R+D$DE+$svLgJ1ZXt>t@Ym&wC?Yluw>YCb&RgM&C@$9;IE6u_uH~;_pAucD7>(@1XjFY=J_HQX+qyx03i^T=R3`@m-2q^;VZLhz4;=-C>w298=3+&HJtE~+3paYQ`XUMm^Rckn-qtzHe3i0_Kr#2b+CoM4dzCc!oH+U1q9_I>>kCudg>CRf_uly~-=wW?<IgXg(hP$nRk(^3cFli#1`S=bxOTBM{;d!hbFLnyVPU>cznZV~oegBG<RV7qV%+4`p+R`)^9-5)e`-0CB}9=R3_lCu3xI&avDgI!5fJ3YrtFId2v0xuL{F0wGpC83vlSsxnfcY9m6-*Czl`=5$D+Ac{Jw(nr9>2&c%x{Nb2+H|4dvnlf^)~p8`u$)*=ySEcYQs8)^Uz;4AR$BuM}SHM%pkBig;X>`>Gr`3M?O#u3P)HPreZYa$UZ-2&(cGiOOx8_WBB&GgDx;A2a%Sn~^O!_0*MW894{f+XjZD@Ltbiv!5;Z;DFZ6>gWoYa_xz?6L0S;loH|fMy6kk&P}$aAu00L^nN#v&)Mkq0IOm;G92#CMC;Q40o^il{MpB|xsrh8(bJ^mcxJ_%0W~~ST9L*vsrXGhz!}ZRdr271#My?I*KAHp)uhHd>$D$0L?Xg@VZ+oDRO|zie=}b+a|l_l`Pzf!ZeHv4OnB`8Ucf6+iY1)+X_&Flw>f++YQApP(G(%>eu?TI%O9haR#xCi)3nXSl<2(+%&r(UzE>o${2rm%Fo;WcU_rlRwU?P&!mr`wW?X@wNtFkdY2M8d5*YC1&70Q#!m}6!3f>4kSlS|!c^4M+1}{;Za?4T)yvJX^-UIpZ^5UaqpT|xOO&uJkC_MS=0X2jEHn*7oj&&7*&-qLHK#2#J2Rn<#?J^k0EwL#%bdPDxp3=n}0U#orueeiQ8-eQs?NZUD%?HGdGBk|(T`2eqY*V6rh(KgRegEH3@MnL3Ni${R$)g>>#OdEq@cm(5ENvkLqWq!h--Cj!8>XSOXLTS_Mi}$|9|iw}>2E**C|efk<m{-GASdAk>U)1f0mz|d<c^gvwJ!CyBcq#%!*$4|Dm>%h3{9={D-}4q3O+}m2Uwk4Rt1mU)?lwdKD^GF``9<1K_0<>vI9!31N~NwMvlN0OSUFoJtgOqWmKRBnJZQ)^2?}IR}XAfI2^zJKCNAG-N!&WHG?Eg>$M!S@c{~UdD`GTiRtOrb%EJ(@x<LulPSoUR=^mnFivI5KE&@0a4ZzXml_ZA<U^i7TLzM-jNNI=xxfepz(Z2<`S51=!F~5I?-3W{abg^)bzdiNK;T#BME2tQ{%jjy3)VVyuDQRUaKXCG5yRlky$N5G^eY2yaoJv0lim|0V!HMKHd%4o@xH=eOydsPEOKAmqri?B*UO2`7I~FvS2t)gf{bh+Zp)&PFq_c?S-5Otb9t%NwdVw#VERM|IL^PPcO}HQEj#39i&9wi>V#IkmL|&r0s4wAz0vXI?m*sw!{BzZ^y4!smyZDRfQTJm$Gha|KYLt$evLOS3OT%S#$YqZeWujNyo}xB5CNDmM(MSCV<G#q*#RWp{WZ{SKRu3_0W(?gn}3{+>QY}#Aht95yW1+GE&JG!fy1O@<sHQ0Pzzvskj-^F@Udq})q}SKw&0g}z&x6&d?5mddzrZOLcEheI6e=+7Mh1kkN0AxDVhPbg~*u`MVb-GJrN+6jb4-bq*H3ZVi3G(OR@8+yymibY~jK&?!)HO^HWCD5eBcI<0N|<SA@MlL0uZrE|u!+S_fthD4#PVFX;SX_d1yp2wvyOw=bs+%5%Cs10sce@HA5_&)qvG0$Wt(dDOERS8%q4+0(7=@?jq@4<D2Q!(30@-7C;89|sNKN`}X@?_Np9Ku8TFW7Y(<l1JjaCLRc00T(jvW`zmv7T`FOt;^!4R}K3NdwAEjCIS26@DDx2+lznSO#h0-T0;tBw_JcNqAb7LI-|zKSq8F{#fVBdVQubC&_rzA;+fh|a+RNOz}G@05odRAZfdg|a2U=&m3q*)aw@@XZeHIbjXZO16AF;84NI!Tr+E#Px4?96!Ecg(`+S2SmN&kZazKZyC@9=})POB`y^L2KA??BT6mS?P>>D?zj;LAPKLByTR>l'
        Z = decipher(Z)
        seq = [bin(match.find(c)) for c in Z]
        for i in range(len(seq)): seq[i] = '0'*(8-len(seq[i]))+seq[i][2:]
        _.seq = ''.join(seq)
        
        for sz in range(1, 71):
            for i in range(sz):
                s+= f"A_{sz} = " if i == sz//2 else " "*(len(str(sz)) + 5); s+= _.read(sz)
                s+= f"   B_{sz} = " if i == sz//2 else " "*(len(str(sz)) + 8); s+= _.read(sz)+'\n'
            s+= '\n'
        print(s)
    
q = gen10()
q.gen()

assert open('gen10.out').read().rstrip() == open('res10.txt').read().rstrip()