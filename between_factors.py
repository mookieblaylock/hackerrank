def isFactorOfInt(a, b):
    # does a divide evenly into b (is A a factor of B)
    if b % a == 0:
        return 'yes'
    else:
        return 'no'

def getTotalX(a, b):
    len_arr = len(arr)
    len_brr = len(brr)
    min_brr = min(brr)
    max_arr = max(arr)
  
    brr_fail = []
    brr_success = []
   
    for int_considered in range(1, 101):
        for a in range(0, len_brr):
            int_check = isFactorOfInt(int_considered, brr[a])
            if int_check == 'no':
                brr_fail.append(int_considered)
            else:
                brr_success.append(int_considered)
                
    len_brr_fail = len(brr_fail)
    len_brr_success = len(brr_success)
    
    brr_final = []

    for n in range(0, len_brr_success):
        if brr_success[n] not in brr_fail:
           brr_final.append(brr_success[n])
           
    len_brr_final = len(brr_final)
           
    double_success = []
    double_fail = []
    
    for abc in range(0, len_brr_final):  
        for xyz in range(0, len_arr):
            int_check2 = isFactorOfInt(arr[xyz], brr_final[abc])
            #print('I checked arr[xyz] with value ', arr[xyz], ' and successful_b_ints[abc] value ', brr_final[abc], ' and the result was ', int_check2)
            if int_check2 == 'no':
                double_fail.append(brr_final[abc])
            else:
                double_success.append(brr_final[abc])
                
    
    len_double_success = len(double_success)
    len_double_fail = len(double_fail)
    
    final = []
    
    for n in range(0, len_double_success):
        if double_success[n] >= max_arr and double_success[n] <= min_brr and double_success[n] not in double_fail:
            final.append(double_success[n])
    
    final_set = set(list(final)) 
    len_final_set = len(final_set)
    print(len_final_set)

  
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #first_multiple_input = input().rstrip().split()
    #n = int(first_multiple_input[0])
    #m = int(first_multiple_input[1])
    #arr = list(map(int, input().rstrip().split()))
    #brr = list(map(int, input().rstrip().split()))
    arr = [2, 4, 8]
    brr = [32, 64, 80]
    total = getTotalX(arr, brr)
    