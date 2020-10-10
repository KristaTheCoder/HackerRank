#This is the working code for String Formatting Problem available at Hackerrank in Python3

#Given an integer, n, print the following values for each integer from 1 to n:
#1. Decimal
#2. Octal
#3. Hexadecimal(capitalized)
#4. Binary

#he four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n

#Input Format

#A single integer denoting n.
#Constraints

#1 <=n <= 99

#Output Form
# Print n lines where each line i (in the range 1<=i <=n ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.

#Sample Input 

#17 

#Sample Output

# 1     1     1     1
# 2     2     2    10
# 3     3     3    11
# 4     4     4   100
# 5     5     5   101
# 6     6     6   110
# 7     7     7   111
# 8    10     8  1000
# 9    11     9  1001
#10    12     A  1010
#11    13     B  1011
#12    14     C  1100
#13    15     D  1101
#14    16     E  1110
#15    17     F  1111
#16    20    10 10000
#17    21    11 10001     

def print_formatted(number): 
    spacePad = len(str(bin(number))) 
    for i in range(1, number + 1): 
        floatVar = str(i) 
        octVar = str(oct(i)[2:]) 
        hexVar = str(hex(i)[2:]).upper() 
        binVar = str(bin(i)[2:]) 
        formatFloat = ((" " * (spacePad - len(str(floatVar)) - 2)) + floatVar) 
        formatOct = ((" " * (spacePad - len(str(octVar)) - 2)) + octVar) 
        formatHex = ((" " * (spacePad - len(str(hexVar)) - 2)) + hexVar) 
        formatBin = ((" " * (spacePad - len(str(binVar)) - 2)) + binVar) 
        print(formatFloat + " " + formatOct + " " + formatHex + " " + formatBin)

# This is the required answer. Directly put this in compiler for results. Thank you.