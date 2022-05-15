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
        <tr><td colspan="2"><span style="font-weight:bold;">Formato</span>: Primer trabajo en git</td></tr>        
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE GIT</span><br />
</div>

<table>
<theader>
<tr><th colspan="2">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>

<tr><td>TÍTULO DE LA PRÁCTICA:</td>Pimer practica git<td>Git - GitHub</td></tr>
<tr><td colspan="2">RECURSOS A UTILIZAR:
<ul>
<li></li>
<li></li>
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

- Aprender a manejar un sistema de control de versiones de manera colaborativa con varios
usuarios

## TEMAS
- Git
- GitHub

# CONTENIDO DEL TRABAJO

## MARCO CONCEPTUAL

- Instalar Git en el ordenador

	- GNU/Linux

	- MS Windows
		- Descargar Git-2.36.0-64-bit.exe desde https://git-scm.com/download/win

	- MacOS

- git init
    - Crea un nuevo proyecto local, se crean archivos en el directorio oculto .git
    ```sh
    git init
    ```

- git config
    - Establece variables de configuración. Por ejemplo para los commits se necesita los datos del desarrollador. Se puede especificar el editor y hasta el tiempo que deseas almacenar tus credenciales en la cache y otras cosas más
    ```sh
    git config --global user.name "ArcZero"
    git config --global user.email ldezac@ulasalle.edu.pe
    git config --list
    git config user.name
    git config --global core.editor "code --wait"
    git config --global credential.helper 'cache --timeout=3600'
    ```

- git status
    - Permite verificar el estado de los archivos
    ```sh
    git status
    ```
- git add
    - Añade archivos al staging area. El punto "." agrega todos
    ```sh
    git add HolaMundo.java
    git add .
    ```

- git commit
    - Sube los archivos al área de staging, en la máquina local. La opción -m permite escribir el mensaje en línea
    ```sh
    git commit -m "Probando el Hola Mundo"    
    ```

- git clone
    - Clona un repositorio remoto como un repositorio local, en el cual se puede hacer push
    ```sh
    git clone https://github.com/ArcZLeo/proyecto.git
    ```

- git remote
    - Persigue un repositorio remoto para hacer push.
    ```sh
    git remote add origin https://github.com/ArcZLeo/proyecto.git
    ```

- git push
    - Permite subir archivos al repositorio remoto
    ```sh
    git push -u origin main    
    ```

- git show
    - Muestra detalles del commit actual
    ```sh
    git show
    ```

-   git log
    - Permite ver un resumen de los commit realizados
    ```sh
    git log
    git log --pretty=oneline
    git log --graph --pretty=oneline --abbrev-commit --all
    git log --pretty=format:"%h - %an, %ar : %s"
    git log -p -2
    ```
    ![image](https://user-images.githubusercontent.com/79063417/166128248-733c7308-04f1-4b7f-8af1-d351cc758100.png)

    ```
    

## EJERCICIO/PROBLEMA RESUELTO 
Primer repositorio en GitHub


- Crearemos un repositorio local usando git init
    ```sh
    pwd
    /home/cumputadora/descargas/proyecto
    git init
    ```

- Crearemos un archivo Readme.md con contenido Markup
    ```sh
    echo "# Mi proyecto Git" > README.md
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
    ```

- Hacemos un primer commit en nuestro repositorio local 
    ```sh
    git commit -m "Mi primer proyecto en github"
    ```
- Asociamos el repositorio local con el repositorio remoto 
    ```sh
    git remote add origin https://github.com/ArcZLeo/proyecto.git
    ```

- Actualizamos el repositorio remoto
    ```sh
    git push -u origin main
    ```

- Ahora podemos verificar en GitHub que nuestro repositorio se actualizó con el proyecto local
    - ![Readme.md](Readme.md.png)

- Cree una clase python calculadora.py que funcione con las cuatro operaciones basicas, haga commit y súbalo al repositorio GitHub.
   
    <pre>
    n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Cambiar los números elegidos
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
    </pre>
    ```sh    
    python -version
    ```
    ```sh
    git add calculadora.py
    git commit -m "Primera parte"
    git push -u origin main
    ```
    ![image](https://user-images.githubusercontent.com/79063417/166128767-a3b4a9e2-3a11-4b5d-8367-34824cac553c.png)

