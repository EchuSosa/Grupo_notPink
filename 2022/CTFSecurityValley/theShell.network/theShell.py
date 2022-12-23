#!/bin/bash
import subprocess
def proc():
    command="strings recurso/rev_shell.pcapng | grep { "
    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return result.stdout.read()
print("Buscando...")
resultado= proc()
resultado= str(resultado).split("'")
print("FLAG: "+str(resultado[1][:-2]))
