#!/bin/bash
import subprocess
import sys


dic_vacio=False

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
    vacio=0
    lines=diccionario.readlines()
    
    command="strings " + file + " | grep '"
    for line in lines:
        cant=cant+1
        if (line != "\n"):
            command+= line
            if (cant<len(lines)):
                command+=  "\|"
        else:
            vacio=vacio+1
    command=command.replace("\n","")
    fin=command[-2:]
    if (fin=="\|"):
        command=command[:-2]

    command+="'"


    if (vacio==len(lines)):
        global dic_vacio
        dic_vacio=True


    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return result.stdout.read()

print("Buscando...")
resultado= proc()
resultado= str(resultado).split("'")
if (dic_vacio==True):
    print("Contenido del diccionario inválido")
else:
    try:
        if (str(resultado[1][:-2])==""):
            print("No se encontró la flag")
        else:
            print("FLAG: "+str(resultado[1][:-2]))
    except: 
        print("No se encontró la flag")
        sys.exit()

