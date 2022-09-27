pris = int(input("Oppgi vanlig pris : "))
prosent = int(input("Oppgi prosent i rabatt : "))
rabatt = pris*prosent/100
nypris = pris - rabatt

print(f"Rabatten er {rabatt} kr")
print(f"Den nye prisen er {nypris:.2f} kr.")

