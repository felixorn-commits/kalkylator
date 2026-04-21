# Funktion för addition
def addera(tal1, tal2):
    return tal1 + tal2


# Funktion för subtraktion
def subtrahera(tal1, tal2):
    return tal1 - tal2


# Funktion för multiplikation
def multiplicera(tal1, tal2):
    return tal1 * tal2


# Funktion för division
def dividera(tal1, tal2):
    if tal2 == 0:
        return "Fel: division med noll är inte tillåten."
    return tal1 / tal2


# Huvudloop som gör att programmet kan köras flera gånger
while True:
    print("\n--- KALKYLATOR ---")
    print("Välj ett räknesätt:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")

    val = input("Skriv ditt val (1/2/3/4): ")

    # Felhantering för inmatning av tal
    try:
        tal1 = float(input("Skriv in första talet: "))
        tal2 = float(input("Skriv in andra talet: "))
    except:
        print("Fel: du måste skriva in giltiga tal.")
        continue

    # Väljer rätt funktion beroende på användarens val
    if val == "1":
        resultat = addera(tal1, tal2)
        print("Resultat:", resultat)
    elif val == "2":
        resultat = subtrahera(tal1, tal2)
        print("Resultat:", resultat)
    elif val == "3":
        resultat = multiplicera(tal1, tal2)
        print("Resultat:", resultat)
    elif val == "4":
        resultat = dividera(tal1, tal2)
        print("Resultat:", resultat)
    else:
        print("Fel: ogiltigt val.")

    # Frågar om användaren vill köra igen
    igen = input("\nVill du räkna igen? (ja/nej): ").lower()
    if igen != "ja":
        print("Programmet avslutas.")
        break