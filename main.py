import math


def get_key(data, key: tuple):
    A, C, X = key
    M = 2**31 - 1
    result = []
    if math.gcd(A, M) == 1:
        if C % 2 != 0:
            if A % 4 == 1 and A >= 4:
                for i in range(len(data)):
                    result.append(str(X).encode('utf-16'))
                    X = A * X + C
                    X %= M
                return result
            else:
                print("'A' % 4 должно == 1 и >= 4")
        else:
            print("'C' должно быть нечетным")
    else:
        print("'A' и 'M' не взаимно простые")
    return None


def byte_xor(a, b):
    byte = b""
    for _a, _b in zip(a, b):
        byte += (_a ^ _b).to_bytes(1, byteorder="little")
    return byte


def process(data, key):
    b = b""
    for i, byte in enumerate(data):
        print(f"{byte}:{byte.to_bytes(1, byteorder='little')} -- {key[i]}")
        b += (byte_xor(byte.to_bytes(1, byteorder="little"), key[i]))
    return b


def main(key, text=None, path=None):
    source = not all([path, text]) and any([path, text])
    if not all([key, source]):
        print("Invalid arguments!")
    else:
        if path:
            with open(path[0], "rb") as file:
                data = file.read()
        else:
            data = text.encode('utf-16')
        key = get_key(data, key)
        if not key:
            return
        data = process(data, key)
        if path:
            with open(path[1], "wb") as file:
                file.write(data)
        else:
            print(str(data[2:], "utf-16"))


if __name__ == '__main__':
    print("Введите значение ключа")
    A = int(input("A: "))
    C = int(input("C: "))
    X = int(input("X: "))
    choice = int(input("Ввод: \n1. Файл \n2. Текст\nx: "))
    if choice == 1:
        path_from = input("Введите путь до исходного файла: ")
        path_to = input("Введите путь до конечного файла: ")
        main(key=(A, C, X), path=(path_from, path_to))
    elif choice == 2:
        text = input("Введите текст: ")
        main(key=(A, C, X), text=text)
    else:
        print("Неверный пункт")
