# https://www.hackerrank.com/challenges/palindrome-index

def isPalindrome(string):
    return string == string[::-1]       # checks if string == it's reverse

T = int(input())
for _ in range(T):
    string = input()
    if(isPalindrome(string)):           # check if input string is a palindrome or not
        print(-1)
    else:                               # else, compare first char with last char (and so on...)
        j = len(string)-1
        i = 0
        while(i <= j):
            if(string[i] == string[j]): # check next one
                i+=1
                j-=1
            else:                       # when chars at two indices do not match
                sub1 = string[i+1:j+1]  # create two substrings, each without the non-matching index
                sub2 = string[i:j]      # then check if rest of the chars are palindrome or not
                if(isPalindrome(sub1)):
                    print(i)
                elif(isPalindrome(sub2)):
                    print(j)
                else:
                    print(-1)
                break
