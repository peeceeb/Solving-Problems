#This is the program to generate all the binary string for a given n
# for example
# if n=2 output should be ['00','01','10','11']
# if n=3 output should be ['000','001','010','011','100','101','110','111']

#Here we will you two defined function 
# 1. Append Bits:
#    It returns 1st element + all the element in the list l
# 2. Generate Bits: 
#    It is function which returns [] when n==0
#    It returns ["0","1"] when n==1
#    If above two conditions are not satisfied, it will append "0" with all the element created by recursive generate_bit function eith [] or ["0","1"]
#    and it will also append "1" with all the element created by recursive generate_bit function eith [] or ["0","1"]

def append_bit(x, L):
    return [x+ element for element in L]
    
def generate_bits(n):
    if n==0: 
       return []
    if n==1:
       return ["0","1"]
    else:
       return (append_bits("0", generate_bit(n-1) + append_bits("1", generate_bit(n-1)))
print(generate_bit(3))

