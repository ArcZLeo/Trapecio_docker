<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoulasalle/git_github/blob/main/ulasalle.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD LA SALLE</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍAS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO DE INGENIERÍA Y MATEMÁTICAS</span><br />
                <span style="font-weight:bold;">CARRERA PROFESIONAL DE INGENIERÍA DE SOFTWARE</span>
            </th>            
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="2"><span style="font-weight:bold;">Formato</span>: Trabajo de cliente servidor en docker</td></tr>        
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">Examen parcial</span><br />
</div>

<table>
<theader>
<tr><th colspan="2">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>

<tr><td>TÍTULO DE LA PRÁCTICA:</td>Ejercicio de docker<td>Git - GitHub</td></tr>
<tr><td colspan="2">RECURSOS A UTILIZAR:
<ul>
<li>Docker</li>
<li>Python</li>
</ul>
</td>
</<tr>
<tr><td colspan="2">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe (r.escobedo@ulasalle.edu.pe)</li>
</ul>
</td>
</<tr>
</tdbody>
</table>


# OBJETIVOS TEMAS Y COMPETENCIAS

## OBJETIVOS

- Demostrar lo aprendido en el curso en cuanto a hilos y a virtualización de imagenes mediante docker.

## TEMAS
- Docker
- Hilos (threads)
- Python

# CONTENIDO DEL TRABAJO

## MARCO CONCEPTUAL

Trabajo hecho en python. Tiene dos partes:
- La primera es mostrar el proceso para subir el codigo y explicar este.
- La segunda es mostrar capturas de docker.

## CODIGO DE CLIENTE Y SERVIDOR
- Crearemos un repositorio local usando git init
    ```sh
    pwd
    	D:\LeonardoU\VIIsemestre\CDP\Parcial
    git init
    ```

- Crearemos un archivo Readme.md con contenido Markup
    ```sh
    echo "# Readme" > README.md
    ```

- Agregaremos este archivo al staging area usando git add .
    ```sh
    git status
    ```
    <pre>
    En la rama main

    No hay commits todavía

    Archivos sin seguimiento:
    (usa "git add <archivo>..." para incluirlo a lo que se será confirmado)
	README.md
    no hay nada agregado al commit pero hay archivos sin seguimiento presentes (usa "git add" para hacerles seguimiento)
    </pre>
    ```sh
    git add README.md
    git add cliente.py
    git add servidor.py
    ```

- Hacemos commit en nuestro repositorio local 
    ```sh
    git commit -m "Cliente servidor python"
    ```
- Asociamos el repositorio local con el repositorio remoto 
    ```sh
    git remote add origin https://github.com/ArcZLeo/Trapecio_docker.git
    ```

- Actualizamos el repositorio remoto de forma forzosa debido a la falta de permisos de mi maquina (NOTA: Esto no es recomendable. Lo que estaba antes se borrara)
    ```sh
    git push -f origin main
    ```

- Ahora podemos verificar en GitHub que nuestro repositorio se actualizó con el proyecto local

- Cliente: 

    <pre>
  	#Variables
	host = 'localhost'
	port = 8050
	#Se importa el módulo
	import socket

	#Creación de un objeto socket (lado cliente)
	obj = socket.socket()

	#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
	obj.connect((host, port))
	print("Conectado al servidor")

	#Creamos un bucle para retener la conexion
	while True:
	#Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
	    mens = input("Mensaje desde Cliente a Servidor >> ")
	    #Con el método send, enviamos el mensaje
	    obj.send(mens.encode('ascii'))
	    recibido = obj.recv(1024)
	    print(recibido)

	#Cerramos la instancia del objeto servidor
	obj.close()

	#Imprimimos la palabra Adios para cuando se cierre la conexion
	print("Conexión cerrada")

	#Prueba:-x**2/((x**4)+1),2,8
    </pre>
    
- Servidor: 

  <pre>
	#Se importa el módulo
	import socket

	from multiprocessing.pool import ThreadPool


	def ksum(f,a,b,k):
	  npanel = 2**(k-1)
	  H = (b-a)
	  sum = 0.0
	  nsum = 2**(k-2)
	  for j in range(nsum):
	    xj = (( 2*(j+1)-1 )*H)/npanel
	    sum = sum + f( a + xj )
	    aux = (H/npanel)*sum
	  return aux


	#En esta funcion trasnformamos el string que nos mande el cliente en una funcion para poder trabajarla.
	def createFunc(f):
	  with open("D:\LeonardoU\VIIsemestre\construccion\socket\Function.py",'w') as file:
	    file.write("def f(x):\n\treturn ("+f+")")

	  from Function import f
	  return f

	#Se crea una función para resolver el problema del trapesio, para esto se hace uso de hilos e iteraciones. En este caso en especifico se 
	#trabaja con ThreadPool el cual sirve para poder obtener el resultado de la funcióm ksum (en la cual se realiza el metodo del trapecio como tal)
	#y a su vez para limitar los hilos que creemos para no sobrecargar la maquina.
	def Traprecursive1(f,a,b): 

	  f=createFunc(f)
	  Iold = (f(a) + f(b))*(b - a)/2.0
	  iter=1
	  while (True):
	    pool = ThreadPool(processes=1)
	    t1= pool.apply_async(ksum, (f,a,b,iter+1))
	    Ik = 0.5*Iold + t1.get()

	    if (round(Iold,10)==round(Ik,10)):
	      return (iter)
	    else:
	      Iold=Ik
	      iter=iter+1


	def transform(lista):
	  texto=lista.split(",")
	  return Traprecursive1(texto[0],int(texto[1]),int(texto[2]))

	#instanciamos un objeto para trabajar con el socket
	ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#Puerto y servidor que debe escuchar
	ser.bind(("", 8050))

	#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
	ser.listen(1)

	#Instanciamos un objeto cli (socket cliente) para recibir datos
	cli, addr = ser.accept()

	while True:

	#Recibimos el mensaje, con el metodo recv recibimos datos. Por parametro la cantidad de bytes para recibir
	    recibido = cli.recv(1024)

	    #Si se reciben datos nos muestra la IP y el mensaje recibido
	    print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))
	    print(recibido)
	    msg2=transform(recibido.decode())

	    #Devolvemos el mensaje al cliente
	    msg_toSend=("Mensaje recibido, mejor cantidad de iteraciones: "+ str(msg2))
	    cli.send(msg_toSend.encode('ascii'))

	#Cerramos la instancia del socket cliente y servidor
	cli.close()
  </pre>

## CAPTURAS DOCKER

- Creamos la red que usaremos a futuro con nuestras imagens para poder realizar el enlace.
![image](https://user-images.githubusercontent.com/79063417/168498322-726a0961-3d4f-4c56-9fcd-b863b8a72eb7.png)

-Creamos las imagens en el docker.
 ```sh
 docker -it name
 ```
 
- Iniciamos las imagenes en la misma red.
- Corremos el servidor y el cliente.

![image](https://user-images.githubusercontent.com/79063417/168501033-19bb6798-cc8b-4dbe-934d-6536712e39ab.png)

![image](https://user-images.githubusercontent.com/79063417/168504561-efdb426d-56d7-4244-9172-1c95e7684de1.png)

- Usamos el comando start y attach para inicializar y dejar corriendo el server y el cliente


![image](https://user-images.githubusercontent.com/79063417/168508805-a9bc9afa-df7e-4c6d-befb-7676f40fb0a4.png)

- El cliente le manda al servidor los datos para hacer la función, luego el cliente los lee y le manda como respuesta al cliente el resultado.
![image](https://user-images.githubusercontent.com/79063417/168513656-4c420b77-fcd3-43c3-9b01-aae5c8d86ce0.png)




