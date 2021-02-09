'''
Jacky (IG: chih_yoyo) 覺得'M' '$'是世界上最匹配的兩個字母了。 所以他覺得完美的廣告標語裡面，就該要有對稱地'M'與'$'的存在 (左邊有幾個M右邊就要有幾個對應的$，順序很重要)，其他多餘的'M'與'$'應該廢除。

且 Jacky 覺得除了'M'與'$'，在座的其他字元都是垃圾，可以直接忽視。

Jacky 想知道目前存在的不完美廣告標語裡面，有幾種方式可以在移除最少的'M'或'$'來產生完美的廣告標語，而原本廣告的其他字元就放在原位就好，因為 Jacky 覺得那些東西是垃圾，可以直接無視。

請按照字母排序輸出所有完美的廣告標語。


Input
Each input set will contain a single line of string.


Output
Output all possible results in sorted order.


Sample Input 1 

M$M$$M$
Sample Output 1

M$M$M$
MM$$M$
Sample Input 2 

Mg$M$$M$a
Sample Output 2

Mg$M$M$a
MgM$$M$a
Sample Input 3 

$M
Sample Output 3



'''

#input1 = '$M'
input1 = 'M$M$$M$'
# input1 = input()
clone1 = input1

top = -1
list = []
remove = []

def push(element):
    global top, list
    top += 1
    list.append(element)

def pop():
    global top, list
    if top < 0:
        return 'error'
    else:
        element = list.pop(top)
        top -= 1
        return element
    
for i in range(0,len(input1)):
    if input1[i] == 'M':
        push(input1[i])
    elif input1[i] == '$':
        paired = pop()
        if paired == 'error':
            remove.append(i)
    else:
        continue
for i in range(0, len(remove)):
    indicies = (int(remove[i])+1,int(remove[i])+1)
    clone1 = ''.join([clone1[:indicies[0]-1], clone1[indicies[1]:]])
if top != -1: 
    delNum = top + 1
    for i in range(len(clone1)-1, -1, -1):
        if clone1[i] == 'M':
            indicies = (i+1,i+1)
            clone1 = ''.join([clone1[:indicies[0]-1], clone1[indicies[1]:]])
            delNum -= 1
            if delNum == 0: break

if clone1 != '':    print(clone1)

remove = []
clone1 = input1
top = -1
list = []

for i in range(len(input1)-1, -1, -1):
    if input1[i] == '$':
        push(input1[i])
    elif input1[i] == 'M':
        paired = pop()
        if paired == 'error':
            remove.append(i)
    else:
        continue
for i in range(0, len(remove)):
    indicies = (int(remove[i])+1,int(remove[i])+1)
    clone1 = ''.join([clone1[:indicies[0]-1], clone1[indicies[1]:]])
if top != -1: 
    delNum = top + 1
    for i in range(0, len(clone1)):
        if clone1[i] == '$':
            indicies = (i+1,i+1)
            clone1 = ''.join([clone1[:indicies[0]-1], clone1[indicies[1]:]])
            delNum -= 1
            if delNum == 0: break

if clone1 != '':    print(clone1)
    
