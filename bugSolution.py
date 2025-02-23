def function_with_uncommon_error_corrected(a, b):
    if a == 0 or b == 0:
        return 0 #This return 0 when any of the variable is 0
    return b / a

result = function_with_uncommon_error_corrected(0, 10)
print(result) # Output: 0

result = function_with_uncommon_error_corrected(10,0) 
print(result) # Output: 0

result = function_with_uncommon_error_corrected(10,10)
print(result) #Output: 1.0