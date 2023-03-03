import random as r

from blocks import *

def making_dna_list():
    
    print("How much you wanna use?\nType a number or random")
    
    adenin_in = input("Adenin->")
    if adenin_in == "random":
        adenin_in = r.choice(choice)
    emp.append(int(adenin_in))
    for x in range(int(adenin_in)):
        dna.append(adenin)

    guanin_in = input("Guanin->")
    if guanin_in == "random" :
        guanin_in = r.choice(choice)
    emp.append(int(guanin_in))
    for x in range(int(guanin_in)):
        dna.append(guanin)

    thymin_in = input("Thymin->")
    if thymin_in == "random":
        thymin_in = r.choice(choice)
    emp.append(int(thymin_in))
    for x in range(int(thymin_in)):
        dna.append(thymin)

    cytosin_in = input("Cytosin->")
    if cytosin_in == "random":
        cytosin_in = r.choice(choice)
    emp.append(int(cytosin_in))
    for x in range(int(cytosin_in)):
        dna.append(cytosin)

def sorting_dna():

    print("Sorting DNA...")
    sorted_dna = {}
    for idx, b in enumerate(dna):
        if b == "A":
            b2 = "T"
        elif b == "T":
            b2 = "A"
        elif b == "C":
            b2 = "G"
        elif b == "G":
            b2 = "C"
        sorted_dna[idx] = [b, b2]

    print(sorted_dna)

if __name__ == "__main__":
    
    making_dna_list()
    sorting_dna()
