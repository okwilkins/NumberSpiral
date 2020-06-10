import math
import numpy as np

target = 15

if target < 1:
    print('Target needs to be a valid number!')
    exit()

class SpirtalPrinter:

    def __init__(self):
        self.target = self.get_target()
        self.root = int(math.sqrt(self.target))
        self.matrix = np.zeros((self.root, self.root))
        self.mid_index = int(self.root / 2)

        self.gen_spiral()

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
    def addition_seq(n):
        '''
        Generates the sequence of differences between each of a complete square
        '''
        # Should use iterator here! Look at fibonachi example
        return [math.floor(i / 2) for i in range(2, n + 1)]

    def gen_spiral(self):
        '''
        Manipulates the matrix so that the number spiral is generated.
        '''
    

        # Determines all the corners that will change the direction that the
        # spiral travels in
        rot_nums = {sum(self.addition_seq(j)) for j in range(2, 2 * self.root + 1)}
        rot_index = 4

        # Find the mid point of the matrix
        if self.root % 2 == 0:
            # If the root is even, the start point will be off centre
            i = self.mid_index - 1
            j = self.mid_index
        else:
            i = self.mid_index
            j = self.mid_index

        for n in range(1, self.target + 1):
            self.matrix[j][i] = n

            if rot_index == 1:
                j -= 1
            elif rot_index == 2:
                i -= 1
            elif rot_index == 3:
                j += 1
            elif rot_index == 4:
                i += 1

            if n in rot_nums:
                rot_index += 1

                if rot_index > 4:
                    rot_index = 1

    def print_spiral(self):
        '''
        Nicely prints out the matrix
        '''
        for row in self.matrix:
            for value in row:
                # Use int as numpy defaults to float
                print(str(int(value)) + '\t', end='')
            print('\n')


printer = SpirtalPrinter()
printer.print_spiral()
