#!/usr/bin/env python

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
  

def createFunc(f):
  with open("D:\LeonardoU\VIIsemestre\construccion\socket\Function.py",'w') as file:
    file.write("def f(x):\n\treturn ("+f+")")
    
  from Function import f
  return f

  
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