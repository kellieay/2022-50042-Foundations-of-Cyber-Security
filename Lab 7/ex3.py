import ex2

# 1
print('Encrypting: 100')
y = ex2.encrypt(100, ex2.rsakey_pub.e, ex2.rsakey_pub.n)
print(f'Result: {y}')

# 2
y_s = ex2.encrypt(2, ex2.rsakey_pub.e, ex2.rsakey_pub.n)
print(f'Modified to: {y_s}')

# 3
m = y * y_s

# 4
decrypt_m = ex2.decrypt(m, ex2.rsakey_priv.d, ex2.rsakey_priv.n)
print(f'Decrypted: {decrypt_m}')
