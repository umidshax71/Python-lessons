import talaba
class Talaba:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def malumot(self):
        return f"{self.ism} | {self.familiya} | {self.yosh}"

    def ism_info(self):
        return self.ism

    def familiya_info(self):
        return self.familiya

    def yosh_info(self):
        return self.yosh

a = Talaba("Umid","Ismoilov","16")

print(Talaba.familiya_info(a))


