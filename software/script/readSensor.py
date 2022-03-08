import serial
import time
from datetime import date, datetime


def initSensor():
    sensor = "MPU6050"
    serialPort = '/dev/ttyACM0'
    baudRate = 115200

    return [sensor, serialPort, baudRate]


def writeLog(sensor: str, serialPort: str, baudRate: int):
    path = f"{str(datetime.now())}_LOG_{sensor}.txt"
    ser = serial.Serial(serialPort, baudRate)

    oldTime = int(round(time.time() * 1000))

    with open(path, 'w+') as f:
        while True:
            newTime = int(round(time.time() * 1000))
            if newTime - oldTime > 500:
                line = ser.readline()
                f.write(
                    f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\tdata: {line}")
                f.flush()
                print(line)


def main():
    Sensor = initSensor()
    writeLog(Sensor[0], Sensor[1], Sensor[2])


if __name__ == "__main__":
    main()
