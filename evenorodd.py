import sys

def even_odd(num):
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

if __name__ == "__main__":
    num = int(sys.argv[1])
    print("Even and odd:", even_odd(num))