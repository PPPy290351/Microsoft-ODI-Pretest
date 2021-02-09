def factor(num):
    if num == 1: return 1
    else: return num*factor(num-1)

n = input()
# x + 2y = n 
# x = n, if y = 0
y = 0
output = 0
# time = y/2
x = int(n)
while x >= 0:
    if x==0 or y==0:
        output += 1
    else:
        up = x+y
        down1 = x
        down2 = y
        time = factor(up)/(factor(down1)*factor(down2))
        output += time
    y+=1
    x -= 2
print( str( int(output) % (pow(10,9) + 7) ) )

# @ Partial Accepted
