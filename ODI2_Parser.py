import sys
''' test data
1
01 00 e5 07 01 1c 07 2e e5 00 02
'''
# file = open(r'C:\Users\Intel(R) Willix\Documents\WorkSpace\python\test.txt', 'r')
# line = file.readline().strip('\n')
# print('Total {0} lines'.format(line))

line = input()
for i in range(0,int(line)):
    input_line = input()
    # para = sys.argv[i]
    # para = file.readline().strip('\n')
    paraArr = input_line.split(' ')
    if paraArr[8] == 'd2': event = 'BIOS'
    else: event = 'BMC'
    if paraArr[10] == '01': success = 'Success'
    else: success = 'Fail'
    print("Record {0}: {1}/{2:02}/{3:02} {4:02}:{5:02} {6} Event {7}".format(int(paraArr[0],16),int(paraArr[3] + paraArr[2],16),int(paraArr[4],16),int(paraArr[5],16),int(paraArr[6],16),int(paraArr[7],16),event,success))
