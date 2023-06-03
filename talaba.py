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
talaba1 = Talaba("Umid","Ismoilov",2006)
print(talaba1.get_info())




