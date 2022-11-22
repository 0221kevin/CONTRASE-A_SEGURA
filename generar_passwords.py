import random

#clasificador de caracteres
def class_carac(letra):
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        return 1
    elif letra=="0" or letra=="1" or letra=="2" or letra=="3" or letra=="4" or letra=="5" or letra=="6" or letra=="7" or letra=="8" or letra=="9":
        return 2
    else: 
        return 0


# mayuscula minuscula
def mayus(letra):
    azar=random.randrange(0,3)
    if azar==2:
        let="".join(letra)
        letMa=let.upper()
        return letMa
    else:
        return letra


#intercambio de numeros
def interc_num(num):
    nueNum=round((num+random.randrange(0,9))%random.randrange(1,9))
    return nueNum


#intercambio de vocales

def interc_vocales(letra):
    if letra=="a":
        letra="@"

        return letra
    if letra=="e":
        letra="3"

        return letra
    if letra=="i":
        letra="!"
        return letra
    if letra=="o":
        letra="0"
        return letra
    if letra=="u":
        letra="U"
        return letra

#GENERADOR DE CONTRASEÑA SEGURA

passElegido=input("Ingrese una contraseña: ")
passEleLower=passElegido.lower()
passcifrado=[]

i=0

for i in range(len(passEleLower)):
    letra=passEleLower[i]
    passcifrado.append(letra)

for element in passcifrado:
    #intercambio de vocales
    if class_carac(element)==0:
        letraFnal=mayus(element)
        ubi=passcifrado.index(element)
        passcifrado[ubi]=letraFnal
     

    if class_carac(element)==1:
        ubi=passcifrado.index(element) 
        NCarac=interc_vocales(element)
        passcifrado[ubi]=NCarac
    if class_carac(element)==2:
        ubi=passcifrado.index(element) 
        element=int(element)
        nueNum=interc_num(element)
        nueNum=str(nueNum)
        passcifrado[ubi]=nueNum

pas="".join(passcifrado)
print("---------------------------------------------------")
print("Su contraseña:   ",pas,)
print("----------------------------------------------------")

        
    

    

    
    

        





