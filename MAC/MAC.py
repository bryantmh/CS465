# Source: https://codereview.stackexchange.com/questions/37648/python-implementation-of-sha1
# Modified by Bryant Hinton
def sha1(data, h0, h1, h2, h3, h4, ogLength=0):
    bytes = ""

    for n in range(len(data)):
        bytes += '{0:08b}'.format(ord(data[n]))
    bits = bytes + "1"
    pBits = bits
    # pad until length equals 448 mod 512
    while len(pBits) % 512 != 448:
        pBits += "0"
    # append the original length
    pBits += '{0:064b}'.format(len(bits) - 1 + ogLength)

    hexData = hex(int(pBits, 2))
    print("HexData: " + hexData)
    def chunks(l, n):
        return [l[i:i + n] for i in range(0, len(l), n)]

    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    for c in chunks(pBits, 512):
        words = chunks(c, 32)
        w = [0] * 80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # Main loop
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

def getHexData(data):
    bytes = ""

    for n in range(len(data)):
        bytes += '{0:08b}'.format(ord(data[n]))
    bits = bytes + "1"
    pBits = bits
    # pad until length equals 448 mod 512
    while len(pBits) % 512 != 448:
        pBits += "0"
    # append the original length
    pBits += '{0:064b}'.format(len(bits) - 1)

    return hex(int(pBits, 2))

messageString = "0000000000000000No one has completed lab 2 so give them all a 0"
messageHex = getHexData(messageString)
print("Old Hex: " + messageHex)

mac = "f4b645e89faaec2ff8e443c595009c16dbdfba4b"
macA = int(mac[0:8], 16)
macB = int(mac[8:16], 16)
macC = int(mac[16:24], 16)
macD = int(mac[24:32], 16)
macE = int(mac[32:40], 16)
toAppend = ", except for Bryant"

newMac = sha1(toAppend, macA, macB, macC, macD, macE, 512 + 512)
print("NewMac: " + newMac)
