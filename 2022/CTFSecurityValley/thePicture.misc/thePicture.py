#!/bin/bash
import subprocess


def proc():
    command = "zsteg -c 'rgb' recurso/challenge.png"
    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return result.stdout.read()


print("Buscando...")
resultado = proc()
resultado = str(resultado).split('"')
print("FLAG: "+resultado[1])
