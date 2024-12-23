def Palindrome(x):
    if x>0:
        x_other_copy = x
        length = 0
        while x_other_copy != 0:
            x_other_copy = x_other_copy // 10
            length = length + 1
            
        x_copy = x
        reverse = 0
        for i in range(length):
            rest = x_copy % 10
            x_copy = x_copy // 10
            reverse = reverse + (rest * 10**(length-i-1))
        print(reverse)
        if reverse == x:
            return True
    elif x==0:
        return True
    
    return False


if __name__ == '__main__':

    x = 1231
    print(Palindrome(x))