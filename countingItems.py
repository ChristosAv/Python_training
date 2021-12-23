# List of data
sweets = {"pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"}


#  Function that gets the list of data as argument
def countingItems(data):
    # counter
    k = 0

    # Iterate through the list
    for sweet in sweets:
        k += 1

    return k


amount = countingItems(sweets)

print(amount)
