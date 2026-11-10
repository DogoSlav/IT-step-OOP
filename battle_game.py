"""
BOJOVÁ HRA – kostra programu
============================

CO MUSÍ ŘEŠENÍ OBSAHOVAT (povinné):
  - základní třídu Character a aspoň 3 hrdiny (potomci) a aspoň 3 nepřátele (potomci)
  - aspoň jednu metodu přepsanou v potomkovi (např. special_ability)
  - výběr hrdiny na začátku hry
  - souboj s aspoň 3 nepřáteli po sobě

VOLITELNÉ (pro rychlejší):
  - hrdina po výhře získá zkušenosti a zesílí
  - lektvary (třída Item) a inventář
  - uložení nejlepšího skóre do souboru
  - boss na konci hry
"""
import random


class Character:
    """Základní třída – společná pro hrdiny i nepřátele. NEMĚNIT (jen číst)."""

    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health            # zdraví měníme jen přes metody (take_damage)
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def hit(self, target):
        """Běžný útok na cíl. Poškození je trochu náhodné."""
        damage = max(1, self.attack_power + random.randint(-2, 2) - target.defense)
        target.take_damage(damage)
        print(self.name + " útočí na " + target.name + " a způsobí " + str(damage) + " poškození.")

    def special_ability(self, target):
        """V potomcích PŘEPIŠ. Tady postava žádnou schopnost nemá."""
        print(self.name + " nemá žádnou speciální schopnost.")

    def __str__(self):
        return self.name + " (zdraví " + str(self.health) + "/" + str(self.max_health) + ")"


# ---------------------------------------------------------------- HRDINOVÉ
class Warrior(Character):
    """HOTOVÝ PŘÍKLAD – podle něj udělej další hrdiny."""

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15, defense=8)

    def special_ability(self, target):
        # Silný úder: dvojnásobný útok, ale ignoruje obranu
        damage = self.attack_power * 2
        target.take_damage(damage)
        print(self.name + " zasadí DRTIVÝ ÚDER za " + str(damage) + " poškození!")


# TODO 1: Vytvoř třídu Mage (málo zdraví, vysoký útok).
#         Speciální schopnost: ohnivá koule – velké poškození.

# TODO 2: Vytvoř třídu Archer (střední hodnoty).
#         Speciální schopnost: dvojitý výstřel – dva útoky za sebou.

# TODO 3 (vlastní nápad): Vytvoř čtvrtého hrdinu, např. Healer
#         (schopnost: vyléčí sám sebe – změň self.health).


# ---------------------------------------------------------------- NEPŘÁTELÉ
class Goblin(Character):
    """HOTOVÝ PŘÍKLAD nepřítele."""

    def __init__(self):
        super().__init__("Goblin", health=40, attack_power=8, defense=2)


# TODO 4: Vytvoř třídy Skeleton a Dragon (Dragon = silný, pro poslední souboj).
#         Aspoň jednomu nepříteli přepiš special_ability
#         (např. drak dýchne oheň).


# ---------------------------------------------------------------- HRA
def choose_hero():
    """Hráč si vybere hrdinu. Vrátí vytvořený objekt."""
    print("Vyber si hrdinu:")
    print("  1) Válečník")
    # TODO 5: Doplň další hrdiny do nabídky.
    choice = input("Tvoje volba: ")
    name = input("Jak se tvůj hrdina jmenuje? ")
    if choice == "1":
        return Warrior(name)
    # TODO 6: Doplň další větve (elif) pro ostatní hrdiny.
    print("Neplatná volba, dostaneš válečníka.")
    return Warrior(name)


def fight(hero, enemy):
    """Jeden souboj. Vrátí True, pokud hrdina vyhrál."""
    print("\n=== " + hero.name + " vs. " + enemy.name + " ===")
    while hero.is_alive() and enemy.is_alive():
        print("\n" + str(hero))
        print(str(enemy))
        action = input("[1] Útok  [2] Speciální schopnost: ")

        # TODO 7: Podle action zavolej hero.hit(enemy)
        #         nebo hero.special_ability(enemy).

        # TODO 8: Pokud nepřítel ještě žije, zaútočí zpět na hrdinu.
        #         (nezapomeň: při smrti nepřítele souboj končí!)
        break  # <- tento řádek SMAZAT, až bude cyklus hotový

    return hero.is_alive()


def main():
    print("*** BOJOVÁ HRA ***")
    hero = choose_hero()

    # TODO 9: Vytvoř seznam nepřátel (např. Goblin(), Skeleton(), Dragon()).
    enemies = [Goblin()]

    for enemy in enemies:
        if not fight(hero, enemy):
            print("Prohrál jsi. Konec hry.")
            return
        print("Porazil jsi: " + enemy.name + "!")

    print("VYHRÁL JSI CELOU HRU!")


main()
