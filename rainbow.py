import machine, neopixel, math


def read_data(filepath):
    points = []
    with open(file=filepath) as f:
        for line in f:
            x, y = line.strip().split(",")
            points.append((float(x), float(y)))
    return points


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


def run(points, block, max_iter=1000, speed=0.05, stripe_freq=0.5):
    PIN = 2
    np = neopixel.NeoPixel(machine.Pin(PIN), len(points))
    
    kx = stripe_freq
    ky = stripe_freq * 0.5
    
    t = 0.0
    iteration = 0
    while True:
        for i, (x, y) in enumerate(points):
            phase = x * kx + y * ky + t
            color = hsv_to_rgb(phase, 1.0, 1.0)
            np[i] = color
        np.write()
        t += speed

        iteration += 1
        if not block and iteration >= max_iter:
            break

if __name__ == "__main__":
    points = read_data("data.csv")
    run(points, True)
