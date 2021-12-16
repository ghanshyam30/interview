# decorator function
def modify_salary(basic):
    
    def calculateDA(turn2):
        da = 0
        basic_sal = turn2()
        da = basic_sal * 0.03
        print("DA:",da)
        return da+basic_sal
    
    # da = calculateDA(basic)
    
    return calculateDA(basic)


@modify_salary
# Original fucntion
def base_salary():
    print("Base salary is 10 rs")
    return 10

# base_salary = modify_salary(base_salary)
store_final= base_salary
print("Final: ",store_final)
