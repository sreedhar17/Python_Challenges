def palindrome(str):
    rev_str=str[::-1]
    if str==rev_str:
        print("Palindrome")
        print(str+"=="+rev_str)
    else:
        print("Not Palindrome")
        print(str + "==" + rev_str)


if __name__=="__main__":
    palindrome("MADAM")