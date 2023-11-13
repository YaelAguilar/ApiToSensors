import pika
import random
import time

def simular_MAX30102():
    saturacion_oxigeno = round(random.uniform(95.0, 100.0), 2)  # Simulación de la saturación de oxígeno
    return saturacion_oxigeno

def simular_MLX90614():
    temp_objeto = round(random.uniform(30.0, 40.0), 2)  # Simulación para MLX90614
    return temp_objeto

def simular_PulseSensor():
    frecuencia_cardiaca = random.randint(60, 100)  # Simulación para Pulse Sensor
    return frecuencia_cardiaca

def simular_ADXL345():
    lectura_x = round(random.uniform(-2.0, 2.0), 2)
    lectura_y = round(random.uniform(-2.0, 2.0), 2)
    lectura_z = round(random.uniform(-2.0, 2.0), 2)
    return lectura_x, lectura_y, lectura_z

def enviar_lecturas():
    credentials = pika.PlainCredentials('zenAdmin', 'pulsepasswrd_')  # Reemplaza con tus credenciales reales
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))

    try: 
        channel = connection.channel()

        channel.exchange_declare(exchange='MAX30102', exchange_type='fanout', durable=True)
        channel.exchange_declare(exchange='MLX90614', exchange_type='fanout', durable=True)
        channel.exchange_declare(exchange='PulseSensor', exchange_type='fanout', durable=True)
        channel.exchange_declare(exchange='ADXL345', exchange_type='direct', durable=True)

        while True:
            lectura_max30102 = simular_MAX30102()
            lectura_mlx90614 = simular_MLX90614()
            lectura_pulse = simular_PulseSensor()
            lectura_adxl = simular_ADXL345()

            channel.basic_publish(exchange='MAX30102', routing_key='', body=str(lectura_max30102))
            channel.basic_publish(exchange='MLX90614', routing_key='', body=str(lectura_mlx90614))
            channel.basic_publish(exchange='PulseSensor', routing_key='', body=str(lectura_pulse))
            channel.basic_publish(exchange='ADXL345', routing_key='x', body=str(lectura_adxl[0]))
            channel.basic_publish(exchange='ADXL345', routing_key='y', body=str(lectura_adxl[1]))
            channel.basic_publish(exchange='ADXL345', routing_key='z', body=str(lectura_adxl[2]))

            print(f"Enviado a MAX30102: Saturación de oxígeno: {lectura_max30102}%")
            print(f"Enviado a MLX90614: Temperatura corporal: {lectura_mlx90614}°C")
            print(f"Enviado a PulseSensor: Frecuencia cardiaca: {lectura_pulse} bpm")
            print(f"Enviado a ADXL345: Lectura en el eje X: {lectura_adxl[0]}")
            print(f"Enviado a ADXL345: Lectura en el eje Y: {lectura_adxl[1]}")
            print(f"Enviado a ADXL345: Lectura en el eje Z: {lectura_adxl[2]}")

            time.sleep(1)
    finally:
        connection.close()

if __name__ == '__main__':
    enviar_lecturas()
