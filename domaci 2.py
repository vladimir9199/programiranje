# -*- coding: utf-8 -*-
rečnik={"Debeo":{"Sinonimi":["Ugojen", "Punacak"],"Antonimi":["Mrsav","Tanak"]},"Hladan":{"Sinonimi":["Leden","Studen"],"Antonimi":["Topao","Vreo"]},"Brz":{"Sinonimi":["Okretan","Hitar"],"Antonimi":["Spor","Trom"]}}

print(rečnik["Debeo"]["Sinonimi"])
print(rečnik["Hladan"]["Sinonimi"])
print(rečnik["Brz"]["Sinonimi"])

print(rečnik["Debeo"]["Antonimi"])
print(rečnik["Hladan"]["Antonimi"])
print(rečnik["Brz"]["Antonimi"])

print(rečnik["Hladan"]["Sinonimi"][0])
print(rečnik["Hladan"]["Antonimi"][1])

for reč in rečnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]:
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n")