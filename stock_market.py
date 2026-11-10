"""
SIMULACE AKCIOVÉHO TRHU – kostra programu
=========================================

CO MUSÍ ŘEŠENÍ OBSAHOVAT (povinné):
  - základní třídu Asset a aspoň 3 potomky (málo / středně / hodně riskantní)
  - aspoň jednu přepsanou metodu v potomkovi (change_price)
  - třídu Portfolio (hotovost + držená aktiva) s metodami buy a sell
  - hlavní smyčku po tazích: každý tah se ceny změní a hráč může obchodovat
  - na konci výpis, kolik hráč vydělal nebo prodělal

VOLITELNÉ (pro rychlejší):
  - náhodné události ("zpráva z trhu": firma ohlásila zisk / skandál)
  - graf vývoje ceny (knihovna matplotlib)
  - uložení historie obchodů do souboru
  - poplatek za každý obchod
"""
import random


class Asset:
    """Základní třída pro cokoliv, s čím lze obchodovat. NEMĚNIT (jen číst)."""

    def __init__(self, name, price, volatility):
        self.name = name
        self.price = price
        self.volatility = volatility     # jak moc cena "skáče" (0.05 = až o 5 %)
        self.history = [price]           # seznam všech dosavadních cen

    def change_price(self):
        """Posune cenu náhodně nahoru nebo dolů podle volatility."""
        change = random.uniform(-self.volatility, self.volatility)
        self.price = round(self.price * (1 + change), 2)
        self.history.append(self.price)

    def __str__(self):
        return self.name + ": " + str(self.price) + " Kč"


# ---------------------------------------------------------------- AKTIVA
class Bond(Asset):
    """HOTOVÝ PŘÍKLAD – bezpečná investice, cena se hýbe jen málo."""

    def __init__(self, name, price):
        super().__init__(name, price, volatility=0.01)


# TODO 1: Vytvoř třídu Stock se střední volatilitou (např. 0.08).

# TODO 2: Vytvoř třídu Crypto s velkou volatilitou (např. 0.25).
#         PŘEPIŠ metodu change_price tak, aby měla 5% šanci na krach
#         (cena klesne na 10 % hodnoty). Nezapomeň na super().change_price().

# TODO 3 (vlastní nápad): Přidej další aktivum, např. Gold nebo RealEstate.


# ---------------------------------------------------------------- PORTFOLIO
class Portfolio:
    """Peněženka hráče: hotovost + kolik kusů čeho vlastní."""

    def __init__(self, cash):
        self.cash = cash
        self.starting_cash = cash
        self.holdings = {}               # slovník: název aktiva -> počet kusů

    def buy(self, asset, amount):
        cost = asset.price * amount
        if cost > self.cash:
            print("Nemáš dost peněz!")
            return
        # TODO 4: Odečti cost z hotovosti a přičti kusy do self.holdings.

    def sell(self, asset, amount):
        # TODO 5: Zkontroluj, že hráč tolik kusů vlastní.
        #         Pak přičti utržené peníze a odečti kusy.
        pass

    def total_value(self, market):
        """Hotovost + hodnota všech držených aktiv podle aktuálních cen."""
        # TODO 6: Projdi market, u každého aktiva vynásob cenu počtem držených kusů.
        return self.cash

    def show(self):
        print("Hotovost: " + str(round(self.cash, 2)) + " Kč")
        for name in self.holdings:
            print("  " + name + ": " + str(self.holdings[name]) + " ks")


# ---------------------------------------------------------------- HRA
def main():
    market = [
        Bond("Státní dluhopis", 1000),
        # TODO 7: Přidej další aktiva (Stock, Crypto, ...).
    ]
    player = Portfolio(10000)
    turns = 20

    for turn in range(1, turns + 1):
        print("\n===== TAH " + str(turn) + "/" + str(turns) + " =====")
        number = 1
        for asset in market:
            print(str(number) + ") " + str(asset))
            number = number + 1
        player.show()

        while True:
            action = input("[k]oupit  [p]rodat  [d]alší tah: ").lower()
            if action == "d":
                break
            # TODO 8: Pro 'k' a 'p' se zeptej na číslo aktiva a počet kusů
            #         a zavolej player.buy(...) / player.sell(...).
            #         Ošetři špatný vstup (int(input()) může spadnout – použij try/except).

        for asset in market:
            asset.change_price()

    # TODO 9: Na konci vypiš celkovou hodnotu a zisk/ztrátu
    #         (total_value - starting_cash).
    print("\nKonec hry!")


main()
