#!/usr/bin/env python 



def is_vowel(s):
    length = 0 
    vowel = ["a", "e", "i" ,"o", "u"]
    for itm in s:
        length +=1
    if length == 1:
        if itm in vowel:
	    print "yes it is vowel "
	else:
	    print "no this is not a vowel"
    else:
        print " Entered input  is not a single character "
    
        
    
    return length 

if __name__=="__main__":
    ch =  str(raw_input("Enter a single charchter: "))
    is_vowel(ch)

