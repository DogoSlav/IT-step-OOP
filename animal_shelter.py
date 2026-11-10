"""
VIRTUÁLNÍ ZVÍŘECÍ ÚTULEK (Tamagotchi) – kostra programu
=========================================================

CO MUSÍ ŘEŠENÍ OBSAHOVAT (povinné):
  - základní třídu Animal a aspoň 3 potomky (Dog, Cat, Parrot)
  - každý potomek přepisuje metodu sound() a aspoň jednu další věc
    (např. jinak rychle roste hlad)
  - třídu Shelter, která drží seznam zvířat
  - hlavní smyčku po kolech: každé kolo se zvířatům změní hlad, energie a nálada
  - hráč může zvíře nakrmit, pohrát si s ním nebo ho uspat
  - zvíře, které je moc dlouho hladové, uteče

VOLITELNÉ (pro rychlejší):
  - nové zvíře lze do útulku přijmout (hráč zadá druh a jméno)
  - zvířata mohou onemocnět a hráč je léčí
  - uložení stavu útulku do souboru
  - body: kolik kol se hráči podařilo udržet všechna zvířata šťastná
"""
import random


class Animal:
    """Základní třída. NEMĚNIT (jen číst)."""

    def __init__(self, name, hunger_rate=10):
        self.name = name
        self.hunger = 30                 # 0 = sytý, 100 = umírá hlady
        self.energy = 70                 # 0 = vyčerpaný, 100 = plný sil
        self.mood = 70                   # 0 = smutný, 100 = nadšený
        self.hunger_rate = hunger_rate   # o kolik hlad vzroste každé kolo

    def limit(self, value):
        """Drží hodnotu v rozmezí 0 až 100."""
        return max(0, min(100, value))

    def sound(self):
        return "..."

    def next_round(self):
        self.hunger = self.limit(self.hunger + self.hunger_rate)
        self.energy = self.limit(self.energy - 5)
        if self.hunger > 70:
            self.mood = self.limit(self.mood - 15)

    def feed(self):
        self.hunger = self.limit(self.hunger - 40)
        print(self.name + " se nají. " + self.sound())

    def play(self):
        if self.energy < 20:
            print(self.name + " je moc unavený na hraní.")
            return
        self.mood = self.limit(self.mood + 25)
        self.energy = self.limit(self.energy - 20)
        print(self.name + " si hraje. " + self.sound())

    def sleep(self):
        self.energy = self.limit(self.energy + 50)
        print(self.name + " si zdřímne. Chrr...")

    def is_happy(self):
        return self.hunger < 70 and self.mood > 30

    def __str__(self):
        return (self.name + " | hlad " + str(self.hunger) +
                " | energie " + str(self.energy) +
                " | nálada " + str(self.mood))


# ---------------------------------------------------------------- ZVÍŘATA
class Dog(Animal):
    """HOTOVÝ PŘÍKLAD – pes je pořád hladový a hrozně rád si hraje."""

    def __init__(self, name):
        super().__init__(name, hunger_rate=15)

    def sound(self):
        return "Haf haf!"

    def play(self):
        super().play()                   # nejdřív uděláme to, co umí každé zvíře
        self.mood = self.limit(self.mood + 10)   # a pes se navíc ještě víc raduje


# TODO 1: Vytvoř třídu Cat. Zvuk "Mňau". Kočka je soběstačná –
#         hlad jí roste pomaleji (hunger_rate=7).

# TODO 2: Vytvoř třídu Parrot. Zvuk: vymysli (třeba aby opakoval náhodnou větu
#         ze seznamu přes random.choice). Přepiš i next_round(),
#         aby se papoušek nudil: nálada klesá o 5 každé kolo navíc.

# TODO 3 (vlastní nápad): Další zvíře, např. Rabbit nebo Turtle.


# ---------------------------------------------------------------- ÚTULEK
class Shelter:
    def __init__(self):
        self.animals = []

    def admit(self, animal):
        self.animals.append(animal)
        print("Do útulku přišel nový obyvatel: " + animal.name + ".")

    def show(self):
        number = 1
        for animal in self.animals:
            print(str(number) + ") " + str(animal))
            number = number + 1

    def next_round(self):
        for animal in self.animals:
            animal.next_round()
        # TODO 4: Zvíře s hladem 100 uteče. Odeber ho ze seznamu a vypiš zprávu.
        #         POZOR: nemaž ze seznamu, přes který zrovna procházíš cyklem for!
        #         Tip: vytvoř nový seznam jen se zvířaty, která zůstávají.

    def choose_animal(self):
        """Zeptá se hráče na číslo zvířete. Vrátí objekt, nebo None."""
        # TODO 5: Načti číslo 
        #         a vrať odpovídající zvíře ze seznamu.
        return None


# ---------------------------------------------------------------- HRA
def main():
    shelter = Shelter()
    shelter.admit(Dog("Rex"))
    # TODO 6: Přijmi do útulku ještě kočku a papouška.

    for round_number in range(1, 31):
        print("\n===== KOLO " + str(round_number) + " =====")
        shelter.show()
        action = input("[n]akrmit  [h]rát si  [u]spat  [k]onec: ").lower()

        if action == "k":
            break
        animal = shelter.choose_animal()
        if animal is not None:
            if action == "n":
                animal.feed()
            # TODO 7: Doplň akce 'h' (play) a 'u' (sleep).

        shelter.next_round()

    # TODO 8: Na konci vypiš, kolik zvířat je šťastných (is_happy()).
    print("\nKonec hry!")


main()
