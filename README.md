# flaskapp
Flask application using docker
Hay que tener docker instalado y descargar los archivos en este repositorio
Hay que usar cd para llegar a la carpeta donde esten los archivos
Una vez hecho esto hay que correr el siguiente comando: docker build -t flaskapp -f flaskapp.txt .
Esto genera una imagen llamada flaskapp en base al archivo flaskapp.txt y el . le dice a docker que esta en la carpeta actual
Ya hecho esto se debe crear el contenedor con el siguiente comando: docker run -d -p 5000:5000 flaskapp
Esto hara que se cree un contenedor con la imagen llamada flaskapp que exponga el puerto (-p) 5000 del contenedor con el fisico 50000
Y lo correra de manera detach.
Una vez hecho esto se debe ingresar a localhost:5000 y mostrara una imagen parecida a esta:

![image](https://user-images.githubusercontent.com/61640540/224519942-9f1de646-3647-499f-acab-7918f918ef83.png)


Ahi se debe llenar ambos text box el de la izquierda con un username y el de la derecha con un password de la siguietne manera:


![image](https://user-images.githubusercontent.com/61640540/224519974-b8f7ba03-2f94-4d56-9c56-e1dd68c2e2d9.png)


Debe tener el username con la primer letra mayuscula y el password debe contener letras y números.
Despues al darle enviar debe mostrar lo siguiente:

![image](https://user-images.githubusercontent.com/61640540/224519996-7e317262-7d24-46e4-87c9-20b798837a53.png)

De lo contrario mostrara la pagina de login nuevamente como acontinuación:

![image](https://user-images.githubusercontent.com/61640540/224520003-e0481ef4-a559-4b74-92f3-677f3d5eee4b.png)
