# Modular Exponentiation function
def mod_exp(x, y, N):
    if y is 0:
        return 1
    z = mod_exp(x, y//2, N)
    if y % 2 is 0:
        return (z**2) % N
    else:
        return x * (z**2) % N


def extended_gcd(a, b):
    s = 0
    t = 1
    r = b
    old_s = 1
    old_t = 0
    old_r = a

    while r != 0:
        quotient = old_r // r

        temp = r
        r = old_r - quotient * temp
        old_r = temp

        temp = s
        s = old_s - quotient * temp
        old_s = temp

        temp = t
        t = old_t - quotient * temp
        old_t = temp

    return old_r, old_s, old_t


e = 65537
# Generated with openssl prime -hex -generate -bits 512 -safe
p = 0xF2942F30C32253FCAA3940D82B5C5A2D20C8B4F0949AC7A063E0FE6F5D0EC6E65D68C01A121C4C95AEA839ED920874BE861B43C7B18A3F970F338B4BDEF43A9F
q = 0xF3F3DC32B7E1CFAE054B8ADEE953D0AAB056A2F6F9B8F9E0B45747438FB12EA1C6EFD5D6EA8359ADC4BB706219AF21400B6B3497350EF300EF48CF81B27F2D7F
phi = (p - 1) * (q - 1)

# gcd(phi, e))
gcdVar, d, k = extended_gcd(e, phi)
n = p * q

print(p)
print(q)
print(n)
print(e)
print(d)

# Run some tests
m = n - 1000
if mod_exp(mod_exp(m, e, n), d, n) != m:
    print("Something's broken!")

m -= 103242343245
if mod_exp(mod_exp(m, e, n), d, n) != m:
    print("Something's broken!")

m -= 324235757234235374834843837
if mod_exp(mod_exp(m, e, n), d, n) != m:
    print("Something's broken!")

encrypted = mod_exp(50621797699281218732720030711939699869186525029214072278510413587231791695964154468605731465727196380884127897998149337911036630344278602617632607782151540784059987, e, n)
print(encrypted)

decrypted = mod_exp(65581909080564655827822096400714840637754637658215714105432652192996829052136160885204975010122949233171995832599534236606825794201676810705798424610389416623620710597359474757674473595036752684854260574076601751511853237154415015229055377895721865676917508555424213870785720395498956697130609660768039674370, d, n)
print(decrypted)
