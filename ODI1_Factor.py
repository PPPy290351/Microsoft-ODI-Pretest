'''
Description

Bing是一個很環保的人，也是一位健身巨獸。雖然他的辦公室 Microsoft AI R&D Center 位於32樓，但是他仍然每天爬樓梯上班。有一天，Bing想知道他有幾種方式可以走到辦公室。Bing一次只能走一層、兩層樓梯。舉例來說，若是辦公室距離地面三層樓梯，則Bing可以有三種方法(1, 1, 1)、(2, 1)、(1, 2)可以走到辦公室。


Input
輸入只有一行，包含一個整數nn，代表辦公室距離地面nn層樓梯。其中1≤n≤10^91≤n≤10 
9
 
其中20%的測試資料滿足n≤10n≤10
20%的測試資料滿足n≤30n≤30
40%的測試資料滿足n≤10^5n≤10 
5
 

Output
輸出一個數字代表Bing有幾種方法可以走到辦公室。為了避免數字太大，請將答案除以1000000007後取餘數 (mod (10^9 + 7)(10 
9
 +7))


Sample Input 1 

3
Sample Output 1

3
Sample Input 2 

5
Sample Output 2

8
Hint

你能想到O(logN)的作法嗎?
'''
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
