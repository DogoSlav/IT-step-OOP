"""
FARMA – kostra programu
=======================

CO MUSÍ ŘEŠENÍ OBSAHOVAT (povinné):
  - základní třídu Plant a aspoň 3 potomky (např. Carrot, Sunflower, Apple)
  - každý potomek má jinou cenu semínka, dobu růstu a cenu při prodeji
  - aspoň jednu přepsanou metodu v potomkovi
  - třídu Farm s penězi a záhony (seznam rostlin)
  - hlavní smyčku po dnech: hráč sází, zalévá, sklízí a prodává
  - cíl hry: vydělat zadanou částku za omezený počet dní

VOLITELNÉ (pro rychlejší):
  - počasí (déšť zalije rostliny za tebe, sucho je vysuší)
  - škůdci, kteří občas napadnou náhodnou rostlinu
  - obchod, kde se dají kupovat vylepšení (např. větší počet záhonů)
  - uložení hry do souboru
"""
import random


class Plant:
    """Základní třída. NEMĚNIT (jen číst)."""

    def __init__(self, name, seed_price, growth_days, sell_price):
        self.name = name
        self.seed_price = seed_price
        self.growth_days = growth_days   # kolik dní musí růst, než je zralá
        self.sell_price = sell_price
        self.age = 0
        self.watered = False
        self.healthy = True

    def next_day(self):
        """Rostlina roste jen když byla ten den zalitá."""
        if self.watered:
            self.age = self.age + 1
        self.watered = False             # další den je potřeba zalít znovu

    def water(self):
        self.watered = True

    def is_ripe(self):
        return self.healthy and self.age >= self.growth_days

    def __str__(self):
        if self.is_ripe():
            return self.name + ": ZRALÁ"
        return self.name + ": " + str(self.age) + "/" + str(self.growth_days) + " dní"


# ---------------------------------------------------------------- ROSTLINY
class Carrot(Plant):
    """HOTOVÝ PŘÍKLAD – rychlá a levná plodina."""

    def __init__(self):
        super().__init__("Mrkev", seed_price=5, growth_days=3, sell_price=12)


# TODO 1: Vytvoř třídu Sunflower (střední cena, doba růstu 5 dní).

# TODO 2: Vytvoř třídu Apple (drahá, roste dlouho – 8 dní – ale vyplatí se).
#         PŘEPIŠ metodu next_day(): jabloň roste i když není zalitá
#         s 20% šancí (random.random() < 0.2) – stromy mají hluboké kořeny.
#         Nezapomeň na super().next_day().

# TODO 3 (vlastní nápad): Přidej další plodinu, např. Pumpkin, Strawberry, Corn.


# ---------------------------------------------------------------- FARMA
class Farm:
    def __init__(self, money, plots_count):
        self.money = money
        self.plots_count = plots_count
        self.plots = []                  # seznam rostlin, které právě rostou

    def show(self):
        print("Peníze: " + str(self.money) + " Kč   Záhony: " +
              str(len(self.plots)) + "/" + str(self.plots_count))
        number = 1
        for plant in self.plots:
            print("  " + str(number) + ") " + str(plant))
            number = number + 1

    def plant_seed(self, new_plant):
        if len(self.plots) >= self.plots_count:
            print("Všechny záhony jsou plné!")
            return
        # TODO 4: Zkontroluj, že máme dost peněz na semínko (new_plant.seed_price).
        #         Pak odečti peníze a přidej new_plant do self.plots.

    def water_all(self):
        # TODO 5: Projdi všechny rostliny a zavolej u každé water().
        pass

    def harvest_and_sell(self):
        # TODO 6: Projdi záhony. Zralé rostliny prodej (přičti sell_price
        #         k penězům) a odstraň je ze seznamu.
        #         POZOR: nemaž ze seznamu, přes který zrovna procházíš cyklem for!
        #         Tip: sestav nový seznam jen z rostlin, které ještě rostou.
        pass

    def next_day(self):
        for plant in self.plots:
            plant.next_day()


# ---------------------------------------------------------------- HRA
def main():
    farm = Farm(money=50, plots_count=4)
    goal = 300
    days = 30

    for day in range(1, days + 1):
        print("\n===== DEN " + str(day) + "/" + str(days) + " (cíl: " + str(goal) + " Kč) =====")
        farm.show()

        while True:
            action = input("[s]adit  [z]alít vše  [p]rodat zralé  [d]alší den: ").lower()
            if action == "d":
                break
            if action == "s":
                print("  1) Mrkev")
                # TODO 7: Doplň nabídku dalších plodin, zeptej se hráče
                #         a zavolej farm.plant_seed(Carrot()) / farm.plant_seed(Sunflower()) ...
                farm.plant_seed(Carrot())
            # TODO 8: Doplň akce 'z' (water_all) a 'p' (harvest_and_sell).

        farm.next_day()

        if farm.money >= goal:
            print("\nVYHRÁL JSI! Za " + str(day) + " dní máš " + str(farm.money) + " Kč.")
            return

    print("\nKonec času. Vydělal jsi " + str(farm.money) + " Kč z " + str(goal) + ".")


main()
