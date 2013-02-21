import random
#input data and avoid redundent data
def input_from_user(question):
    isRedundent=False
    while True:
        if isRedundent:
            print "Numbers must be different."
            isRedundent=False
        raw = raw_input(question)
        input_array = raw.split(" ")
        temp_array = [0,0,0,0,0,0,0,0,0,0]
        for i in range(0,4):
            input_array[i] = int(input_array[i])
            if(temp_array[input_array[i]] != 0):
        		isRedundent = True
        		break
            else:
        	    temp_array[input_array[i]] = 1
      	if(isRedundent==False):
            break
    return input_array

#print title
def print_title():
    print("------------------------------------")
    print("|   basball game with 4 numbers!   |")
    print("------------------------------------")

#generate random answer
def gen_answer(ea):
    answer=[]
    for int_0_to_9 in range(0,10):
     answer.append(int_0_to_9)
    random.shuffle(answer)
    arr_data = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    for i in range(0,ea):
        arr_data[answer[i]] = i;
    return arr_data

#print result
def print_result(strike,ball):
    print("------------------------------------")
    print("|     strike(s)   :    %d          |")%strike
    print("|       ball(s)   :    %d          |")%ball
    if strike < 4:
		print("|           Try again!            |")
    else:
		print("|      4 strikes and out!         |")
		print("|          Good Game!             |")
    print("------------------------------------")

#bs judgement
def judge_bs(input_array,answer,ea):
    strike= ball =0
    for i in range(0,ea):
        if answer[input_array[i]] != -1 :
            if answer[input_array[i]] == i:
                strike += 1
            else:
                ball += 1
    return (strike,ball)

#program body start
debug = True
print_title()
answer=gen_answer(4)
#for debug
if debug:
    print(answer)
#main loop
strike=0
while strike < 4:
    input_array = input_from_user("input like [1 2 3 4] : ")
    strike=ball=0
    (strike,ball) = judge_bs(input_array,answer,4)
    print_result(strike,ball)