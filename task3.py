import numpy as np
import timeit

def usually(arr):
    #считаем определитель
    opr = arr[0][0] * arr[1][1] * arr[2][2] + arr[1][0] * arr[2][1] * arr[0][2] + arr[0][1] * arr[1][2] * arr[2][0] - arr[0][2] * arr[1][1] * arr[2][0] - arr[0][1] * arr[1][0] * arr[2][2] - arr[1][2] * arr[2][1] * arr[0][0]
    
    #считаем алгебраические дополнения
    a11 = arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1]
    a12 = -1 * (arr[1][0] * arr[2][2] - arr[1][2] * arr[2][0])
    a13 = arr[1][0] * arr[2][1] - arr[1][1] * arr[2][0]
    a21 = -1 * (arr[0][1] * arr[2][2] - arr[0][2] * arr[2][1])
    a22 = arr[0][0] * arr[2][2] - arr[0][2] * arr[2][0]
    a23 = -1 * (arr[0][0] * arr[2][1] - arr[0][1] * arr[2][0])
    a31 = arr[0][1] * arr[1][2] - arr[0][2] * arr[1][1]
    a32 = -1 * (arr[0][0] * arr[1][2] - arr[0][2] * arr[1][0])
    a33 = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]

    #создаём транспонированную матрицу алгебраических дополнений
    a_trans = [[a11, a21, a31], [a12, a22, a32], [a13, a23, a33]]

    #делим каждый элемент на определитель
    for i in range(3):
        for j in range(3):
            a_trans[i][j] /= opr
    
    return a_trans
    
#ввод изначальной матрицы
inp_arr = [[0 for i in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        try:
            inp_arr[i][j] = int(input("Введите значение в " + str(i + 1) + " строке, " + str(j + 1) + " столбце: "))
        except:
            print("Введите корректное значение!")
            quit()

usuall_arr, numpy_arr = [], []
try:
    usuall_arr = usually(inp_arr)    #матрица, сделанная обычным методом
    numpy_arr = np.linalg.inv(inp_arr)     #матрица, сделанная через библиотеку
except:
    print("Определитель данной матрицы равен нулю! Обратной матрицы не существует.")
    quit()

print("\nИзначальная матрица:")    #вывод изначальной и обратной матрицы
for i in range(3):
    for j in range(3):
        print(inp_arr[i][j], end=" ")
    print("\n", end="")
print("\nОбратная матрица:")
for i in range(3):
    for j in range(3):
        print(usuall_arr[i][j], end=" ")
    print("\n", end="")

print("\nВремя работы программы без библиотеки - ", timeit.timeit('usually(inp_arr)', number=10000, globals=globals()))
print("Время работы программы с библиотекой - ", timeit.timeit('np.linalg.inv(inp_arr)', number=10000, globals=globals()))