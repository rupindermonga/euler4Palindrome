
#finding Palindrome from 2 n digit numbers

def Palindrome(n):
    
    def reverse(n):
        x = n
        rev = 0
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x  //= 10
        return rev == n
    
    c = 0
    
    for a in range(ndigit(n)[0], ndigit(n)[1], -1):
        for b in range(ndigit(n)[0], ndigit(n)[1], -1):
            x = a*b
            if x > c:
                if reverse(x):
                    c = a*b
    return c

def ndigit(n):
    i = 1
    bnum = 0
    snum = 1
    while i <= n :
        bnum = bnum*10 +9
        snum = snum*10
        i += 1
    return [bnum, snum//10]
    
final = Palindrome(2)
print(final)
