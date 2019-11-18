
#Here the user has been given easy and clear access to the menu where they're given an option to enter what they want
menu = int(input("Welcome to the menu, choose from the following(number)options:\n1.Enter RLE\n2.Display ASCII art\n3.Convert to ASCII art\n4.Convert to RLE\n5.Quit"))
#option1
if menu == 1:
    
        con = 0
        while con == 0:
            #Straight forward instructions about the option they chose 
            decom = int(input("How many lines of RLE compressed data do you want to enter"))
            con = con + 1
            line_ns = 0
            while decom <= 2 and line_ns == 0:
                #As stated in the instructions, if the user is wanting to input a number of lines below 2 or equal to it, and friendly message is outputted 
                print("Number has to be greater than 2 in order for the action to proceed")
                line_ns = line_ns + 1
            
            def decode(mstr):
                    ret_str = ''

                    if mstr != '':
                        for i in range(0,len(mstr),2):
                            num = int(mstr[i])
                            ch = mstr[i+1]
                            ret_str = ret_str + ch*num
                    return ret_str



            decom2 = input("Enter your RLE data line by line")
            y = decode(decom2)
            print(y)
             
                    

            
                                    
#option 2
elif menu == 2:
    file = input("What is your file name that contains the ASCII art")
    open_f = open(file + '.txt', 'r')
    read_f = open_f.readlines()
    open_f.close()
    
#option 3
if menu == 3:
     u_file = input("What is your file name that contains the ASCII art " )
     open_f = open(u_file+'.txt', 'r')
     open_f.close()





#option 4
if menu == 4:
    u_file = input("What is your file name that contains the ASCII art " )
    open_f = open('u_file'+'.txt', 'r')




else:
        print("There isn't a an option as such")





