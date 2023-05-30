import numpy

a = numpy.array([[0, 0, 1], [1, 1, 0], [0, 1, 0]])  #0 - круг
                                                    #1 - крестик


def tic_tac_toe(field):
    if field.shape != (3, 3):
        return -1
    for i in range(3):
        if field[i, :].max() == field[i, :].min() == 0 or field[:, i].max() == field[:, i].min() == 0:
            return 0
        if field[i, :].max() == field[i, :].min() == 1 or field[:, i].max() == field[:, i].min() == 1:
            return 1
    if field[0, 0] == field[1, 1] == field[2, 2] == 0 or field[0, 2] == field[1, 1] == field[2, 0] == 0:
        return 0

    if field[0, 0] == field[1, 1] == field[2, 2] == 1 or field[0, 2] == field[1, 1] == field[2, 0] == 1:
        return 0

    return -1

print(*a, sep='\n')
print(tic_tac_toe(a))


