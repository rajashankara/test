import sys

rajlkasjrlkja
def isAnagram(str1, str2):
    if len(str1) == len(str2):
        wd1 = []
        wd2 = []

        for i in range(len(str1)):
            wd1.append(str1[i])
            wd2.append(str2[i])

        for letter in wd1:
            if letter in wd2:
                wd2.remove(letter)
        if len(wd2) == 0:
            print("Its is an Anagram")
        else:
            print("It is not an Anagram")
    else:
        print("It is not an Anagram")

def isAnagram2(str1, str2):
    if sorted(str1) == sorted(str1):
        print(sorted(str1))
        print(sorted(str1))
        print("Anagram")
    else:
        print("Not an Anagram")

if __name__ == "__main__":

    wd1 = input("input string one")
    wd2 = input("input string two")


    isAnagram(wd1,wd2)
    isAnagram2(wd1,wd2)

