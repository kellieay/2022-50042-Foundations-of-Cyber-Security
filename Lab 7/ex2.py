from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

def square_multiply(a,x,n):
    n_b = bin(x)[2:]
    y = 1
    for i in range(len(n_b)):
        y = y * y % n
        if (int(n_b[i]) == 1):
            y = a * y % n
    return y

def encrypt(x, e, n):
    m = square_multiply(x, e, n)
    return m

def decrypt(x, d, n):
    m = square_multiply(x, d, n)
    return m

keypub = open('mykey.pem.pub','r').read()
rsakey_pub = RSA.importKey(keypub)
# public key
# print(rsakey_pub.n)
# print(rsakey_pub.e)
# private key
# print(rsakey_pub.n)
# print(rsakey_pub.d)

keypriv = open('mykey.pem.priv', 'r').read()
rsakey_priv = RSA.importKey(keypriv)
# public key
# print(rsakey_priv.n)
# print(rsakey_priv.e)
# private key
# print(rsakey_priv.n)
# print(rsakey_priv.d

message = open('message.txt', 'rb').read()
h = SHA256.new(message)
print('hashed plaintext: ', hex(int(h.hexdigest(), 16)))
# h.update(str.encode(message))
# print(message)
# h.update(message)
# print(type(h.hexdigest()))

create_sig = decrypt(int(h.hexdigest(), 16), rsakey_priv.d, rsakey_priv.n)
# print(create_sig)
print('---')
verify_sig = encrypt(create_sig, rsakey_pub.e, rsakey_pub.n)
print('verify signature: ', hex(verify_sig))

