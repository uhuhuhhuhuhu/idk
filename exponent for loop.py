user_base_number= int(input("Please enter your base number:"))
user_pow_number= int(input("Please enter your power number:"))
def  power_number(user_base_number, user_pow_number):
    result = 1
    for number in range(user_pow_number):
        result = result * user_base_number
    return result
print (power_number(user_base_number, user_pow_number))
