def insertion_sort(a_list):
    for index in range(1,len(a_list)):
        current_value=a_list[index] # record current value
        position=index   # record position


        # if front value is larger that current value then switch
        # and record position
        while position>0 and a_list[position-1]>current_value:
            a_list[position]=a_list[position-1]
            position=position-1
        
        # finally put the current value in the right place
        a_list[position]=current_value

a_list=[54,26,93,17,77,31,44,55,20]
# import pdb
# pdb.set_trace()
insertion_sort(a_list)
print(a_list)
