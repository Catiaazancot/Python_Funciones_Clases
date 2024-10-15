'''
# Ejercicio 1. Función contar_caracteres :
# Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
  contador = 0
  for cad in cadena:
    contador += 1
  return contador
print(contar_caracteres("ordenador"))

# Ejercicio 2. Función calcular_promedio :
# Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(lista): 
  contador = 0
  for i in lista:
    contador += i
  promedio = contador / len(lista)
  return promedio
lista = [2, 4, 6, 8 ]
print(calcular_promedio(lista))

# Ejercicio 3. Función encontrar_duplicado :
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def encontrar_duplicado(lista):
  elementos_almacenados = set()
  for elemento in lista:
    if elemento in elementos_almacenados:
      return elemento
    else:
      elementos_almacenados.add(elemento)
  return print("No hay elementos duplicados")
lista = [3, 1, 4, 2, 5, 1, 6, 3]
primer_duplicado = encontrar_duplicado(lista)
print(primer_duplicado)

# Ejercicio 4. Función enmascarado_datos :
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro

def enmascarado_datos(texto):
  texto = str(texto)
  if len(texto) <= 4:
    return texto
  else:
    return '#' * (len(texto) - 4) + texto[-4:]
variable = 457382938
enmascar_texto = enmascarado_datos(variable)
print(enmascar_texto)

# Ejercicio 5. Función es_anagrama :
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def es_anagrama(palabra1, palabra2):
  if len(palabra1) != len(palabra2):
    return False
  return sorted(palabra1) == sorted(palabra2)
palabras = es_anagrama("roma", "amor")
print(palabras)

# Ejercicio 6. Función buscar_nombre :
# Crea una función que solicite al usuario ingresar una lista de nombres y luego
# solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se
# imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza
# una excepción.
# Caso de uso:
# Incorpora los siguientes nombres a la lista y comprueba que la función
# funciona correctamente: "Jaime", "Silvia" y "Ana

def buscar_nombre():
  ingresar_lista = input("Introduce una lista de nombres: ")
  nombre_buscado = input("Ingresa el nombre que buscas: ")
  if nombre_buscado in ingresar_lista:
    print(f"El nombre {nombre_buscado} ha sido encontrado en la lista proporcionada")
  else:
    print(f"el nombre {nombre_buscado} no se ha encontrado en la lista proporcionada")

#print(buscar_nombre())

 # Ejercicio 8. Función encontrar_puesto_empleado
def encontrar_puesto_empleado(nombre_empleado, lista_empleados):
   for empleado in lista_empleados:
      nombre_completo = f"{empleado['nombre']} {empleado['apellido']}"             #duda
      if nombre_completo == nombre_empleado:
        return empleado['puesto']
   return (f" {nombre_completo} no trabaja aqui")
     
     
nombre_empleado = 'Mabel García'
lista_empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]
print(encontrar_puesto_empleado(nombre_empleado, lista_empleados))

#Ejercicio 9. Función cubo_numero usando lambdas:

cubo = lambda numero: numero ** 3
numero = 5
print(cubo(numero))

# Ejercicio 10. Función resto_division usando lambdas:

resto_division = lambda a,b : a % b
print(resto_division(50,25))

# Ejercicio 11. Función numeros_pares usando lambdas y filter :

numeros_pares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))
numeros = [24, 56, 2.3, 19, -1, 0]
pares = numeros_pares(numeros)
print(f"Números pares: {pares}")

# Ejercicio 12. Función numeros_suma usando lambdas y map :

numeros_suma = lambda lista: list(map(lambda lista: lista + 3, lista))
lista = [24, 56, 2.3, 19, -1, 0]
print(numeros_suma(lista))

#Ejercicio 13. Función sumar_listas usando lambdas:

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

lista1 = [1, 4, 5, 6 , 7 , 7] 
lista2 = [3, 11, 34, 56]
print(sumar_listas(lista1,lista2))

#Ejercicio 14. No te vayas por las ramas :
class arbol:
  def __init__(self):
    self.tronco = 1
    self.ramas = []
    
  def crecer_tronco(self):
    self.tronco += 1
  
  def nueva_rama(self):
    self.ramas.append(1)
  
  def crecer_ramas(self):
    self.ramas = [rama + 1 for rama in self.ramas]
  
  def quitar_ramas(self, posicion):
    self.ramas.pop(posicion)
  
  def info_arbol(self):
    info = {
      "longitud tronco": self.tronco,
      "numero ramas" : len(self.ramas),
      "longitud ramas" : self.ramas
    }
    return info

arbol.arbol()
arbol.crecer_tronco() 
arbol.nueva_rama()  
arbol.crecer_ramas() 
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)


#Ejercicio 15. Clase UsuarioBanco
class UsuarioBanco:
  def __init__(self, nombre, saldo, cuenta_corriente):
    self.nombre = nombre
    self.saldo = saldo
    self.cuenta_corriente = cuenta_corriente
    
  def retirar_dinero(self, cantidad):
    if self.saldo >= cantidad:
      self.saldo -= cantidad
    else:
      raise ValueError(f"no se puede retirar {cantidad}")
    
  def transferir_dinero(self, otro_usuario, cantidad):
    try:
      otro_usuario.retirar_dinero(cantidad)
      self.saldo += cantidad
    except:
      raise ValueError("No se pudo realizar la transferencia")

  def agregar_dinero(self, cantidad):
    self.saldo += cantidad 

Alicia = UsuarioBanco('Alicia', 100, True)
Bob = UsuarioBanco('Bob', 50, True)
Alicia.agregar_dinero(20)
Bob.transferir_dinero(Alicia,80)
Alicia.retirar_dinero(50)
'''
#Ejercicio 16. Función procesar_texto :
def contar_palabras(texto):
  texto = texto.lower()
  palabras = texto.split()
  contador = {}
  for palabra in palabras:
    if palabra in contador:
      contador[palabra] += 1
    else:
      contador[palabra] = 1
  return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
  if palabra_original in texto:
    palabra_original = palabra_nueva
    return texto 

def eliminar_palabra(texto, palabra_eliminada):
 nuevo_texto = [palabra for palabra in texto if palabra != palabra_eliminada]
 return nuevo_texto
  
def procesar_texto(texto, opcion, *args):
  if opcion == "contar":
    return contar_palabras(texto)
  elif opcion == "reemplazar":
    palabra_original, palabra_nueva = args
    return reemplazar_palabras(texto, palabra_original, palabra_nueva)
  elif opcion == "eliminar":
    palabra_eliminada = args
    return eliminar_palabra(texto, palabra_eliminada)
  
texto1 = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
contar = procesar_texto(texto1, 'contar')
reemplazar = procesar_texto(texto1, 'reemplazar', 'texto', 'relato')
eliminar = procesar_texto(texto1, 'eliminar', 'ejemplo')

