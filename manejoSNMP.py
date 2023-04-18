import time
from getSNMP import consultaSNMP
import re

def extraerSO(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.1.1.0')
    respuesta = re.search('(Linux .*)|(Windows .*)',respuesta).group()
    respuesta = respuesta.replace('Software: ','')
    return respuesta

def extraerNombre(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.1.5.0')
    respuesta = re.search('= .*',respuesta).group()
    respuesta = respuesta.replace('= ','')
    return respuesta

def extraerContacto(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.1.4.0')
    respuesta = re.search('sysContact.0 = .*',respuesta).group()
    respuesta = respuesta.replace('sysContact.0 = ','')
    respuesta = respuesta.replace('(Software: )|\(','')
    return respuesta

def extraerUbicacion(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.1.6.0')
    respuesta = re.search('sysLocation.0 = .*',respuesta).group()
    respuesta = respuesta.replace('sysLocation.0 = ','')
    return respuesta

def extraerNumInter(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.2.1.0')
    respuesta = re.search('= [0-9]*',respuesta).group()
    respuesta = respuesta.replace('= ','')

    return int(respuesta)

def extraerInterfaz(agente, numInter):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.2.2.1.2.'+str(numInter))
    if(re.search('Windows',extraerSO(agente))):
        respuesta = re.search('mib-2.2.2.1.2.'+str(numInter)+' = .*',respuesta)
        respuesta = respuesta.group()
        respuesta = respuesta.replace('mib-2.2.2.1.2.'+str(numInter)+' = 0x','')
        octet = ''
        for i in range(0, len(respuesta), 3):
            octet += respuesta[i:i+3]+' '

        octetos = respuesta.split()
        decimales = [int(octeto, 16) for octeto in octetos]

        # Convertir cada valor decimal en su caracter ASCII correspondiente
        ascii_chars = []
        for decimal in decimales:
            while decimal > 0:
                ascii_chars.append(chr(decimal % 256))
                decimal //= 256

        # Invertir la lista de caracteres ASCII y unirlos en un solo string
        ascii_string = (''.join(ascii_chars[::-1])).replace('\x00','')

        return ascii_string
    else:
        respuesta = re.search(' = .*',respuesta)
        respuesta = respuesta.group()
        respuesta = respuesta.replace(' = ','')
        return respuesta


def extraerTabla(agente):
    numInter = extraerNumInter(agente)
    listaInterfaces = []
    tabla = []
    if numInter > 5:
        numInter = 5
    for i in range(1,numInter+1):
        listaInterfaces.append(extraerInterfaz(agente,i))
        listaInterfaces.append(extraerEstado(agente,i))
        tabla.append(listaInterfaces)
        listaInterfaces = []
    return tabla

def extraerEstado(agente,numInter):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.2.2.1.7.'+str(numInter))
    respuesta = re.search('= .*',respuesta).group()
    respuesta = int(respuesta.replace('= ',''))
    if respuesta == 1:
        respuesta = 'UP'
    if respuesta == 2:
        respuesta = 'DOWN'
    if respuesta == 3:
        respuesta = 'testing'
    return respuesta

#Paquetes multicast que ha enviado la interfaz de la interfaz de red de un agente
def ifInNUcastPkts(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.2.2.1.12.2')
    respuesta = re.search('= .*',respuesta).group()
    respuesta = respuesta.replace('= ','')
    return respuesta

#Paquetes IP que los protocolos locales (incluyendo ICMP) suministraron a IP en las solicitudes de transmisión.
def ipInDelivers(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.4.9.0')
    respuesta = re.search('= .*',respuesta).group()
    respuesta = respuesta.replace('= ','')
    return respuesta

#Mensajes ICMP que ha recibido el agente.
def icmpInMsgs(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.5.1.0')
    respuesta = re.search('= .*',respuesta).group()
    respuesta = respuesta.replace('= ','')
    return respuesta

#Segmentos retransmitidos; es decir, el número de segmentos TCP transmitidos que contienen uno o más octetos transmitidos previamente
def tcpRetransSegs(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.6.12.0')
    respuesta = re.search('= .*',respuesta).group()
    respuesta = respuesta.replace('= ','')
    return respuesta

#Datagramas enviados por el dispositivo.
def udpOutDatagrams(agente):
    respuesta = consultaSNMP(agente['comunidad'],agente['ip'], '1.3.6.1.2.1.7.4.0')
    respuesta = re.search('= .*',respuesta).group()
    respuesta = respuesta.replace('= ','')
    return respuesta

'''agente = {'comunidad': 'comunidadSNMP', 'version': 1, 'puerto': 1244, 'ip': 'localhost'}
print(ifInNUcastPkts(agente))
print(ipInDelivers(agente))
print(icmpInMsgs(agente))
print(tcpRetransSegs(agente))
print(udpOutDatagrams(agente))'''
