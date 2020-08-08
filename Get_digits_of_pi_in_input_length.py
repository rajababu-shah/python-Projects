# !/rajababushah
# https://github.com/rajababu-shah/python-Projects/blob/3050140daae155b9495f7d955733b2b3d308e214/Get_digits_of_pi_in_input_length.py
# Find PI to the Nth Digit
# Have the user enter a number 'n'
# and print out PI to the 'n' th digit

def calcDigits(lim):    #Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """
    decimal = lim
    rem = 22%7
    
    print('3.',end="") #print 3. with no end
    
    while decimal > 0:
        if rem < 7:
            rem *= 10
            b = rem % 7
            yield rem // 7
        rem = b
        decimal -= 1

def main():     #wrapper function
    #calls calcDigits with the given limit
    pi_digits = calcDigits(int(input()))
    
    #Prints the output of calcDigits function
    for digit in pi_digits:
        print(digit,end='')

if __name__ == '__main__':
    main()
