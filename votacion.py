cantidad=0
vuelta=0
paneo=0
diferencia=0
voto=[]
comparacion= []
vuelta_entera=0
repeticion=1
guardar=0
descarte={0}
mayor=[]
descarte.remove(0)


#ingresamos la cantidad de votantes
cantidad=int (input("cuantas personas van a participar: "))
print("cantidad de votos: ", cantidad)
print("empezaran las votaciones")


#se va a repetir hasta que tengamos la misma cantidad de votos que de votantes
while (len(voto)!=cantidad):
   while (vuelta!=cantidad):
    print("")
    candidato=input("ingrese al votante: ")
    print("")
    print(vuelta)
    voto.append(candidato)
    #print(voto)
    print("votos: ", voto)
    vuelta+=1


#buscamos leer cada uno de los votos y ver cual se repite 
#Hago 2 vueltas, en la vuelta grande vamos moviendo el comparado y reiniciando el comparador y el numero de votos
while (vuelta_entera<len(voto)):
  vuelta=0
  diferencia=0
  repeticion=0
  #En la vuelta chica el comparado es un numero fijo y el comparador va sumandose uno y guardando la cantidad de veces que aparece el numero repetido
  while (vuelta<len(voto)):
    if (voto[paneo]==voto[diferencia]):
      repeticion+=1
    diferencia+=1
    vuelta+=1
  #Aca guardo los votos en una lista para facilitar la muestra de datos y en un set para recortar todos los que se repiten ya que solo necesitamos el mayor
  comparacion.append(repeticion) 
  descarte.add(repeticion)
  print("con paneo en: ", paneo, "= ",voto[paneo], " aparece: ", comparacion[paneo], " veces")
  paneo+=1
  vuelta_entera+=1
  print("vuelta entera: ", vuelta_entera)

#Pasamos el set devuelta a una lista solo para sacar el mayor con la funcion MAX
mayor=descarte
mayor=max(mayor)
print(comparacion)
print("la cantidad de veces mas votada es: ", mayor)

#Para mostrar quien es el ganador, guardo en donde estan ubicadas el voto mas grande para luego solo mostrar una de las ubicaciones 
if (mayor in comparacion):
  for a in range(0, len(voto), 1):
    if (mayor==comparacion[a]): 
      guardar=a
print(voto[guardar])

#en caso de empate terminaria ganando el que se voto ultimo
#no se si seria un error porque en la consigna dice se asume que no hay empates, pero creo que es solo para el ejemplo
#La manera que hice para comparar es poca  efectiva a mayor cantidad de votos.