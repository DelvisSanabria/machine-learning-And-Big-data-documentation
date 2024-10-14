## Conceptos importantes para entender Big Data

## Data Warehouse

Un data warehouse o almacén de datos, es un sistema de gestión de bases de datos diseñado específicamente para recopilar, almacenar y administrar grandes volúmenes de datos de diversas fuentes en un formato estructurado y optimizado para el análisis. 

Su principal objetivo es permitir a las organizaciones tomar decisiones basadas en la información contenida en los datos históricos y actuales.


## On premise Data System

Un sistema de datos on-premise, “sistema local” o “en sitio”, es la infraestructura informática y de almacenamiento de datos que se encuentra físicamente dentro de las instalaciones de una organización o empresa. 

En otras palabras, todos los componentes del sistema, como servidores, almacenamiento, redes y otros equipos, que se mantienen y gestionan internamente en la organización.


## Cloud computing

El cloud computing o computación en la nube, es un modelo de entrega de servicios informáticos a través de internet. 

En lugar de tener que adquirir y mantener hardware y software localmente, las organizaciones pueden acceder a recursos informáticos como servidores, almacenamiento, bases de datos, redes, software y más a través de proveedores de servicios en la nube como por ejemplo AWS (Amazon Web Services) y más.

## Que es la Big Data

El término "Big Data" se refiere al vasto conjunto de datos que excede la capacidad de las herramientas tradicionales de procesamiento y gestión de datos para capturar, almacenar, administrar y analizar de manera eficiente.

## Que incluye la Big Data 

Datos de banca, casas de acciones, email

tambien incluye datos menos conocidos como: cadenas de suministros , codigo de barras

Esta siempre ha existido

## Ciclo de vida de los Datos

El ciclo de vida de los datos es fundamental para entender cómo se manejan grandes volúmenes de información en la era de la Big Data. Cada una de las etapas que mencionas adquiere una dimensión particular cuando se trabaja con conjuntos de datos masivos.

1. Extracción o Recopilación:

*Fuentes diversas*: En la Big Data, los datos se recopilan de una amplia variedad de fuentes, tanto estructuradas (bases de datos) como no estructuradas (textos, imágenes, videos, redes sociales).

*Volumen masivo*: La cantidad de datos a extraer es exponencialmente mayor, lo que requiere herramientas y técnicas especializadas para capturar y almacenar la información de manera eficiente.

*Velocidad*: Los datos se generan a una velocidad vertiginosa, lo que exige sistemas de extracción capaces de procesarlos en tiempo real o casi real.

*Variedad*: La diversidad de formatos y tipos de datos (numéricos, textuales, geográficos, etc.) plantea desafíos adicionales en la etapa de extracción.

2. *Almacenamiento*:

*Infraestructura escalable*: Se necesitan sistemas de almacenamiento altamente escalables y distribuidos para manejar grandes volúmenes de datos.

*Diferentes tipos de almacenamiento*: Los datos se almacenan en diversos formatos y niveles de detalle, desde almacenamiento en la nube hasta sistemas de archivos distribuidos.

*Gestión de datos*: Es crucial implementar estrategias de gestión de datos para garantizar la integridad, seguridad y accesibilidad de la información a largo plazo.

3. *Procesamiento y Análisis*:

*Herramientas especializadas*: Se utilizan herramientas y frameworks de Big Data (Hadoop, Spark, etc.) para procesar grandes volúmenes de datos de manera distribuida y paralela.

*Análisis en tiempo real*: La capacidad de analizar los datos en tiempo real es fundamental para tomar decisiones informadas rápidamente.

*Aprendizaje automático*: Las técnicas de aprendizaje automático se aplican a los grandes conjuntos de datos para descubrir patrones, tendencias y relaciones ocultas.

4. *Visualización*:

*Herramientas interactivas*: Se emplean herramientas de visualización interactivas que permiten explorar los datos de manera dinámica y descubrir insights de forma más intuitiva.

*Dashboards personalizados*: Se crean dashboards personalizados para monitorear métricas clave y comunicar los resultados del análisis a los usuarios finales.

*Mapas y gráficos*: La visualización geográfica y la creación de gráficos complejos son esenciales para representar datos multidimensionales.

## Las 7 V's del big data son un marco que se utiliza para describir las características clave de los datos masivos.

*Volumen*: El tamaño de los datos (terabytes de datos de la banca).

*Velocidad*: Cuán rápido los datos entran (El GPS y los sensores en autos envían datos cada segundo).

*Variedad*: Diferentes fuentes y formatos de datos (post, fotos y estados en apps y redes sociales).

*Veracidad*: La credibilidad de los datos (Los datos de redes sociales pueden ser inexactos o engañosos).

*Viabilidad*: Dificultad de almacenar y analizar los datos (requerimientos de infraestructura, costos, etc.).

*Visualización*: Presentación de los datos de manera comprensible (gráficos, mapas, etc.).

*Valor*: Beneficios al aprovechar los datos (mejora la toma de decisiones, innovación, el serv. al cliente, etc.).

## Herramientas y Lenguajes Utilizados

En el Big Data se emplean una gran variedad de herramientas agrupadas por categorías y subcategorías. Cada una aborda aspectos específicos del procesamiento, almacenamiento, análisis y gestión de datos, veamos algunas de ellas.

- **Análisis y Visualización**:
    - **Plataformas de Inteligencia Empresarial (BI)**:
        - **IBM Cognos**: Plataforma de inteligencia empresarial para acceder y analizar datos para la toma de decisiones.
        - **SAP Business Objects**: Suite de herramientas de BI para informes, análisis y visualización.
        - **MicroStrategy**: Plataforma de análisis empresarial con informes interactivos y aplicaciones móviles.
    - **Herramientas de Visualización Interactiva**:
        - **ZoomData**: Plataforma de análisis y visualización de datos en tiempo real.
        - **Qlik**: Herramienta de análisis y visualización con visualizaciones interactivas.
        - **PowerBI**: Herramienta de análisis y visualización de Microsoft.
        - **Tableau**: Software de visualización de datos interactivo.
    - **Procesamiento y Computación**:
        - **Entornos de Desarrollo y Análisis de Datos:**
            - **Anaconda:** Plataforma para análisis de datos, procesamiento y desarrollo de machine learning
        - **Frameworks de Procesamiento en Clúster**:
            - **Hadoop MapReduce**: Framework para procesar datos en clústeres distribuidos.
            - **HIVE**: Plataforma de análisis de datos en Hadoop con SQL.
            - **TEZ**: Framework de procesamiento en Hadoop para tareas complejas.
        - **Procesamiento en Tiempo Real**:
            - **Apache Drill**: Motor de consulta SQL para datos no estructurados.
            - **Apache Storm**: Plataforma para procesamiento de datos en tiempo real.
            - **Flink**: Framework de procesamiento de datos en tiempo real.
        - **Bases de Datos en la Nube**:
            - **Google BigQuery**: Servicio de análisis de datos en la nube de Google.
        - **Procesamiento de Flujos de Datos**:
            - **Spark Streaming**: Procesamiento en tiempo real con Apache Spark.
            - **Kafka**: Plataforma de streaming en tiempo real.
        - **Almacenamiento y Gestión de Datos**:
            - **Almacenamiento Distribuido y Ecosistema Hadoop**:
                - **Hadoop** **(HDFS y MapReduce)**: Ecosistema de almacenamiento y procesamiento distribuido.
                - **MAPR** Tables: Sistema de almacenamiento en Hadoop.
- **Sistemas de Almacenamiento NoSQL y SQL**:
    - **KUDU**: Almacén de datos distribuido.
    - **MemSQL**: Base de datos en memoria.
- **Distribución y Almacenamiento de Datos**:
    - **Sistemas de Almacenamiento Masivo y Distribución**:
        - **Pivotal**: Plataforma de almacenamiento y análisis en la nube.
        - **Oracle** **EXADATA**: Sistema de base de datos de alto rendimiento.
        - **Teradata**: Plataforma de almacén de datos y análisis.
        - **GreenPlum**: Base de datos de análisis masivo.
        - **Netezza**: Sistema de almacenamiento de alto rendimiento.
    - **Distribuciones de Hadoop y Plataformas en la Nube**:
        - **HortonWorks**: Distribución de Hadoop.
        - **Cloudera**: Plataforma de Hadoop.
        - **Azure** **HDInsight**: Servicio de análisis en la nube de Microsoft.
        - **Amazon** **EMR**: Servicio de procesamiento en la nube de Amazon.
    - **Sistemas de Archivo y Distribución**:
        - **IBM** **GPFS**: Sistema de archivos paralelos y distribuidos.
    - **Plataformas de Streaming y Procesamiento en Tiempo Real**:
        - **Apache Storm**: Plataforma de procesamiento en tiempo real.
        - **Flink**: Framework de procesamiento en tiempo real.
        - **Kafka**: Plataforma de streaming en tiempo real.

## Desafios de la Big Data

Explicar usando laminas del curso

## Que es anaconda

Anaconda es una distribución de los lenguajes de programación Python y R para computación científica (ciencia de datos, aplicaciones de Machine Learning, procesamiento de datos a gran escala, análisis predictivo, etc.).
Tiene como ventaja simplificar la gestión e implementación de paquetes. La distribución incluye paquetes de “data science” adecuados para Windows, Linux y macOS. 

## Que es jupyter NoteBooks

Los Jupyter Notebooks es una aplicación web, también de código abierto que nos va a permitir crear y compartir documentos con código en vivo, ecuaciones, visualizaciones y texto explicativo. Estos documentos registran todo el proceso de desarrollo y, lo más interesante, pueden ser compartidos fácilmente con otras personas a través de correo electrónico, Dropbox, sistemas de control de versiones como git/GitHub y nbviewer.

Este viene incluido con Anaconda

## Que es pandas

Pandas es una muy popular librería de código abierto dentro de los desarrolladores de Python, y sobre todo dentro del ámbito de Data Science y Machine Learning, ya que ofrece unas estructuras muy poderosas y flexibles que facilitan la manipulación y tratamiento de datos.

Pandas surgió como necesidad de aunar en una única librería todo lo necesario para que un analista de datos pudiese tener en una misma herramienta todas las funcionalidades que necesitaba en su día a día, como son: cargar datos, modelar, analizar, manipular y prepararlos.

Documentación: https://pandas.pydata.org/docs/

## Que es Google Collab

Google Colab, también conocido como Colaboratory, es un servicio de Google Research que permite a cualquier persona escribir y ejecutar código Python en el navegador. Es ideal para proyectos de aprendizaje automático, análisis de datos y educación.
En términos técnicos, Colab es un servicio de notebooks de Jupyter alojados que no requiere instalación para usarlo y brinda acceso sin costo a recursos computacionales, incluidas GPU.

## Estructuras de Datos

*Serie*: Una serie es una estructura de datos unidimensional que puede contener datos de un solo tipo (por ejemplo, números, cadenas, fechas, etc.). Es decir, una forma de llamar a los arrays o listas.

*Dataframe*: Es una estructura de datos bidimensional similar a una tabla en una base de datos o una hoja de cálculo. Los dataframes están compuestos por series y se utilizan para representar y manipular datos tabulares (información en filas y columnas).

## Que es la regresion Lineal 

Este es un algoritmo usado para modelar la relación entre dos variables o más.

La regresión lineal es una forma sencilla de encontrar patrones en los datos y hacer predicciones. Es como encontrar una tendencia en una gran cantidad de información.

## Para que Sirve

*Predecir*: Si conoces un valor de una variable, puedes usar la línea para estimar el valor correspondiente de otra variable.

*Entender la relación*: La línea te muestra cómo cambia una variable cuando la otra cambia. Si la línea sube, significa que las variables están relacionadas de forma positiva (cuando una aumenta, la otra también). Si la línea baja, la relación es negativa (cuando una aumenta, la otra disminuye).

*Ejemplo sencillo*:

Imagina que quieres saber si hay una relación entre la cantidad de horas que estudias y la nota que obtienes en un examen. Recolectas datos de varios estudiantes (horas de estudio, nota) y los representas en un gráfico. Si al dibujar una línea recta, ves que a medida que aumentan las horas de estudio, generalmente también aumenta la nota, puedes decir que existe una relación positiva entre ambas variables.