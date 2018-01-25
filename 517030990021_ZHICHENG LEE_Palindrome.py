def check(charac):  #check is it empty string or alphabet
    if charac == '':
        return False
    if 65<=ord(charac)<=90 or 97<=ord(charac)<=122:
        return True

test = "A man, a plan, a canal, Panama!"

def palind(s):
    first = s[0]
    last = s[-1]

    if len(s)==1 or len(s) == 0:        #length of string will equal to 1 or 0 in the end
        return True

    elif len(s) == 2 and first.lower()==last.lower():   #if length of string equal to 2, and each other are the same, return True
        return True

    else:
        if check(s[0]): #check the first character of the string
            if check(s[-1]):
                if first.lower() == last.lower():
                    return palind(s[1:-1])  #return the middle part of the string and compare again

                else:
                    return False

            else:
                return palind(s[:-1])   #if the last character is not alohabet, return string not including the that character

        else:
            return palind(s[1:])    #if the first character is not alohabet, return string not including the that character

def main():
    if palind(test):
        print 'Yes. This is palindrome!' #print yes if the string is palindrome

    else:
        print 'No. This is NOT palindrome!'  #print no if the string is not palindrome
main()
