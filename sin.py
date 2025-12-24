import machine, neopixel, math


def read_data(filepath):
    points = []
    with open(file=filepath) as f:
        for line in f:
            x, y = line.strip().split(",")
            points.append((float(x), float(y)))
    return points


def run(points, block, max_iter=1000, speed=0.2):
    PIN = 2
    np = neopixel.NeoPixel(machine.Pin(PIN), len(points))

    iteration = 0
    t = 0.0
    while True:
        for i, (x, y) in enumerate(points):
            brightness = (math.sin(10 * y - t) + 1) / 2
            brightness = math.pow(brightness, 10)
            color = (int(255 * brightness), int(255 * brightness), int(255 * brightness))
            np[i] = color

        np.write()
        t += speed
        iteration += 1
        if not block and iteration >= max_iter:
            break

if __name__ == "__main__":
    points = read_data("data.csv")
    run(points, True)
