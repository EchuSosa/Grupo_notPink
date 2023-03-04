#!/bin/bash
import subprocess
import sys

def proc():
    file=sys.argv[1]
    dic=sys.argv[2]
    diccionario= open(dic,"r")

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
print("FLAG: "+resultado[1])

