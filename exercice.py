#!/usr/bin/env python


def dissipated_power(voltage, resistance):
    return voltage ** 2 / resistance


def orthogonal(v1, v2):
    produit_scalaire = 0
    for i in range(len(v1)):
        produit_scalaire += v1[i] * v2[i]

    if produit_scalaire == 0:
        return True
    else:
        return False


def average(values):
    somme = 0
    termes = 0

    for v in values:
        if v >= 0:
            somme += v
            termes += 1


    return somme / termes


def bills(value):
    twenties = tens = fives = ones = 0

    while value != 0:
        if value >= 20:
            twenties += 1
            value -= 20
        elif value >= 10:
            tens += 1
            value -= 10
        elif value >= 5:
            fives += 1
            value -= 5
        elif value >= 1:
            ones += 1
            value -= 1

    return (twenties, tens, fives, ones)


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
