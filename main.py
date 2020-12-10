import sys
#citeste si salveaza intr-o lista liniile fisierului
def lista_fisier(fisier):
    file = open(fisier,'r')
    lista = file.readlines()
    file.close()
    return lista

#trece prin lista cu toate liniile unui fisier
def extrage_linie(lista_linii,fisier):
    for linie in lista_linii:
        extrage_propozitie(linie.strip(),fisier)

#salveaza intr-o lista fiecare propozitie dintr-o linie
def extrage_propozitie(linie,fisier):
    global propozitii1
    global propozitii2
    propozitie = ""
    for i in range(0, len(linie)):
        if linie[i] != ".":
            propozitie += linie[i]
        else:
            propozitie += linie[i]
            new_sentence = linie[i + 1:]
            if fisier == "file1":
                propozitii1.append(propozitie)
                extrage_propozitie(new_sentence,"file1")

            elif fisier =="file2":
                propozitii2.append(propozitie)
                extrage_propozitie(new_sentence,"file2")

def compara_propozitii(propozitie1, propozitie2):
    if len(propozitie1) != len(propozitie2):
        return False
    else:
         i = 0
         while i < len(propozitie1):
             if propozitie1[i] != propozitie2[i]:
                 return False
             i = i + 1
    return True

def creeaza_lista_comuna(propozitii1, propozitii2, final_list):
    for prop1 in propozitii1:
        for prop2 in propozitii2:
            if compara_propozitii(prop1, prop2):
                final_list.append(prop1)

propozitii1 =[]
propozitii2=[]
final_list = []

if len(sys.argv) != 3:
    print("Wrong number of arguments !")
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    lista_linii_f1 = lista_fisier(file1)
    lista_linii_f2 = lista_fisier(file2)

    extrage_linie(lista_linii_f1,"file1")
    extrage_linie(lista_linii_f2,"file2")

    creeaza_lista_comuna(propozitii1,propozitii2,final_list)
    print(final_list)