
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
            #function from the internet which gathers the characters     
            def splitCount(s, count):
                return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]


            def decompress(string):
                #a new line between the string is created
                string = string.split('\n')
                print(string)
                pl = []
                for i in string:
                
                    pl.append(splitCount(i,3))

                output =''
                for i in pl:
                    for m in i:
                        print(m)
                        output = output + (m[2]*int(m[0:2]))
                    output = output + '\n'
                print(output)
            decom2 = input("Enter your RLE data")
            y = decompress(decom2)
            print(y)
            r = 0
            if r == 0:
                menu = int(input("Welcome back to the menu, choose from the following(number)options:\n1.Enter RLE\n2.Display ASCII art\n3.Convert to ASCII art\n4.Convert to RLE\n5.Quit"))
                
                    

            
                                    
#option 2
elif menu == 2:
        #user is asked to input their file name so it can be displayed
    file = input("What is your file name that contains the ASCII art(without the .txt extension)")
    open_f = open(file + '.txt', 'r')
    read_f = open_f.read()
    print("File =\n" + read_f)
    open_f.close()
    r = 0
    if r == 0:
        menu = int(input("Welcome back to the menu, choose from the following(number)options:\n1.Enter RLE\n2.Display ASCII art\n3.Convert to ASCII art\n4.Convert to RLE\n5.Quit"))
    
#option 3
elif menu == 3:
    def splitCount(s, count):
        return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]


    def decompress(string):
        string = string.split('\n')
        print(string)
        pl = []
        for i in string:
            pl.append(splitCount(i,3))

        output =''
        for i in pl:
            for m in i:
                print(m)
                output = output + (m[2]*int(m[0:2]))
            output = output + '\n'
        print(output)            
    #user is again asked to enter file name which can then be decompressed 
    u_file = input("What is your file name that contains the ASCII art(without the .txt extension)  " )
    open_f = open(u_file + '.txt', 'r')
    read_f = open_f.read()
    y = decompress(read_f)
    print(y)
    open_f.close()
    r = 0
    if r == 0:
        menu = int(input("Welcome back to the menu, choose from the following(number)options:\n1.Enter RLE\n2.Display ASCII art\n3.Convert to ASCII art\n4.Convert to RLE\n5.Quit")) 





#option 4
elif menu == 4:
    #compression function is inputted
    def compress(data):
        encoding = ''
        prev_char = ''
        count = 1

        if not data: return ''

        for char in data:
            # If the prev and current characters
            # don't match...
            if char != prev_char:
                # ...then add the count and character
                # to our encoding
                if prev_char:
                        
                    encoding += str(count) + prev_char
                count = 1
                prev_char = char
            else:
                # Or increment our counter
                # if the characters do match
                count += 1
        else:
            # Finish off the encoding
            encoding += str(count) + prev_char
            return encoding
    u_file = input("What is your file name that contains the ASCII art(without the .txt extension)  " )
    open_f = open(u_file + '.txt', 'r')
    read_f = open_f.read()
    y = compress(read_f)
    print(y)
    num_of_chars_f = len(read_f)
    
    num_of_chars_c = len(y)
    print("\nThe difference in characters between the compressed and normal file is", num_of_chars_f - num_of_chars_c)
    open_f.close()
    r = 0
    if r == 0:
     menu = int(input("\nWelcome back to the menu, choose from the following(number)options:\n1.Enter RLE\n2.Display ASCII art\n3.Convert to ASCII art\n4.Convert to RLE\n5.Quit"))

else:
        print("There isn't a an option as such")





