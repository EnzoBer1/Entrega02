from time import perf_counter
from numpy import zeros
from scipy import linalg
import matplotlib.pyplot as plt
from numpy import zeros, double
import numpy as np

Ns = [2,50,100,200,500,1000,1500,2000,5000,10000]
corridas = np.arange(len(Ns))

def laplaciana(N):
    A = zeros((N,N), dtype = double)
    
    for i in range(N):
        for j in range(i+1):
            
            if i == j:
                A[i,i] = 2
                
            elif abs(i-j) == 1:
                A[i,j] = -1
                A[j,i] = -1
    
    return A

dts_solucion = [] #guardo los tiempos en que se soluciona A*x = b por corrida
dts_ensamblaje = [] #guardo los tiempos en que se ensambla el sistema por corrida

txt = open("timing_SOLVE_Matriz_Llena_double.txt","w")

for corrida in corridas:
    for N in Ns:
        
        t1= perf_counter()
        
        A = laplaciana(N)
        b = np.ones(N)
        
        t2 = perf_counter()
        
        x = linalg.solve(A,b) #Soluciono el sistema A*x = b
        
        t3 = perf_counter()
        
        dt_ensamblaje = t2 - t1
        dt_solucion = t3 - t2 

        dts_ensamblaje.append(dt_ensamblaje)
        dts_solucion.append(dt_solucion)
        
        txt.write(f"N = {N}; Tiempo solución = {dt_solucion} seg.; Tiempo ensamblaje = {dt_ensamblaje} seg.\n" )
        
        print ("Corrida =", corrida+1)
        print ("N =", N)
        print (f"Tiempo ensamblaje: {dt_ensamblaje} seg.")
        print (f"Tiempo solución: {dt_solucion} seg.")
        print ("----------------------------------------------------")
     
txt.close()


x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1 = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
sin = ["","","","","","","","","","",""]

tiempo1 = [0.001,1/1000,10/1000,0.1,1,10,60,60*10]
tamaño1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]


solucion_max = max(dts_solucion)
ensamblaje_max = max(dts_ensamblaje)
N_max = max(dts_solucion)

constante0 = [max(dts_solucion),max(dts_solucion),max(dts_solucion),max(dts_solucion),max(dts_solucion),max(dts_solucion),max(dts_solucion),max(dts_solucion),max(dts_solucion),max(dts_solucion)]
constante1 = [max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje),max(dts_ensamblaje)]



for i in range(len(corridas)):
    
    plt.subplot(2,1,1)
    
    plt.loglog(Ns,constante0,"--",color="blue")
    plt.loglog([3,max(Ns)],[dts_solucion[0],max(dts_solucion)],"--",color="orange")
    plt.loglog([10,max(Ns)],[0.00000001,max(dts_solucion)],"--",color="green")
    plt.loglog([100,max(Ns)],[0.00000001,max(dts_solucion)],"--",color="red")
    plt.loglog([400,max(Ns)],[0.00000001,max(dts_solucion)],"--",color="purple")
    
    plt.loglog(Ns,dts_solucion[i*10:i*10+10],"-o",color="black",alpha=0.2)
    
    plt.xticks(tamaño1,sin)
    plt.yticks(tiempo1,y1)
    plt.xlim(right=20000)
    plt.ylim([0.000001,600])
    plt.grid()
    plt.ylabel("Tiempo de solución")
    plt.title("Desempeño SOLVE para Matrices Llenas")
    
    ####################################
    
    plt.subplot(2,1,2)
    
    plt.loglog(Ns,constante1,"--",color="blue")
    plt.loglog([3,max(Ns)],[dts_ensamblaje[0],max(dts_ensamblaje)],"--",color = "orange")
    plt.loglog([10,max(Ns)],[0.00000001,max(dts_ensamblaje)],"--",color="green")
    plt.loglog([100,max(Ns)],[0.00000001,max(dts_ensamblaje)],"--",color="red")
    plt.loglog([400,max(Ns)],[0.00000001,max(dts_ensamblaje)],"--",color="purple")
    
    plt.loglog(Ns,dts_ensamblaje[i*10:i*10+10],"-o",color="black",alpha=0.2)
    
    plt.legend(["Constante","O(N)","O(N**2)","O(N**3)","O(N**4)"])
    
    plt.xticks(tamaño1,x1,rotation=45)
    plt.yticks(tiempo1,y1)
    plt.xlim(right=20000)
    plt.ylim([0.000001,600])
    plt.grid()
    plt.ylabel("Tiempo de ensamblado")
                             
plt.show()          
               