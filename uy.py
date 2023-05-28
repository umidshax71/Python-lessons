def market(Mahsulot_nomi,grami,narxi):
    Market={"Mahsulot":Mahsulot_nomi,
            "Gram":grami,
            "Narx":narxi}
    return Market

Market1 = []





while True:
    Mahsulot = input("Mahsulot")
    Gram = input("mahsulot gramini kiriting:")
    narx = input("Maxsulot narxini kiriting")

    Market1.append(market(Mahsulot , Gram , narx))




    javob = input("Yana qushasizmi y/n")
    if javob == "n":
        break


    for i in Market1:
        if i["narx"]:
            narx = i["narx"]
        else:
            narx = "Nomalum"

print(Mahsulot , Gram , narx)

print(f"Sizni nimadiringgiz {Mahsulot},{Gram},{narx}")

