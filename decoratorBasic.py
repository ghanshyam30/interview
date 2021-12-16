# decorator function
def modify_salary(basic):
    
    def calculateDA(turn2):
        da = 0
        basic_sal = turn2(10000)
        da = basic_sal * 0.3
        print("DA:",da)
        return da+basic_sal
    
    # da = calculateDA(basic)
    
    return calculateDA(basic)


@modify_salary
# Original fucntion
def base_salary(total_due):
    basic = total_due / 2
    print("Base salary is 10 rs")
    return basic

# store_final = modify_salary(base_salary)    #without using @decorator execution

# How to call a function which has wrapper/decorator
# You don't need to provide arguments here like base_salary(10000) or it will complain that the result is float and is not callable
store_final= base_salary     
print("Final: ",store_final)


''' OUTPUT
Base salary is 10 rs
DA: 1500.0
Final:  6500.0
'''