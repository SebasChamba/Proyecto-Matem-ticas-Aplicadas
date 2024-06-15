
from scipy.integrate import quad
from djitellopy import Tello
import time

# Conectar con el dron Tello
tello = Tello()
tello.connect()

altura_en_cp = []
# Despegar

tello.takeoff()




# Lista de puntos para formar un cuadrado en el plano XY a una altura de 50 unidades sobre el plano XY
puntos = [(100,0, 100), (100,0 ,-100), (0,-100 ,100), (0, -100,-100 ),(-100,0,100), (-100,0 ,-100)]

altura1=tello.get_height()
altura_en_cp.append(altura1)

# Movimiento siguiendo el cuadrado
for punto in puntos:

    x, y, z = punto

    tello.go_xyz_speed(x, y, z, 30)

    altura = tello.get_height()

    print(altura)

    altura_en_cp.append(altura)

tello.go_xyz_speed(0, 200, 0, 30)

altura1=tello.get_height()
altura_en_cp.append(altura1)



# Aterrizar
tello.land()

# Imprimir las alturas
print("Alturas:", altura_en_cp)

