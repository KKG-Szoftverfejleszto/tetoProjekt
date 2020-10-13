print("Készítette: Tamás Dávid Sándor")

print("Az alábbi program egy ház tetejének teljes lefedéséhez szükséges cserépmennyiséget számolja ki.")

hazhossz = 23

print( "A ház hossza:", hazhossz , "méter.")

tetomagassag = 3.2

print( "A tető magassága:" , tetomagassag , "méter." )

hazszelesseg = 9.6

print( "A ház szélessége:" , hazszelesseg , "méter." )

cserephossz = 25

cserepszelesseg = 12

print( "Egy cserép mérete:" , cserephossz , "cm *" , cserepszelesseg , "cm.")

import math 

tetorovidoldal = math.sqrt(math.pow(tetomagassag , 2) + math.pow(hazszelesseg/2, 2))

tetofelulet = (tetorovidoldal * hazhossz)

cserepterulet = (cserephossz * cserepszelesseg)

cserepteruletnmben = cserepterulet / 1000

cserepmennyiseg = tetofelulet / cserepteruletnmben

teljescserepmennyiseg = math.ceil(cserepmennyiseg) * 2 #Mivel egy cserép két felét nem minden esetben lehet felhasználni így a tető egyik oldalára szánt cserepek mennyiségét felfelé kell kerekíteni.

print("A fenti adatok alapján a tető teljes lefedéséhez", teljescserepmennyiseg , "cserépre van szükség." )



