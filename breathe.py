import machine, neopixel, math


def read_data(filepath):
    points = []
    with open(file=filepath) as f:
        for line in f:
            x, y = line.strip().split(",")
            points.append((float(x), float(y)))
    return points


def run(points, block, max_iter=1000, speed=0.02):
    PIN = 2
    np = neopixel.NeoPixel(machine.Pin(PIN), len(points))
    global_phase = 0.0
    iteration = 0
    t = 0.0
    while True:
        global_phase += speed
        for i, (x, y) in enumerate(points):
            local = math.sin(global_phase + y * 2)
            brightness = 0.1 + 0.15 * (local + 1)/2
            brightness = math.pow(brightness, 2.3)
            np[i] = (int(255 * brightness), int(255 * brightness), int(255 * brightness))
        np.write()

        iteration += 1
        if not block and iteration >= max_iter:
            break

if __name__ == "__main__":
    points = read_data("data.csv")
    run(points, True)
