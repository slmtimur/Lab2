def transposition():
    n, m = 0, 0   #ввод размера матрицы
    try:
        n, m = map(int, input("\nВведите количество строк и столбцов матрицы через пробел.\nВозможные размеры матрицы: 1x2, 2x1, 1x3, 3x1, 2x2, 3x3\n").split())
        if n > 3 or m > 3 or (n == 1 and m == 1) or (n == 2 and m == 3) or (n == 3 and m == 2): 
            quit()
    except:
        print("Введите корректные значения!")
        quit()
    print("\n", end="")
    
    arr = [[0 for i in range(m)] for i in range(n)]   #ввод значений матрицы
    for i in range(n):
        for j in range(m):
            try:
                arr[i][j] = int(input("Введите значение в " + str(i + 1) + " строке, " + str(j + 1) + " столбце: "))
            except:
                print("Введите корректное значение!")
                quit()
    
    trans_arr = [[0 for i in range(n)] for i in range(m)]   #транспонирование матрицы
    for i in range(m):
        for j in range(n):
            trans_arr[i][j] = arr[j][i]
            
    print("\nИзначальная матрица:")    #вывод изначальной и транспонированной матрицы
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("\n", end="")
    print("Транспонированная матрица:")
    for i in range(m):
        for j in range(n):
            print(trans_arr[i][j], end=" ")
        print("\n", end="")

def multiplication():
    n, m = 0, 0   #ввод размера первой матрицы
    try:
        n, m = map(int, input("\nВведите количество строк и столбцов первой матрицы через пробел.\nВозможные размеры матрицы: 1x2, 2x1, 1x3, 3x1, 2x2, 3x3\n").split())
        if n > 3 or m > 3 or (n == 1 and m == 1) or (n == 2 and m == 3) or (n == 3 and m == 2): 
            quit()
    except:
        print("Введите корректные значения!")
        quit()
    
    p, k = 0, 0    #ввод размера второй матрицы
    try:
        p, k = map(int, input("\nВведите количество строк и столбцов второй матрицы через пробел.\n").split())
        if p > 3 or k > 3 or (p == 1 and k == 1) or (p == 2 and k == 3) or (p == 3 and k == 2): 
            quit()
    except:
        print("Введите корректные значения!")
        quit()
    print("\n", end="")
    
    if m != p:     #проверка возможности перемножения матриц
        print("Данные матрицы нельзя перемножить!")
        quit()
        
    print("Ввод значений первой матрицы: ")        #ввод значений матриц
    arr1 = [[0 for i in range(m)] for i in range(n)]   #ввод значений первой матрицы
    for i in range(n):
        for j in range(m):
            try:
                arr1[i][j] = int(input("Введите значение в " + str(i + 1) + " строке, " + str(j + 1) + " столбце: "))
            except:
                print("Введите корректное значение!")
                quit()
    print("Ввод значений второй матрицы: ")
    arr2 = [[0 for i in range(k)] for i in range(p)]    #ввод значений второй матрицы
    for i in range(p):
        for j in range(k):
            try:
                arr2[i][j] = int(input("Введите значение в " + str(i + 1) + " строке, " + str(j + 1) + " столбце: "))
            except:
                print("Введите корректное значение!")
                quit()

    trans_arr = [[0 for i in range(p)] for i in range(k)]   #транспонирование второй матрицы для удобства умножения
    for i in range(k):
        for j in range(p):
            trans_arr[i][j] = arr2[j][i]
        
    res = [[0 for i in range(k)] for i in range(n)]     #перемножение матриц
    for i in range(n):
        for j in range(k):
            for t in range(p):
                res[i][j] += arr1[i][t] * trans_arr[j][t]
    
    print("\nПервая матрица:")    #вывод изначальных матриц и резульат умножения
    for i in range(n):
        for j in range(m):
            print(arr1[i][j], end=" ")
        print("\n", end="")
    print("\nВторая матрица:")
    for i in range(p):
        for j in range(k):
            print(arr2[i][j], end=" ")
        print("\n", end="")
    print("\nРезультат умножения этих двух матриц:")
    for i in range(n):
        for j in range(k):
            print(res[i][j], end=" ")
        print("\n", end="")

def rang():
    n, m = 0, 0   #ввод размера матрицы
    try:
        n, m = map(int, input("\nВведите количество строк и столбцов матрицы через пробел.\nВозможные размеры матрицы: 2x2, 3x3\n").split())
        if (n != 2 and m != 2) and (n != 3 and m != 3): 
            quit()
    except:
        print("Введите корректные значения!")
        quit()
    print("\n", end="")

    arr = [[0 for i in range(m)] for i in range(n)]   #ввод значений матрицы
    for i in range(n):
        for j in range(m):
            try:
                arr[i][j] = int(input("Введите значение в " + str(i + 1) + " строке, " + str(j + 1) + " столбце: "))
            except:
                print("Введите корректное значение!")
                quit()
    
    orp = 0
    if n == 2 and m == 2:
        opr = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
        if arr[0][0] == 0 and arr[0][1] == 0 and arr[1][0] == 0 and arr[0][1] == 0:
            print("Ранг равен 0")
        elif opr == 0:
            print("Ранг равен 1")
        else:
            print("Ранг равен 2")
    if n == 3 and m == 3:
        quit()     #заглушка
inp = input("Введите команду: транспонирование, умножение, определение ранга\n")
if inp == "транспонирование":
    transposition()
elif inp == "умножение":
    multiplication()
elif inp == "определение ранга":
    rang()
else:
    print("Введите корректную команду!")