
def pan (s):

    alpha='abcdefghijklmnopqrstuvwxyz'

    unique=[]

    for char in s:

        if char in alpha and char not in unique:

            unique.append(char)

    return len(unique)==26

print(pan('the quick brown fox jumps over the lazy dog'))