import machine, neopixel, math


def hsv_to_rgb(h, s, v):
    h = h % 1.0
    i = int(h * 6)
    f = (h * 6) - i
    p = int(255 * v * (1 - s))
    q = int(255 * v * (1 - f * s))
    t = int(255 * v * (1 - (1 - f) * s))
    v = int(255 * v)
    i = i % 6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)


def run(block, max_iter=1000, speed=math.pi/10):
    PIN = 2
    np = neopixel.NeoPixel(machine.Pin(PIN), len(points))
    iteration = 0
    t = 0.0
    while True:
        color = hsv_to_rgb(t, 1.0, 0.5)
        t += speed
        for i in range(len(points)):
            np[i] = color
        np.write()
        for i in range(len(points)):
            np[i] = (0, 0, 0)
        np.write()

        iteration += 1
        if not block and iteration >= max_iter:
            break

if __name__ == "__main__":
    run(True)
