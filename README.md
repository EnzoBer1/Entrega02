# P0
Incoveniente 1: Para el Caso 1 (Numpy.inv) utilizando un np.half no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 16.

![image](https://user-images.githubusercontent.com/89056734/129997478-b018b813-8ae8-4775-9959-3cc862d650c2.png)

Incoveniente 2: Para el Caso 1 (Numpy.inv) utilizando un np.longdouble no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 64.

![image](https://user-images.githubusercontent.com/89056734/129997533-6bd8445f-9128-4f11-a791-f58a07604baf.png)

Inconveniente 3: Mi computador no fue capaz de hacer 10 corridas para un valor de N mayor a 8000, posiblemente se iba a demorar demasiado tiempo, incluso en ocasiones que se intentó, spyder no respondía y debía cerrarlo.

Análisis del uso de memoria: Como puede apreciarse en los gráficos y archivos txt; para cada caso (y cada corrida) el uso de memoria permanece constante, esto es debido a que la cantidad de bytes para un cierto N en cada caso no cambia, es decir, la memoria utilizada para almacenar las matrices no depende del tipo de dato, ni de la librería, ya que son simplemente una cantidad específica de números.

Análsis del tiempo de inversión: Se ve claramente en los gráficos y en los txt como el tiempo de inversión del caso 2 y 3, para N = 5000, son considerablemente menores al del caso 1. Se puede afirmar que scipy es más rápido al momento de invertir matries que numpy.

Uso de overwrite_a: Puede apreciarse claramente en los txt como, para la última corrida del código en el caso de N = 5000, al usar overwrite_a = False (caso 2), se alenta el proceso, por otro lado, se ve una significativa ganancia en cada tipo de dato (half, single, double y longdouble) en comparación con el caso 2 al usar overwrite_a = True (caso 3). Resumiendo, usando overwrite_a = True, se obtiene una ganancia de desempeño. Esto se debe a que el programa reescribe o re utiliza la memoria anterior para escribir la nueva, lo que se traduce en un modo de optimizar espacio.

Caso 3; Longdouble, corrida 10 y N = 5000, overwrite_a = True
![image](https://user-images.githubusercontent.com/89056734/129997659-7e669850-1165-423a-83b4-b83c30988c32.png)

Caso 2; Longdouble, corrida 10 y N = 5000, overwrite_a = False
![image](https://user-images.githubusercontent.com/89056734/129997716-4ac6449e-28aa-4257-b1b2-44efd117d401.png)

