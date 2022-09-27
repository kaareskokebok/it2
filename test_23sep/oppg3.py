# Løsning av Sebastian Schumann
tall = 3
summ = tall
while tall < 200:
    print(tall, end=" + ")
    tall = tall + 4
    summ += tall
    
print(tall, end=" = ")
print(summ)
