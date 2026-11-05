# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:50:07 2019

@author: reinaqu_2
"""

from collections import namedtuple
import statistics


Rio = namedtuple("Rio", "nombre longitud continente")

###############Recorridos
def mostrar_rios1(rios):
    '''
    Ejemplo de recorrido con for usando una tupla.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    Muestra por consola una lista de tuplas de forma que cada tupla se muestra
    en una linea distinta.
    '''
    for rio in rios:
        print(rio)
        
def mostrar_rios2(rios):
    '''
    Ejemplo de recorrido con for usando una variable para cada campo de la tupla.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    Muestra por consola una lista de tuplas de forma que cada tupla se muestra
    en una linea con el formato Rio {nombre del rio} ({continente del rio}) . 
    Longitud: {longitud del rio} km.
    '''
    for nombre, longitud, continente in rios:
          print(f"Río {nombre}({continente}). Longitud: {longitud} kms")
          
def mostrar_rios3(rios):
    '''
    Ejemplo de recorrido con for usando una variable para cada campo de la tupla 
    y un guión bajo en lugar de una variable en los campos no usados.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    Muestra por consola una lista de tuplas de forma que cada tupla se muestra
    en una linea con el formato Rio: El río {nombre} tiene una longitud de {longitud} kms.
    '''
    for nombre, longitud, _ in rios:
          print(f"El río {nombre} tiene una longitud de {longitud} kms" )
      

def mostrar_rios4(rios):
    '''
    Ejemplo de recorrido con for usando una tupla con nombre.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    Muestra por consola una lista de tuplas de forma que cada tupla se muestra
    en una linea con el formato Rio: El río {nombre} tiene una longitud de {longitud} kms.
    '''
    for rio in rios:
          print(f"El río {rio.nombre} tiene una longitud de {rio.longitud} kms")
        
############### Filtrado
def filtra_rios_de_continente(rios, continente):
    '''
    Ejemplo de recorrido con filtrado (for + if).
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @param continente: Nombre del continente del que queremos obtener los ríos 
    @type contienente: str
    @return: Una lista de tuplas de tipo Rio con los ríos del continente que se pasa
    como parámetro
    @rtype: list[Rio]
    '''
    res = [rio for rio in rios if rio.continente == continente]
    return res 

############### Transformación/selección
def selecciona_nombre_longitud(rios):
    '''
    Ejemplo de selección.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista de tuplas de con el nombre del río y la longitud de los ríos
    @rtype: list[tuple[str, int]]
    '''
    res= [(r.nombre, r.longitud) for r in rios] 
    return res

def selecciona_nombre_longitud_miles_km(rios):
    '''
    Ejemplo de selección con transformación.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista de tuplas de con el nombre del ríoy la longitud de los ríos en kilómetros
    @rtype: list[tuple[str, float]]
    '''
    res= [(r.nombre, r.longitud/1000) for r in rios] 
    return res

def selecciona_nombre(rios):
    '''
    Ejemplo de selección.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con los nombres de los ríos
    @rtype: list[str]
    '''   
    res= [r.nombre for r in rios] 
    return res

############### Filtrado y transformación/seleccion
def selecciona_nombre_rios_de_continente(rios, continente):
    '''
    Ejemplo de selección con filtrado.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con el nombre de los ríos que están en el continente dado como
    parámetro 
    @rtype: list[str]
    '''
    res = [rio.nombre for rio in rios if rio.continente == continente]
    return res   

############### Eliminación duplicados
def selecciona_continentes_con_duplicados(rios):
    '''
    Ejemplo de selección.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con el nombre de los ríos
    @rtype: list[str]
    '''
    lista = [rio.continente for rio in rios]
    return lista

def selecciona_continentes_sin_duplicados(rios):
    '''
    Ejemplo de selección sin duplicados.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con el nombre de los ríos sin duplicados
    @rtype: set[str]
    '''
    conjunto =  {rio.continente for rio in rios}
    return conjunto

################### Ordenación, máximo y mínimo
def selecciona_continentes_sin_duplicados_ordenado_1(rios):
    '''
    Ejemplo de selección sin duplicados con ordenación.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con el nombre de los ríos sin duplicados y ordenados alfabéticamente
    @rtype: list[str]
    '''
    conjunto =  {rio.continente for rio in rios}
    lista = list(conjunto)
    lista.sort()
    return lista

def selecciona_continentes_sin_duplicados_ordenado_2(rios):
    '''    
    Ejemplo de selección sin duplicados con ordenación.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con el nombre de los ríos sin duplicados y ordenados alfabéticamente
    @rtype: list[str]
    '''
    conjunto =  {rio.continente for rio in rios}
    lista = sorted(conjunto)
    return lista

def selecciona_longitudes_ordenadas_1(rios):
    '''    
    Ejemplo de selección con ordenación.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con las longitudes de los ríos ordenadas de menor a mayor longitud
    @rtype: list[int]
    '''
    lista = [rio.longitud for rio in rios]
    lista.sort()
    return lista

def selecciona_longitudes_ordenadas_2(rios):
    '''    
    Ejemplo de selección con ordenación.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con las longitudes de los ríos ordenadas de menor a mayor longitud
    @rtype: list[int]
    '''
    return sorted(rio.longitud for rio in rios)
    
def selecciona_longitudes_ordenadas_inv_1(rios):
    '''    
    Ejemplo de selección con ordenación inversa.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con las longitudes de los ríos ordenadas de mayor a menor longitud
    @rtype: list[int]
    '''    
    lista = [rio.longitud for rio in rios]
    lista.sort(reverse=True)
    return lista

def selecciona_longitudes_ordenadas_inv_2(rios):
    '''    
    Ejemplo de selección con ordenación inversa.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Una lista con las longitudes de los ríos ordenadas de mayor a menor longitud
    @rtype: list[int]
    '''    
    lista = [rio.longitud for rio in rios]
    return sorted(lista, reverse=True)

def longitud_max(rios):
    '''    
    Ejemplo de cálculo de máximo
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: La longitud del río con mayor longitud
    @rtype: int
    '''    
    lista = [rio.longitud for rio in rios]
    return max(lista)

def selecciona_n_longitudes_mayores(rios, n=3):
    '''    
    Ejemplo de selección de n mejores.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: La longitud del río con mayor longitud
    @rtype: list[int]
    '''    
    lista = selecciona_longitudes_ordenadas_inv_1(rios)
    if (n<=len(lista)):
        lista = lista[:n]
    return lista
        
####################Ordenación, máximo y mínimo con listas de tuplas
def ordenar_rios_1(rios):
    '''    
    Ejemplo de ordenación de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por el nombre del río
    @rtype: list[Rio]
    '''    
    rios.sort()
    return rios

def ordenar_rios_2(rios):
    '''    
    Ejemplo de ordenación de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por el nombre del río
    @rtype: list[Rio]
    '''    
    return sorted(rios)

def ordenar_rios_inv_1(rios):
    '''    
    Ejemplo de ordenación inversa de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por el nombre del río
    @rtype: list[Rio]
    '''    
    rios.sort(reverse=True)
    return rios

def ordenar_rios_inv_2(rios):
    '''    
    Ejemplo de ordenación inversa de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por el nombre del río
    @rtype: list[Rio]
    '''    

    return sorted(rios, reverse=True)
    
def ordenar_rios_por_longitud_1(rios):
    '''    
    Ejemplo de ordenación de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por la longitud de los ríos
    @rtype: list[Rio]
    '''    
    rios.sort(key=lambda r:r.longitud)
    return rios

def ordenar_rios_por_longitud_2(rios):
    '''    
    Ejemplo de ordenación de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por la longitud de los ríos
    @rtype: list[Rio]
    '''    
    return sorted(rios, key=lambda r:r.longitud)

def ordenar_rios_por_longitud_inv_1(rios):
    '''    
    Ejemplo de ordenación de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por la longitud de los ríos en 
    orden inverso
    @rtype: list[Rio]
    '''        
    rios.sort(key=lambda r:r.longitud, reverse=True)
    return rios

def ordenar_rios_por_longitud_inv_2(rios):
    '''    
    Ejemplo de ordenación de listas de tuplas.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: Lista de tuplas de tipo Rio ordenadas por la longitud de los ríos en 
    orden inverso
    @rtype: list[Rio]
    '''        
    return sorted(rios, key=lambda r:r.longitud, reverse=True )

####################Otras operaciones
def media_longitudes_rios_de_continente(rios, continente):
    '''    
    Ejemplo de cálculo de media con bucle.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: La longitud media de los ríos. Si la longitud no se puede calcular 
    devuelve None
    @rtype: float | None
    '''        
    longitudes = [rio.longitud for rio in rios if rio.continente == continente]    
    media = None
    if len(longitudes)>0:
        media = sum(longitudes)/len(longitudes)
    return media

def media_longitudes_rios_de_continente_2(rios, continente):
    '''    
    Ejemplo de cálculo de media con bucle.
    @param rios: Lista de tuplas de tipo Rio
    @type rios: list[Rio]
    @return: La longitud media de los ríos. Si la longitud no se puede calcular 
    se eleva la excepción StatisticsError
    @rtype: float | None
    '''        
    return statistics.mean (rio.longitud for rio in rios if rio.continente == continente)    
    



