import math


def main():
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line.lower() == "exit":
            break
        parts = line.split()
        if not parts:
            print("Error")
            continue
        op = parts[0].lower()

        try:
            if op == "add" and len(parts) == 3:
                a, b = float(parts[1]), float(parts[2])
                print(str(a + b))
            elif op == "sub" and len(parts) == 3:
                a, b = float(parts[1]), float(parts[2])
                print(str(a - b))
            elif op == "mul" and len(parts) == 3:
                a, b = float(parts[1]), float(parts[2])
                print(str(a * b))
            elif op == "div" and len(parts) == 3:
                a, b = float(parts[1]), float(parts[2])
                if b == 0:
                    print("Error")
                else:
                    print(str(a / b))
            elif op == "pow" and len(parts) == 3:
                a, b = float(parts[1]), float(parts[2])
                print(str(a**b))
            elif op == "fact" and len(parts) == 2:
                n = float(parts[1])
                if n < 0 or not n.is_integer():
                    print("Error")
                else:
                    print(str(math.factorial(int(n))))
            elif op == "sqrt" and len(parts) == 2:
                n = float(parts[1])
                if n < 0:
                    print("Error")
                else:
                    print(str(math.sqrt(n)))
            else:
                print("Error")
        except:
            print("Error")


if __name__ == "__main__":
    main()
