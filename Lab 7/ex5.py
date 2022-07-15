import random
import ex2
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS

def generate_RSA(bits=1024):
    privkey = ex2.RSA.generate(bits)
    pubkey = privkey.publickey()
    with open('mykey.pem.priv', 'wb') as fpriv:
        fpriv.write(privkey.exportKey('PEM'))
    with open('mykey.pem.pub', 'wb') as fpub:
        fpub.write(pubkey.exportKey('PEM'))

def encrypt_RSA(public_key_file, message):
    key = open(public_key_file, 'r')
    pub_rsa_key = ex2.RSA.importKey(key.read())
    cipher = PKCS1_OAEP.new(pub_rsa_key)
    # ciphertext = cipher.encrypt(bytes(message, 'utf8'))
    ciphertext = cipher.encrypt(message)
    return ciphertext

# cipher -> ciphertext
def decrypt_RSA(private_key_file, cipher):
    key = open(private_key_file, 'r')
    priv_rsa_key = ex2.RSA.importKey(key.read())
    cipher_algo = PKCS1_OAEP.new(priv_rsa_key)
    plaintext = cipher_algo.decrypt(cipher)
    return plaintext.decode()

def sign_data(private_key_file, data):
    key = ex2.RSA.importKey(open(private_key_file, 'r').read())
    h = ex2.SHA256.new(data)
    signed = PKCS1_PSS.new(key)
    signature = signed.sign(h)
    return signature

def verify_sign(public_key_file, sign, data):
    key = ex2.RSA.importKey(open(public_key_file, 'r').read())
    h = ex2.SHA256.new(data)
    verified = PKCS1_PSS.new(key)
    return verified.verify(h, sign)

## Task
generate_RSA()
plaintext = open('mydata.txt', 'rb').read()
encryption = encrypt_RSA('mykey.pem.pub', plaintext)
print(f'encrypted mydata.txt: {encryption}')
decryption = decrypt_RSA('mykey.pem.priv', encryption)
print(f'decrypted mydata.txt: {decryption}')
sign_text = sign_data('mykey.pem.priv', plaintext)
verification = verify_sign('mykey.pem.pub', sign_text, plaintext)
print(f'verify signature: {verification}')

## Protocol Attack (pt 3)
print('---')
print('Part 3 Protocol Attack using new RSA')
int_100 = 100
int_2 = 2
y = encrypt_RSA('mykey.pem.pub', int_100.to_bytes(1, 'big'))
print('Encrypting: 100')
print(f'Result: {y}')
y_s = encrypt_RSA('mykey.pem.pub', int_2.to_bytes(1, 'big'))
m = int.from_bytes(y, 'big') * int.from_bytes(y_s, 'big')
print(f'Modified to: {y_s}')
try:
    decrypt_3 = decrypt_RSA('mykey.pem.priv', m.to_bytes((m.bit_length() + 7) // 8, 'big'))
    print(f'Decrypted: {decrypt_3}')
except ValueError:
    print(f'Decrypted: {ValueError}')

## RSA Digital Signature Protocol Attack (pt 4)
# used 86 bits instead of 1024 since the plaintext would be too long for 1024 bits integer
s = random.getrandbits(86)
x = encrypt_RSA('mykey.pem.pub', s.to_bytes(s.bit_length() + 7 // 8, 'big'))
print(f'Alice sent signature s, {s} and new message x, {x} to Bob!')

x_prime = encrypt_RSA('mykey.pem.pub', s.to_bytes(s.bit_length() + 7 // 8, 'big'))
print(x_prime)
if (x_prime == x):
    print('Bob accepts message pair, (x, s)!')






        
