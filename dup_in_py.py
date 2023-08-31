""" Goal is to be able to tell if there is the same file regardless of the file name. 
    Purpose for now is for this program to be able to work with image files """
import os
import re

""" Search through the dir for only jpg files """
def only_scan_jpg( array ):
    temp = array
    index_to_remove = [] 
    for i in range(len(array)):
        if re.search(".*JPG", array[i]) == None:
              index_to_remove.append(array[i])
    for element in index_to_remove:
        temp.remove(element)
    return   temp   
        
""" Return an array with the binary data """
def load_file(file_path):
    ret  = [] 
    try:
        with open(file_path,"rb") as binary_file:
            binary_data = binary_file.read()
    except FileNotFoundError:
        print("File was not Found. -----> "+ str(file_path))
    except IOError:
        print("Error reading the file")
    for byte in binary_data:
        ret.append(byte)
    binary_file.close
    
    return ret

""" Return a dictonary with the files and the binary data"""
def load_jpg_dir( ):
    file_path_array = only_scan_jpg(os.listdir())
    ret = {} 
    for file in file_path_array:
        data = load_file(file)
        ret[file] = data
    return ret
        
        
" Check to see if the array contains the same information"
def compare_array(array1 , array2):
    if len(array1) != len(array2):
        return False
    for i in  range(len(array1)):
        if array1[i] != array2[i]:
            return False 
    
    return True
""" Using an array . Creates a dic with key set as the array value and the value set as a boolean """
def create_pass_thru_map(array):
    ret = {} 
    for i in range(len(array)):
        ret[array[i]] = False
    return ret
def create_rel_map(array):
    ret = {}
    for i in range (len(array)):
        ret[array[i]]= []
    return ret 
def print_pretty(dic):
    for key in dic:
        if dic[key] == []:
            continue
        print("File Name ----> "+str(key) + "Is similar to ------>"+str(dic[key]))
def trim_rel_map(dic):
    ret = {} 
    for key in dic:
        if dic[key] == []:
            continue
        ret[key] = dic[key]
    return ret
        
""" Sudo Code for how to compare all files in one directory to each other 
 Steps 
 1. Scan the directory for all the files with extension jpeg 
 2. Create a dic to have key as filename and value as passed through or not 
 3. Create another dictonary with key  as file name and value as all same files
 4. Scan through each file and compare them to one another .
 5. If a match is found mark that file as passed through and mark that key as passed through 
 6. Add it to  the dictonary file 
 7. Continue untill all keys have been scanned 
 
 Returns a dictonary with file name and relative files 
 """
def check_dir():
     data = load_jpg_dir()
     jpg_file_list = only_scan_jpg(os.listdir())
     pass_thru = create_pass_thru_map(jpg_file_list)
     rel_map = create_rel_map(jpg_file_list)
     """ Check files against files here """
     max_len = len(jpg_file_list)
     for i in range(len(jpg_file_list)):
         curr_p = (i/max_len)*100
         print(curr_p)
         if pass_thru[jpg_file_list[i]]:
             continue
         for j in range(i+1, len(jpg_file_list)):
            curr_p = (j/max_len)*100
            print(curr_p)
            if  compare_array(data[jpg_file_list[i]], data[jpg_file_list[j]]):
                pass_thru[jpg_file_list[j]] = True
                curr_ar = rel_map[jpg_file_list[i]]
                curr_ar.append(jpg_file_list[j]) 
                rel_map[jpg_file_list[i]] = curr_ar
     return trim_rel_map(rel_map)

