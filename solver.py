from formater import *

def is_it_possible_to_get_diagonal(matrix, size): 
    for i in range(size):
        sumo = 0
        for j in range(size):
            sumo += abs(matrix[i][j])
        if sumo==0:
            return False
        if abs(matrix[i][i]) < (sumo - abs(matrix[i][i])):
            flag = True
            sumo = sum(abs(i) for i in matrix[i][: size - 1])
            for j in range(size - 1):
                if abs(matrix[i][j]) <= sumo - (abs(matrix[i][j])):
                    flag = False
            if not flag:
                return False
    return True

def get_diag_matrix(matrix, size): 
    for i in range(len(matrix) - 1):
        maxi = -1
        minn = 10 ** 20
        k = -1
        for j in range(i + 1, len(matrix)):
            sum_of_row = sum(map(abs, matrix[j][: size]))
            sum_after_element = sum(map(abs, matrix[j][j:]))
            if abs(matrix[j][i]) >= sum_of_row - abs(matrix[j][i]) \
                    and abs(matrix[j][i]) >= maxi \
                    and sum_after_element <= minn:
                maxi = matrix[j][i]
                minn = sum_after_element
                k = j
        if k != -1:
            matrix[i], matrix[k] = matrix[k], matrix[i]
    return matrix

def iterate_matrix(matrix, accuracy, size):
        if is_it_possible_to_get_diagonal(matrix, size):
            matrix = get_diag_matrix(matrix, size)
            print(f"{Colors.CYAN}\nПосле перестановки строк\n{Colors.END}")
            print_matrix(matrix)
            c = [[0] * size for _ in range(size)] 
            vector = [0] * size 

            for i in range(size):
                vector[i] = matrix[i][size] / matrix[i][i] 
                for j in range(size): 
                    if i != j:
                        c[i][j] = (-1) * matrix[i][j] / matrix[i][i]
                    else:
                        c[i][j] = 0
            x_current = [0] * size 
            x_previous = vector 
            x_max = [0] * size 
            k = -1  
            while True:  
                k += 1
                x_previous = x_current
                x_current = [0] * size
                for i in range(size):
                    for j in range(size):
                        x_current[i] += c[i][j] * x_previous[j] 
                    x_current[i] += vector[i]
                for i in range(size): 
                    x_max[i] = abs(x_current[i] - x_previous[i])
                if max(x_max) <= accuracy:
                    break
            print_results(matrix, accuracy, x_current, max(x_max), k)
        else:
            print(f"{Colors.FAIL}Невозможно привести матрицу к диагональному виду{Colors.END}")