def Avto_mashina(Kompaniya, Nomi, Ranggi, tayp):
    avto = {"Kompaniya":Kompaniya,
            "Nomi":Nomi,
            "rangi":Ranggi,
            "Tayp":tayp}
    return avto

print("Avtomobil Ro'yxatini shakillantiring:")
avtolar = []


while True:
    print("Avtomobil malumotlarini kiriting:", end='')
    kompaniya = input("Ishlab chiqargan kompaniya nomi kiriting:")
    model = input("Avtomobil madelini kiriting:")
    rangi = input("Avtomabil rangini kiritng:")
    yili = input("Avtomobil yilini kiriting:")
    narxi = input("Avtomobil Narxi :")
    avtolar.append(Avto_mashina(kompaniya , model , rangi , yili ))

    javob = input("Yana avtomobil qushasizmi y/n :")
    if javob == "n":
        break


print(f"Mashinang giz ",kompaniya,"\n",model,"\n",rangi,"\n",yili,"\n",narxi,)