import machine, neopixel, time, math

PIN = 2
N = 301

np = neopixel.NeoPixel(machine.Pin(PIN), N)

time.sleep(3)
for i in range(N):
    np[i] = (int(255 * 0.75), int(255 * 0.75), int(255 * 0.75))
    np.write()
    time.sleep(1/15.0)
    np[i] = (0, 0, 0)
    np.write()
    time.sleep(1/15.0)
