def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

#Recursive 递归
def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

#Iterative 迭代
def iter_palindrome(s):
    for i in range(0, len(s) / 2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
        
def faster_fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print is_palindrome('')
print is_palindrome('a')
print is_palindrome('wer')
print is_palindrome('level')