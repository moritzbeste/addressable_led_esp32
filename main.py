import machine, time, rotating_line, level, stripes, firework


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
        rotating_line.run(points, False)
        level.run(points, False)
        stripes.run(points, False)
        firework.run(points, False)
