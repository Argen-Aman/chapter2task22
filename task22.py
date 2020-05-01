num_list = input('Type some digits (don\'t forget to put commas between them): ')
num_list = num_list.split(', ')

def new_list (num_list):
    positive = []
    negative = []
    zeros = []
    for i in num_list:  
        if int(i) > 0:
            positive.append(i)
        elif int(i) < 0:
            negative.append(i)
        else:
            zeros.append(i)
    print('Positive digits: ' + str(positive))
    print('Negative digits: ' + str(negative))
    print('Zeros: ' + str(zeros))
new_list (num_list)
