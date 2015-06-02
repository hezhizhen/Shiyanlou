if True:
    print "It is true"

print "I\'m True" if True else "False"

a = ['cat', 'window', 'defenestrate']

for x in a:
    print x, len(x)

for i in range(len(a)):
    print i, a[i]

for i in range(5):
    if i == 3:
        break
    print i

for i in range(5):
    if i == 3:
        continue
    print i


def fib(n):
    print """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

fib(2000)


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5


def f(arg=i):
    print arg
i = 6
f()


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It\'s", state, "!"

parrot(1000)   # comment
parrot(voltage=1000)
parrot(voltage=100000000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=10000000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')


def test(tep, *args):
    print args

test(1, 2, 3, 4, 5)


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)
