#option 1
menu = int(input("Welcome to the menu, choose from the following(number)options:\n1.Enter RLE\n2.Display ASCII art\n3.Convert to ASCII art\n4.Convert to RLE\n5.Quit"))
if menu == 1:
    def op1():
        con = 0
        while con == 0:
            decom = int(input("How many lines of RLE compressed data do you want to enter"))
            con = con +1
            line_ns = 0
            while decom <= 2 and line_ns == 0:
                print("Number has to be greater than 2 in order for the action to proceed")
                con = con - 1
                line_ns = line_ns + 1
    
            con = con - 1
            con = con+1
            def decompress (string):
                decom2 = str("Enter your lines of RLE one line at a time")
                string = string.split('\n')
                print(string)
                pl = ()
                for i in string:
                    pl.append(splitCount(i,3))

                output =''
                for i in pl:
                    for m in i:
                        print(m)
                        output = output + (m[2]*int(m[0:2]))
                    output = output + '\n'
                print(output)
            decompress(str)
    op1()

    def splitCount(s, count):
            return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]   
#option 2
if menu == 2:
    u_file = input("What is your file name that contains the ASCII art " )
    open_f = open('u_file'+'.txt', 'r')
    print(open_f.readlines())
    opem_file.close()
#option 3
if menu == 3:
     u_file = input("What is your file name that contains the ASCII art " )
     open_f = open('u_file'+'.txt', 'r')





#option 4
if menu == 4:
    u_file = input("What is your file name that contains the ASCII art " )
    open_f = open('u_file'+'.txt', 'r')
    
    


