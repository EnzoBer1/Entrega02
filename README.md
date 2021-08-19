# P0
Incoveniente 1: Para el Caso 1 (Numpy.inv) utilizando un np.half no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 16.

Incoveniente 2: Para el Caso 1 (Numpy.inv) utilizando un np.londouble no corrió el codigo, es más, ni siquiera pudo importarse al momento de crear la matriz laplaciana. Viendo el error que arroja python, se aprecia que en el caso de usar linalg con numpy, no es posible operar el float 64.

Análisis del uso de memoria: Como puede apreciarse en los gráficos y archivos txt; para cada caso (y cada corrida) el uso de memoria permanece constante, esto es debido a que la cantidad de bytes para un cierto N en cada caso no cambia, es decir, la memoria utilizada para almacenar las matrices no depende del tipo de dato, ni de la librería, ya que son simplemente una cantidad específica de números.
