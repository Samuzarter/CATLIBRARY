#Consumir libreria
from decouple import config
from catlibrary import cats, cat_say,cats_count

print("¡Bienvenido al test de Catlibrary!")


def menu():
    print("1. Obtener ID y TAGS de gatos. \n"
          +"2. Obtener la imagen de un gato con la frase que quieras. \n"
          +"3. Obtener la cantidad de gatos que hay en la API CATAAS. \n"
          +"4. Imprimir variables de entorno. \n"
          +"5. Salir.")

while True:
    menu()
    opcion= input("¿Qué deseas realizar?: ")
    if opcion == "1":
        print(cats())
        print("\n")
    elif opcion == "2":
        print(cat_say(input("Ingresa la frase que quieres en la imagen: \n")))
        print("\n")
    elif opcion == "3":
        print(cats_count())
        print("\n")
    elif opcion == "4":
        print(config('URL_API'))
        print(config('URL_CAT'))
        print("\n")
    elif opcion == "5":
        break
    else:
        print("Opcion no valida, porfavor ingrese una opcion valida. \n")
print("Hasta luego!")
