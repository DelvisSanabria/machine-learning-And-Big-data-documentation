""" 

## **¿Qué es la Inteligencia Artificial?**

La inteligencia artificial (IA) se refiere a la capacidad inherente de una computadora o un sistema informático para imitar o simular la inteligencia humana. Esta habilidad les permite realizar tareas que, en circunstancias normales, requerirían la inteligencia de un ser humano. Algunos ejemplos de estas tareas son el aprendizaje automático, el razonamiento lógico, la comprensión del lenguaje natural y la percepción visual. En esencia, la inteligencia artificial es la simulación de la inteligencia humana por parte de las máquinas, especialmente los sistemas informáticos.

## **¿Qué es el Machine Learning o Aprendizaje Automático?**

El aprendizaje automático, también conocido como machine learning, es una rama especializada de la inteligencia artificial que se centra en el desarrollo y la optimización de algoritmos y modelos. El propósito principal de estos algoritmos y modelos es permitir a las computadoras aprender y mejorar su rendimiento en tareas específicas a través de la interacción con la experiencia y los datos, en lugar de ser programadas explícitamente para realizar dichas tareas. En otras palabras, las máquinas tienen la capacidad de aprender de manera autónoma sin la intervención humana directa. Esto les permite mejorar y refinar sus habilidades a medida que procesan más datos.

Las aplicaciones del aprendizaje automático son vastas y diversas. Por ejemplo, las computadoras pueden aprender a realizar tareas tan diversas y complejas como reconocer objetos en imágenes, clasificar imágenes según diferentes criterios, traducir idiomas con alta precisión y mucho más. Todo esto se logra mediante el uso de datos de entrenamiento que se proporcionan a las máquinas. Estos datos de entrenamiento son ejemplos de la tarea en cuestión y ayudan a la computadora a entender y aprender cómo se debe realizar la tarea.

##En resumen

El machine learning es una técnica de aprendizaje para la computadora basada en datos y estadísticas. Estos datos pueden venir en cualquier forma desde arrays o una base de datos completas.

Ejemplo: [99,86,87,88,111,86,103,87,94,78,77,85,86]

De este array podrás sacar cual es el valor más alto, el más pequeño y el promedio, entre otros datos, lo cual veremos luego de conocer algunas librerías necesarias.

##librerias 

Uno de los lenguajes de programacion mas usado para el machine learning es Python, el cual tiene incluso librerias preparadas con funcionalidades y mejoras para el aprendizaje automático.

como:

Numpy

NumPy es una librería de Python que proporciona un objeto de matriz de alto rendimiento y herramientas para trabajar con ellas. Sirve para realizar operaciones matemáticas en arreglos multidimensionales de manera eficiente, como por ejemplo, álgebra lineal, transformaciones de Fourier y generación de números aleatorios. 

También es utilizado como base para otras librerías de cálculo científico en Python, como SciPy y scikit-learn.

SciPy

SciPy es una librería de Python que se basa en NumPy y proporciona una amplia variedad de algoritmos y herramientas científicas avanzadas. Sirve para hacer tareas específicas como optimización, integración, interpolación, procesamiento de señales e imágenes, entre otras. 

En resumen, SciPy extiende a NumPy, brindando una amplia variedad de herramientas y algoritmos para la resolución de problemas científicos y técnicos de manera eficiente.

Google Colab

Colaboratory, o "Colab" para abreviar, es un producto de Google Research. Permite a cualquier usuario escribir y ejecutar código arbitrario de Python en el navegador. Es especialmente adecuado para tareas de aprendizaje automático, análisis de datos y educación.

Esto nos ahorra tener que instalar tantas librerías y herramientas en nuestra PC, además de que nos ahorra usar los recursos.

Vamos a ver ahora como calculariamos algunos datos de interes para nuestro proximo tema "Big Data", con una de estas librerias, en este caso con numPy

para instalar numpy:

pip install numpy


"""

##promedio o media (Mean)

""" 

El promedio es el valor que se obtiene al sumar todos los números de un conjunto y dividirlos entre la cantidad de elementos

Dado el siguiente array:
[99,86,87,88,111,86,103,87,94,78,77,85,86]

Calcular promedio:

Para calcular el promedio en estos datos necesitamos sumar todos los datos y dividirlos por la cantidad de datos

1167/13 = 89.769


"""

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

## el promedio podemos calcularlo con el metodo mean() de numPy

x = numpy.mean(speed)

print(x)

""" 

##Mediana

La mediana es el valor que se encuentra en la mitad de un conjunto de números una vez organizados. En caso de que el conjunto de los elementos sea un número par, los dos números en el medio se suman y se dividen entre dos

Dado el siguiente array:
[99,86,87,88,111,86,103,87,94,78,77,85,86]

Al organizarlo se veria asi:
[77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111]

La mediana es 87


"""


speed2 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

""" 

##La moda(Mode)

La moda es el numero que mas se presenta en un conjunto de números

Utilizaremos el siguiente array para un ejemplo:

[99,86,87,88,111,86,103,87,94,78,77,85,86]

Verificamos la cantidad de números repetidos y notamos lo siguiente:

[99,"86",87,88,111,"86",103,87,94,78,77,85,"86"]

numPy no tiene un metodo para calcular la moda por tanto usaremos scipy que si tiene un modulo para ello

para instalar scypy:

pip install scipy

"""

from scipy import stats

speed3 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)

"""

##Desviacion estandar 

La desviación estándar es un número que nos dice cuánto varían los números en un conjunto de datos. 

Es como una medida de "dispersión" de los números. Si los números son muy parecidos entre sí, la desviación estándar será pequeña. Si los números son muy diferentes entre sí, la desviación estándar será grande. 

Es una forma de medir cuán "alejados" están los números de un conjunto de datos entre sí.


Un ejemplo de esto dado el siguiente array:
[86, 87, 88, 86, 87, 85, 86]

La desviación estándar es: 0.9

Dado el siguiente array: [32, 111, 138, 28, 59, 77, 97]

la desviación estándar es: 37.85

A mayor diferencia entre los números, mayor es la desviación estándar


"""

data = [86, 87, 88, 86, 87, 85, 86]

x = numpy.std(data)

print(x)

""" 
##Programacion regular

## **¿Qué es la programación regular?**

La programación regular es un proceso sistemático y estructurado de escritura de código. Este proceso implica la definición explícita de cómo se debe realizar una tarea en particular. Esto se logra detallando todos los pasos que se deben seguir y las funciones que se deben implementar para alcanzar soluciones o resultados específicos. En otras palabras, la programación regular es un método preciso y detallado que permite a los programadores crear programas que pueden realizar tareas específicas y entregar resultados concretos.

"""

def saludar(nombre):
    """Imprime un saludo personalizado.

    Args:
        nombre (str): El nombre de la persona a saludar.
    """
    return f"Hola, {nombre}!"

saludo = saludar("Delvis")
print(saludo)

## Salida: Hola, Delvis!

""" 

Otro ejemplo de programacion regular


"""

""" Transforma 4.6 kilómetros a metros.

Para realizar este ejercicio necesitamos multiplicar 4.6 * 1000
4.6 x 1000 = 4600 metros """

def convertir(km): 
  metros = km * 1000
  return metros

print(f"Total: {convertir(4.6)}")

""" 

para comparar un ejemplo con machine learning utilizando la libreria sklearn

si quieren instalarla:



"""


from sklearn.linear_model import LinearRegression

# Datos de entrenamiento (kilómetros como característica y metros como etiqueta)
X = [[1], [2], [3]]  # Kilómetros (una sola característica)
y = [1000, 2000, 3000]  # Metros correspondientes

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos
model.fit(X, y)

# Predecir la conversión de 4.6 kilómetros
km_a_convertir = [[4.6]]
resultado = model.predict(km_a_convertir)

print(f"Total: {resultado[0]} metros")

""" 

Machine learning VS Programación regular

A diferencia de la programación regular, donde se deben dar instrucciones para que un algoritmo realice una operación, cuando hablamos de un software de Machine learning (Aprendizaje Automático) nos referimos a un software que tiene unos inputs (entradas), y este, a través de un proceso que desconocemos retornará un resultado.

Es decir, determinará por sí mismo cuál es la forma de llegar a un resultado en base al aprendizaje que adquiere durante un proceso conocido como entrenamiento.


"""

""" 

##Que es una red neuronal

Una red neuronal artificial es un componente esencial y poderoso que forma la base de muchos sistemas de aprendizaje automático y la inteligencia artificial. Esta tecnología, que está inspirada y modelada basándose en la intrincada red de neuronas presentes en el cerebro humano, tiene el poder de llevar a cabo una amplia gama de tareas de procesamiento de información.

Las redes neuronales artificiales se utilizan frecuentemente para abordar desafíos tales como la clasificación de información, el reconocimiento de patrones y la ejecución de cálculos de gran complejidad. También se están explorando y aplicando en una serie de campos nuevos y emergentes, lo que refleja su versatilidad y su capacidad para adaptarse a una variedad de contextos y necesidades.

La red neuronal consiste en una serie de elementos interconectados, a menudo referidos como neuronas artificiales o nodos. Estos nodos se organizan en capas, lo que permite a la red neuronal procesar información de una manera estructurada y ordenada. Cada nodo en la red tiene la capacidad de procesar información y transmitirla a otros nodos, creando así una red de procesamiento de información que puede adaptarse y aprender de los datos que procesa.

## Que es una neurona artificial


Una neurona artificial, también conocida como perceptrón, es la unidad básica de procesamiento en una red neuronal artificial. Estas redes son una simulación computacional de cómo las neuronas en el cerebro humano interactúan y procesan la información.

La neurona artificial acepta múltiples valores de entrada, cada uno de los cuales está ponderado por un valor numérico llamado peso. Estos pesos son esenciales para la función de la neurona, ya que determinan la importancia relativa de cada entrada. En términos sencillos, el peso asignado a una entrada específica puede intensificar o atenuar la señal de dicha entrada.


Una vez que las entradas son recibidas y ponderadas, la neurona realiza una suma ponderada de estas entradas y pesos. Esta suma es esencialmente una combinación lineal de las entradas y sus pesos correspondientes.

Posteriormente, la neurona aplica una función de activación a la suma resultante para producir una salida. La función de activación es una pieza fundamental en el procesamiento de la información por parte de la neurona, ya que introduce no linealidad en el modelo. Esta función debe cumplir con un umbral determinado y, en base a eso, se determina si la neurona se activa (produce una salida significativa) o no.

Explicar con la imagen de Excalidraw:

En este ejemplo tenemos una neurona con 3 factores de entradas para tomar la decisión de Ir a un concierto o No, estos son: “¿Tengo Dinero?”, “¿Voy acompañado(a)?”, “¿Me gusta el artista?”. Cada factor (entrada) tiene un peso (importancia) asignado y se usara para determinar si te toma la decisión (es decir, si se activa la neurona) o no.

Si se da el caso de que los factores “¿Tengo dinero?” y “¿Me gusta el artista?” tienen como respuesta “Si” y “Si”, se introduce el peso de estos factores a la neurona, dando como resultado una sumatoria de 3 en peso de entrada. Si se tiene como umbral de activación que los pesos de entradas sean mayores que 2, tendríamos como resultado la activación de esta neurona.

Por lo tanto, podríamos decir que en este caso la aseveración seria: “Tengo dinero y me gusta el artista, aunque no voy acompañado, he tomado la decisión de ir”.

Entender el funcionamiento de una neurona es de vital importancia para la comprensión del funcionamiento de una red neuronal, en resumidas palabras, es el mismo proceso que realiza una neurona, pero multiplicado por el total de neuronas por cada capa en la red.

##Capas de una red neuronal

Explicar con la imagen de Excalidraw:

Una capa es un conjunto de neuronas que están conectadas entre sí y procesan los datos de entrada. En una red neuronal con múltiples capas, las capas se encuentran jerárquicamente una sobre la otra. La primera capa se conoce como la capa de entrada, la última capa se conoce como la capa de salida, y las capas intermedias se conocen como capas ocultas.

Capa de Entrada (Input Layer): Esta es la capa inicial en la arquitectura de una red neuronal, y su función principal es recibir los datos de entrada. Cada nodo o neurona en esta capa representa una característica única o una entrada individual en el conjunto de datos. En esta etapa, no se realizan cálculos complejos ni transformaciones significativas en los datos. Su función es fundamentalmente pasiva, ya que simplemente se encarga de transmitir los valores de entrada sin alteración a la siguiente capa en la red. Este proceso de transmisión de datos es crucial para el funcionamiento de la red neuronal, ya que prepara el escenario para las operaciones más complejas que se realizarán en las capas posteriores.

Capas Ocultas (Hidden Layers): Las capas ocultas son un elemento esencial en la arquitectura de las redes neuronales. Estas capas, que se encuentran estratégicamente situadas entre la capa de entrada y la capa de salida, cumplen una función crucial al ser las responsables de realizar cálculos y transformaciones complejas en los datos que reciben. Las capas ocultas reciben información de la capa de entrada o de otras capas ocultas en el caso de redes con múltiples capas ocultas. Estas capas, por lo general, procesan y manipulan los datos que reciben, aplicando una variedad de funciones y operaciones matemáticas, antes de enviarlos a la siguiente capa en la secuencia. Este proceso se repite hasta que los datos llegan a la capa de salida, que sintetiza toda la información procesada y produce el resultado final.

Capa de Salida (Output Layer): La capa de salida, que es una componente integral y crucial de cualquier red neuronal, es donde se produce el resultado final de la red. Esta capa procesa y traduce los patrones complejos y abstracciones aprendidos por las capas ocultas en predicciones o clasificaciones concretas que son útiles para el problema que estamos tratando de resolver. El número de nodos en la capa de salida está directamente relacionado con la naturaleza del problema que la red neuronal está diseñada para abordar. Por ejemplo, en tareas de regresión, generalmente hay un solo nodo que produce un valor continuo. Sin embargo, para tareas de clasificación multiclase, hay múltiples nodos, cada uno representando una clase diferente. 


## ¿Qué es mejor, más Capas o más Neuronas?

La respuesta corta es que **depende del problem**a que se esté resolviendo. En general, más capas pueden ayudar a una red neuronal a aprender patrones más complejos, mientras que más neuronas pueden ayudar a una red neuronal a aprender patrones más finos.

- **Patrones finos:** pueden ser difíciles de detectar porque son sutiles o porque están ocultos por otros patrones. Por ejemplo, la diferencia entre dos tipos de tejido en una imagen médica, o la diferencia entre dos tipos de voz en una grabación de audio.
- **Patrones complejos:** son patrones que están formados por múltiples patrones más pequeños. Por ejemplo, una imagen de un perro, que está formada por patrones de color, forma y tamaño.

Sin embargo, hay algunos factores que deben tenerse en cuenta al decidir si agregar más capas o más neuronas.

- **Más Capas**: Agregar más capas a una red neuronal puede ayudar a la red a aprender patrones más complejos. Esto se debe a que las capas adicionales brindan a la red más espacio para representar estos patrones. Sin embargo, agregar más capas también puede aumentar la complejidad de la red y hacerla más difícil de entrenar. Además, las redes neuronales con muchas capas pueden ser más propensas a sobreajustar los datos de entrenamiento, lo que puede conducir a un rendimiento deficiente en datos nuevos.
- **Más Neuronas:** Agregar más neuronas a una capa puede ayudar a una red neuronal a aprender patrones más finos. Esto se debe a que las neuronas adicionales brindan a la red más capacidad para representar estos patrones. Sin embargo, agregar más neuronas también puede aumentar la complejidad de la red y hacerla más difícil de entrenar. Además, las redes neuronales con muchas neuronas pueden consumir más recursos informáticos.

En general, es mejor comenzar con una red neuronal pequeña y simple y luego ajustar el número de capas y neuronas según sea necesario.

##Peso entre conexiones neuronales

En una red neuronal, el peso de las conexiones se refiere a los valores numéricos asociados a las conexiones entre las neuronas en la red. Estos valores indican la importancia o el impacto de cada conexión en la propagación de la información a través de la red.

Los pesos de las conexiones son uno de los aspectos más importantes de una red neuronal, ya que tienen un gran impacto en su rendimiento y capacidad para aprender y generalizar patrones. Los pesos se ajustan durante el proceso de entrenamiento de la red mediante algoritmos de optimización, como el gradiente descendente, para minimizar el error entre los resultados esperados y los resultados reales.

##Cosas que involucra el peso

Algunas de las cosas que involucran los pesos de las conexiones son:

La cantidad de información que se transmite a través de una conexión es proporcional al peso de la conexión.
Los pesos pueden ser positivos o negativos, lo que significa que pueden aumentar o disminuir el impacto de una conexión en la propagación de la información.
Un peso cero indica que una conexión no tiene ningún impacto en la propagación de la información.

Los pesos son los parámetros que se ajustan durante el entrenamiento de una red neuronal para mejorar su rendimiento.
Los pesos iniciales son esenciales para el proceso de aprendizaje, ya que pueden afectar significativamente el rendimiento de la red.


"""

""" 

##Librerias para Machine Learning

Existen varias librerías populares para machine learning en Python, algunas de las más comunes son:

scikit-learn: Es una librería de aprendizaje automático de código abierto para Python que proporciona una amplia variedad de herramientas de aprendizaje automático, incluyendo clasificación, regresión y clustering.

TensorFlow: Es una librería de código abierto desarrollada por Google que se utiliza para la implementación de redes neuronales y deep learning. Es ampliamente utilizado en investigación y producción.

Keras: Es una librería de alto nivel para la construcción de redes neuronales en Python. Es fácil de usar y es compatible con TensorFlow, Microsoft Cognitive Toolkit (CNTK) y Theano.

Explicar el ejemplo de google Collab:

https://colab.research.google.com/drive/1ehETBOVtCqe7G6HOvm84hfXba8Gd9ILW?usp=sharing#scrollTo=FVDejrBgcokc
"""
