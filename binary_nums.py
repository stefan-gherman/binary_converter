
def dec_to_binary(num):

    bin_num = []

    while num // 2 > 0:
        bin_num.append(num % 2)
        num = num // 2

    bin_num.append(num)
    bin_num = bin_num[-1::-1]

    num_ret = ""
    for digit in bin_num:
        num_ret += str(digit)
    return num_ret


def bin_to_dec(string):
    new_str = string[-1::-1]

    num = 0
    for i in range(len(new_str)):
        num += int(new_str[i]) * (2)**(i)

    return num


def main_exec():
    in1 = input("Enter num and base with whitespace between them:")

    in1 = in1.split()

    if(in1[1] == "2"):
        print(bin_to_dec(in1[0]), str(10))

    elif(in1[1] == "10"):
        print(dec_to_binary(int(in1[0])), str(2))


main_exec()
