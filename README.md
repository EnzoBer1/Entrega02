# P0
Incoveniente 1: Para el Caso 1 (Numpy.inv) utilizando un np.half no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 16.

Incoveniente 2: Para el Caso 1 (Numpy.inv) utilizando un np.longdouble no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 64.

Inconveniente 3: Mi computador no fue capaz de hacer 10 corridas para un valor de N mayor a 8000, posiblemente se iba a demorar demasiado tiempo, incluso en ocasiones que se intentó, spyder no respondía y debía cerrarlo.

Análisis del uso de memoria: Como puede apreciarse en los gráficos y archivos txt; para cada caso (y cada corrida) el uso de memoria permanece constante, esto es debido a que la cantidad de bytes para un cierto N en cada caso no cambia, es decir, la memoria utilizada para almacenar las matrices no depende del tipo de dato, ni de la librería, ya que son simplemente una cantidad específica de números.

Análsis del tiempo de inversión: se ve claramente en los gráficos y en los txt como el tiempo de inversión del caso 2 y 3, para N = 5000, son considerablemente menores al del caso 1. Se puede afirmar que scipy es más rápido al momento de invertir matries que numpy.
