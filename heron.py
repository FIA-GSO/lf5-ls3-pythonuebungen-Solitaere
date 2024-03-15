laengeA = 25;
laengeB = 1; 
mittelwert = 0;
threshold =0.01;
while True:

    mittelwert = laengeA + laengeB /2
    laengeA -= mittelwert
    if laengeA - laengeB < threshold:
        print("sugma")