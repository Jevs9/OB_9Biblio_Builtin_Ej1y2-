listaPaises = input("Ingrese lista de paises, separados por comas: ")

#Inicialización del set o conjunto

set_paises = set()
for pais in listaPaises.split(","):
    #Añado los elementos de mi lista, quito las espacios y capitalizo
    set_paises.add(pais.strip().capitalize())

print("lista de paises ordenada".center(50, "-"))
print(sorted(set_paises))
