# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:48 2019

@author: reinaqu_2
"""
from picos import *

if __name__=='__main__':
    PICOS = [Pico("Mulhacén", 3479, "Granada"), 
             Pico("Torreón", 1648, "Cádiz"),
             Pico("Peña Santa", 2596, "León"), 
             Pico("Naranjo", 2519, "Asturias"),
             Pico("Alcazaba", 3371, "Granada"), 
             Pico("Veleta", 3396, "Granada"),
             Pico("Torrecilla", 1919, "Málaga"), 
             Pico("Llambrión", 2647, "León"),
             Pico("Teide", 3718, "Santa Cruz de Tenerife")]
             
    mostrar_picos1(PICOS)