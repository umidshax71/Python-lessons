# def Avto_mashina(Kompaniya, Nomi, Ranggi, tayp):
#     avto = {"Kompaniya":Kompaniya,
#             "Nomi":Nomi,
#             "rangi":Ranggi,
#             "Tayp":tayp}
#     return avto
#
# print("Avtomobil Ro'yxatini shakillantiring:")
# avtolar = []
#
#
# while True:
#     print("Avtomobil malumotlarini kiriting:", end='')
#     kompaniya = input("Ishlab chiqargan kompaniya nomi kiriting:")
#     model = input("Avtomobil madelini kiriting:")
#     rangi = input("Avtomabil rangini kiritng:")
#     yili = input("Avtomobil yilini kiriting:")
#     narxi = input("Avtomobil Narxi :")
#     avtolar.append(Avto_mashina(kompaniya , model , rangi , yili ))
#
#     javob = input("Yana avtomobil qushasizmi y/n :")
#     if javob == "n":
#         break
#
#
# print(f"Mashinang giz ",kompaniya,"\n",model,"\n",rangi,"\n",yili,"\n",narxi,)


# class Avto:
#     """Avtomobil klassi"""
#
#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#
#
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id


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



talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_info())

talaba1.update_bosqich() # 1 bosqichga oshiramiz
print(talaba1.get_info())