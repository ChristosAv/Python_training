# List of data
sweets = {"pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"}

# # Initialize the dictionary
letters = {}

def letterFunction(data, letter):
    # variable used as counter
    letterCounter = 0

    for sweet in sweets:
        letterCounter += sweet.count(letter)

    return letterCounter


found = letterFunction(sweets, "a")
print("The letter 'a' appears %d times" % found)
letters['a'] = found

found = letterFunction(sweets, "e")
print("The letter 'e' appears %d times" % found)
letters['e'] = found

found = letterFunction(sweets, "i")
print("The letter 'i' appears %d times" % found)
letters['i'] = found

found = letterFunction(sweets, "o")
print("The letter 'o' appears %d times" % found)
letters['o'] = found

found = letterFunction(sweets, "u")
print("The letter 'u' appears %d times" % found)
letters['u'] = found

print(letters)
