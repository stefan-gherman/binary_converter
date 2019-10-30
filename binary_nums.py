
def dec_to_binary(num):

    bin_num = []

    while num // 2 > 0:
        bin_num.append(num%2)
        num = num // 2 

    bin_num.append(num)
    bin_num = bin_num[-1::-1]

    num_ret =""
    for digit in bin_num:
        num_ret+= str(digit) 
    return num_ret 

def bin_to_dec(string):
    new_str = string[-1::-1]

    num = 0
    #print(new_str)
    for i in range(len(new_str)):
        num += int(new_str[i]) * (2)**(i)

    return num    


in1 = int(input("Enter decimal num:"))



print(dec_to_binary(in1), str(2))


in2 = input("Enter binary num:")


print(bin_to_dec(in2), str(10))


if "1000111100111" == "dec_to_binary(in1)":
    print("True")
else:
    print("False")    