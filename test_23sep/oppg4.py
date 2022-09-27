import time

tid = int(input("Oppgi et tall som må være minst 3 og samtidig mer enn 10 "))

if tid < 3 or tid > 10:
    print("Er du en idiot? les teksten på nytt")
    exit()


if tid > 3 or tid < 10:
    while tid > 0:
        print(f"{tid:.1f}")
        tid = tid - 0.1
        time.sleep(0.1)


