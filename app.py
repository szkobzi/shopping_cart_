import sys
import os
import time
import json

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


typewrite("\n\n     👋   Üdvözöllek az alkalmazásban!\n")
typewrite("Az az alkalmazásban 4 féle művelet közül választhatsz, amik a kövezketőek:")
typewrite("--------------------------------------------")
typewrite(" ×    1. Elem hozzáadása a kosárhoz")
typewrite(" ×    2. Elem törlése a kosárból")
typewrite(" ×    3. Elem módosítása")
typewrite(" ×    4. Kosár tartalmának törlése")
typewrite(" ×    5. Kosár megtekintése")
typewrite(" ×    6. Kilépés az alkalmazásból")

def app():

    option = str(input("Kérlek válassz egy opciót! (1,2,3,4,5,6) "))

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
                typewrite(f"{torlendo_termek} sikeresen törölve lett a kosaradból.")
                mentes()
                app()
            else: 
                print("Nem létező termék!")
                app()
        else:
            print("Szerveroldali hiba történt")
            app()

        
    elif option == "3":
        app()
        pass
    elif option == "4":
        app()
        pass
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
        typewrite("\n\n👋 Viszontlátásra!\n")
        time.sleep(0.02)
        typewrite("🪢  Leállítás... \n\n")
        time.sleep(1)
        sys.exit()
    else:
        typewrite("Kérlek válassz egy valid opciót")
        app()
app()