# P0

ENTREGAS EN ESTE README HASTA EL MOMENTO: P0E3 , P0E4 , P0E5, P0E6.

Link Repositorio: https://github.com/EnzoBer1/P0

###################################################################################################################################################################################

ENTREGA P0E3

En esta entrega se comparará el tiempo que tarda la librería numpy y scipy en invertir una matriz cuadrada de gran tamaño una cierta cantidad de veces. Para ambos casos se susaran datos tipo half, single, double y longdouble (siempre que el computador lo permita). Ahora bien, para scipy, como se puede elegir si usar o no la función overwrite_a, la cual reescribe los datos, se comparará el rendimiento para ver efectivamente cual optimiza el proceso. 

Incoveniente 1: Para el Caso 1 (Numpy.inv) utilizando un np.half no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 16.

![image](https://user-images.githubusercontent.com/89056734/129997478-b018b813-8ae8-4775-9959-3cc862d650c2.png)

Incoveniente 2: Para el Caso 1 (Numpy.inv) utilizando un np.longdouble no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 64.

![image](https://user-images.githubusercontent.com/89056734/129997533-6bd8445f-9128-4f11-a791-f58a07604baf.png)

Inconveniente 3: El computador no fue capaz de hacer 10 corridas para un valor de N mayor a 8000, posiblemente se iba a demorar demasiado tiempo, incluso en ocasiones que se intentó, spyder no respondía y debía cerrarlo.

Análisis del uso de memoria: Como puede apreciarse en los gráficos y archivos txt; para cada caso (y cada corrida) el uso de memoria permanece constante, esto es debido a que la cantidad de bytes para un cierto N en cada caso no cambia, es decir, la memoria utilizada para almacenar las matrices no depende del tipo de dato, ni de la librería, ya que son simplemente una cantidad específica de números.

Análsis del tiempo de inversión: Se ve claramente en los gráficos y en los txt como el tiempo de inversión del caso 2 y 3, para N = 5000, son considerablemente menores al del caso 1. Se puede afirmar que scipy es más rápido al momento de invertir matries que numpy.

Uso de overwrite_a: Puede apreciarse claramente en los txt como, para la última corrida del código en el caso de N = 5000, al usar overwrite_a = False (caso 2), se alenta el proceso, por otro lado, se ve una significativa ganancia en cada tipo de dato (half, single, double y longdouble) en comparación con el caso 2 al usar overwrite_a = True (caso 3). Resumiendo, usando overwrite_a = True, se obtiene una ganancia de desempeño. Esto se debe a que el programa reescribe o re utiliza la memoria anterior para escribir la nueva, lo que se traduce en un modo de optimizar espacio. Tal vez no es "mucho" tiempo más, pero si consideramos procesos iteraivos muy repetidos, uno podría ahorrarse minutos y hasta horas de trabajo y esferzo de la CPU.

Caso 3; Longdouble, corrida 10 y N = 5000, overwrite_a = True
![image](https://user-images.githubusercontent.com/89056734/129997659-7e669850-1165-423a-83b4-b83c30988c32.png)

Caso 2; Longdouble, corrida 10 y N = 5000, overwrite_a = False
![image](https://user-images.githubusercontent.com/89056734/129997716-4ac6449e-28aa-4257-b1b2-44efd117d401.png)

==> ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 

Respuesta: Numpy usa una factorización LU para encontrar la solución de Ax = b, es decir, usa algebra matricial para encontrar la inversa de A. Por otro lado, scipy usa la función inv, pero al ocupar la función overwrite, reescribe la matriz aprovechando de mejor manera la RAM del computador y agilizando el proceso.

==> ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 

Respuesta: El objetivo principal de la caché es aumentar el rendimiento de recuperación de datos para evitar tener que acceder a la capa subyacente de almacenamiento, que es más lenta. El paralelismo es la capacidad del programa de hacer cosas en simultáneo en vez de seguir un hilo de procesos. Python lamentablemente no permite usar paralelismo, lo que fuerza al computador a seguir el hilo programado, ahora bien, usando la funnción overwrite, se recuperan los datos con mayor rapidez para así aumentar el rendimiento del procesador, almacenando datos de manera transitoria e iterativa, tal como se observó al comparar los tiempos de inversión para un N alto, para los casos 2 y 3.

###################################################################################################################################################################################

ENTREGA P0E4

Esta entrega constará de analizar el desempeño de la función scipy.linalg.solve para encontrar el vector x solución del sistema Ax = b, siendo b un vector de unos, y A la mariz laplaciana de la entrega P0E3. Se analizará el desempeño para distintos tipos de datos (float y double); para distintas configuraciones de la función solve (6 casos en total)
Luego, se graficarán los resultados en una misma figura con el fin de comparar los tiempos en que se ejecuta la ecuación matricial. 
Con el mismo procedimiento, se analizará la función scipy.linalg.eigh (la cual entrega los valores y vectores propios de una matriz), para los mismos tipos de datos y 5 distintas configuraciones. La idea es poder comparar directamente en un mismo gráfico y ver rápidamente cual configuración optimiza cada proceso.

Para comparar rendimientos para cada tipo de dato, se harán distintos gráficos, comparando el rendimiento de cada función (solve y eigh) con sus configuraciones o parámetros por defecto, contra el rendimiento de cada caso de driver con overwrite_a = True y overwrite_a = False. Los resultados se presentan a continuación.

==> Rendimiento de la función Scipy.linalg.solve() para tipo de dato "float" (sinlge) para N del 2 al 10.000:

![image](https://user-images.githubusercontent.com/89056734/130293954-0d1da7de-8faa-4e09-893d-a8db26fed279.png)


Aquí se ve como x = solve(A,b, assume_a="pos") da el tiempo de ejecución más bajo, es decir, es la configuración más rápida para resolver el sistema. Por otro lado, se ve como usando el método de invertir A y luego multiplicarla por b da los tiempos más bajos para matrices pequeñas, pero una vez que aumenta el tamaño de dichas matrices, se convierte en el proceso más lento. También, se nota como los parámetros por defecto de la función dan los tiempos más lentos para matrices pequeñas y unos no tan buenos para las grandes, lo que indica que casi por "obligación" se deben de modificar los parámetros para obtener tiempos de ejecución bajos.

==> Rendimiento de la función Scipy.linalg.solve() para tipo de dato "double" para N del 2 al 10.000:

![image](https://user-images.githubusercontent.com/89056734/130304330-aff3cf96-7b4a-435d-ab9a-c2686b25ffc8.png)

En este caso, cuando se usa una matriz definida positiva (assume_a = pos), se obtiene el mejor desempeño. Por otro lado, al usar el proceso de invertir la matriz y luego multilicarla por b, se obtiene el peor rendimiento.


==> Rendimiento de la función Scipy.linalg.eigh() para tipo de dato "float" (sinlge) para N del 2 al 10.000:


![image](https://user-images.githubusercontent.com/89056734/130304350-98f58515-154e-4612-be88-56d21ffd4e60.png)
![image](https://user-images.githubusercontent.com/89056734/130304354-866ef826-7dfc-41aa-9908-ad1d64ee7544.png)
![image](https://user-images.githubusercontent.com/89056734/130304363-42192c0b-f656-460c-9687-eb58fe0ac86c.png)
![image](https://user-images.githubusercontent.com/89056734/130304367-767fe28a-f580-44e2-84d1-0a237f5ab297.png)


Por temas de simplicidad se usa N hasta 5000, ya que el tiempo de ejecución al usar N = 10.000 pasa los 2 minutos; se muestran 4 gráficos en donde se comparan cada uno de 4 casos v/s el rendimiento con parámetros por defecto.
Puede verse como el caso de scipy.linalg.eigh() con driver = "ev" y overwrite_a = True es el MENOS eficiente al momento de encontrar los valores y vectores propios de la matriz. Por otro lado, y a diferencia de la función solve(), el caso por defecto es el que mejor optimiza el proceso (entre algunos otro), por lo que en esta función eigh() NO es estrictamente necesario cambiar parámetros para obtener el mejor rendimiento.


==> Rendimiento de la función Scipy.linalg.eigh() para tipo de dato "double" para N del 2 al 10.000:


![image](https://user-images.githubusercontent.com/89056734/130306987-35a80223-ef9b-45d0-8fe7-1fc58a0e74cd.png)
![image](https://user-images.githubusercontent.com/89056734/130306991-244f5a70-59b0-4ec1-9941-e36b1f2c7a95.png)
![image](https://user-images.githubusercontent.com/89056734/130306994-d1bd7b7e-bb1d-4b08-80d4-d4c6892e9b28.png)
![image](https://user-images.githubusercontent.com/89056734/130306997-818d0424-8a51-4fa4-8cb0-b0108ca9ef6f.png)
 

Se aprecia como los parámetros por defecto comtinúan siendo los más eficientes. 


==> ¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? ¿Qué algoritmo gana (en promedio) en cada caso? ¿Depende del tamaño de la matriz? ¿A que se puede deber la superioridad de cada opción? ¿Su computador usa más de un proceso por cada corrida? ¿Que hay del uso de memoria (como crece)? 

Respuesta: Tal como se ve en los gráficos anteriores, el caso de la función scipy.linalg.eigh() con driver = "evx" y overwrite_a = False, y driver = "ev" y overwrite_a = Trie son los procesos que poseen MAYOR variabilidad (para float) en los tiempos de ejecución, los datos tipo "double" no presentaron varianzas considarables a salvo para N pequeños. Los algoritmos ganadores se comentaron bajo los gráficos, siendo los parámetros por defecto muy buenas opciones. Los procesadores del computador se ocuparon casi en su mayoría. El uso de memoria (como se puede ver en los txt), permanecen constantes para cada caso, y solo suben al momento de subir de N, no obstante, son considerablemente mayores a los de la entre PE03, debido a que son procesos más complejos que retornan mayores output.


###################################################################################################################################################################################

ENTREGA P0E5

En esta entrega se usarán por primera vez matrices dispersas, las cuales corresponden a dichas matrices en las cuales los ceros dentro de ella, no se consideran dentro de las operaciones matemáticas en Python, ahorrando así tiempo y memoria, además de bajar considerablemente la complejidad computacional de la operación. Para ambos casos se usarán datos tipo DOUBLE y el mismo código para generar matrices laplacianas de tamaño N de las entregas pasadas, ahora dichas funciones laplacianas estarán al principio de cada código.

El código de ensamblaje para la matriz laplaciana utilizado fue el siguiente:

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

En primer lugar, se analizará el desempeño de la función MATMUL (multiplicación de matrices) para las matrices llenas Laplacianas de tamaño N creciente, corriendo 10 veces cada N, luego se graficarán las líneas de complejidad computacional y la gráfica de desempeño (en segundos) correspondiente. En segundo lugar, usando la función sparse.csr_matrix() se multiplicarán matrices dispersas laplacianas, y se analizarán de igual manera que para las matrices llenas.

A continuación se muestran los resultados:

![image](https://user-images.githubusercontent.com/89056734/131061194-8c98ea63-682e-49c7-a761-02b2197b4121.png)
![image](https://user-images.githubusercontent.com/89056734/131061208-cd9cb15a-bb12-4816-9b76-7d49b7aaece8.png)

Puede apreciarse claramente como el tiempo de solución de A*B (o A@B) es significantemente menor para el caso de las matrices dispersas, llenado como tope a los 10 ms, cuando las matrices llenas llegan hasta el segundo de duración. Esto es debido a que con las matrices dispersas, el computador no "pierde" tiempo con las multiplicaciones por cero, ahorrando valiosos micro-segundos. Ahora bien, en cuanto al tiempo de ensamblaje, no se ven diferencias considerables, debido a que ensamblar el sistema es lo mismo para ambos casos por el hecho de ser los mismos valores de N respectivos.

En cuanto a la complejidad computacional; para las matrices llenas, solucionar el sistema tiende a estar más cerca del N**2, esto significa que al aumentar N en 2 unidades, requiero 4 veces más tiempo para resolver, y en el caso del ensamblado, es de una complejidad más bien lineal o directamente proporcional. Ahora bien, analiando las matrices dispersas ocurre algo muy interesante, la complejidad computacional de solucionar el sistema tiende a ser CONSTANTE, a diferencia del proceso de ensamblado que tiende a ser lineal. Esto indica claramente como es de INCREIBLE utilidad el uso de matrices dispersas para optimizar los tiempo de solución de MATMUL, ya que prácticamente no cambia el tiempo conforme crece N, esto significa que se podría llegar a valores de N muy grandes (del orden de 100 000) fácilmente sin esperar hasta 2 minutos en que se resuelva el sistema. Sin duda una muy buena herramienta para trabajar computacionalmente con matrices de gran tamaño. Sería interesante probar hasta cual N es posible llegar sin esperar más de 10 segundos, pero para lograr comparar diretamente los desempeños, se usaron exactamente los mismos N.

###################################################################################################################################################################################

ENTREGA P0E6

Esta continuación de la entrega anterior (análisis de complejidad computaciona) usrará como base los mismos códigos que la entrega P0E5, con la diferencia que en este caso se analizará la complejidad computacional de SOLVE y INV para matrices laplacianas llenas y dispersas. Para todo se utilizarán datos tipo DOUBLE. Se correrán un cierto número de tamaños para la matriz varias veces cada uno.

Para los 2 primeros análisis, se usarán N hasta 10000, esto debido a que el tipo de dato utilizado no permite tamaños mucho mayores por el siguiente error:

![image](https://user-images.githubusercontent.com/89056734/131600209-96abb320-1727-43d7-9eea-a19669c048c2.png)

Primer análisis; para este caso se analizó la complejidad de resolver el sistema A*x = b, siendo A una matriz laplaciana llena y b un vector de unos de tamaño N respectivo. Los resultados fueron los siguientes.

![image](https://user-images.githubusercontent.com/89056734/131600251-9f229163-1c29-412c-8114-3ab8ecaa5c8f.png)

Segundo análisis; para este caso se analizó la complejidad de resolver el sistema A*x = b, siendo A una matriz laplaciana dispersa, es decir, se utilizó la función x = lin.spsolve(A,b), siendo b un vector de unos de tamaño N respectivo. Los resultados fueron los siguientes.

![image](https://user-images.githubusercontent.com/89056734/131600505-9e3d1da2-409c-4125-b930-76a71aec6887.png)

