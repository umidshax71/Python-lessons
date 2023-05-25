print("Assalomu alaykum Master panda onlin dukonga xush kelipsiz!")
print("Katigoriyalar""\n""$-->Kiyimlar""\n""%->Admin<-%")
a = input("Katigoriya tanlang: ")
if a == "Kiyim":
    print("O'g'il bolalar uchun!_Id raqami:1""\n""Qizlar uchun!_ Id raqami:2")
    b = input("Id raqamni tanlang:")
    if b ==  1:
        print("Siz O'g'il bolalar ID ni tanladinggiz ")
        print("Sizga qanaqa kiyim yoqadi""\n""clasic""\n""Sport")
        n = input("Sizga qanaqa kiyim turi yoqadi:")
        if n == "clasic":
            print("Clasic kiyimlar kategoriyasini tanladinggiz")
            print(list["Clasic Shim" , "Clasic Kastyum"])
        elif n == "Sport":
            print("Sport kiyim kategoriyasini tanladinggiz ")
            print("")

            pass

    else:
        pass

elif a == "admin":
    while True:
        print("Admin")
        a = int(input("parolinggiz:"))
        if a == 2006:
            print("Parol to'g'ri")
            print("salom")
        elif a != 2006:
            print("eror")
            break


















        # if a == 2006:
        #     print("Serverga kirdinggiz ")
        #     print("tanlang",'\n', "Maxsulotlartni ko'rish       >1<",'\n',"Maxsulot qushish      >2<","")
        #
        # else:
        #     print("Error Qayta kiriting:")
        #     print(a)
        #
        # break












