import os

ABSPATH = os.path.abspath('.')

for i in range(60, 100):
    os.mkdir(os.path.join(ABSPATH, 'source/', '%g' % i))
    with open (os.path.join(ABSPATH, 'source/', '%g' % i, '%g.txt' % i), 'a') as f:
        f.write('hello, world')
