from nucoin import NucoinWallet
# 14 de Junho xD
w = NucoinWallet(75.00, filename='my-wallet-transactions.csv')
w.freeze(50.00)
w.freeze(25.00)
w.reward(spent=60.00, date='14-05-2023')
w.buy(BRL=39.00,NCN=3000.00, date='15-05-2023')
w.freeze(1000.00)
w.freeze(2000.00)
w.buy_crypto(BRL=90.00,amount=.0003,name='BTC',date='15-05-2023')
w.sell(BRL=5.90, NCN=64.96, date='11-02-2024')
w.melt(3075.00)
w.sell_crypto(BRL=100.00, amount=  .0003, name='BTC', date='11-02-2024')
qty_NCN = w.available["NCN"]
val_NCN = w.available["NCN"].convert_to("BRL")
w.sell(NCN=qty_NCN.value, BRL=val_NCN.value,date='01-03-2024')
print(w)
