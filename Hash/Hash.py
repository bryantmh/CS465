import hashlib
import random
import string


# Expected 2 ^ (n / 2)
def collision(n):
    letters = string.hexdigits
    stringCounter = ''.join(random.choice(letters) for i in range(20))
    hashSet = set()
    counter = -1
    while 1:
        newHash = hash(stringCounter, n)
        stringCounter = str(hex(int(stringCounter, 16) + 1))
        counter += 1
        if newHash in set(hashSet):
            return counter
        else:
            hashSet.add(newHash)


# Expected 2 ^ n
def preImage(inputString, n):
    preHash = hash(inputString, n)

    letters = string.hexdigits
    stringCounter = ''.join(random.choice(letters) for i in range(10))
    newHash = ''
    counter = 0
    while preHash != newHash:
        newHash = hash(stringCounter, n)
        stringCounter = str(hex(int(stringCounter, 16) + 1))
        counter += 1
    return counter


def hash(inputString, n):
    inputString = bytes(inputString, 'utf-8')
    hash = hashlib.sha1(inputString).hexdigest()
    binaryHash = bin(int(hash, 16))[2:]
    shortenedHash = binaryHash[0:n + 1]
    return shortenedHash


n = 8
expectedPreImage = 2**n
expectedCollision = 2**(n / 2)
numTrials = 100
average = 0
trial = 0
i = 0
while i < numTrials:
    trial = preImage("kwan", n)
    average += trial
    i += 1
print("N = " + str(n) + ": Average number of Pre-Image trials was " + str(average / numTrials) + " out of an expected " + str(expectedPreImage))

average = 0
i = 0
while i < numTrials:
    trial = collision(n)
    average += trial
    i += 1
print("N = " + str(n) + ": Average number of Collision trials was " + str(average / numTrials) + " out of an expected " + str(expectedCollision))