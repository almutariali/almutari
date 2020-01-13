
#1)menu is displayed

def mainMenu():
    global optionSelect
    optionSelect = int(input('MAIN MENU: \n Enter the number of what youd like to do \n    1)Enter RLE\n    2)Display ASCII Art\n    3)Convert to ASCII Art\n    4)Convert to RLE\n    5)Quit\nOption you want:'))
    
#3)allows user to enter an RLE code and displays it as ASCII
def optionOne():
    
    global lineCheck

    lineCheck = int(0)
    global lineNum
    lineNum = int(0)
    global line
    global RLElist
    
    line = int(input('How many lines of RLE compressed data do you want to enter?\n'))
    while line <= 2 or line >= 15:
        line = int(input('Please enter a number above 2 and below 15:\n'))
    
    file = open('optionOne.txt','w')

    userinput = (str(input('Enter your first line of RLE data with a space between each value:\n')))
    file.write(userinput + ' ')
    file.close()

    
    
    def Convert(string):

        li = list(string.split(' '))
        return li

    file = open('optionOne.txt', 'r')
    text = file.read()
    str1 = text
    
    RLElist = (Convert(str1))
    print(RLElist)
    
    lineLength = int(input('How long is this line'))
    from itertools import islice 
  
    def convert(lst, var_lst): 
        it = iter(lst) 
        return [list(islice(it, i)) for i in var_lst] 
      
# Driver code 
    lst = RLElist
    var_lst = [lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength,lineLength] 
    
    x = 0
    y = 1
    z = 2
    while z <= lineLength:
        code1 = convert(lst, var_lst)[0][x]*10 
        code2 = convert(lst, var_lst)[0][y]
        amountOfCode = int(code1 + code2 )
        
        firstLine = str(convert(lst, var_lst)[0][z] * amountOfCode)

        x = x+3
        y = y+3
        z = z+3
                              
                     
                     
    
    
    
    
    lineCheck = lineCheck + 1
    lineNum = lineNum + 1
    
    for i in range(1,line):
        file = open('optionOne.txt','a')
        userinput = (str(input('Enter the next line of RLE data with a space between each value:\n')))
        file.write(userinput + ' ')
        file.close()
        lineCheck = lineCheck + 1
    
        file = open('optionOne.txt', 'r')
        text = file.read()

        def Convert(string):

            li = list(string.split(' '))
            return li

        file = open('optionOne.txt', 'r')
        text = file.read()
        str1 = text
        RLElist = (Convert(str1))

        print(RLElist)

        
        linelength1 = int(input('How long is this line'))
        lengthlist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        lengthlist[i] = linelength1


        from itertools import islice 
  
        def convert(lst, var_lst): 
            it = iter(lst) 
            return [list(islice(it, i)) for i in var_lst] 
      
        lst = RLElist
        var_lst = [lineLength,lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i],lengthlist[i]]
                           
        
            

    x = 0
    y = 1
    z = 2
    
    print(firstLine)
    while z <= lengthlist[i]:
        code1 = convert(lst, var_lst)[i][x]*10 
        code2 = convert(lst, var_lst)[i][y]
        amountOfCode = int(code1 + code2 )
    
        print(convert(lst, var_lst)[i][z] * amountOfCode)
        

        x = x+3
        y = y+3
        z = z+3
    
    answer = input('\n\n\n\nPress enter to see the main menu')
        
    
#4) diplay ASCII art from an already saved file        
def optionTwo():
     fileName = str(input('Please enter the name of the file you would like to see'))
     file = open(fileName, 'r')
     text = file.read()
     print(text)

def optionThree():
    fileName = str(input("Enter the name of the file you'd like to convert into ASCII: "))
    file = open(fileName, 'r')
    text = file.read()

    def split(word): 
        return list(word) 
          
    word = (text)
    
    splitList = (split(word))
    x = 0
    y = 1
    z = 2
    while z <= len(splitList):
        while splitList[x]==('\n'):
            x = x + 1
            y = y + 1
            z = z + 1
            print('\n')
            
        
        code = int((splitList[x]))
        code1 = code * 10
        code2 = int((splitList[y]))
        amountOfCode = int(code1 + code2)
        #print(amountOfCode)
        
        print(str(splitList[z]) * amountOfCode, end ="")
        
        
        
        x = x+3
        y = y+3
        z = z+3
    Continue = str(input('\n\n\n\nPress enter to continue'))
    if Continue == (''):
        mainMenu()
    else:
        Continue == str(input('Please enter enter'))
    

    
    
    


def optionFour():
    fileName = str(input('Please enter the name of the file you would like to compress: '))
    file = open(fileName, 'r')
    text = file.read()
    def split(word): 
        return list(word)
    word = (text)
    splitList = (split(word))
    x = 0
    y = 1
    z = 0
    while x <= len(splitList):       
        while splitList[x] == splitList[x+1]:
            y = y + 1
            x = x + 1
            def createList():
                mylist = []
                for i in range(200):
                    mylist.append(i)
                return mylist
            myList = createList()
        
        
            if y < 10:
                listNum = ('0' + str(y) + str(splitList[x]))
                myList[z-1] = listNum
                print(myList)
            elif y >= 10:
                listNum = (str(y) + str(splitList[x]))
                myList[z-1] = listNum

        if splitList[x] != splitList[x+1]:
            z = z + 1
            x = x + 1
            y = 1 

        def createList():
            mylist = []
            for i in range(200):
                mylist.append(i)
            return mylist
        myList = createList()
        
        
        if y < 10:
            listNum = ('0' + str(y) + str(splitList[x-1]))
            myList[z-1] = listNum
            print(myList)
        elif y >= 10:
            listNum = (str(y) + str(splitList[x-1]))
            myList[z-1] = listNum



    print(myList)

                             
                                     
#this will cause each option which is in a function to be printed depending on what the user entered. It then prints the main menu funtion so the user can continue to use the program
def askUser():
    
    if optionSelect == 1:
        optionOne()
        mainMenu()
        askUser()
    elif optionSelect == 2:
        optionTwo()
        mainMenu()
        askUser()
    elif optionSelect == 3:
        optionThree()
        askUser()
    elif optionSelect == 4:
        optionFour()
        mainMenu()
        askUser()
    elif optionSelect == 5:
        print('Thank you for using our program, have a nice day.')
        #2)if user selects 'quit' a message is displayed              
    else:            
        print('Please enter a valid number')
        mainMenu()
        askUser()

mainMenu()
askUser()

    
            
    



