import ex2
import random

# Alice
s = random.getrandbits(1024)
x = ex2.encrypt(s, ex2.rsakey_pub.e, ex2.rsakey_pub.n)
print(f'Alice sent signature s, {s} and new message x, {x} to Bob!')

# Bob
x_prime = ex2.encrypt(s, ex2.rsakey_pub.e, ex2.rsakey_pub.n)
if (x_prime == x):
    print('Bob accepts message pair, (x, s)!')