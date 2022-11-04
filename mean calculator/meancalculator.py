import numpy

summary = open(r"C:\Users\marco\OneDrive\Documents\mean calculator\summary.txt", "r")
s = summary.readlines()

moyenne = []
for line in s:
    moyenne.append(line[8:-1])


for i in range(0, len(moyenne)):
    moyenne[i] = float(moyenne[i])

moyenneSansZeros = [i for i in moyenne if i > 50]

    
print ("moyenne 2010 : ", numpy.mean(moyenne))
print ("moyenne 2010 sans les notes en dessous de 50 : ", numpy.mean(moyenneSansZeros))