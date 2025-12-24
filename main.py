import machine, time, rotating_line, level, rainbow, sin, breathe

def read_data(filepath):
    points = []
    with open(file=filepath) as f:
        for line in f:
            x, y = line.strip().split(",")
            points.append((float(x), float(y)))
    return points


if __name__=="__main__":
    points = read_data("data.csv")
    while True:
        level.run(points=points, block=False, max_iter=500, speed=0.05)
        sin.run(points=points, block=False, max_iter=250, speed=0.5)
        rainbow.run(points=points, block=False, max_iter=500, speed=0.05)
        breathe.run(points=points, block=False, max_iter=250, speed=0.5)


