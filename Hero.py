import random


class Hero:
   def __init__(self,atak,obrona,żywotność,imię):
       self.atak=atak
       self.obrona=obrona
       self.żywotność=żywotność
       self.imię=imię

   def walcz(self, przeciwnik):
       trafienie = random.randint(1,10)+self.atak
       if trafienie>= przeciwnik.obrona:
           przeciwnik.żywotność -= 1
           print(f"Bohater {self.imię} trafił {przeciwnik.imię} !")
           if przeciwnik.żywotność<=0:
               print(f"Bohater {self.imię} pokonał {przeciwnik.imię} !")
       else:
            print(f"Bohater {self.imię} spudłował!")


bohater1 = Hero(5, 7, 10, "Maciej")
bohater2 = Hero(5, 7, 10, "Zbyszko")

while bohater1.żywotność>0 and bohater2.żywotność>0:
    bohater1.walcz(bohater2)
    if bohater2.żywotność>0:
        bohater2.walcz(bohater1)
if bohater1.żywotność>0:
    print(f"Bohater {bohater1.imię} Wygrywa! Bohater {bohater2.imię} Pada na ziemię!")
else:
    print(f"Bohater {bohater2.imię} Wygrywa! Bohater {bohater1.imię} pada na ziemię!")

