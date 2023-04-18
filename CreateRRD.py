#!/usr/bin/env python
import rrdtool
def createDB(name):
    ret = rrdtool.create(name+".rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:datoUno:COUNTER:120:U:U",
                         "DS:datoDos:COUNTER:120:U:U",
                         "DS:datoTres:COUNTER:120:U:U",
                         "DS:datoCuatro:COUNTER:120:U:U",
                         "DS:datoCinco:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:5:5",
                         "RRA:AVERAGE:0.5:1:20")

    if ret:
        print (rrdtool.error())