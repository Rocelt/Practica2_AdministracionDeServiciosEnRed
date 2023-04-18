import time
import datetime

'''tiempo_actual0 = time.localtime()
tiempo_actual = time.mktime(tiempo_actual0)
print("tiempo actual con time"+str(time.time()))
print(tiempo_actual0)
print(tiempo_actual)'''
fecha = "2023-04-18 5:30:00"
fecha_time = datetime.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
epoch_time = int(time.mktime(fecha_time.timetuple()))

print(epoch_time)