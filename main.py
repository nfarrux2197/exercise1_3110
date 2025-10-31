class Vaqt:
    def __init__(self, soat=0, minut=0, sekund=0):
        self.soat = soat
        self.minut = minut
        self.sekund = sekund

    def vaqt_korsat(self):
        return f"{self.soat:02d}:{self.minut:02d}:{self.sekund:02d}"

    def sekund_qosh(self, son):
        self.sekund += son

        if self.sekund >= 60:
            self.minut += self.sekund // 60
            self.sekund %= 60

        if self.minut >= 60:
            self.soat += self.minut // 60
            self.minut %= 60

        if self.soat >= 24:
            self.soat %= 24


vaqt1 = Vaqt(10, 59, 50)
print("Boshlang‘ich:", vaqt1.vaqt_korsat())

vaqt1.sekund_qosh(15)
print("Qo‘shilgandan keyin:", vaqt1.vaqt_korsat())
