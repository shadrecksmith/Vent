import random

char = "abcdefghijklmnopqrstuvwxyz"

char_list = list(char)
print(char_list)

inp = str(input())
query= " searching for " + str(inp)

rand_char =""
char_index = 0

#colors
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'       
while(rand_char != inp ):
    rand_char ="".join(random.sample(char_list ,len(inp)) ) 
    char_index += 1    
    char_string = str(char_index)
    
   
    print(char_string+": "+rand_char + query ) 
    while(rand_char == inp ):
        if(True):
            print ("* "*6+ GREEN+inp + ' found '+RESET+"* "*6)
            break   
           
    