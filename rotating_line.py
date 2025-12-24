import machine, neopixel, time, math


def read_data(filepath):
    points = []
    with open(file=filepath) as f:
        for line in f:
            x, y = line.strip().split(",")
            points.append((float(x), float(y)))
    return points


def line_points(t):
    pi = math.pi
    t *= pi
    A = (math.cos(t), math.sin(t))
    B = (math.cos(pi - t), math.sin(2 * pi - t))
    return A, B


def direction_of_point(A, B, P):
    bx = B[0] - A[0]
    by = B[1] - A[1]
    px = P[0] - A[0]
    py = P[1] - A[1]
    cross_product = bx * py - by * px
    if cross_product > 0:
        return True
    else:
        return False


def assign_color(np, i, A, B, P):
    np[i] = (255, 0, 0) if direction_of_point(A, B, P) else (0, 255, 0)


def run(points, block, max_iter=1000):
    PIN = 2
    N = 301
    np = neopixel.NeoPixel(machine.Pin(PIN), N)
    np[0] = (255, 0, 0)
    t = 0.0
    iteration = 0
    while True:
        A, B = line_points(t=t)
        t += 0.05
        for i, P in enumerate(points):
            assign_color(np, i, A, B, P)
        np.write()

        iteration += 1
        if not block and iteration >= max_iter:
            break


if __name__=="__main__":
    points = read_data("data.csv")
    run(points, True)
