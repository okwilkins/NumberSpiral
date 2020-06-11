from math import sqrt, sin, cos, pi
import numpy as np
from PIL import Image, ImageDraw
from ent import factor
from pyx import document, canvas, path

def get_target(self):
    '''
    Gets the user input for a target amount of numbers to print.
    '''

    user_input = False

    while not user_input:
        try:
            target = int(input('\nPlease enter a prime number: '))

            if (target == 2) or not(is_prime(target)):
                raise ValueError
        except ValueError:
            print('Please enter a valid number!')
        else:
            break

    return target

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

def prime_spiral(n):
    '''
    Generate an n x n number spiral with only primes.
    '''
    
    matrix = np.zeros(shape=(n, n), dtype=int)
    x = (n // 2) * (1j + 1)
    real = 1
    imaginary = 1j

    for n in range(1, n ** 2 + 1):
        if is_prime(n):
            matrix[int(x.imag), int(x.real)] = n
        else:
            matrix[int(x.imag), int(x.real)] = -1

        if n == real:
            real += round(sqrt(real))
            imaginary *= -1j
        x += imaginary

    return matrix

def print_spiral(self, matrix):
    '''
    Nicely prints out the matrix
    '''
    for row in matrix:
        for value in row:
            if value != -1:
                print(str(value) + '\t', end='')
            else:
                print(' ' + '\t', end='')
        print('\n')

class NumberSpiralPrinter:

    def __init__(self, n):
        self.n = n
        self.img_size = 2000
        self.img = Image.new('RGB', (self.img_size, self.img_size), color='black')
        self.draw = ImageDraw.Draw(self.img)
    
    def draw_matrix(self, matrix):
        for j, row in enumerate(matrix):
            for i, value in enumerate(row):
                if value != -1:
                    # -1 signifies that we don't want to draw anything
                    self.draw.point((i, j), 'white')
                    # point_1 = (i - 1, j - 1)
                    # point_2 = (i + 1, j + 1)
                    # self.draw.ellipse([point_1, point_2], fill='white')

    def draw_radial_matrix(self, matrix):
        centre = self.img_size // 2

        for j, row in enumerate(matrix):
            for i, value in enumerate(row):
                theta = sqrt(i)
                r = sqrt(j)

                x = r * (j // 4) * cos(theta) + centre
                y = r * (j // 4) * sin(theta) + centre

                if value != -1:
                    # -1 signifies that we don't want to draw anything
                    self.draw.point((x, y), 'white')
    
    def draw_ural_spiral(self, n):
        ca = canvas.canvas()

        for i in range(1, n + 1):
            r = sqrt(i)
            theta = r * 2 * pi

            x = cos(theta) * r
            y = -sin(theta) * r

            factors = factor(i)

            point_1 = (x - 1, y - 1)
            point_2 = (x + 1, y + 1)

            if len(factors) > 1: 
                # point_radius = 0.05 * pow(2, len(factors) - 1)
                # self.draw.ellipse([point_1, point_2], fill='white')
                radius = 0.05 * pow(2, len(factors) - 1)
                ca.fill(path.circle(x, y, radius))
        
        d = document.document(pages = [document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
        d.writeSVGfile("spiral_simple.svg")
    
    def draw_vogel_spiral(self, n):
        ca = canvas.canvas()

        phi = (1 + sqrt(5)) / 2

        for i in range(1, n + 1):
            r = sqrt(i)
            theta = i * 2 * pi  / (phi ** 2)

            x = cos(theta) * r
            y = sin(theta) * r

            if i <= n:
                factors = factor(i)

            if len(factors) > 1: 
                radius = 0.05 * pow(2, len(factors) - 1)
                ca.fill(path.circle(x, y, radius))
        
        d = document.document(pages = [document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
        d.writeSVGfile("spiral_simple.svg")

    
    def show_image(self):
        self.img.show()


n = 100000
# matrix = prime_spiral(n)

spiraliser = NumberSpiralPrinter(n=n)
spiraliser.draw_vogel_spiral(n)
# spiraliser.show_image()
