def getNum(file_name):# Function to read the input file
    "It will read the input file and check the number range"
    global n
    try:
        input_file=open(file_name,"r")
        n=int(input_file.read())
        if 0<=n<=20:
            return n
        else:
            print("Invalid input.")
    except FileNotFoundError:
        print("File is not found")
    

def calculate_fib(num):#Function to Calculate the fibinacci number
    "It is calculate the fibbinacci number for that input number"
    if num!=None:#When previous function is return that input number then calculate the fibonacci
        fib_0=0
        fib_1=1
        if num==0:
            fib=0
        elif num==1 or num==2:
            fib=1
        else:
            fib_1=fib_2=1
            fib=0
            for i in range(2,num):
                fib=fib_1+fib_2
                fib_1=fib_2
                fib_2=fib
        return fib

        
def show(fibb):#Function to Display the output value on screen
    if fibb != None:
        print("Fibonacci("+str(n)+") = "+str(fibb))
        return fibb
    
def saveFile(output):#Function to write the output in text file
    if output != None:
        out_put=open("result.txt","w")
        out_put.write("Fibonacci("+str(n)+") = "+str(output))
        out_put.close()
#Main program        
input_file=input()
read_n=getNum(input_file)
caculation= calculate_fib(read_n)
show(caculation)
saveFile(caculation)
