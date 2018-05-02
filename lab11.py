# Lab 11
# Written by Michelle Cantin

# Postal code input
postalCode = input("What is the postal code? ")

# Function to read the postal code
def readPostalCode(postalCode):
    # Province dictionary
    provinceDic = {
        "A" : "Newfoundland",
        "B" : "Nova Scotia",
        "C" : "Prince Edward Island",
        "E" : "New Brunswick",
        "G" : "Quebec",
        "H" : "Quebec",
        "J" : "Quebec",
        "K" : "Ontario",
        "L" : "Ontario",
        "M" : "Ontario",
        "N" : "Ontario",
        "P" : "Ontario",
        "R" : "Manitoba",
        "S" : "Saskatchewan",
        "T" : "Alberta",
        "V" : "British Columbia",
        "X" : "Nunavut or Northwest Territories",
        "Y" : "Yukon"
    }

    # Rural or urban
    if (postalCode[1] == 0):
        isRural = "The postal code is for a rural address. "
    elif (postalCode[1].isdigit()):
        isRural = "The postal code is for an urban address. "
    elif (postalCode[1].isalpha()):
        isRural = "You entered an invalid second character. "
        
    # Province
    if (postalCode[0].upper() in provinceDic):
        province = "You are in the province of " + provinceDic[postalCode[0].upper()] + "."
    else:
        province = "You entered an invalid first character."

    # Message
    message = isRural + province
    return message

print(readPostalCode(postalCode))
