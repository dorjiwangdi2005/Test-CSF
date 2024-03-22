def reverse_string(s):
    
    if len(s) == 0:
        return (s)  
    
    else:
    # Recursive case: reverse the substring excluding the last character
        return s[-1] + reverse_string(s[:-1])
a = str(input ("enter any word to be reversed: "))
print(reverse_string(a))
    
