#!/bin/bash
import subprocess
import sys

def proc():
    file=sys.argv[1]
    dic=sys.argv[2]
    diccionario= open(dic,"r")

    cant=0
    lines=diccionario.readlines()

    command="strings " + file + " | grep '"
    for line in lines:
        cant=cant+1
        if (line != "\n"):
            command+= line
            if (cant<len(lines)):
                command+=  "\|"
            
    command=command.replace("\n","")
    fin=command[-2:]
    if (fin=="\|"):
        command=command[:-2]

    command+="'"
    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return result.stdout.read()
print("Buscando...")
resultado= proc()
resultado= str(resultado).split("'")
print("FLAG: "+str(resultado[1][:-2]))
