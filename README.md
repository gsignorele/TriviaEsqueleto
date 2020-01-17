"# TriviaEsqueleto" 

Como Flask es un micro framework, no viene con una estructura pre-armada, como sí lo hace Django por ejemplo
Esta organización que les mando acá, es una agrupación posible, pero hay varias opciones, incluso hay algo que se llama Blueprint que es especialmente útil para esto (queda para el avanzado, pueden ir investigando).

Dentro del directorio del proyecto tenemos
- apptrivia.py
- config.py
- routes.py
- models/
- templates/

- apptrivia: Inicializa flask y la base de datos (valiéndose de config,py) Levanta las rutas y lanza flask
- config.py: Básicamente tiene la ubicación de la bd. Se podrían incluir otras configuraciones globales
- routes.py: Ya lo conocen, se definen las rutas, en este caso, sólo agregué 2, una que usa modelos (categoria) y la otra no. Una que usa template y la otra no,
- models/ tiene la definición de los modelos y la bd
- templates/ tiene una template base y otra que usar para mostrar las categorías leídas desde la BD

El proyecto que les mando, es un sólo un ejemplo recortado de Trivia (solo está modelado categoría)
El código está bastante comentado.
Lo levantan, desde una consola de Win o Linux así: python apptrivia.py
Van a responder estos 2 recursos:
- http://localhost:5000/trivia
- http://localhost:5000/trivia/categorias




