import math

# this function is used to check if all the characters in file are >=32 and <=126
# that is, whether they are ascii encoded
def checkChars():
    with open("../dataset_after_bwt/grammar.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                print "End of file"
                break
            if ord(c)>126 and ord(c)<32:
                print("error")


# this is the mtf function to process data
def mtf():

    asciiList = []
    access_cost_list = []
    for i in range(0,128):
        asciiList.append(i)

    with open("../dataset_after_bwt/grammar.txt") as f:
        while True:
            # this is the current char read from the file  
            c = f.read(1)
            if not c:
                break
            # find the index of that char
            index = asciiList.index(ord(c))
            # record the access cost
            access_cost_list.append(index)
            # remove that char from the list
            asciiList.pop(index)
            # insert that char at the front of the list
            asciiList.insert(0, ord(c))
            
            if ord(c)>126 and ord(c)<32:
                print("error")
    print(len(access_cost_list))
    # compute the cost use log fomula
    cost = 0
    for j in access_cost_list:
        if j != 0:
            cost += 2*math.floor( math.log(j) ) +1
        else:
            cost += 1
    print "the cost is: ", cost, " bits ", cost/8, " bytes"
    writeList(access_cost_list)
    mtf_reverse(access_cost_list)

def mtf_reverse(access_cost_list):
    asciiList = []
    with open("testOutput.txt", 'w') as file_handler:
        for i in range(0,128):
            asciiList.append(i)
        for j in access_cost_list:
            # find the value of that item in cost list, that is the char we reverted
            value = asciiList[j]
            # find the index
            index = asciiList.index(value)
            # write that char in file
            file_handler.write(chr(value))
            # remove the index
            asciiList.pop(index)
            # insert at the front
            asciiList.insert(0, value)

def writeList(access_cost_list):
    with open("cost.txt", 'w') as file_handler:
        for j in access_cost_list:
            file_handler.write(" "+str(j))



mtf()
        