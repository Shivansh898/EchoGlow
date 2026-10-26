from gpiozero import LED, Buzzer, DistanceSensor
from time import sleep

r = LED(25)
y = LED(16)
g = LED(20)
b = Buzzer(5)
sensor = DistanceSensor(echo=23, trigger=18, max_distance=3)

while True:
    distance = sensor.distance * 100

    if distance <= 6:
        r.off()
        y.off()
        g.off()
        b.off()

        r.on()
        b.on()
        sleep(0.055)
        r.off()
        b.off()
        sleep(0.055)

    elif distance <= 30:
        r.off()
        y.off()
        g.off()
        b.off()

        y.on()
        b.on()
        sleep(0.08)
        y.off()
        b.off()
        sleep(0.08)

    elif distance <= 50:
        r.off()
        y.off()
        g.off()
        b.off()

        g.on()




