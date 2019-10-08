print(" ")
print("Sistema de clasificación de suelos según norma VN-E4-84 de la Dirección de Vialidad Nacional de Argentina.")
print("El ingreso de datos debe ser realizado en porcentaje pero sin incluir el %.")
print("Como separador decimal debe usarse un punto")

#Primero defino la función de ingreso de datos. La idea es hacer una validación previo a la utilización de los valores.
def IngresoDatos():
  while True:
    try:
        Pasante_N10 =float(input("Ingrese porcentaje de suelo pasante por tamiz N°10: ")) 
        Pasante_N40 =float(input("Ingrese porcentaje de suelo pasante por tamiz N°40: "))
        Pasante_N200 =float(input("Ingrese porcentaje de suelo pasante por tamiz N°200: "))
        WL=float(input ("Ingrese el limite liquido: "))
        WP=float(input ("Ingrese el limite plastico: "))
    except ValueError:
        print("El dato es incorrecto")
        continue

    if Pasante_N40 > Pasante_N10:
        print("El suelo pasante no puede ser mayor a medida que la abertura es menor.")
        continue
    if Pasante_N200 > Pasante_N40:
        print("El suelo pasante no puede ser mayor a medida que la abertura es menor.")
        continue
    if WP > WL:
        print("El límite líquido no puede ser menor que el plástico")
        continue
    if Pasante_N200 <0 or Pasante_N40<0 or Pasante_N10<0 or WP<0 or WL<0:
        print("El porcentaje pasante no puede ser menor a cero.")
        continue
    else:
        print("Datos correctamente cargados")
        break
  return(Pasante_N10, Pasante_N40, Pasante_N200, WL, WP)

#Despues tengo la función clasificación, que basicamente son muchos if.
def Clasificacion (Pasante_N10,Pasante_N40,Pasante_N200,WL,IP):
  if(Pasante_N10<=50 and Pasante_N40<=30 and Pasante_N200<=15 and IP<=6):
    x="A1-a"
  elif(Pasante_N40<=50 and Pasante_N200<=25 and IP<=6):
    x="A1-b"
  elif(Pasante_N40>50 and Pasante_N200<=10 and IP<=0):
    x="A3"
  elif(Pasante_N200<=35 and WL<=40 and IP<=10):
    x="A2-4"
  elif(Pasante_N200<=35 and WL>40 and IP<=10):
    x="A2-5"
  elif(Pasante_N200<=35 and WL<=40 and IP>10):
    x="A2-6"
  elif(Pasante_N200<=35 and WL>40 and IP>10):
    x="A2-7"
  elif(Pasante_N200>35 and WL<=40 and IP<=10):
    x="A4"
  elif(Pasante_N200>35 and WL>40 and IP<=10):
    x="A5"
  elif(Pasante_N200>35 and WL<=40 and IP>10):
    x="A6"
  elif(Pasante_N200>35 and WL>40 and IP>10 and IP<=WL-30):
    x="A7-5"
  elif(Pasante_N200>35 and WL>40 and IP>10 and IP>WL-30):
    x="A7-6"

  if(x=="A1-a" or x=="A1-b"):
    y="Fragmentos de rocas, grava y arena"
  elif(x=="A3"):
    y="Arena Fina"
  elif(x=="A2-4" or x=="A2-5" or x=="A2-6" or x=="A2-7"):
    y="Gravas y arenas arcillosas limosas"
  elif(x=="A4" or x=="A5"):
    y="Suelos limosos"
  elif(x=="A6" or x=="A7-5"or x=="A7-6"):
    y="Suelos arcillosos"
  return (x,y)


i=0
while True:
  try:
    i+=1
    print(" ")
    print("Suelo "+str(i))    
    Datos=IngresoDatos()
    Pasante_N10=Datos[0]
    Pasante_N40=Datos[1]
    Pasante_N200=Datos[2]
    WL=Datos[3]
    WP=Datos[4]
    IP=WL-WP
    suelo=Clasificacion(Pasante_N10,Pasante_N40,Pasante_N200,WL,IP)
    
  
    print(" ")
    print("Pasante Tamiz N10: "+str(Pasante_N10)+"%")
    print("Pasante Tamiz N40: "+str(Pasante_N40)+"%")
    print("Pasante Tamiz N200: "+str(Pasante_N200)+"%")
    print("WL: "+str(WL))
    print("WP: "+str(WP))
    print("IP: "+str(IP))
    print("Tipo de suelo: " + str(suelo[0])+": "+str(suelo[1]))
    print(" ")
    q=str(input("¿Desea clasificar otro suelo? Ingrese \"Y\" para reiniciar y cualquier otro valor para finalizar: "))

    if (q=="Y" or q=="y"):
      continue
  except ValueError:
      print("El dato es incorrecto")
      continue
  else:
      print("Fin del programa")
      print(" ")
      print(" ")
      break

