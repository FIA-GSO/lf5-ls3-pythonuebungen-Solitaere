# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int,int,int]:
    """
        Computes the r2d2 population for the given step amount
    :param steps: amount of steps to compute the population (e.g.: 5)
    :return: tuple of childs adults and old r2d2
    """
    return (0,0,0)

#---------------------Aufgabe 2 Streichholz------------------------------
def streichholz():
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
        compStreichholz = compStreichholz - spielerStreichholz
        mengeStreichholz = mengeStreichholz - compStreichholz
        print("Der Computer nimmt",compStreichholz,"noch",mengeStreichholz,"Streichhölzer sind vorhanden.")

#---------------------Aufgabe 3 Heron ------------------------------------
def heron_verfahren(area : float, threshold:float) -> float:
    area = 25;
    barea = 1;
    average = 0;
    difference = 1;
    threshold = 0.01;
    loopyLoop = True
    while(loopyLoop):
        average = (area + barea) / 2
        difference = area - barea
        area = average
        difference = area - barea
        if(average - barea < threshold):    
            print("",area," ",barea," ",average, " " , difference)
            loopyLoop = False
        else:
            print("",area," ",barea," ",average, " " , difference)
#---------------------Aufgabe 4 Quersumme------------------------------
#IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!


#---------------MANAGEMENT----------------------
#-------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    #print(f"""
        # R2D2 Population after 5 steps is: 
        # Young: {compute_r2d2_population(5)[0]}
        # Adults: {compute_r2d2_population(5)[1]}
        # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    # TO BE IMPLEMENTED

    # Aufgabe 3
    print (f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
