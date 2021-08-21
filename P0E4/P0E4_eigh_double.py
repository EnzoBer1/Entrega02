from time import perf_counter
from scipy.linalg import eigh
from laplaciana import laplaciana
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

Ns = [2,10,50,100,200,500,1000,1500,2000,5000] 
#Ns = [10,20,30,40,50,60,70,80,90,100] 

corridas = [1,2,3,4,5,6,7,8,9,10] 

####################

lista_defecto_scipy = []

lista_ev1_scipy = [] #contendrá los valores de 10 corridas de cada N en ORDEN
lista_ev2_scipy = []

lista_evd1_scipy = []
lista_evd2_scipy = []

lista_evr1_scipy = []
lista_evr2_scipy = []

lista_evx1_scipy = []
lista_evx2_scipy = []

#####################

graf_defecto_scipy = [] #listas de promedios para los gráficos

graf_ev1_scipy = []
graf_ev2_scipy = []

graf_evd1_scipy = []
graf_evd2_scipy = []

graf_evr1_scipy = []
graf_evr2_scipy = []

graf_caso4_scipy = []
graf_caso4_scipy = []

graf_evx1_scipy = []
graf_evx2_scipy = []

#####################

txt0 = open("timing_eigh_caso_0_double.txt","w")
txt1 = open("timing_eigh_caso_1_double.txt","w")
txt2 = open("timing_eigh_caso_2_double.txt","w")
txt3 = open("timing_eigh_caso_3_double.txt","w")
txt4 = open("timing_eigh_caso_4_double.txt","w")
txt5 = open("timing_eigh_caso_5_double.txt","w")
txt6 = open("timing_eigh_caso_6_double.txt","w")
txt7 = open("timing_eigh_caso_7_double.txt","w")
txt8 = open("timing_eigh_caso_8_double.txt","w")

############################################################################
############################################################################

for N in range(len(Ns)): #parámetros por defecto
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_defecto_scipy.append(tiempo_solucion)
        
        txt0.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
      
txt0.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_defecto_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_defecto_scipy.append(promedio)

#############################################################################
#############################################################################

for N in range(len(Ns)): #driver = "ev" y overwrite_a = False
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("ev"), overwrite_a = False) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_ev1_scipy.append(tiempo_solucion)
        
        txt1.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
      
txt1.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_ev1_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_ev1_scipy.append(promedio)

##############################################################################    
    
for N in range(len(Ns)): #driver = "ev" y overwrite_a = True
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("ev"), overwrite_a = True) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_ev2_scipy.append(tiempo_solucion)
        
        txt2.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
      
txt2.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_ev2_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_ev2_scipy.append(promedio)

#############################################################################
#############################################################################

for N in range(len(Ns)): #driver = "evd" y overwrite_a = False
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("evd"), overwrite_a = False) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_evd1_scipy.append(tiempo_solucion)
        
        txt3.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
      
txt3.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_evd1_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_evd1_scipy.append(promedio)

##############################################################################    
    
for N in range(len(Ns)): #driver = "evd" y overwrite_a = True
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("evd"), overwrite_a = True) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_evd2_scipy.append(tiempo_solucion)
        
        txt4.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
        
txt4.close()
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_evd2_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_evd2_scipy.append(promedio)

#############################################################################
#############################################################################

for N in range(len(Ns)): #driver = "evr" y overwrite_a = False
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("evr"), overwrite_a = False) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_evr1_scipy.append(tiempo_solucion)
        
        txt5.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")

txt5.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_evr1_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_evr1_scipy.append(promedio)

##############################################################################    
    
for N in range(len(Ns)): #driver = "evr" y overwrite_a = True
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("evr"), overwrite_a = True) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_evr2_scipy.append(tiempo_solucion)
        
        txt6.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
      
txt6.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_evr2_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_evr2_scipy.append(promedio)

#############################################################################
#############################################################################   

for N in range(len(Ns)): #driver = "evx" y overwrite_a = False
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("evx"), overwrite_a = False) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_evx1_scipy.append(tiempo_solucion)
        
        txt7.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
      
txt7.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_evx1_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_evx1_scipy.append(promedio)

##############################################################################    
    
for N in range(len(Ns)): #driver = "evx" y overwrite_a = True
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        t2 = perf_counter()
        A_valvec = linalg.eigh(A, driver = ("evx"), overwrite_a = True) 
        #saca los valores y vectores propios
        t3 = perf_counter()
        bytes_total = A.nbytes + A_valvec[0].nbytes + A_valvec[1].nbytes
        
        tiempo_solucion = t3-t2
        lista_evx2_scipy.append(tiempo_solucion)
        
        txt8.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        #print (Ns[N])
        #print (tiempo_solucion)
       # print (corrida)
      #  print ("--------------------------------")
      
txt8.close()
        
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_evx2_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_evx2_scipy.append(promedio)

#############################################################################
############################################################################# 


x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1 = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]

tiempo1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]
tamaño1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
 

plt.loglog(Ns,graf_defecto_scipy,"-o")  
plt.loglog(Ns,graf_ev1_scipy,"-o") 
plt.loglog(Ns,graf_ev2_scipy,"-o") 
plt.legend(["Por Defecto","Driver = ev & overwrite_a = False","Driver = ev & overwrite_a = True"])
plt.xticks(tamaño1,x1,rotation=45)
plt.yticks(tiempo1,y1)
plt.xlim(right = 20000)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo solucion (s)")
plt.title("Rendimiento de Scipy.linalg.eigh() para double")
plt.grid()
plt.show()

plt.loglog(Ns,graf_defecto_scipy,"-o")  
plt.loglog(Ns,graf_evd1_scipy,"-o") 
plt.loglog(Ns,graf_evd2_scipy,"-o") 
plt.legend(["Por Defecto","Driver = evd & overwrite_a = False","Driver = evd & overwrite_a = True"])
plt.xticks(tamaño1,x1,rotation=45)
plt.yticks(tiempo1,y1)
plt.xlim(right = 20000)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo solucion (s)")
plt.title("Rendimiento de Scipy.linalg.eigh() para double")
plt.grid()
plt.show()

plt.loglog(Ns,graf_defecto_scipy,"-o")  
plt.loglog(Ns,graf_evr1_scipy,"-o") 
plt.loglog(Ns,graf_evr2_scipy,"-o") 
plt.legend(["Por Defecto","Driver = evr & overwrite_a = False","Driver = evr & overwrite_a = True"])
plt.xticks(tamaño1,x1,rotation=45)
plt.yticks(tiempo1,y1)
plt.xlim(right = 20000)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo solucion (s)")
plt.title("Rendimiento de Scipy.linalg.eigh() para double")
plt.grid()
plt.show()      

plt.loglog(Ns,graf_defecto_scipy,"-o")  
plt.loglog(Ns,graf_evx1_scipy,"-o") 
plt.loglog(Ns,graf_evx2_scipy,"-o") 
plt.legend(["Por Defecto","Driver = evx & overwrite_a = False","Driver = evr & overwrite_a = True"])
plt.xticks(tamaño1,x1,rotation=45)
plt.yticks(tiempo1,y1)
plt.xlim(right = 20000)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo solucion (s)")
plt.title("Rendimiento de Scipy.linalg.eigh() para double")
plt.grid()
plt.show()                