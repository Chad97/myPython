import turtle as t
import math
bob = t.Turtle()


# bob.fd(100)
# bob.lt(90)
# bob.fd(100)


def square(bob, le ,j):
    """
    :param bob: obj
    :param le: int
    :param j: int
    :return:   None
    """
    for i in range(j):
        bob.fd(le)
        bob.lt(360 / j)


square(bob, 100, 7)


def circe(t, r):
    cir = 2 * math.pi * r
    n = 800
    length = cir / n
    square(t, length, n)


circe(bob, 100)


t.mainloop()