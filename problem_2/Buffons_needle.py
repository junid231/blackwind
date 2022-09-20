import math, random

def guess_pi():
    l = float(input('length of needle: '))
    d = float(input('distance between lines: '))
    if l > d:
        print('error!\nneedle cannot be longer than distance.')
        return -1
    print('l:', l, '\td:', d)
    n = int(input('attempts: '))
    tried = 0
    for i in range(n):
        x = random.uniform(-d/2, d/2)
        theta = random.uniform(0, math.pi)
        if abs(x) <= l/2*math.sin(theta):
            tried += 1
    if tried == 0:
        print("Wow... there's no needle cross the line...\ncan't guess pi..")
        return -1
    p = tried/n
    guess = 2*l/(p*d)
    print(guess)

guess_pi()
