#! /usr/bin/env python

def loop(n):
    x = 0
    for i in range(n):
        for j in range(i):
            for k in range(j):
                x += k
    return x

if __name__ == '__main__':
    print('hello, world')
    print('have a nice day!')
    print(loop(1000))

