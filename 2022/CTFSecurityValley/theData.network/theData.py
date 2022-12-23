#!/bin/bash
import subprocess


def proc():
    command = "tshark -Q -r recurso/the_data.pcapng --export-objects 'http,recurso';imgclip -c recurso/flag.png -p;xdg-open recurso/flag.png"
    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return result.stdout.read()


print("Buscando...")
resultado = proc()
resultado = str(resultado).replace('F', ':').split(':')
print("FLAG APROXIMADA: "+str(resultado[2][2:-4]))
