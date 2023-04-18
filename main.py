import time
import datetime
from manejoAgentes import *
from generarPDF import *
from CreateRRD import *
from graphRRD import *
from manejoSNMP import *
import rrdtool

while(True):
    print('\t\t Sistema de administracion de Red')
    print('\t Practica 1 - Adquisicion de Informacion')
    print('\t Andres Vanegas Garcia\t 4CM14\t 2020630529\n\n')
    print('Elige una opcion: ')
    print('0) Lista de Agentes')
    print('1) Agregar Agente')
    print('2) Cambiar informacion de Agente')
    print('3) Eliminar agente')
    print('4) Generar reporte\n')
    opc = int(input('Opcion: '))

    if opc == 0:
        seleccionarAgente(0)
    else:
        if opc == 1:
            
            comunidad = input('Comunidad = ')
            version = int(input('Version = '))
            puerto = int(input('Puerto = '))
            ip = input('IP = ')
            agregarAgente(comunidad, version, puerto, ip)
            print('agente agregado')
        else:
            if opc == 2:
                seleccionarAgente(0)
                indice = int(input('Selecciona el agente a modificar, 0 para cancelar = '))
                agente = seleccionarAgente(indice)
                comunidad = input('Comunidad = ')
                version = input('Version = ')
                puerto = input('Puerto = ')
                ip = input('IP = ')

                print("seleccionaste = ",agente)

                if comunidad !='':
                    agente['comunidad'] = comunidad
                if version !='':
                    agente['version'] = int(version)
                if puerto !='':
                    agente['puerto'] = int(puerto)
                if ip !='':
                    agente['ip'] = ip
                
                modificarAgente(indice,agente)
            else:
                if opc == 3:
                    seleccionarAgente(0)
                    indice = int(input('Selecciona el agente a eliminar, 0 para cancelar = '))
                    eliminarAgente(indice)
                else:
                    if opc == 4:
                        seleccionarAgente(0)
                        inicio = input('Ingrese la hora de inicio: ')
                        final = input('Ingrese la hora de termino: ')
                        indice = int(input('Selecciona el agente : '))


                        fecha_time = datetime.datetime.strptime(inicio, "%Y-%m-%d %H:%M:%S")
                        epoch_time_inicio = int(time.mktime(fecha_time.timetuple()))
                        print(epoch_time_inicio)

                        fecha_time = datetime.datetime.strptime(final, "%Y-%m-%d %H:%M:%S")
                        epoch_time_final = int(time.mktime(fecha_time.timetuple()))
                        print(epoch_time_final)

                        agente = seleccionarAgente(indice)

                        contacto = extraerContacto(agente)
                        nombre = extraerNombre(agente)
                        sistema = extraerSO(agente)
                        ubicacion = extraerUbicacion(agente)
                        numInter = extraerNumInter(agente)
                        tabla = extraerTabla(agente)

                        print("Contacto: ",contacto)
                        print("Nombre Dispositivo: ",nombre)
                        print("Sistema Operativo: ",sistema)
                        print("Ubicacion: ",ubicacion)
                        print("Numero Interfa4ces: ",numInter)
                        print("Tabla: ",tabla)
                        print("tiempo inicio ")

                        nombreGrap = graficar(nombre,epoch_time_inicio,epoch_time_final)

                        export_to_pdf(tabla= tabla, contacto= contacto, nombre= nombre, numInterfaces= numInter, sistema= sistema, ubicacion= ubicacion,
                                      nombreGrap0=nombreGrap[0],
                                      nombreGrap1=nombreGrap[1],
                                      nombreGrap2=nombreGrap[2],
                                      nombreGrap3=nombreGrap[3],
                                      nombreGrap4=nombreGrap[4])
                    else:
                        print('Opcion incorrecta')