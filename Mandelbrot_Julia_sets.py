# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 10:53:16 2025

@author: helen
"""

import numpy as np
import matplotlib.pyplot as plt

#Mandelbrot

x=np.linspace(-2,1,1000)
y=np.linspace(-1.5,1.5,1000)

X, Y = np.meshgrid(x, y)
c=X+1j*Y
z=np.zeros((1000,1000), dtype=complex)
VC=np.zeros((1000,1000), dtype=int) 
m = np.ones((1000,1000), dtype=bool) # True = encara cal divergir


for n in range (1,101,1):
    z [m]=z[m]**2+c[m] # només agafo punts que no han divergit encara (m=true)
    #z[np.abs(z) > 2] = 2
    diverge = (np.abs(z) > 2) & (VC == 0)  # divergeix & és un 0 (primera iteració)
    VC[diverge] = n                        # diverge => true/false
    m[diverge] = False #punt ja ha divergit, "l'elimino".
    # posem matriu de trues/falses
    
    # exemple:
        #VC = np.array([0, 0, 0, 0, 0])
        #diverge = np.array([False, True, False, True, False])
        #n = 5
        #VC[diverge] = n
        # print => [0 5 0 5 0]
    
    
print(z)

CM=np.zeros((1000,1000))
CM=np.abs(z) < 2

#figura 1
plt.figure()
plt.imshow(CM, cmap='gray')
plt.show()



VC_plot = VC.copy()
VC_plot[VC_plot == 0] = 100 #max d'iteracions (no divergeix)

#figura 2
plt.figure()
plt.imshow(VC_plot, cmap='jet', extent=[-2, 1, -1.5, 1.5])
plt.colorbar(label='Iteracions fins divergència')
plt.title('Velocitat de convergència')
plt.axis('off')
plt.show()





# Julia

x = np.linspace(-1.5, 1.5, 1000)
y = np.linspace(-1.5, 1.5, 1000)
X, Y = np.meshgrid(x, y)
z = X + 1j * Y  
c = 0.7269 - 0.1889j


fig, (ax1,ax2,ax3)=plt.subplots(1,3)

#bucles per graficar tres iteracions, però la manera és la mateixa que abans
#la "comanda principal" és basicament com abans: m_2 = np.abs(z_2) < 2 
for t in [100, 250, 500]:
    z_2 = z.copy()  #copia per no editar la z en si
    m_2 = np.ones((1000,1000), dtype=bool)
    for n in range(t):
        z_2[m_2] = z_2[m_2]**2 - c
        m_2 = np.abs(z_2) < 2  
       
        
#figura 3        
    if t==100:
        ax1.imshow(m_2, cmap='gray', extent=[-2,2,-2,2])  
        ax1.set_title(f'Conjunt de Julia – {t} iteracions')      
    if t==250:
        ax2.imshow(m_2, cmap='gray', extent=[-2,2,-2,2])  
        ax2.set_title(f'Conjunt de Julia – {t} iteracions')         
    if t==500:
        ax3.imshow(m_2, cmap='gray', extent=[-2,2,-2,2])  
        ax3.set_title(f'Conjunt de Julia – {t} iteracions')

        
plt.tight_layout()
plt.show()        


#mateix procés que abans per el gràfic de VC
z_julia = z.copy()
m = np.ones((1000,1000), dtype=bool)
VC = np.zeros((1000,1000), dtype=int) 

for n in range(1, 500 + 1):  #com més iteracions més definida les espirals
    z_julia[m] = z_julia[m]**2 - c    
    diverge = (np.abs(z_julia) > 2) & m
    VC[diverge] = n
    m[diverge] = False


VC_plot = VC.copy()
VC_plot[VC_plot == 0] = 500

plt.figure()
plt.imshow(VC_plot, cmap='turbo', extent=[-2,2,-2,2], vmin=1, vmax=500)
plt.colorbar(label='Iteracions fins divergència')
plt.title('Velocitat de divergència – Conjunt de Julia')
plt.axis('off')
plt.show()

