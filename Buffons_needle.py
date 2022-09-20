import math, random

def guess_pi():
    l = input('length of needle: ')
    d = input('distance between lines: ')
    if float(l) > float(d):
        print('error!\nneedle cannot be longer than distance.')
        return -1
    print('l: '+l+'\td: '+d)
    n = input('attempts: ')
    tried = 0
    for i in range(int(n)):
        x = random.uniform(-float(d)/2, float(d)/2)
        theta = random.uniform(0, math.pi)
        if abs(x) <= float(l)/2*math.sin(theta):
            tried += 1
        else:
            continue
    if tried == 0:
        print("Wow... there's no needle cross the line...\ncan't guess pi..")
        return -1
    p = tried/int(n)
    guess = 2*float(l)/(p*float(d))
    print(guess)

guess_pi()