# nucoin-wallet-sim

This python module allows you simulate your nucoin wallet using simple functions.

```python
from nucoin import NucoinWallet, BTC_BRL, NCN_BRL
# 14 de Junho xD
w = NucoinWallet(75.00)
w.freeze(50.00)
w.freeze(25.00)
w.reward(spent=60.00)
w.buy(BRL=39.00,NCN=3000.00)
w.freeze(1000.00)
w.freeze(2000.00)
w.buy_crypto(BRL=90.00,amount=.0003,name='BTC')
w.sell(BRL=5.90, NCN=64.96)
w.melt(3075.00)
# Selling everything the world is melting!
w.sell_crypto(BRL=100.00, amount=  .0003, name='BTC')
w.sell(NCN=w.available["NCN"].value, BRL=w.available["NCN"].convert_to("BRL").value)
print(w)
```
```txt
FREEZE: -50.0 NCN
LEVEL UP: 1 to 2
FREEZE: -25.0 NCN
REWARD: 0.6 NCN from 60.0 BRL spent.
BUY:    3000.0 NCN = 39.0 BRL @ 0.013000
FREEZE: -1000.0 NCN
LEVEL UP: 2 to 4
FREEZE: -2000.0 NCN
LEVEL UP: 4 to 5
(BTC) BUY:    0.00029999 BTC = 90.0 BRL @ 0.300010
(BTC) REWARD: 6.3 NCN from 90.0 BRL spent.
SELL:   64.95 NCN = 5.9 BRL @ 0.090839
MELT: 3075.0 NCN
LEVEL DOWN: 5 to 1
SELL (BTC):   0.00029999 BTC = 100.0 BRL @ 0.333344
SELL:   3016.95 NCN = 165.03 BRL @ 0.054701
------------------------------------------------
---------------- WALLET SNAPSHOT ---------------
------------------------------------------------
1 NCN = R$ 0.05470000
1 BTC = R$ 309471.00
CURRENT LEVEL: 1
NEXT LEVEL: 50.0 NCN = 2.73 BRL
------------------------------------------------
-------------------- REWARDS -------------------
------------------------------------------------
CC: 60.0 BRL and got 0.6 NCN (1.00%)
NCN: 39.0 BRL and got 0.0 NCN (0.00%)
BTC: 90.0 BRL and got 6.3 NCN (7.00%)
MATIC: 0.0 BRL and got 0.0 NCN (0.00%)
------------------------------------------------
In total you spent 189.0 BRL and got 6.9 NCN (3.65%).
------------------------------------------------
-------------------- LIQUID --------------------
------------------------------------------------
NCN: 0.0 NCN = 0.0 BRL
BTC: 0.0 BTC = 0.0 BRL
MATIC: 0.0 MATIC = 0.0 BRL
BRL: 141.93 BRL = 141.93 BRL
------------------------------------------------
In total you have liquid 141.93 BRL and 0.0 BRL frozen.
------------------------------------------------
MEAN PRICE NCN: 3000.0 NCN = 39.0 BRL @ 0.013000
SELL PRICE NCN: 3081.9 NCN = 170.93 BRL @ 0.055463
------------------------------------------------
PROFIT NCN: 131.93 BRL
------------------------------------------------
MEAN PRICE BTC: 0.00029999 BTC = 90.0 BRL @ 0.300010
SELL PRICE BTC: 0.00029999 BTC = 100.0 BRL @ 0.333344
------------------------------------------------
PROFIT BTC: 10.0 BRL
------------------------------------------------
TOTAL_PROFIT: 141.93 BRL
------------------------------------------------
WALLET WORTH: 141.93 BRL
------------------------------------------------

```

<style type="text/css">
pre {background-color: black;
	font-weight: normal;
	color: #bbb;
	white-space: -moz-pre-wrap;
	white-space: -o-pre-wrap;
	white-space: -pre-wrap;
	white-space: pre-wrap;
	word-wrap: break-word;
	overflow-wrap: break-word;
}
b {font-weight: normal}
b.BOLD {color: #fff}
b.ITA {font-style: italic}
b.UND {text-decoration: underline}
b.STR {text-decoration: line-through}
b.UNDSTR {text-decoration: underline line-through}
b.BLK {color: #000000}
b.RED {color: #aa0000}
b.GRN {color: #00aa00}
b.YEL {color: #aa5500}
b.BLU {color: #0000aa}
b.MAG {color: #aa00aa}
b.CYN {color: #00aaaa}
b.WHI {color: #aaaaaa}
b.HIK {color: #555555}
b.HIR {color: #ff5555}
b.HIG {color: #55ff55}
b.HIY {color: #ffff55}
b.HIB {color: #5555ff}
b.HIM {color: #ff55ff}
b.HIC {color: #55ffff}
b.HIW {color: #ffffff}
b.BBLK {background-color: #000000}
b.BRED {background-color: #aa0000}
b.BGRN {background-color: #00aa00}
b.BYEL {background-color: #aa5500}
b.BBLU {background-color: #0000aa}
b.BMAG {background-color: #aa00aa}
b.BCYN {background-color: #00aaaa}
b.BWHI {background-color: #aaaaaa}
</style>

<pre><b style="color:#5555ff;">FREEZE:</b> -50.0 NCN
<b style="color:#ffff55;">LEVEL UP: 1 to 2</b>
<b style="color:#5555ff;">FREEZE:</b> -25.0 NCN
<b style="color:#55ffff;">REWARD:</b> 0.6 NCN from 60.0 BRL spent.
<b style="color:#55ff55;">BUY:</b>    3000.0 NCN = 39.0 BRL @ 0.013000
<b style="color:#5555ff;">FREEZE:</b> -1000.0 NCN
<b style="color:#ffff55;">LEVEL UP: 2 to 4</b>
<b style="color:#5555ff;">FREEZE:</b> -2000.0 NCN
<b style="color:#ffff55;">LEVEL UP: 4 to 5</b>
<b style="color:#55ff55;"></b><b class=UND style="color:#55ff55;">(BTC) BUY:</b>    0.00029999 BTC = 90.0 BRL @ 0.300010
<b style="color:#55ffff;"></b><b class=UND style="color:#55ffff;">(BTC) </b><b class=UND style="color:#55ffff;">REWARD:</b> 6.3 NCN from 90.0 BRL spent.
<b style="color:#ff5555;">SELL:</b>   64.95 NCN = 5.9 BRL @ 0.090839
<b style="color:#5555ff;">MELT:</b> 3075.0 NCN
<b style="color:#ffff55;">LEVEL DOWN: 5 to 1</b>
<b style="color:#ff5555;"></b><b class=UND style="color:#ff5555;">SELL (BTC):</b>   0.00029999 BTC = 100.0 BRL @ 0.333344
<b style="color:#ff5555;">SELL:</b>   3016.95 NCN = 165.03 BRL @ 0.054701
<b class="BOLD">------------------------------------------------
---------------- WALLET SNAPSHOT ---------------
------------------------------------------------
</b>1 NCN = R$ 0.05470000
1 BTC = R$ 309471.00
<b class="BOLD">CURRENT LEVEL: 1</b>
<b class="BOLD">NEXT LEVEL: 50.0 NCN = 2.73 BRL</b>
<b style="color:#55ffff;">------------------------------------------------
-------------------- REWARDS -------------------
------------------------------------------------
</b>CC: 60.0 BRL and got 0.6 NCN (1.00%)
NCN: 39.0 BRL and got 0.0 NCN (0.00%)
BTC: 90.0 BRL and got 6.3 NCN (7.00%)
MATIC: 0.0 BRL and got 0.0 NCN (0.00%)
------------------------------------------------
In total you spent 189.0 BRL and got 6.9 NCN (3.65%).
<b style="color:#55ffff;">------------------------------------------------
-------------------- LIQUID --------------------
------------------------------------------------
</b>NCN: 0.0 NCN = 0.0 BRL
BTC: 0.0 BTC = 0.0 BRL
MATIC: 0.0 MATIC = 0.0 BRL
BRL: 141.93 BRL = 141.93 BRL
------------------------------------------------
In total you have liquid 141.93 BRL and 0.0 BRL frozen.
------------------------------------------------
MEAN PRICE NCN: 3000.0 NCN = 39.0 BRL @ 0.013000
SELL PRICE NCN: 3081.9 NCN = 170.93 BRL @ 0.055463
------------------------------------------------
<b style="color:#55ff55;"></b><b class="BOLD" style="color:#55ff55;">PROFIT NCN: 131.93 BRL</b>
------------------------------------------------
MEAN PRICE BTC: 0.00029999 BTC = 90.0 BRL @ 0.300010
SELL PRICE BTC: 0.00029999 BTC = 100.0 BRL @ 0.333344
------------------------------------------------
<b style="color:#55ff55;"></b><b class="BOLD" style="color:#55ff55;">PROFIT BTC: 10.0 BRL</b>
------------------------------------------------
TOTAL_PROFIT: 141.93 BRL
------------------------------------------------
WALLET WORTH: 141.93 BRL
------------------------------------------------

</pre>
