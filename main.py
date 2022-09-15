import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef = float(sys.argv[index])
    except:
        # Вводим с клавиатуры
        print(prompt)
        while(True):
            try:
                # Переводим строку в действительное число
                coef = float(input())
            except:
                print('Некорректный ввод. Повторите ввод:')
            else:
                return coef
    # Переводим строку в действительное число
    return coef


def get_roots(a, b, c):
    result = []
    D = b ** 2 - 4 * a * c
    if D == 0.0:
        try:
            root = math.sqrt(-b / (2.0 * a))
        except ArithmeticError:
            return result
        else:
            if (c == 0) and (b == 0):
                result.append(0)
            else:
                result.append(root)
                result.append(-root)

    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        if root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        root2 = (-b - sqD) / (2.0 * a)
        if (root1 == 0 or root2 == 0):
            result.append(0)
        if root2 > 0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()
