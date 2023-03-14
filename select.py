from pojisteny import Pojisteny
from evidence import EvidencePojisteny

if __name__ == '__main__':
    evidence = EvidencePojisteny()

    while True:
        print("Evidence pojištěných")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        volba = input("Vyberte volbu: ")

        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = input("Zadejte věk: ")
            telefon = input("Zadejte telefonní číslo: ")
            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            evidence.pridej_pojisteneho(pojisteny)
            print("Pojištěný byl úspěšně přidán do seznamu.")
            print("Pokračujte libovolnou klávesou")
            input()

        elif volba == "2":
            print("Seznam pojištěných:")
            evidence.vypis_pojistene()
            print("Pokračujte libovolnou klávesou")
            input()

        elif volba == "3":
            jmeno = input("Zadejte jméno pojištěného: ")
            prijmeni = input("Zadejte příjmení pojištěného: ")
            pojisteny = evidence.najdi_pojisteneho(jmeno, prijmeni)
            if pojisteny:
                print(f"Vyhledán pojištěný: {pojisteny}")
            else:
                print("Pojištěný nebyl nalezen")
            print("Pokračujte libovolnou klávesou")
            input()
            
        elif volba == "4":
            break

        else:
            print("Neplatná volba")
