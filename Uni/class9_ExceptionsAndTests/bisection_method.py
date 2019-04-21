if __name__ == "__main__":
    while True:
        try:
            numbers = raw_input(
                "Enter interval with a space in between. f(number1) and f(number2) must be with opposite signs.")
            number1, number2 = numbers.split(" ")[0], numbers.split(" ")[1]
            number1 = float(number1)
            number2 = float(number2)

            break
        except ValueError:
            print "Incorrect value for one of the numbers: |", number1, "|", number2, "|"
        except IndexError:
            print "You need 2 numbers!"


def f(x):
    return x * x * x + 3 * x - 5


def bisection(func, a, b, minMargin, NMAX):
    (a, b) = (b, a) if a > b else (a, b)

    if (func(a) * func(b) > 0):
        raise Exception, "Function values within the provided interval have the same sign."

    N = 1
    while (N <= NMAX):
        c = (a + b) / 2.0
        # print "debug funct(c)", func(c)
        # print "debug (b-a)/2.0", (b - a) / 2.0
        # print "debug (b-a)/2.0 <", minMargin, (b - a) / 2.0 < minMargin
        # print ""
        if (func(c) == 0 or (b - a) / 2.0 < minMargin):
            print "Solution found:", c
            return
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        N += 1

    print "Solution not found for", NMAX, "tries"


if (__name__ == "__main__"):
    bisection(f, number1, number2, 0.0001, 1000)
