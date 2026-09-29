def indice_de_masse_corporelle(weight, height): # creation de la focntion pour calculer l'IMC
    imc = weight / (height ** 2)  # Indiquer la formule pour calculer l'IMC.
    print("IMC = {:0.1f}".format(imc))
    if imc <= 18.5:
        print("Valeur d'IMC indiquant une maigreur")
    elif 18.5 < imc <= 24.9:
        print("Valeur d'IMC normal")
    elif 24.9 < imc <= 29.9:
        print("Valeur d'IMC indiquant un surpoids")
    elif 29.9 < imc <= 39.9:
        print("Valeur d'IMC indiquant un obésité")
    else :
        print("Valeur d'IMC indiquant une obésité massive")
    return imc

# je calcule mon IMC avec mon poids et ma taille SAMY K
weight = 100  # poids en kg
height = 1.80  # taille en m
indice_de_masse_corporelle(weight, height)  # appel de la fonction pour

