# Salva un peludo
Salva un peludo es un proyeto que trata de concienciar sobre la adopcion, mediante una aplicacion que al introducir una foto te devuelve la de un perro que este en adopcion que se parezca a la foto introducida.

## Tecnologías y funcionamiento:
La base del proyecto es un autoencoder hecho con la libreria Keras, configurado con capas convolucionales.
Esta red neuronal tiene la mision de descomponer las fotos en vectores que la representen, para asi poder pasarlo al sistema de recomendación de la aplicación y poder generar una respuesta.

La red neuronal tiene dos partes:
- 1º Parte: Se encarga de generar los vectores, lleva fijada unas dimensiones de entrada de (220,220,3) y el vector de salida es de (28,28,8).
- 2º Parte: Se encarga de recomponer la foto del vector obetenido por la primera parte de la red neuronal, con este paso se comprueba que el vector represente correctamente la foto original.

El proceso de entrenamiento de la red neuronal está hecho en Google Colab, paara optimizar los recursos del sitema he usado un sistema generador que envia en lotes de 100 las imagenes procesadas a la red neuronal.

Para el almacenamiento de los datos de las imágenes (vectore, nombre del animal, imagen y asociacion a la que pertenece) he utilizado una base de datos de MongoDB y Cloudinary para el almacenamiento de las imgenes.

La interfaz de usuario esta hecha con flask, hay una parte reservada para ONGs a la que se accede con usuario y contraseña. Y una zona para el resto de usuarios, que no esta protegida.

La zona reservad a ONGs sirve para poder subir los animales a la base de datos, en el proceso hay una multi-subida de imagenes, que se procesan, suben a cloudinary y finalemente se añaden a la base de datos.

En el procesado de las imagenes hay varios pasos. Para que el proceso se complete bien hay que subit la imagen en formato JPEG, JPG o PNG y con una nomenglatura contreta(Nombre del animal_Nombre de la asocicacion)
 - Procesado de las imágenes par ajustar el tamaño. 
 - Paso por la red neuronal y obtención del vector.
 - Subida de la imagen a Cloudinary y obtención del link.
 - Subida de todos los datos a la base de datos:
    - Nombre.
    - Asociación.
    - Vector de la imagen.
    - link a Cloudinary para poder usarla en el HTML. 

## Próximos pasos:
Los pasos a seguir con este proyecto son los siguientes:
- Implementar un algoritmo de reconocimiento de perros para poder poder cinseguir mejores resultados.
- Incluir una parte visual para ONGs para poder dar de baja los aimales.
- Incluir datos sobre las historias de los animales.
- Desplegar en un servidor.
