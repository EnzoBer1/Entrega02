# P0

Link Repositorio: https://github.com/EnzoBer1/P0

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

ENTREGA P0E4

Esta entrega constará de analizar el desempeño de la función scipy.linalg.solve para encontrar el vector x solución del sistema Ax = b, siendo b un vector de unos, y A la mariz laplaciana de la entrega P0E3. Se analizará el desempeño para distintos tipos de datos (float y double); para distintas configuraciones de la función solve (6 casos en total)
Luego, se graficarán los resultados en una misma figura con el fin de comparar los tiempos en que se ejecuta la ecuación matricial. 
Con el mismo procedimiento, se analizará la función scipy.linalg.eigh (la cual entrega los valores y vectores propios de una matriz), para los mismos tipos de datos y 5 distintas configuraciones. La idea es poder comparar directamente en un mismo gráfico y ver rápidamente cual configuración optimiza cada proceso.

Los resultados por ejemplo de la función scipy.linalg.solve fueron los siguientes:
![image](https://user-images.githubusercontent.com/89056734/130177232-eb9016c2-9b20-42e5-84a3-d9e82b511ab4.png)
Aquí se ve como x = solve(A,b, assume_a="pos") da el tiempo de ejecución más bajo, es decir, es la configuración más rápida para resolver el sistema.



