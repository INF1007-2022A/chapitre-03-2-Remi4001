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


def format_base(value, base, digit_letters):
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
    # `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    result = ""
    abs_value = abs(value)
    while abs_value != 0:
        pass
    if value < 0:
        # TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
        pass
    return result


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))