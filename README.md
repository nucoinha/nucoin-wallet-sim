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
```ansi
[94mFREEZE:[0m -50.0 NCN
[93mLEVEL UP: 1 to 2[0m
[94mFREEZE:[0m -25.0 NCN
[96mREWARD:[0m 0.6 NCN from 60.0 BRL spent.
[92mBUY:[0m    3000.0 NCN = 39.0 BRL @ 0.013000
[94mFREEZE:[0m -1000.0 NCN
[93mLEVEL UP: 2 to 4[0m
[94mFREEZE:[0m -2000.0 NCN
[93mLEVEL UP: 4 to 5[0m
[92m[4m(BTC) BUY:[0m    0.00029999 BTC = 90.0 BRL @ 0.300010
[96m[4m(BTC) [96mREWARD:[0m 6.3 NCN from 90.0 BRL spent.
[91mSELL:[0m   64.95 NCN = 5.9 BRL @ 0.090839
[94mMELT:[0m 3075.0 NCN
[93mLEVEL DOWN: 5 to 1[0m
[91m[4mSELL (BTC):[0m   0.00029999 BTC = 100.0 BRL @ 0.333344
[91mSELL:[0m   3016.95 NCN = 165.03 BRL @ 0.054701
[1m------------------------------------------------
---------------- WALLET SNAPSHOT ---------------
------------------------------------------------
[0m1 NCN = R$ 0.05470000
1 BTC = R$ 309471.00
[1mCURRENT LEVEL: 1[0m
[1mNEXT LEVEL: 50.0 NCN = 2.73 BRL[0m
[96m------------------------------------------------
-------------------- REWARDS -------------------
------------------------------------------------
[0mCC: 60.0 BRL and got 0.6 NCN (1.00%)
NCN: 39.0 BRL and got 0.0 NCN (0.00%)
BTC: 90.0 BRL and got 6.3 NCN (7.00%)
MATIC: 0.0 BRL and got 0.0 NCN (0.00%)
------------------------------------------------
In total you spent 189.0 BRL and got 6.9 NCN (3.65%).
[96m------------------------------------------------
-------------------- LIQUID --------------------
------------------------------------------------
[0mNCN: 0.0 NCN = 0.0 BRL
BTC: 0.0 BTC = 0.0 BRL
MATIC: 0.0 MATIC = 0.0 BRL
BRL: 141.93 BRL = 141.93 BRL
------------------------------------------------
In total you have liquid 141.93 BRL and 0.0 BRL frozen.
------------------------------------------------
MEAN PRICE NCN: 3000.0 NCN = 39.0 BRL @ 0.013000
SELL PRICE NCN: 3081.9 NCN = 170.93 BRL @ 0.055463
------------------------------------------------
[92m[1mPROFIT NCN: 131.93 BRL[0m
------------------------------------------------
MEAN PRICE BTC: 0.00029999 BTC = 90.0 BRL @ 0.300010
SELL PRICE BTC: 0.00029999 BTC = 100.0 BRL @ 0.333344
------------------------------------------------
[92m[1mPROFIT BTC: 10.0 BRL[0m
------------------------------------------------
TOTAL_PROFIT: 141.93 BRL
------------------------------------------------
WALLET WORTH: 141.93 BRL
------------------------------------------------

```
