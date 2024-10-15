import sys
import os
import time
import json
from colorama import Fore, Back, Style


kosar = []

def mentes():
    with open('kosar.json', 'w') as file:
        json.dump(kosar, file, indent=4, ensure_ascii=False)

if os.path.exists('kosar.json'):
    with open('kosar.json', 'r') as file:
        kosar = json.load(file)  
else: 
    print("A kosár üres!\n\n")

def typewrite(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.014)
    print("")

def parancsok():
    typewrite("--------------------------------------------")
    typewrite(" ×    1. Elem hozzáadása a kosárhoz")
    typewrite(" ×    2. Elem törlése a kosárból")
    typewrite(" ×    3. Elem módosítása")
    typewrite(" ×    4. Kosár tartalmának törlése")
    typewrite(" ×    5. Kosár megtekintése")
    typewrite(" ×    6. Parancsok megtekintése")
    typewrite(" ×    7. Kilépés az alkalmazásból")
    typewrite("--------------------------------------------")




typewrite(f"\n\n     👋   Üdvözöllek az alkalmazásban!\n")
typewrite("Az az alkalmazásban 4 féle művelet közül választhatsz, amik a kövezketőek:")
typewrite("--------------------------------------------")
typewrite(" ×    1. Elem hozzáadása a kosárhoz")
typewrite(" ×    2. Elem törlése a kosárból")
typewrite(" ×    3. Elem módosítása")
typewrite(" ×    4. Kosár tartalmának törlése")
typewrite(" ×    5. Kosár megtekintése")
typewrite(" ×    6. Parancsok megtekintése")
typewrite(" ×    7. Kilépés az alkalmazásból")

def app():

    option = str(input("Kérlek válassz egy opciót! (1,2,3,4,5,6,7) "))

    if option == "1":
        termek = str(input("Add meg az első terméket amit a kosárhoz akarsz adni! "))
        ar = int(input(f"Kérlek add meg a(z) {termek} árát! "))
        kosar.append({"termek": termek, "ar": ar})
        mentes()
        app()
    elif option == "2":
        if kosar:
            torlendo_termek = int(input("Add meg a törölni kívánt termék sorszámát: "))
            if 1 <= torlendo_termek <= len(kosar):
                torolt_termek = kosar.pop(torlendo_termek - 1)
                typewrite(f"{torolt_termek['termek']} sikeresen törölve lett a kosaradból.")
                mentes()
                app()
            else: 
                print("Nem létező termék!")
                app()
        else:
            print("Szerveroldali hiba történt")
            app()

        
    elif option == "3":
        if kosar:
            valtoztatando_termek = int(input("Kérlek add meg a változtatni kívánt termék sorszámát: "))
            if 1 <= valtoztatando_termek <= len(kosar):
                valtoztatott_termek = kosar[valtoztatando_termek - 1]
                typewrite(f"Kiválasztott termék: {valtoztatott_termek['termek']}, Ár: {valtoztatott_termek['ar']} Ft")

                termek_valtoztatas = str(input("Szeretnéd módosítani a termék nevét? (nyomj entert, ha nem!) "))
                ar_valtoztatas = str(input("Szeretnéd változtatni a termék árát? (nyomj entert, ha nem!) "))
                
                if termek_valtoztatas.strip():
                    kosar[valtoztatando_termek - 1]['termek'] = termek_valtoztatas

                if ar_valtoztatas.strip():
                    try: 
                        kosar[valtoztatando_termek - 1]['ar'] = int(ar_valtoztatas)
                    except ValueError:
                        typewrite("Érvénytelen ár, az ár módosítása elmarad!")
                
                mentes()
                typewrite(f"A(z) {kosar[valtoztatando_termek - 1]['termek']} sikeresen módosítva!")
            else:
                typewrite("Érvénytelen sorszám!")
         
            typewrite("Frisített kosár tartalom:")
            for index, item in enumerate(kosar):
                typewrite(f"{index + 1}. Termék: {item['termek']}, Ár: {item['ar']} Ft")
        else:
            typewrite("Nincs mit módosítani, a kosár üres!")
        
        
        app()
        
    elif option == "4":
        torles = input("Biztosan törölni akarod az egész kosarad? (y/n): ")
        if torles == 'y':
            typewrite("Sikeresen törölted a kosaradat! ")
            with open('kosar.json', 'w') as file:
                json.dump({}, file, indent=4, ensure_ascii=False)
        elif torles == 'n':
            pass
        else:
            typewrite("Igen (y) vagy Nem (n) közül választhatsz! ")
        app()
    elif option == "5":
        if kosar:
            typewrite("A kosár tartalma:")
            for index, item in enumerate(kosar):
                typewrite(f"{index + 1} {item['termek']}, Ár: {item['ar']} Ft")
                app()
        else:
            typewrite("A kosár üres!")
            app()
    elif option == "6":
        parancsok()
        app()
    elif option == "7":
        typewrite("\n\n👋 Viszontlátásra!\n")
        time.sleep(0.02)
        typewrite(f"{Fore.RED}🪢  Leállítás... \n\n")
        time.sleep(1)
        sys.exit()
    else:
        typewrite("Kérlek válassz egy valid opciót")
        app()
app()
