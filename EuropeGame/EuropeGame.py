import csv

# Lists
europeList = []

userGuessList = []

with open ('EuropeCountries - Sheet1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader: 
        europeList.append(line[0].strip())

# Number of European Countries
len_EU = len(europeList)

# Opening Game Info
print("Welcome to my Sporcle game recreated in Visual Studio Code")
print()
print("Please read the intructions carefully...")
print("----------------------------------------")
print(f"- There are {len_EU} countries in the entirety of Europe.\n")
print("- You must enter maximun 20 countries.\n- Please capitalize the first letter (also do this if there are 2 words).\n- If you put the same country twice, the game will end automatically.\n- Finally if you want to quit, simply enter Q.")
print ("If you score between 0 and 5, you are bronze tier. 5- 10 is silver tier and 10+ is gold tier.")
# User Info
counter = 0

while counter <= 51:
    userGuess = input("Please enter a country: ")
    cap_UserGuess = userGuess.capitalize()

    if cap_UserGuess == "Q":
        check = input("Sure to quit? Y = Yes and N = No: ")
        if check == "Y":
            break
        else:
            continue

    if cap_UserGuess in userGuessList:
        print ("You already guessed this")
        print ("Sorry, the game ends")
        break

    elif cap_UserGuess not in europeList:
        print ("This country does not exist")
        continue

    userGuessList.append(cap_UserGuess)

    counter = counter + 1

print (userGuessList)
user_score = len(userGuessList)
print ("You got",user_score,"out of",len_EU)

if user_score < 6:
    print ("You are in Bronze tier")

elif user_score < 11 and user_score > 5:
    print ("You are in silver tier")

else:
    print ("You are in Gold tier")

