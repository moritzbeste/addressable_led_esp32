import machine, neopixel, time, math, urandom, main


class firework:
    def __init__():
        self.x = 2 * (float(urandom.randrange(0, 256)) / 255) - 1
        self.y = 2 * (float(urandom.randrange(0, 256)) / 255) - 1
        self.max_radius2 = 0.75 * (float(urandom.randrange(0, 256)) / 255)
        self.max_radius2 *= self.max_radius2
        self.curr_radius2 = 0.0
        self.primary = (int(urandom.randrange(0, 256)), int(urandom.randrange(0, 256)), int(urandom.randrange(0, 256)))
        self.secondary = (int(urandom.randrange(0, 256)), int(urandom.randrange(0, 256)), int(urandom.randrange(0, 256)))
        self.speed = float(urandom.randrange(0, 256)) / 2048 + 0.1
        self.lifetime = int(urandom.randrange(0, 200))


def assign_color(np, i, P, t, fireworks):
    for f in fireworks:
        dist2 = dot_product2(P, (f.x, f.y))
        if dist2 < f.curr_radius2:
            np[i] = interpolate_color(f.primary, f.secondary, dist2 / f.curr_radius2)


def clear_all(np, N):
    for i in range(N):
        np[i] = (0, 0, 0)


def dot_product2(A, B):
    a = B[0] - A[0]
    b = B[1] - A[1]
    return a * a + b * b


def interpolate_color(color1, color2, fraction):
    r = (color2[0] - color1[0]) * fraction + color1[0]
    g = (color2[1] - color1[1]) * fraction + color1[1]
    b = (color2[2] - color1[2]) * fraction + color1[2]
    return (r, g, b)


def run(points, block, max_iter=1000):
    PIN = 2
    N = 301
    np = neopixel.NeoPixel(machine.Pin(PIN), N)

    iteration = 0
    fireworks = []
    while True:
        clear_all(np, N)
        rand_int = int(urandom.getrandbits(4))
        if rand_int == 0:
            fireworks.append(Firework())

        for i, P in enumerate(points):
            assign_color(np, i, P, fireworks)
        np.write()

        for f in fireworks:
            f.lifetime -= 1
            if f.lifetime <= 0:
                fireworks.remove(f)
            else:
                rad_update = (f.max_radius2 - f.curr_radius2) * f.speed
                f.curr_radius2 += rad_update * rad_update

        iteration += 1
        if not block and iteration >= max_iter:
            break


if __name__=="__main__":
    points = main.read_data("data.csv")
    run(points, True)
