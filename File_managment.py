import os
import dup_in_py as dp 
dataset = dp.check_dir()


def  choose_file_to_keep(array):
    list_num = 0 
    for  item in array:
        print ( str(list_num)  + "  : "+str(item))
        list_num = list_num +1 
    user_choice = input("Hit the number that u want to keep ")
    ret =[] 
    for i in range(len(array)):
        if str(i) == user_choice:
            continue
        ret.append(array[i])
    
    return ret

""" Create an array with all the files listed """
def parse_dataset():
    files_to_be_deleted = []
    for key in dataset:
        temp = dataset[key]
        temp.append(key)
        files_to_be_deleted.append(choose_file_to_keep(temp))
    for r in files_to_be_deleted:
        remove_file_list(r) 


""" Given an array of files name. Delete files in that array """
def remove_file_list( array ):
    for file in array:
        try:
            os.remove(file)
        except OSError: 
            print("Sorry file was not found")
    return True    

parse_dataset()