alder = int(input("Hvor gammel er du? "))

if alder <= 18:
    typekort = input("kjører du på dagen eller kvelden (skriv dag eller kveld)")
    if typekort == "dag":
        print("Dagskort, barn: 240kr")
    if typekort == "kveld":
        print("Kveldskort, barn: 165kr")
        
if alder > 18:
    typekort = input("kjører du på dagen eller kvelden (skriv dag eller kveld)")
    if typekort == "dag":
        print("Dagskort, voksen: 380kr")
    if typekort == "kveld":
        print("Kveldskort, voksen: 275kr")