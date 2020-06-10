from math import sqrt
import numpy as np

class SpirtalPrinter:

    def __init__(self):
        self.target = self.get_target()
        self.matrix = self.prime_spiral(self.target)
        self.print_spiral()

    def get_target(self):
        '''
        Gets the user input for a target amount of numbers to print.
        '''

        user_input = False

        while not user_input:
            try:
                target = int(input('\nPlease enter a prime number: '))

                if (target == 2) or not(self.is_prime(target)):
                    raise ValueError
            except ValueError:
                print('Please enter a valid number!')
            else:
                break

        return target
    
    @staticmethod
    def is_prime(n):
        '''
        CREDIT: https://stackoverflow.com/a/17377939/9592086
        Checks if number is prime.
        '''
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        sqr = int(sqrt(n)) + 1

        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

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

    def prime_spiral(self, n):
        '''
        Generate an n x n number spiral with only primes.
        '''
        
        matrix = np.zeros(shape=(n, n), dtype=int)
        x = (n // 2) * (1j + 1)
        real = 1
        imaginary = 1j

        for n in range(1, n ** 2 + 1):
            if self.is_prime(n):
                matrix[int(x.imag), int(x.real)] = n
            else:
                matrix[int(x.imag), int(x.real)] = -1

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
                if value != -1:
                    print(str(value) + '\t', end='')
                else:
                    print(' ' + '\t', end='')
            print('\n')


printer = SpirtalPrinter()
