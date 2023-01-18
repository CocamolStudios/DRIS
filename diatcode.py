import math
import random
import art
import numpy as np
import sympy as sy
import re
from colorama import Fore
import fractions

def var(var1, op, var2, var3):
    """The var function takes two numeric variables and performs an operation depending on the operator and stores them in a variable."""
    if op == "+":
        a = var1 + var2
        var3.append(a)
    elif op == "-":
        a = var1 - var2
        var3.append(a)
    elif op == "*":
        a = var1 * var2
        var3.append(a)
    elif op == "/":
        a = var1 / var2
        var3.append(a)
    elif op == "%":
        a = var1 % var2
        var3.append(a)
    elif op == "^":
        a = var1 ^ var2
        var3.append(a)
    elif op == "//":
        a = var1 // var2
        var3.append(a)

def passing(inp, inprow):
    """The passing function takes an input of type input and converts it to whatever data type you want."""
    inp2 = eval(inp)
    inprow = inp2
    print(type(inp2))

def match(a, b):
    """The match function takes two numeric variables and if they are the same, it puts them both in a list, and if they are not the same, it puts the one that is bigger in the list."""
    if a == b:
        print(True)
        l = [a, b]
        print(l)
    else:
        print(False)
        if a > b:
            l = [a]
            print(l)

        elif a < b:
            l = [b]
            print(l)

def alt_o(char, palse, fac, reg):
     """Alt_o function takes 4 inputs and the first input is the letter it is supposed to find in your string as a regular expression and puts it in a list and the index returns the same letter from the list."""
     char = re.compile(str(reg))
     result = char.findall(fac)
     l = result
     palse = l[reg]
     print(char, fac, reg, palse, result, l)

def listrow(lis=list, gen=int, genrow=int):
    """The listrow function takes three inputs, which are lists, integers, and integers, respectively. You give a list to the function and along with the generation and generation of the row, then the function checks if the generation of the row is the product of the length of the list and its generation, it drops it in the list."""
    print(len(lis))
    print(gen)
    a = lis
    b = gen
    c = lis[gen]
    d = genrow
    if d == b * len(c):
        e = a.append(d)
        print("index of genrow in your list:", a[e])
    else:
        print("your gen not have a row")

def searchi(array, val):
    """The searchi function uses a binary search to return the value you want to find in a list."""
    low = 0
    high = len(array) - 1
    mid = high // 2
    while low <= high:
        if val > array[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid
    return low

def isomorphic(s, t):
    """The isomorphic function determines the isomorphism of two words and even sentences."""
    if not len(s) == len(t):
        return False

    dic = {}
    set_value = set()
    for i in range(len(s)):
        if s[i] not in dic:
            if t[i] not in set_value:
                return False
            dic[s[i]] = t[i]
            set_value.add(t[i])
        else:
            if not dic[s[i]] == t[i]:
                return False

    return True

class a1z26:
    """This class encodes the word with its own Unicode."""
    def encode(self, plain):
        """This function encodes the word with its own Unicode."""
        print([ord(elm) - 92 for elm in plain])

    def decode(self, encode):
        """This function decodes the word with its own Unicode."""
        print("".join([chr(elm + 92) for elm in encode]))

class OneTime:
    """This class uses the One Time Pad encryption method to generate a one-time password by combining Unicode with some random numbers and mathematical operations."""
    def encrypt(self, text):
        """The encryption function generates the password"""
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        print(cipher)
        print(key)

    def decrypt(self, cipher, key):
        """The decryption function breaks the password"""
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        result = ''.join([i for i in plain])
        print(result)

def binary_search(array, query):
    """The binary search function uses the binary search method, with this method we halve the list until we reach the number. Most of the time, the most optimal algorithm for finding a number in the list sorted from small to large is the binary search method."""
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        val = array[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

class Refactor:
    """The Refactor class consists of several other classes that allow you to perform operations such as opening and marking down the code while working with DRIS."""
    class flag:
        """The flag class previews the coloring of a string."""
        def red(self, string=str):
            string = Fore.RED+string
            print("preview:", string)

        def blue(self, string=str):
            string = Fore.BLUE+string
            print("preview:", string)

        def green(self, string):
            string = Fore.GREEN+string
            print("preview:", string)

    class markdown:
        """The markdown class consists of several functions that are related to marking down and referencing a piece of code."""
        def markdown(self, code):
            """Markdowns a piece of code, which can be in the form of a list or a multi-line string, in the file."""
            file = open("markdown.py", "w")
            data = code
            for line in data:
               file.write(data)
            file.close()
            print("your code in",file, "have a markdown")

        def retype(self, count, code, file):
            """Writes a piece of code as a string to a number entered by the user in a file"""
            file2 = open(file, "w")
            data = code
            for line in data in range(count):
                file2.write(data)
            file2.close()

    class tile:
        """The Tile class consists of two functions that provide conditions similar to the Markdown class but different from it."""
        def tileup(self, file, tile):
            """The tileup function takes a piece of tile (code) in the form of a multi-line string and writes it if it does not exist in the file you want."""
            fil = open(file, "r")
            data = tile
            if data not in fil:
                fil.close()
                fil = open(file, "w")
                for line in data:
                    fil.write(data)
                fil.close()
            elif data in fil:
                fil.close()

        def tiledown(self, file):
            """This function closes a file if it is open"""
            if file is open():
                file = file.close

class functions:
    def m_sequence(self=None, r=None):
        m = r + r + r - r ^ r - r
        print(m)

    def push(self=None, n=None, k=None):
        p =  fractions.Fraction(math.factorial(n), math.factorial(n - k))
        print(p, "Possibility of substitution")

    def g_logarithm(self=None, num=None, base=None, q=None):
        q_sequence = q ^ q - (q * q) / (q * q) + q - (q * q) ^ 2
        g = math.log(num, base=base) - math.factorial(math.pi) * q_sequence ^ (q_sequence - math.log10(q_sequence) - math.e)
        print(g)

    def alpha_function(self=None, n=None):
        ε = np.sqrt(n * 4 / 2 - n ^ 3 + 1)
        a = ε * (ε ^ ε - 1 + (ε / 2 + (ε ^ 3)))
        b = a * a ^ a - (a + a - a + a) ^ 2
        α = complex(b)
        c = α + α - (α + α) * α
        print(c)

    def m_function(self=None, x=None, y=None):
        lower = x
        upper = y
        print("Prime numbers between", lower, "and", upper, "are:")
        for num in range(lower, upper + 1):
            # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)

    def l(self=None, n=None):
        l = (n + n) ^ 2 + (n - n) ^ 2
        print(l)

    def r(self=None, li=None, n=None, lis=list):
        a = li + n
        b = a + n
        c = n * a + b
        d = c - b + c * 2
        d = c + c - a
        lis.append(d)
        r = max(lis)
        r2 = min(lis)
        r3 = random.randint(r2, r)
        r4 = r + r2 / 2
        r5 = r4 * r3 + r2 * r - r4 * 3
        print(lis)
        print("max:",r)
        print("min:",r2)
        print("possible:", r3)
        print("mid:", r4)
        print("max of infinite:", r5, "of infinite")
        l = [lis, r5]
        print("total:",l)

    def u_p(self=None, u=None, p=None):
        x = u - p
        m = u - x - 1
        if u > p:
            a = u + m - p
            print("u is p:", u, p, a == p)

        elif u < p:
            x = p - u
            m = p - x - 1
            a = p + m - u
            print('p is u:', p, u, a == u)

        elif u == p:
            x = p - u
            m = p - x - 1
            a = p + m - u
            print("p and u is u and p:", u, p, a == u)
            x = u - p
            m = u - x - 1
            a = u + m - p
            print("p and u is u and p:", u, p, a == p)

        elif u or p == 0:
            print("u or p are 0")































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# TODO : makeing a cap class
# TODO : fixing passing function
# TODO : makeing a funcmaker function           e