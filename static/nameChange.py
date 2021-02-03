import os
import re
import sys

if sys.platform == 'win32':
    os.system('cls')
elif sys.platform == 'linux':
    os.system('clear')

data = os.listdir(os.getcwd())
contador = 0
encontrador = []
ultimo_numero = []

for i in range(len(data)):
    if re.search("\.py$", data[i]):
        pass
    else:
        if re.search("^video+\w+\.webm$", data[i]) == None:
            # si hay un archivo con el mismo nombre entonces cuenta cuantos videos son y empezar desde el último
            # vamos a contar cuantos de estos hay:
            # guardo el indice
            if os.path.isdir(data[i]) == True:
                pass
            else:
                encontrador.append(i)
        elif re.search("^video+\w+\.webm$", data[i]):
            contador += 1
            ultimo_numero.append(int(re.findall("^video+\w+", data[i])[0][5:]))
for encontrado in encontrador:
    if len(ultimo_numero):
        contador = max(ultimo_numero)+1
        os.rename(data[encontrado], "video{}.webm".format(contador))
    else:
        os.rename(data[(i+1)], "video{}.webm".format((i+1)))
            
