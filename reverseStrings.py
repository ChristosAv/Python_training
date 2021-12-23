# List of data
sweets = {"pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"}

# Initialize a new list
sweetsReversed = []
for sweet in sweets:

    reversedSweet = sweet[::-1]
    sweetsReversed.append(reversedSweet)

print(sweetsReversed)
