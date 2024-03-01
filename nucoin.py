import sys
import json
import requests
import datetime
def request_new_data():
    try:
        price_history = json.load(open('price_history.json'))
    except FileNotFoundError:
        price_history = None
        r = requests.get("https://explorer.nucoin.com.br/files/blockchain/price_history.json")
        if r.ok:
            price_history = r.json()
            json.dump(price_history, open('price_history.json','w'))
    return price_history

price_history = request_new_data()
NCN_BRL = price_history['latest']

r = requests.get("http://economia.awesomeapi.com.br/json/last/BTC-BRL")
price_btc = r.json()
btc_hi = int(price_btc['BTCBRL']['high'])
btc_lo = int(price_btc['BTCBRL']['low'])
BTC_BRL = (btc_hi + btc_lo) / 2

if len(sys.argv) > 1:
    read = float(sys.argv[1])
    NCN_BRL = read if read > 0 else NCN_BRL
if len(sys.argv) > 2:
    read = float(sys.argv[2])
    BTC_BRL = read if read > 0 else BTC_BRL

def profit_percent(IN, OUT):
    return 100 * (OUT-IN) / IN

def profit(IN, OUT):
    return (OUT-IN)

class color:
    HEADER = '\033[95m'
    FREEZE = '\033[94m'
    REWARD = '\033[96m'
    BUY = '\033[92m'
    SELL = '\033[91m'
    LEVEL_UP = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NEGATIVE = SELL + BOLD
    POSITIVE = BUY  + BOLD

def make_title(text, c=color.BOLD, length=48, fill="-"):
    fill_len = (length - len(text) - 2)
    fill_r = fill * (fill_len // 2)
    fill_l = fill * (fill_len - fill_len // 2)
    ret = c
    ret += length*fill + '\n'
    ret += f'{fill_l} {text} {fill_r}\n'
    ret += length*fill + '\n'
    ret += color.ENDC
    return ret

ASSETS_INFO = {
    'NCN':   {'precision': 2, 'symbol': 'NCN'  , 'price': NCN_BRL },
    'BTC':   {'precision': 8, 'symbol': 'BTC'  , 'price': BTC_BRL },
    'MATIC': {'precision': 8, 'symbol': 'MATIC', 'price': 0.0     },
    'BRL':   {'precision': 2, 'symbol': 'BRL'  , 'price': 1.0     },
}

class Monetary:
    def __init__(self, value, symbol='BRL'):
        precision = ASSETS_INFO[symbol]['precision']
        self.amount = value
        if isinstance(value, float):
            self.amount = int(round(value,precision)*10**precision)
        self.precision = precision
        self.symbol = symbol

    def convert_to(self, symbol):
        price = ASSETS_INFO[self.symbol]['price']
        return Monetary(self.value * price, 'BRL')

    @property
    def value(self):
        return self.amount / (10**self.precision)

    def __str__(self):
        return f'{self.value} {self.symbol.upper()}'

    def __mul__(self, other):
        if not isinstance(other,Monetary):
            return Monetary(int(self.amount * other), self.symbol)
        raise ValueError()

    def __truediv__(self, other):
        if not isinstance(other,Monetary):
            return Monetary(self.amount // other, self.symbol)
        if self.symbol != other.symbol:
            raise ValueError()
        raise ValueError()

    def __add__(self, other):
        if not isinstance(other,Monetary):
            return Monetary(self.amount + other, self.symbol)
        if self.symbol != other.symbol:
            raise ValueError()
        return Monetary(self.amount + other.amount, self.symbol)

    def __sub__(self, other):
        if not isinstance(other,Monetary):
            return Monetary(self.amount - other, self.symbol)
        if self.symbol != other.symbol:
            raise ValueError()
        return Monetary(self.amount - other.amount, self.symbol)

    def __pos__(self):
        return Monetary(+self.amount, self.symbol)

    def __neg__(self):
        return Monetary(-self.amount, self.symbol)

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount


class Asset:
    def __init__(self, fiduciary: Monetary, quantity: Monetary):
        self.fiduciary = fiduciary
        self.quantity  = quantity

    @property
    def unitary_price(self):
        return self.fiduciary.amount / self.quantity.amount if self.quantity.amount > 0 else 0

    def __str__(self):
        return f'{self.quantity} = {self.fiduciary}' \
                + (f' @ {self.unitary_price:{self.quantity.precision}f}' if self.unitary_price > 0 else '')

    def __add__(self, other):
        return Asset(fiduciary=self.fiduciary + other.fiduciary,
                      quantity=self.quantity + other.quantity)

    def __sub__(self, other):
        return Asset(fiduciary=self.fiduciary - other.fiduciary,
                      quantity=self.quantity - other.quantity)


class NucoinWallet:
    def __init__(self, initial=0.00):
        ZERO_BRL = Monetary(0,'BRL')
        ZERO_NCN = Monetary(0,'NCN')
        self.frozen = ZERO_NCN
        self.rewards = {}
        self.spent = {}
        self.mean_price = {}
        self.sell_price = {}
        self.available  = {}
        self.spent['CC'] = ZERO_BRL # CREDIT CARD
        self.rewards['CC'] = ZERO_NCN # CREDIT CARD
        for k, v in ASSETS_INFO.items():
            ZERO = Monetary(0,k)
            self.available[k] = ZERO
            if k == "BRL": continue
            self.spent[k] = ZERO_BRL
            self.rewards[k] = ZERO_NCN
            self.mean_price[k] = Asset(ZERO_BRL,ZERO)
            self.sell_price[k] = Asset(ZERO_BRL,ZERO)
        self.available["NCN"] += Monetary(float(initial),'NCN')

    @property
    def level(self):
        if self.frozen.amount >= 50000000: return 7
        if self.frozen.amount >=  5000000: return 6
        if self.frozen.amount >=   250000: return 5
        if self.frozen.amount >=    75000: return 4
        if self.frozen.amount >=    15000: return 3
        if self.frozen.amount >=     5000: return 2
        return 1

    @property
    def next_level(self):
        if self.level == 6: return Monetary(50000000-self.frozen.amount,'NCN')
        if self.level == 5: return Monetary( 5000000-self.frozen.amount,'NCN')
        if self.level == 4: return Monetary(  250000-self.frozen.amount,'NCN')
        if self.level == 3: return Monetary(   75000-self.frozen.amount,'NCN')
        if self.level == 2: return Monetary(   15000-self.frozen.amount,'NCN')
        if self.level == 1: return Monetary(    5000-self.frozen.amount,'NCN')
        return self.frozen

    @property
    def reward_rate(self):
        if self.level == 2: return 0.01 # NCN per R$ 1
        if self.level == 3: return 0.02 # NCN per R$ 1
        if self.level == 4: return 0.04 # NCN per R$ 1
        if self.level == 5: return 0.07 # NCN per R$ 1
        if self.level == 6: return 0.30 # NCN per R$ 1
        if self.level == 7: return 1.00 # NCN per R$ 1
        return 0.00

    def adjust(self, NCN):
        NCN = Monetary(float(NCN),'NCN')
        self.available['NCN'] -= NCN

    def airdrop(self, NCN):
        NCN = Monetary(float(NCN),'NCN')
        self.available['NCN'] += NCN

    def reward(self, spent, NCN=None, origin="CC"):
        REWARD = Monetary(spent * self.reward_rate if not NCN else NCN,'NCN')
        self.available['NCN'] += REWARD
        self.rewards[origin] += REWARD
        self.spent[origin] += Monetary(spent, "BRL")
        print(f'{color.REWARD}REWARD:{color.ENDC} {REWARD} from {Monetary(spent,"BRL")} spent.')

    def freeze(self, amount):
        amount = Monetary(float(amount),'NCN')
        self.available['NCN'] -= amount
        old_level = self.level
        self.frozen += amount
        print(f'{color.FREEZE}FREEZE:{color.ENDC} {-amount}')
        if old_level != self.level:
            msg = f'LEVEL UP: {old_level} to {self.level}'
            print(color.LEVEL_UP + msg + color.ENDC)

    def melt(self, amount):
        amount = Monetary(float(amount),'NCN')
        old_level = self.level
        self.frozen -= amount
        self.available['NCN'] += amount
        print(f'{color.FREEZE}MELT:{color.ENDC} {+amount}')
        if old_level != self.level:
            msg = f'LEVEL DOWN: {old_level} to {self.level}'
            print(color.LEVEL_UP + msg + color.ENDC)

    def buy_crypto(self, BRL, amount, name):
        BRL    = Monetary(float(BRL),'BRL')
        amount = Monetary(float(amount),name)
        self.available['BRL']-= BRL
        self.available[name] += amount
        crypto = Asset(BRL,amount)
        self.mean_price[name] += crypto
        print(f'{color.BUY+color.UNDERLINE}({name}) BUY:{color.ENDC}    {crypto}')
        print(f'{color.REWARD+color.UNDERLINE}({name}) ',end='')
        self.reward(BRL.value,origin=name)

    def buy(self, BRL, NCN):
        BRL = Monetary(float(BRL),'BRL')
        NCN = Monetary(float(NCN),'NCN')
        self.available['BRL'] -= BRL
        self.available['NCN'] += NCN
        self.mean_price['NCN'] += Asset(BRL,NCN)
        self.spent['NCN'] += BRL
        print(f'{color.BUY}BUY:{color.ENDC}    {Asset(BRL,NCN)}')

    def sell_crypto(self, BRL, amount, name):
        BRL = Monetary(float(BRL),'BRL')
        amount = Monetary(float(amount),name)
        self.available["BRL"] += BRL
        self.available[name] -= amount
        crypto = Asset(BRL,amount)
        self.sell_price[name] += crypto
        print(f'{color.SELL+color.UNDERLINE}SELL (BTC):{color.ENDC}   {crypto}')

    def sell(self, BRL, NCN):
        BRL = Monetary(float(BRL),'BRL')
        NCN = Monetary(float(NCN),'NCN')
        self.available["BRL"] += BRL
        self.available['NCN'] -= NCN
        self.sell_price['NCN'] += Asset(BRL,NCN)
        print(f'{color.SELL}SELL:{color.ENDC}   {Asset(BRL,NCN)}')

    def __str__(self):
        ret = make_title('WALLET SNAPSHOT',color.BOLD)
        ret += f'1 NCN = R$ {NCN_BRL:.8f}\n'
        ret += f'1 BTC = R$ {BTC_BRL:.2f}\n'
        ret += f'{color.BOLD}CURRENT LEVEL: {self.level}{color.ENDC}\n'
        ret += f'{color.BOLD}NEXT LEVEL: {self.next_level} = {self.next_level.convert_to("BRL")}{color.ENDC}\n'
        ret += make_title("REWARDS",color.REWARD)
        TOTAL_SPENT = Monetary(0,"BRL")
        TOTAL_REWARD = Monetary(0,"NCN")
        for k, v in self.spent.items():
            spent = self.spent[k]
            reward = self.rewards[k]
            TOTAL_SPENT += spent
            TOTAL_REWARD += reward
            percent = reward.amount / spent.amount * 100 if spent.amount else 0
            ret += f'{k}: {spent} and got {reward} ({percent:.2f}%)\n'
        ret += 48*"-" + '\n'
        percent = TOTAL_REWARD.amount / TOTAL_SPENT.amount * 100 if TOTAL_SPENT.amount else 0
        ret += f'In total you spent {TOTAL_SPENT} and got {TOTAL_REWARD} ({percent:.2f}%).\n'
        ret += make_title("LIQUID",color.REWARD)
        TOTAL_LIQUID = Monetary(0,'BRL')
        for k, v in self.available.items():
            brl_equivalece = self.available[k].convert_to("BRL")
            TOTAL_LIQUID += brl_equivalece
            ret += f'{k}: {self.available[k]} = {brl_equivalece}\n'
        ret += 48*"-" + '\n'
        TOTAL_FROZEN = self.frozen.convert_to("BRL")
        ret += f'In total you have liquid {TOTAL_LIQUID} and {TOTAL_FROZEN} frozen.\n'
        ret += 48*"-" + '\n'
        TOTAL_PROFIT = Monetary(0,'BRL')
        for k, v in ASSETS_INFO.items():
            if k in ['BRL']: continue
            profit = (self.sell_price[k] - self.mean_price[k]).fiduciary
            if profit.amount == 0: continue
            if self.sell_price[k].fiduciary.amount == 0: continue
            ret += f'MEAN PRICE {k}: {self.mean_price[k]}\n'
            ret += f'SELL PRICE {k}: {self.sell_price[k]}\n'
            ret += 48*"-" + '\n'
            if profit.amount > 0:
                ret += f'{color.POSITIVE}PROFIT {k}: {profit}{color.ENDC}\n'
            elif profit.amount < 0:
                ret += f'{color.NEGATIVE}LOSS {k}: {profit}{color.ENDC}\n'
            ret += 48*"-"+ '\n'
            TOTAL_PROFIT += profit
        ret += f'TOTAL_PROFIT: {TOTAL_PROFIT}\n'
        ret += 48*"-" + '\n'
        WALLET_WORTH = TOTAL_LIQUID + self.frozen.convert_to("BRL")
        ret += f'WALLET WORTH: {WALLET_WORTH}\n'
        ret += 48*"-" + '\n'
        return ret

if __name__ == '__main__':
    from nucoin import Monetary

    dez = Monetary(10.0, 'BRL')
    print(dez)
    dois = Monetary( 2.0, 'BRL')
    print(dois)
    dez_ncn = Monetary(10.0, 'NCN')

    print(dez * 2)
    print(dez * 4 + dois)
