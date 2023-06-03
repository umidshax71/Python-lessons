# def Ism_sharf(ism, sharf):
#     print("Mening ismim:",ism,"\n","Sharfim",sharf)
#
#
# Ism_sharf("Umid", "Ismoilov")

# a = int(input("Yoshinggizni kiriting:"))
# b = input("Isminggiz:")
# def ism_yosh(ism , yosh ):
#     print("Mening ismim:",ism,"\n","Meni yoshim:",yosh)
#
#
# ism_yosh(b , a)




# a = int(input("Son kiriting:"))
# def math(kubSon,kvadratson):
#     print("Sizning",kubSon,"\n","Sizni soning giz",kvadratson)
# math(a**3,a**2)



#
# a = int(input("Son kiriting:"))
# def mat(Toqson,JUftson):
#     print( JUftson ,Toqson)
#
# if a % 2 == 0:
#     print("Son juft")
# else:
#    print("Son toq")
#

#
# a = int(input("Son kiriting:"))
# b = int(input("Son 2ni kiriting:"))
# def amt(Son , Daraja):
#     print(Son**Daraja)
#
# amt(a,b)
#
# a = [2,3,4,5,6]
# def Mat(bulinuvhchi):
#     print(bulinuvhchi)
#     if a / 2:
#         print(a)
#     else:
#         pass
#
# Mat(a)


def ism_yasash(ism, familiya, sharif=''):
    if sharif:
        yasash = f"{ism} | {familiya} | {sharif}"
    else:
        yasash = f"{ism} | {familiya}"

    return yasash
t11 = ism_yasash("Umid", "asdasd")
t10 = ism_yasash("Umid","ISmoilov","sdfsdfsdfsdfsd")
print( t11)








