from manejoSNMP import extraerNombre
from CreateRRD import *
def agregarAgente(comunidad,version, puerto, ip):
    archivo = open('agentes.txt','a+')
    agente = {'comunidad': comunidad, 'version': version, 'puerto': puerto, 'ip': ip}
    print("llegue")
    nombre = extraerNombre(agente)
    try:
        base = open(nombre+".rrd")
        base.close()
    except FileNotFoundError:
        print("base de datos "+nombre+".rrd creada")
        createDB(nombre)
    archivo.write(comunidad + '$' + str(version) + '$' + str(puerto) + '$' + ip + '\n')
    archivo.close()

def seleccionarAgente(indice):
    strucAgentes = {'comunidad': '','version': 1, 'puerto': 0, 'ip':''}
    archivo = open('agentes.txt','rb+')

    cont = 1

    for renglon in archivo:
        agente = str(renglon).split('$')
        if len(agente) != 4 :
            print('Error en dividir agente')
        else:
            strucAgentes['comunidad'] = str(agente[0]).replace('b\'','')
            strucAgentes['version'] = int(agente[1])
            strucAgentes['puerto'] = int(agente[2])
            strucAgentes['ip'] = agente[3].replace('\\n\'','')
        #print(indice)
        #print(cont)
        if(cont == indice):
            return strucAgentes
        else:
            print(str(cont)+') ',end='')
            print(strucAgentes)
        cont+=1
    archivo.close()

def eliminarAgente(indice):

    archivo = open('agentes.txt','r+')
    contenido = archivo.readlines()
    archivo.close()

    if(indice == 0):
        print('Eliminar cancelado')
    else:
        if(indice < 0 or indice > len(contenido)):
            print('Indice no encontrado')
        else:
            contenido.pop(indice-1)
            print('Agente '+str(indice)+' eliminado')

    archivo = open('agentes.txt','w+')
    archivo.writelines(contenido)
    archivo.close()

def modificarAgente(indice,agente):
    eliminarAgente(indice)
    agregarAgente(agente['comunidad'],agente['version'], agente['puerto'], agente['ip'])
    print('Agente Modificado')

