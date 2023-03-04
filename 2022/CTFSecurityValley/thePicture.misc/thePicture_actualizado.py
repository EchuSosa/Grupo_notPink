#!/bin/bash
import subprocess
import sys

def proc():
    try:
        file=sys.argv[1]
    except:
        print("Ingrese la ruta de la imagen como primer parámetro ")
        sys.exit()
    try:
        dic=sys.argv[2]
    except:
        print("Ingrese la ruta al diccionario como segundo parámetro")
        sys.exit()
    try:
        diccionario= open(dic,"r")
    except:
        print("Ingrese la ruta a un diccionario válido")
        sys.exit()

    cant=0
    lines=diccionario.readlines()
    command="zsteg -c 'rgb' " + file + " | grep '"
    for line in lines:
        command+= line
        cant=cant+1
        if (cant<len(lines)):
            command+= "\|"
    command+="'"
    command=command.replace("\n","")

    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return result.stdout.read()

print("Buscando...")
resultado= proc()
resultado= str(resultado).split('"')
try:
    print("FLAG: "+resultado[1])
except: 
    print("No se encontró la flag")
    sys.exit()

