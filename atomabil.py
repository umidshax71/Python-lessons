# a = input("asadsda")
# class Gm_UZ:
#
#     def __init__(self , nomi ,madeli , rangi , narxi, yili ,uzatma_turi  ):
#         self.nomi = nomi
#         self.madeli = madeli
#         self.rangi = rangi
#         self.narxi = narxi
#         self.yili = yili
#         self.uzatma_turi = uzatma_turi
#
#
#     def get_info(self):
#         return f"{self.nomi} {self.madeli} {self.rangi} {self.narxi} {self.yili} {self.uzatma_turi}"
#
#
# Gm_1 = Gm_UZ("Mersedes","Gt-12" ,"Qora","12000$", "2006","Aftamat karobka")
# print(Gm_1.get_info())
#
#

class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1



class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talaba_soni = 0
        self.talabalar = []


    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talaba_soni += 1





matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talaba_soni)
print(matematika.talabalar)
