# Función que recibe dos números y me devuelve la totalidad del mismo

def suma(num1,num2):
    
    resultado = (num1+num2)
    
    return print(resultado)



# Función que toma una lista y suma sus elementos

def suma_lista(lista):
    """
    Función suma_lista toma una lista y le suma los valores
    variables:
        lista: lista
    """
    sumatoria = 0
    for i in lista:
        sumatoria = sumatoria + i
    return print(sumatoria)


#Función que recibe tres números y me devuelve el máximo 

def máximo_una(lista):
    """ 
    Encontrar el valor mayor de una lista de números
    """
    máximo = lista[0]
    for i in lista:
        if i > máximo:
            máximo = i
        
    return print(máximo)


# Función que recibe dos listas de números y devuelve una lista con los máximos

def máximo(lista1, lista2):

    """
    Encontrar el máximo de las dos listas
    """
    
    máximo_uno = lista1[0]
    máximo_dos = lista2[0]

    for i in lista1:
        if i > máximo_uno:
            máximo_uno = i

    
    for x in lista2:
        if x > máximo_dos:
            máximo_dos = x
    
    return print(máximo_uno,máximo_dos)



if __name__=="__main__":

    num1 = 10
    num2 = 20
    print(num1+num2)
    
    
    
    lista_prueba = [1,100,3]
    suma_lista(lista_prueba)

    
    máximo_una(lista_prueba)

   
    lista1 = [1,2,3]
    lista2 = [4,5,6]
    máximo(lista1,lista2)
    















