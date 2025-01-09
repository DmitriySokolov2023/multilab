#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor,ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

# Инициализация EV3
ev3 = EV3Brick()

# Инициализация моторов
left_motor = Motor(Port.A)  # Левый мотор
right_motor = Motor(Port.B)  # Правый мотор

# Инициализация ультразвукового сенсора
ultrasonic_sensor = UltrasonicSensor(Port.S1)
ultrasonic_sensor1 = UltrasonicSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)
color_sensor2 = ColorSensor(Port.S4)


# Функция для движения вперед
def move_forward(speed=300):
    left_motor.run(speed)
    right_motor.run(speed)

# Функция остановки робота
def stop_robot():
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

# Функция для поворота направо
def turn_right(speed=800, time_ms=500):
    left_motor.run(speed)
    right_motor.run(-speed)
    wait(time_ms)
    stop_robot()

# Функция для поворота налево
def turn_left(speed=100, time_ms=100):
    left_motor.run(-speed)
    right_motor.run(speed)
    wait(time_ms)
    stop_robot()

# Основной цикл программы
try:
    while True:
        # Получаем расстояние до препятствия
        color = 0

        distance = ultrasonic_sensor.distance()
        distance2 = ultrasonic_sensor1.distance()

        if(color_sensor.color() == Color.WHITE or color_sensor2.color() == Color.WHITE):
            color = 1
        else:
          0

    
        # Если расстояние больше 200 мм (20 см), продолжаем движение вперед
        if distance > 200 and distance2 > 200 and color < 1:
            move_forward()
            ev3.light.on(Color.GREEN) # Зелёные индикаторы, когда робот движется
        else:
            stop_robot()
            ev3.light.on(Color.YELLOW)
            wait(1000) 
            turn_right()
        wait(100)

except KeyboardInterrupt:
    stop_robot()
    ev3.light.off()