import machine, neopixel, time, math, main


def assign_color(np, i, P, t):
    np[i] = (255, 255, 0) if P[1] > -abs(2 * (t)) + 1 else (0, 0, 255)


def run(points, block, max_iter=1000):
    PIN = 2
    N = 301
    np = neopixel.NeoPixel(machine.Pin(PIN), N)

    t = -1.0
    iteration = 0
    while True:
        for i, P in enumerate(points):
            assign_color(np, i, P, t)
        np.write()
        t += 0.03
        if t >= 1:
            t -= 2

        iteration += 1
        if not block and iteration >= max_iter:
            break


if __name__=="__main__":
    points = main.read_data("data.csv")
    run(points, True)
