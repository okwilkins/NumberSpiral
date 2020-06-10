from math import sqrt
import numpy as np

class SpirtalPrinter:

    def __init__(self):
        self.target = self.get_target()
        self.matrix = self.spiral(self.target)
        self.print_spiral()

    def get_target(self):
        '''
        Gets the user input for a target amount of numbers to print.
        '''
        try:
            target = int(input('\nPlease enter a target (more than 1): '))

            if target < 1:
                raise ValueError
        except ValueError:
            print('Please enter a valid number!')
            self.get_target()
        else:
            return target

    @staticmethod
    def spiral(n):
        '''
        CREDIT:
        https://www.reddit.com/r/ProgrammerHumor/comments/h08sul/i_mean_it_does/ftmf8rp
        Generate an n x n number spiral.
        '''
        
        matrix = np.zeros(shape=(n, n), dtype=int)
        x = (n // 2) * (1j + 1)
        real = 1
        imaginary = 1j

        for n in range(1, n ** 2 + 1):
            matrix[int(x.imag), int(x.real)] = n

            if n == real:
                real += round(sqrt(real))
                imaginary *= -1j
            x += imaginary

        return matrix

    def print_spiral(self):
        '''
        Nicely prints out the matrix
        '''
        for row in self.matrix:
            for value in row:
                print(str(value) + '\t', end='')
            print('\n')


printer = SpirtalPrinter()
