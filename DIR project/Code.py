import os
import time



horse = ('C:\\Users\\andre\\Documents\\GitHub\\Python-Projects\\DIR project')

l_files = os.listdir(horse)

for file in l_files:
    file_path = f'{horse}\\{file}'
    print(file_path)

def openFile1():
    with open('hello.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

def openFile2():
    with open('how.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

def openFile3():
    with open('are.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

def openFile4():
    with open('you.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

def openFile5():
    with open('today.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

        
def openFile6():
    with open('my.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()




def openFile7():
    with open('name.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()


def openFile8():
    with open('is.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()



def openFile9():
    with open('andrew.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()


def openFile10():
    with open('weber.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()



print (os.path.getmtime('hello.txt'))
print (os.path.getmtime('how.txt'))
print (os.path.getmtime('are.txt'))
print (os.path.getmtime('you.txt'))
print (os.path.getmtime('today.txt'))
print (os.path.getmtime('my.txt'))
print (os.path.getmtime('name.txt'))
print (os.path.getmtime('is.txt'))
print (os.path.getmtime('andrew.txt'))        
print (os.path.getmtime('weber.txt'))



if __name__ == "__main__":
    openFile1()
    openFile2()
    openFile3()
    openFile4()
    openFile5()
    openFile6()
    openFile7()
    openFile8()
    openFile9()
    openFile10()
  









