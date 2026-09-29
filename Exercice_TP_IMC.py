def indice_de_masse_corporelle(weight, height): # creation de la focntion pour calculer l'IMC
    imc = weight / (height ** 2)  # Indiquer la formule pour calculer l'IMC.
    print("IMC = {:0.1f}".format(imc))
    if imc <= 18.5:
        print("Valeur d'IMC indiquant une maigreur")
    elif imc <= 24.9:
        print("Valeur d'IMC normal")
    elif imc <= 29.9:
        print("Valeur d'IMC indiquant un surpoids")
    elif imc <= 39.9:
        print("Valeur d'IMC indiquant un obésité")
    else :
        print("Valeur d'IMC indiquant une obésité massive")
    return imc

# je calcule mon IMC avec mon poids et ma taille SAMY K
weight = 100  # poids en kg
height = 1.80  # taille en m
indice_de_masse_corporelle(weight, height)  # appel de la fonction 


# Je calcule un IMC GauthierBourdon
poids = 1000  # poids en kg
taille = 1.2  # taille en m
indice_de_masse_corporelle(poids, taille) 

# Idem : Zoe Favier
w = 45
h = 1.50
indice_de_masse_corporelle(w, h) 

# Je viens de remarquer au j'avais oublier de faire un commit aussi du coup j'ajoute un petit exercice en plus 
import sys
import timeit

import numpy as np
c = np.arange(1000000)
copy_number = 100
view_number = 100_000


copie_time = timeit.timeit('c.copy()', globals=globals(), number=copy_number)
view_time = timeit.timeit('c.view()', globals=globals(), number=view_number)
print(f"Time taken to copy the array {copy_number} times: {copie_time:.6f} seconds")
print(f"Time taken to create a view of the array {view_number} times: {view_time:.6f} seconds")

# cost in memory
import sys
c_copy = c.copy()
c_view = c.view()
print("logical size of c:", c.nbytes, "bytes")
print(" logical size of c_copy:", c_copy.nbytes, "bytes")
print(" logical size of c_view:", c_view.nbytes, "bytes")

print("Size of c_copy:", sys.getsizeof(c_copy), "bytes")
print("Size of c_view:", sys.getsizeof(c_view), "bytes")

print("shared memory of c_copy:", np.shares_memory(c, c_copy))
print("shared memory of c_view:", np.shares_memory(c, c_view))




EX 8 : 

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


t1 = [0, 1.73, 2.8, 5.5, 18, 22]
c1 = [c10, 3, 2.5, 1.6, 0.2, 0.1]

plt.figure()
plt.plot(t1,np.log(c1),'ob')
plt.xlabel('time (min)')
plt.ylabel('concentration c1 (mol/L)')
plt.grid()

lr = scipy.stats.linregress(t1,np.log(c1))
print(lr)
k1 = -lr[0]
corr = lr[2]
print("Le coefficient de corrélation vaut {:0.6f}".format(abs(corr)))
print("La constante de vitesse de la réaction d'absorption vaut k1 = {:0.4f} min-1".format(k1))



# super bravo à tous
