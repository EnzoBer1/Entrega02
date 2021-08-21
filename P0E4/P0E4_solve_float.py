from time import perf_counter
from scipy.linalg import solve
from laplaciana import laplaciana
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

Ns = [2,10,100,200,500,1000,1500,2000,5000,10000] 
#Ns = [10,20,30,40,50,60,70,80,90,100] 

corridas = [1,2,3,4,5,6,7,8,9,10] 

lista_caso0_scipy = []
lista_caso1_scipy = [] #contendrá los valores de 10 corridas de cada N en ORDEN
lista_caso2_scipy = []
lista_caso3_scipy = []
lista_caso4_scipy = []
lista_caso5_scipy = []
lista_caso6_scipy = []

graf_caso0_scipy = [] #listas de promedios para los gráficos
graf_caso1_scipy = []
graf_caso2_scipy = []
graf_caso3_scipy = []
graf_caso4_scipy = []
graf_caso5_scipy = []
graf_caso6_scipy = []

############################################################################

txt0 = open("timing_solve_caso_1_float.txt","w")

for N in range(len(Ns)): #directamente invirtiendo
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        b = np.ones(Ns[N])
        t2 = perf_counter()
        A_inv = linalg.inv(A)
        x = A_inv*b #Solución del sistema Ax = b
        t3 = perf_counter()
        bytes_total = A.nbytes + b.nbytes + A_inv.nbytes + x.nbytes
        
        tiempo_solucion = t3-t2
        lista_caso0_scipy.append(tiempo_solucion)
        
        txt0.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print (corrida)
        print (Ns[N])
        print (tiempo_solucion)
        print (bytes_total)
        print ("--------------------------------")
    
txt0.close()
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_caso0_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_caso0_scipy.append(promedio)

#############################################################################

txt1 = open("timing_solve_caso_2_float.txt","w")

for N in range(len(Ns)): #parámetros por defecto
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        b = np.ones(Ns[N])
        t2 = perf_counter()
        x = solve(A,b) #Solución del sistema Ax = b
        t3 = perf_counter()
        bytes_total = A.nbytes + b.nbytes + x.nbytes
        
        tiempo_solucion = t3-t2
        lista_caso1_scipy.append(tiempo_solucion)
        
        txt1.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print (corrida)
        print (Ns[N])
        print (tiempo_solucion)
        print (bytes_total)
        print ("--------------------------------")
  
txt1.close()      
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_caso1_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_caso1_scipy.append(promedio)

##############################################################################    
    
txt2 = open("timing_solve_caso_3_float.txt","w")

for N in range(len(Ns)): #assume_a = pos
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        b = np.ones(Ns[N])
        t2 = perf_counter()
        x = solve(A,b, assume_a="pos") #Solución del sistema Ax = b
        t3 = perf_counter()
        bytes_total = A.nbytes + b.nbytes + x.nbytes
        
        tiempo_solucion = t3-t2
        lista_caso2_scipy.append(tiempo_solucion)
        
        txt2.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print (corrida)
        print (Ns[N])
        print (tiempo_solucion)
        print (bytes_total)
        print ("--------------------------------")
   
txt2.close()
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_caso2_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_caso2_scipy.append(promedio)
    
##########################################################################   
    
txt3 = open("timing_solve_caso_4_float.txt","w")

for N in range(len(Ns)): ##assume_a = sym
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        b = np.ones(Ns[N])
        t2 = perf_counter()
        x = solve(A,b, assume_a="sym") #Solución del sistema Ax = b
        t3 = perf_counter()
        bytes_total = A.nbytes + b.nbytes + x.nbytes
        
        tiempo_solucion = t3-t2
        lista_caso3_scipy.append(tiempo_solucion)
        
        txt3.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print (corrida)
        print (Ns[N])
        print (tiempo_solucion)
        print (bytes_total)
        print ("--------------------------------")
        
txt3.close()
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_caso3_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_caso3_scipy.append(promedio)
    
##########################################################################       
    
txt4 = open("timing_solve_caso_5_float.txt","w")

for N in range(len(Ns)): #overwrite_a = True
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        b = np.ones(Ns[N])
        t2 = perf_counter()
        x = solve(A,b, overwrite_a=True) #Solución del sistema Ax = b
        t3 = perf_counter()
        bytes_total = A.nbytes + b.nbytes + x.nbytes
        
        tiempo_solucion = t3-t2
        lista_caso4_scipy.append(tiempo_solucion)
        
        txt4.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print (corrida)
        print (Ns[N])
        print (tiempo_solucion)
        print (bytes_total)
        print ("--------------------------------")
   
txt4.close()
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_caso4_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_caso4_scipy.append(promedio)
    
##########################################################################   

txt5 = open("timing_solve_caso_6_float.txt","w")

for N in range(len(Ns)): #overwrite_b = True
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        b = np.ones(Ns[N])
        t2 = perf_counter()
        x = solve(A,b, overwrite_b=True) #Solución del sistema Ax = b
        t3 = perf_counter()
        bytes_total = A.nbytes+ b.nbytes + x.nbytes
        
        tiempo_solucion = t3-t2
        lista_caso5_scipy.append(tiempo_solucion)
        
        txt5.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print (corrida)
        print (Ns[N])
        print (tiempo_solucion)
        print (bytes_total)
        print ("--------------------------------")
        
txt5.close()
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_caso5_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_caso5_scipy.append(promedio)
    
##########################################################################   

txt6 = open("timing_solve_caso_7_float.txt","w")

for N in range(len(Ns)): #overwrite_a = True and overwrite_b = True
    for corrida in corridas:
        
        t1= perf_counter()
        A = laplaciana(Ns[N])
        b = np.ones(Ns[N])
        t2 = perf_counter()
        x = solve(A,b, overwrite_a=True, overwrite_b=True) #Solución del sistema Ax = b
        t3 = perf_counter()
        bytes_total = A.nbytes + b.nbytes + x.nbytes
        
        tiempo_solucion = t3-t2
        lista_caso6_scipy.append(tiempo_solucion)
        
        txt6.write(f"N = {Ns[N]}; Tiempo solución = {tiempo_solucion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print (corrida)
        print (Ns[N])
        print (tiempo_solucion)
        print (bytes_total)
        print ("--------------------------------")
        
txt6.close()
  
for i in range(len(corridas)):
    n = 10
    suma = 0
    lista_a_sumar = lista_caso6_scipy[i*10:i*10+10]
    
    for a in lista_a_sumar:
        suma += a
        
    promedio = float(suma/n)
    graf_caso6_scipy.append(promedio)
    
##########################################################################       
    
x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1 = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]

tiempo1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]
tamaño1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
 
plt.loglog(Ns,graf_caso0_scipy,"-o")  
plt.loglog(Ns,graf_caso1_scipy,"-o")
plt.loglog(Ns,graf_caso2_scipy,"-o")
plt.loglog(Ns,graf_caso3_scipy,"-o")
plt.loglog(Ns,graf_caso4_scipy,"-o")
plt.loglog(Ns,graf_caso5_scipy,"-o")
plt.loglog(Ns,graf_caso6_scipy,"-o")
plt.legend(["Invirtiendo","Por Defecto","assume_a = pos","assume_a = sym","overwrite_a = True","overwrite_b = True","overwrite_a,b = True"])
plt.xticks(tamaño1,x1,rotation=45)
plt.yticks(tiempo1,y1)
plt.xlim(right = 20000)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo solucion (s)")
plt.title("Rendimieto de Scipy.linalg.solve() para float")
plt.grid()

plt.show()                 

 


