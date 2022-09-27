alder = input("Hvor gammel er du? ")
while not alder.isnumeric():
    print("Error. Oppgi et positivt heltall")
    alder = input("Hvor gammel er du? ")
alder = int(alder)

kort_type = input("Ønsker du dagskort eller kveldskort? ")
while kort_type != "dagskort" and kort_type != "kveldskort":
    print("Error. Vennligst skriv dagskort eller kveldskort")
    kort_type = input("Ønsker du dagskort eller kveldskort? ")

if alder > 18 and kort_type == "dagskort":
    pris = 380
elif alder > 18 and kort_type == "kveldskort":
    pris = 275
elif alder <= 18 and kort_type == "dagskort":
    pris = 240
elif alder <= 18 and kort_type == "kveldskort":
    pris = 165

alder_tekst = "Voksen" if alder > 18 else "Barn"
print(f"{kort_type.capitalize()}, {alder_tekst}: {pris} kr")
