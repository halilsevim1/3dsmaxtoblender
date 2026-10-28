bl_info = {
    "name": "Max to Blender Scene Importer",
    "author": "Halil Sevim",
    "version": (1, 2),
    "blender": (3, 0, 0),
    "location": "File > Import > Max Scene (JSON)",
    "description": "3ds Max sahnesini (JSON+FBX) Cycles uyumlu olarak import eder (© Halil Sevim)",
    "category": "Import-Export",
}

# =====================================================================
# PROTECTED ADDON - Copyright (c) Halil Sevim - Tum Haklari Saklidir
# Bu dosyanin kaynak kodu sifrelenmistir. Degistirilmesi calismayi bozar.
# =====================================================================
import base64 as _b, zlib as _z

_K = _b.b85decode("`Ja!mx|Z+^m9RGofQu#5L;`mCJekxumZ`_R$LtA~")
_D = _b.b85decode(
    "k{SPF;CbRE9Lp&ehkewg5T74hvY#;c&fOrv6KGD^x-pjmATyg1J^BnLE+;)CFy?$7C1hSj1LWk=e7qBN"
    "Tn*Acr9z81Hpl~VxIp7!{!4lWU1GR|nd1fA(cV^%ES(r%m8pW7cXq{AeJM@&5?P|QT&57n?l6(JzZ6Il"
    "%?$6sz1J;gSZqT>id}LdJ#WlW0>9rnDqRYuHna+6U5Iyr&<P9OjdMmX`x#=z<$6yWKSOwy@USyk*l2O@"
    "p-*MJ+0ekrc#3uHN9us{Al-!<h1gO2GHf>(%2HQ?<87(K;<%2V;w|eW`$5qpz)qr;3ITN=(qlP4t?OCd"
    ")=|aKL}m#h(h9_B>bs{}MIsP~gTTvqyh42deZFT0?i|S%s&OQ`|7#TjkCOD+NRF6-7B3n(CZolZ2L(By"
    "Y;39_7Dc3yC!hE`)r9z%WpRSx2Q}iA+uYfO{J?s71$xB1H!(f$fVb!f8oy}yK8ORTZvXmI)KKQij^!!a"
    "f-x}43BLz0xqN8%R_yPc79vf?2@eG=1t77h2Z8n*^59mHkCr{)iIE*sA8$HSQg0j?4!qkgruW9CYQcCD"
    "F>2pujRbGna=N&jR$WQjWjylHceLeGtLd+~Ka_}BL?+rNIj}vWENzo*mTI^@PUk=4Ddiz7YeP1BSin~P"
    "nYdf5YnTx*s4?;px4}()eUb$u)D+V(?-#}v{3e9`hyTt@O+FujJs7%P{}B?(JgLIu6pW-fZv}jGffxLY"
    "OGciyY5jW=_WLq7c0+vReO&N~-d`Q4vM@<s7sA<-9<YwEQ?z7ophqLnjGCF$;{hoXF_n8f?2yi1*Z-OG"
    "+RJTSFI-Lyu47g(jdV$SvPth>mD;sk3t}3SOmV>_O#cW(m5t*zHt<wj{ByXskVP@0I=wH50XxYPU0jhi"
    "(Eup-gEZ;j9`RQd{FnRXNiK+21L-3phyJ8F3+a~0L!qf7(|U|KuS#kQxjZl26JH^^vb}uxK+xL;0{}T5"
    "_vrpEwmd<u@Vz8IuxDRvFMH_(1-}qtxKu+FTR)+NBLKc!6!DU=;5&rSEM*rWwTM}%Xxr3v;)N0Nwb?e+"
    "+L7uo)E~c=Fbx=Mz0>TP2abKdGq3)DJj{Vw^>irJyo4rjbBWjhZ-Fg*eQ1^crDE^*nP$+(3{{fGL;+4I"
    "n<UuG3{0ycxj{I+T-b`QKCkk}IZ5DVe`Gd^UYLu-0))#4#g^ta&B3vpXn&cj5gIp#a15^0iExFm+Q6o7"
    "lie!40Y11)n2H@MKRijCMHi4wa!mqsDGYxDLPdHT#eV|EL4e-<E&Rjd6C@SxqC#6T5^mmHEF(&d-)%|E"
    "1q!0Ek_0J_&3JAxv-7{Y1Nh6<z>Rs@sFYDI;vCYQ++8{u8UGfI!s~exrXm^peaFZ<1S;Y(vRqn+G`$|z"
    "HKmJ~2a>58<PQ=W1DzsYFM{k2{OEyv82l6NI%(n1Jb|=Q*ItC{D-V~zEcoqmk5Cw>TD8w_w7BmQdfgB<"
    "Bxy};1c8_{<*JMJ?uAz?!l+P;FYI|rgkJ!MP)D(-XsrN!eNAD_Y3bl`mhvZG>EunVTR?GtIKb2EHoCN4"
    "X5G|v?=UgGyf_KocVdh&3#FW|YW}M#-g-A_=)k7V>C{WJ1rskoy=r|Y`C>BhYJeGr^A>J<z+ARPF-Q=J"
    ">z(I})xci{662DJQ*%{GY&J<{&z1=qtep;K?EDaaW)9WeP(XR4gKT|(ghJ!IMnrynYlhX2xB5~6%1Mrh"
    "gKB4$3%HX6zu**%$?tXgv6k~^&A8k+-m#wgnTtR^y%!@rB6U&kVo_dMB_;+qPmHidI+3I_m1^_d;+u{i"
    "D8~^`5#lY)6Wo}r4!br3Crk4;*+*iTdS3=U?HwM7&f!THz?OqL8abC9K@N==ivYQD>#f0S^JOK7Yp+m<"
    "W{>|F70x(RP#>81e{5`%4@=x@p_o7*V+R{FXc2DLHi{`P)Gg^oOyZgpis6r!Kb~)$+Qna5zM%ONb46}A"
    "Gb&^K@-xEhN$BP=DWv6lSypT1({v2h@0FNkDDWwyuw?oc9<Cl$wy!wOfOlmMRTyr?4F`rm+ojjLzFVyf"
    "$pFGG<x#1fAA=01Np#KfNB;y1BRQgUYM*DVbU?MLeXWd>r>YMrU-0WN!63Nkh-V14w36eglT<FkPG9)H"
    "p!nKA1sv267j9m8M-8~p#z8?<08}f?tlRkN3Etzt$zckB1NxE$quG=R2QU!Vwbs=gTe7I2O=<|MkQXV{"
    "8MU>m6bfQ?b<{CIuh+4h&n=5;jUJ@RzBKoRv5J#YiB*2}t4Af`KJ>#c0|HPzt&gOKT_=^=Ls=@x45s*>"
    "NLs!$h0;vs1H(0Cu@S%pdk&~Q0r8l9DXnj>ZJ<AWxp<TcmS1-klDv9z&(z*m2MUAXlbi;k!BgL{NXMN$"
    "iV!fHyh?m4&R;{)m{bz_z<E#-@O0J2^r*_9EBX}vTM%oH9R18^g#1D$_CAZivsER>wg}#sz=mkOs(pZq"
    "odUNd37xE(6-DYW{Kb7@J|Ke?pOrJn<%DQnLJut)L^6mnnj{X?ZNVoZp_}Q8p)Zbkh1tUFU_lkir?-tB"
    "4C7n3b`-gXa<ibAY^UxW{P<z9h;WdeLs-yed?D;zf%x`A3No164_==&8SVC;C61?$&C6O+3SC7;=azck"
    "t+)8|!79ZKUAx`CUaAm;yj}z|s#xj7ScC3h&KufUr4aCU#C@O#9~dB0+gEFrCuB((q6$f5AuAw!qr_Y%"
    "Zj@~V2*Dz}#Yy<DZ(IGSFIlgl2PM-Fm&V8Fj2RzSlpsg()F=O3s~5|mpxwdTaB^RS+T@FMyu9sU1Fji2"
    "6hF;(9Iy$bVmE6<;QN{y(0mfdI&dNIWEW6DEuVbE5%@Vdr+^;1BTlo_b-3_(@<n9#3oKF($_IzL%2}jU"
    "6F<R{U@5cOdMG6}cv%AcJ0kgd)UI$a4+_$Xlnw5xKg6M5A$%;o`-VmWK)_0612+9Y{J1G@iP34XV$TE?"
    "=r&@rvvzn-zG)iBGxRt43090@9V1nO&Yr1#Ai{Uxh0T@8nkYg2w6i*bD*13ZWfDRdsht>L1D^lxBmAq)"
    "$uActlI79bFW|`}Wy+i;l(;FAl-2|9ns=Gm#*u^G7-g~z0a-WXrc9<w1Jb4><4$4!YXn^kT*<dR{|aaD"
    "pjdYI#^=eLo@=}H+XC+B2&D4s8SpuCrQ;zdk$u2s>=s!Fidp7uI@Kf1<cFiWSmB+id~{H%T&q-}jJfC?"
    "JKJ9+S)CY(n3pURWUBZX#&XG|j~msgt4VwibwxAQ$gxor_o_aN#O(^7e!kn@)zdMPcy~O}J*`xfQf^FP"
    "-Ev$hguY8V!v#O5y4MTJqrbV&2+KitX2q%-yt>q=oM8OYW*eE~3i?CZq0-4IY=Dl1w1G_Tw;b{g?_tCX"
    "d)|!O!Q+&dt!I=Z)Go02RcZJDsc1_+3s8C=+`mZCsG(}I56}}7Koe_suwlR?2ox7)l(of^nkH*`nl?3`"
    "U(PZduGNot^_d(Y12DyA)0M9@*K&;KEVfsbsDy90Ol9wRlki6>r@pcC>gwB%cH(L(2e}^FNct&QOh236"
    "C#V4DL9AKl8hIP_>p1wc7_rd7@fP>tSu`<pWr@uv|3=;XuMC~{LYBiLB5-OdG0-FrC#oFuqn=j?=7tl~"
    "`YA8U`^rHp@wGup{H%bQ#$np8o>D1xpn7gfa<3&tH*JB9*^ob!JpVx7aMjVt;ke?f?XqE3^v&r8<?=o;"
    "r{&Q?>q^IpI1Lttzs-Ng$^!)Z=4$tE=?$e})Dq^;<CT1&386M*J=v-H1=K8s@l|VyeL^|R>jt;$b6I`="
    "#V)*Kob|LZ^J@z;BMQ*UEF75;!yuuCg8N7kdWZO6eNg|C_a75@%5BFl*07<|;OTF$U@kxfBj%`~7UJor"
    "(`Tz%<*UB0T{T-zK=><qxR{>WM@_Ig-?{uf#;V;-ChdbgCGxxYr_;{tOj0>fZx+EW!=0_-X(CBE>bEK5"
    ">W+9@dS9(rEL6RD7IrO{So>W^7+(#Y&JuO7OcDsNJCfD|q3|{*S_(?gYs2JOe;INC?j%Z_si;<`=MFEe"
    "-dw=bLEFlNj#oLJgw%7&hF3yK!ZtN}!fo)U!>G<ufd;w<H*3`R*ga$7bz(;jREpBR@iE0ixjPoZMu0$N"
    "t+5i5i2SAo7x4?`r{vP($Ak|HL`N)J1f5Geen&3e>~(D_hGtZaX)?RSXtHpl!{g*Lsnpbv5zxfO*-Dqu"
    "8EdLKHaA(|>#e41xRX>DwZl*r14lES=-k_tvY~XeY2f+yC=k(bKc0iQSd@X%2pvT4b<viHz#;Cit_>R>"
    "gzwPYcUciFf(V0KcWChZ{0up?S){ji_i!Ntr?NysDwUtYmO$ifIdM7>en01}DuNUX4}E2~x>{{~f2&s0"
    "+@u3YHjb9IvR#{&-b7h&h1l3sEA$qfzDKCX0dTbPB>bA#T6@F~yrlV#GbD4G0c1YoCZR}lYlpoe!QaR3"
    "=S=;$nxQ}Qs#Ru|rsYpD4ZCp>fHn3W4#+qW%|tCN@QcJ00<gvmkK@lgU~`1x^W}!0rr4jMw+=LaHcXSU"
    "D50W={F*`mfn-s=btClj9qwBF-j)>;R)xE5bb)sQR(@uZX`W%q6ovBs=Xm(_QS1mOOsdX_TEGPk;CG83"
    "Jmaj&IDkJJo8Cwej*7As7c%r5iZnI;owS@KI<Db8Q)Lkk{8PqMn$13^jqh0y#bw<^Q2<ud&!8w#vJeUJ"
    "ORq>4TqhLtoBr{|11pDJ4{%a9cDr?_Wo~?nI6IUkAJJ-9F9%118aMf7?rK6UfQPCM&*UXS-9~6e>`j2&"
    "=QoXD)7l>iX>*6Vdr7*??g@6HU*bP1Pmj7=A8yBfTEIrB?jt0~L_37+cI$!Glb>vkLy<3gLvvi?w(<a="
    "DYKHH&=*i6j>W1Q@O$jM8ZIDhBl)utDb|6Er~8b4KW%KlHY?b{k5*Ua3^XvETjzlOmhL}K&GprYGaRtZ"
    "Ew|??gOp(j!eUUtdqp6?gV~SOr{9CZb<d!S(xIbv`n$|#rUnY7nc^)JyqysiibYKh*^d7wi2^WU8Oh*O"
    "a2p*FAPYb0$Fz3EK7Tn`nF8?ZcjBczqq3w07#z4_8Uj#3{T|h;x5ZIew`{`5%~!?FNb@c>@ixhe-hxa0"
    "1`FKxoy)3#8hES-L=XM*e~X$8aPNzqJFuW3wIQG1ISm*KxN7p4dWwK$2d~>7Vwy+&Y_06&8e=A@L}g=J"
    "s`O8{^VnMnBHmM?4xNTWO=sCK80&D5%oT4HI>_>EEowo6_3i~>vfPrD4!5OVpbhB7WIEZctzxs|cr5sq"
    "W#n4*%crp0UDhI7Og;5(G61+N5>VpJ>Z*dG(e%k+XP+Ejj2i@P;}tfA6A?VM{rr>krn(rkGxv()H{;sJ"
    "+F3fFp?cT#TkV%i@Rc-kKkI)0trni>KgO$tNCa=YHOMQnD0W*?H@I)0C$$FtvBHVF>~DZEJ-2Wh2XJW0"
    "8-gIS*fKLa4tUQZcK{iBJl4KxaPZNr$PSo;A^)q?G(TCK#Ue1D)u)i{J8Wb?(3|xhRa6VpG7=XvYF9NU"
    "BF<4N+v9nE!b}PEckMrGhah6%ar~>-z8w*vzlc0{nVV7Zkhv)b?9%@TBD4^yS&*qw_Qu4Vx_T02f;wW2"
    "O_uDhOX~=rg_RL21shScjk&b!REJFf98xwcilqmrHVcDV<PW08o<WB#r!(ah0D-loVp_@COd8eI5K`-r"
    "z)f4hU)DyBHt7&3k8oW}h`O#XVH~-WiZVE#6!I~k)emB6=oBWa5I^k1#Y7FK$@LNDl80iY^<_>5Jz5Y|"
    "qXfDOXr|OC9{D}GJMwOHB`@;J=eBfJED82ofeg-H)P2M0EU2ExDj<u)J|hUGBnI1XN)G-<;F>ccjIJY`"
    "t{*C&NFP%;Ujj>%W3Lhyt_a!#e?+gho^csSQTdm5)xb$%bF(PyE9pnkxj;;1f1(XJ@~^Wy#e?PY9q&WS"
    "L*_WFyr;3o%vqOcT>QHZd>@sOB{Vk=Plp6yKA1@tJw>lE^ZA3n+x#{MG2yeq>$pJGyHR8cqj$ZVdgfg1"
    "#x@hKbSPGshNJYckiMzA#faeZtv(*$0qn|&{`-S@Q?U4hQ4$Ep0m)9xr(f}ewpu!^`t1rX>2}|p2ZNBy"
    "bgM9?Fzv7o<4hW|7!u2=4e?A+aL{hgW1v%ht~~pp+kylMgK4OFpyIeKSL_%V&rR5#67v&RL4Q|!;8r&p"
    "ftl6RZeCd%XoHtVRYFAB$=4()Ift+$I8o|9>Pmd1=?Rkk7;FB8Yyp*@X1ClNug8PIw$QKPd<!3_4&0zS"
    "l%`RVfUIfhWmsbY6?UBu=YlxtEU9~dBB5ki7uu=6pUjn~g8Ai}jqiXY{D5eiqR=iHQ_J7b>;F5kKf;&s"
    "x@pN;^Hl00<dC#xBsTU2`(55%JynF#=KQ0oKE-zIQJsgUSoeU0irx@<NM)J2ek8Y!kUAKT2(whPRMLL$"
    "8`uz{-j^Jnh@3HpDDXF-$7kEEm}$@$EE@(xE({fh_R7?L#8eLFYh<*}i3AOreTYa#T*9~MS?wd<1X<h="
    "Qp+3&)#0ft`-@FbkcO>qgS#eLREPR>@vJ~r?Ac^ZeI2|?@;LbyNR5_7@o#%bZ)WT-GeLJO<=L^b59O4u"
    "ulx(0YvBGE&d(?Ef4$x?vq1~wk-x7+Zk2vUVY78~LC|gFc<geHS*53P-Ug__<c-dW320zdv`Mb%0`*(r"
    "V|j<(&jCy36K+C17rKKjytp)^yvM1F(J<T*4E_Za&fPf?ifmYbd06Ia1%RTnBo!_otS6m*UPXTp(92_G"
    "%54x?V|nt?b5uXbB4_iZ*(v%&ek`kT8E&bky6nnqBkw28edT-*r{XWVHhA3ZTCI4#o(_0@Uk*s7-at40"
    "cGZ}wTdNm$6!=Vk(9)d+oQ8{(s9E^LVNEsjo}pWn!V(i`iF(bXyIvWY`T(VZf2ChK_&vCzfuQN$ILu#<"
    "FRlZ<pnuzwXZBZTzKnU0*wHR~jv($<Fc+!1gICV)a6_XTQ5S3i+=9*GUg1o$2qCSZvj51dZVXXgBl|G4"
    "Lg^IN@Dm>rE*}81LZf$?b2rTB^6Xar=dQ37G{%(_`%vUYJY7;*Vb!?R-KWdz%t-#s@<^iRs#=Zwf4eWU"
    "(Ht=Lm_4?BH2d@#o2&$V+rng_xDi{!k0jHil`P@uR>9KO-FHm1jpfERPoL;~qSV3I!Gdb$u~^4RsvrPc"
    ">qaY+uOjx{6C}UPPW^?nQg;xujwuUA8UlY!uV;7jq|7X=!)YzS@QO#?@rfbG@kNYdxumRbN$Fc}q=O+l"
    "MX05o_hcOcxk}PF&oAXs7749<NIv4d>OhsfYm{8|OvcRJ*=X%+;1cOryS%5x%v%CNX5v;>BxO0h{GGD{"
    "5s-sxr;G%QDc_XHFm#9Ba^w?e&`dep9%lr8$Kd7!TcWl+cfxwJ!a$yGE72-Ps>0lY5;(_&_3p}y#cT~3"
    "bId8~w+8h@+;eIL{&f)qU^-Ii3fhk*Q`2Nz@2i@jxHPirZ?QBd(btBIs@<bh5Rsm0dd1S5_r5_$!D~6+"
    "oluWZ7;-L24z@b5;xCx%zkR2?A4gAY!blr-H7v6~1xxuGFBz&!Bs(unHQ31<KWl->be8P#g}i?"
)
_B = bytearray(len(_D))
for _i, _v in enumerate(_D):
    _B[_i] = (_v ^ _K[_i % 32] ^ ((_i * 73 + 19) & 0xFF)) & 0xFF
exec(compile(_z.decompress(bytes(_B)).decode("utf-8"), __file__, "exec"), globals())
