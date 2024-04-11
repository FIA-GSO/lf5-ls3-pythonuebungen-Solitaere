mengeStreichholz: int  = 29;
print("Der Computer nimmt 2 Streichhölzer. Es sind noch",mengeStreichholz,"übrig")
while True:
    
    spielerStreichholz = int(input("Wie viele Streichhölzer möchtest du nehmen?"))
    if spielerStreichholz > 6 or spielerStreichholz > mengeStreichholz:
        print("Gib eine kleinere Zahl an (1-6)")
        continue
    mengeStreichholz = mengeStreichholz - spielerStreichholz

    if mengeStreichholz <= 1:
        print("Du hast verloren.")
        break
    compStreichholz = 7 
    compStreichholz =- spielerStreichholz
    mengeStreichholz =- compStreichholz
    print("Der Computer nimmt",compStreichholz,"noch",mengeStreichholz,"Streichhölzer sind vorhanden.")


