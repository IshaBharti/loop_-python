    
#how to check alphebet 







ch = input("Enter any character: ");
if ch == '0':
    exit
else:
    if (ch>='a' and ch<='z'):
        print(ch, "is lower case alphabet.")
    elif(ch>='A' and ch<='Z'):
        print(ch,"is upper case.")
    else:
        print(ch, "is not an alphabet.");
