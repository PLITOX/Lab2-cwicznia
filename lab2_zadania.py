#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:26:06 2021

@author: caelinux
"""
import numpy as np
print("4.1.4")
A = np.array([[1, 2, 3, 4, 5, 10], [5, 4, 3, 2, 1, 10], [0, 0, 2, 2, 2, 10,], [0, 0, 2, 2, 2, 10], [0, 0, -90, -80, -70, 10]])
print(A)
#utowrzenie tablicy i przypisanie jej do zmiennej A //nie udało sie wygenerować 

#4. dodanie do siebie dwoch wierszy i przypisanie ich do B
print("Po dodaniu")
B = A[1,] + A[3,]
print(B)
#5. Do zmiennej C max wartości z kolumn 
print("Przypisanie max war z kolumn")

C = [0,0,0,0,0,0]
C[0] = np.max(A[:,0])
C[1] = np.max(A[:,1])
C[2] = np.max(A[:,2])
C[3] = np.max(A[:,3])
C[4] = np.max(A[:,4])
C[5] = np.max(A[:,5])
print("Max wartosci")
print('C = ',C)


#6. Modyfikacja B i do D
print("Usuwanie")
D = np.delete(B, 0, 0)
D = np.delete(B, 5, 0)
print(D)

#7. Usuniecie 4 z tab D
print("Wartosci 4")
D = np.delete(B, [1,3], None)
print(D)

#8. 
MAX1 = np.max(C)
MIN1 = np.min(C)
for i in range(6):          #6kolumn
    if C[i] == MAX1: 
        E=np.delete(C,i)
        break
for i in range(5):  
    if E[i] == MIN1:
        E=np.delete(E,i)
        break
print(E)


#9. Wypisz z tablicy A te wiersze, w których znajduje się maksymalny i minimalny element (wykorzystaj funkcje min, max).
print('Zadanie 9')
MAX2 = np.max(A)
MIN2 = np.min(A)    
for i in range(5):
    for j in range(6):
        if A[i,j] == MAX2:
            print('MAX ',MAX2) 
            print('Wiersz max:',A[i,:])            
        elif A[i,j] == MIN2:
            print('MIN ',MIN2)
            print('Wiersz min:',A[i,:])   #ostatnie wiersze to max i min i leci od gory

#10. Mnozenie wektorowe i macierzowe
print('zadanie 10')   
T=D*E   #Tablicowe
W=D@E   #wektorowe
print('Tablicowo:',T)
print('Wektorowo:',W)



#11. 


#12.


#13.


#14.


#15.


#16.


#17.


#18.


#19.





