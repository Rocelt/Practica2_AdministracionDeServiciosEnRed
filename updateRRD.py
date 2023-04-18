import time
import rrdtool
from manejoSNMP import *
from manejoAgentes import *
def actualizarBase():
    strucAgentes = {'comunidad': '', 'version': 1, 'puerto': 0, 'ip': ''}
    while 1:
        archivo = open('agentes.txt', 'r+')
        contenido = archivo.readlines()
        archivo.close()
        for i in range(0,len(contenido)):
            agente = str(contenido[i]).split('$')
            if len(agente) != 4:
                print('Error en dividir agente')
                return 1
            else:
                strucAgentes['comunidad'] = str(agente[0]).replace('b\'', '')
                strucAgentes['version'] = int(agente[1])
                strucAgentes['puerto'] = int(agente[2])
                strucAgentes['ip'] = agente[3].replace('\n', '')
            valor = "N:" + ifInNUcastPkts(strucAgentes) + ":" + ipInDelivers(strucAgentes) + ":" + icmpInMsgs(strucAgentes) + ":" + tcpRetransSegs(strucAgentes) + ":" + udpOutDatagrams(strucAgentes)
            nombre = extraerNombre(strucAgentes)
            print("Agente "+nombre+valor)
            rrdtool.update(nombre+'.rrd', valor)
            rrdtool.dump(nombre+'.rrd', nombre+'.xml')
        time.sleep(1)
    if ret:
        print (rrdtool.error())
        time.sleep(300)

actualizarBase()