import sys
import rrdtool
import time

def graficar(nombre,inicio,final):
    nombresGraf = []
    nombresGraf.append(nombre+str(inicio)+"1"+".png")
    ret = rrdtool.graph(nombresGraf[0],
                        "--start", str(inicio),
                        "--end", str(final),
                        "--vertical-label=Bytes/s",
                        "--title="+"Paquetes multicast que \n ha enviado la interfaz",
                        "DEF:traficoEntrada="+nombre+".rrd:datoUno:AVERAGE",
                        "CDEF:escalaIn=traficoEntrada,8,*",
                        "LINE1:escalaIn#0000FF:" + "Paquetes Multicast")
    nombresGraf.append(nombre + str(inicio) + "2" + ".png")
    ret = rrdtool.graph(nombresGraf[1],
                        "--start", str(inicio),
                        "--end", str(final),
                        "--vertical-label=Bytes/s",
                        "--title=" + "Paquetes IP que los protocolos locales \n suministraron a IP en las solicitudes de transmisión",
                        "DEF:traficoEntrada=" + nombre + ".rrd:datoDos:AVERAGE",
                        "CDEF:escalaIn=traficoEntrada,8,*",
                        "LINE1:escalaIn#0000FF:" + "Paquetes IP")
    nombresGraf.append(nombre+str(inicio)+"3"+".png")
    ret = rrdtool.graph(nombresGraf[2],
                        "--start", str(inicio),
                        "--end", str(final),
                        "--vertical-label=Bytes/s",
                        "--title=" + "Mensajes ICMP que ha recibido el agente.",
                        "DEF:traficoEntrada=" + nombre + ".rrd:datoTres:AVERAGE",
                        "CDEF:escalaIn=traficoEntrada,8,*",
                        "LINE1:escalaIn#0000FF:" + "Mensajes ICMP")
    nombresGraf.append(nombre+str(inicio)+"4"+".png")
    ret = rrdtool.graph(nombresGraf[3],
                        "--start", str(inicio),
                        "--end", str(final),
                        "--vertical-label=Bytes/s",
                        "--title=" + "úmero de segmentos TCP transmitidos que \ncontienen uno o más octetos transmitidos previamente",
                        "DEF:traficoEntrada=" + nombre + ".rrd:datoCuatro:AVERAGE",
                        "CDEF:escalaIn=traficoEntrada,8,*",
                        "LINE1:escalaIn#0000FF:" + "Segmnetos retransmitidos")
    nombresGraf.append(nombre+str(inicio)+"5"+".png")
    ret = rrdtool.graph(nombresGraf[4],
                        "--start", str(inicio),
                        "--end", str(final),
                        "--vertical-label=Bytes/s",
                        "--title=" + "Datagramas enviados por el dispositivo.",
                        "DEF:traficoEntrada=" + nombre + ".rrd:datoCinco:AVERAGE",
                        "CDEF:escalaIn=traficoEntrada,8,*",
                        "LINE1:escalaIn#0000FF:" + "Datagramas envisados")
    return nombresGraf

