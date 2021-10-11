import math
import numpy as np
#import linalg
#import  numbers
def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r > 0 and h > 0:
        return 2 * math.pi * r * r + h * 2 * math.pi * r

    return float('nan')

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """

    if not(isinstance(n, int)):
        return None
    elif n < 0:
        return None
    elif n == 0:
        return None
    elif n == 1:
        return np.array([1])
    else:
        fib_arrey = np.array([1, 1])
        for i in range(n - 2):

            fib_arrey = np.append(fib_arrey, float(fib_arrey[i]+fib_arrey[i+1]))
        return [fib_arrey]

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """

    m = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])


    mdet = np.linalg.det(m)
    if mdet != 0:
        minv = np.linalg.inv(m)
    else:
        minv = float('NaN')

    mt = m.transpose()
    return minv, mt, mdet



def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if not(isinstance(n, int)):
        return None
    elif m <= 0 or n <= 0:
        return None

    matrix = np.zeros((m, n))

    for row in range(len(matrix)):

        for elm in range(len(matrix[row])):
            if row < elm:
                matrix[row][elm] = elm
            else:
                matrix[row][elm] = row

    return matrix