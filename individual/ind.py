import math
from threading import Lock, Thread

E = 10e-7
lock = Lock()

def series1(x, eps, results):
    s = 0
    n = 0
    x_pow = 1  # x^0
    factorial = 1  # 0!
    while True:
        term = ((-1)**n * x_pow) / factorial
        if abs(term) < eps:
            break
        else:
            s += term
            n += 1
            x_pow *= x * x  # x^(2*n)
            factorial *= (2*n) * (2*n - 1)  # (2*n)!
    with lock:
        results["series1"] = s

def series2(x, eps, results):
    s = 0
    n = 0
    x_pow = 1  # x^0
    factorial = 1  # 0!
    while True:
        term = ((-1)**n * x_pow) / factorial
        if abs(term) < eps:
            break
        else:
            s += term
            n += 1
            x_pow *= x * x  # x^(2*n)
            factorial *= (2*n) * (2*n - 1)  # (2*n)!
    with lock:
        results["series2"] = s

def main():
    results = {}

    x = 0.3
    control_value = math.cos(x)

    thread1 = Thread(target=series1, args=(x, E, results))
    thread2 = Thread(target=series2, args=(x, E, results))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    sum1 = results["series1"]
    sum2 = results["series2"]

    print(f"x = {x}")
    print(f"Sum of series 1: {round(sum1, 7)}")
    print(f"Control value: {round(control_value, 7)}")
    print(f"Match 1: {round(sum1, 7) == round(control_value, 7)}")

    print(f"Sum of series 2: {round(sum2, 7)}")
    print(f"Control value: {round(control_value, 7)}")
    print(f"Match 2: {round(sum2, 7) == round(control_value, 7)}")

if __name__ == "__main__":
    main()
