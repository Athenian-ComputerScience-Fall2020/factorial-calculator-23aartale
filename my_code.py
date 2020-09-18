# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  nate copeland & Beginners Book

def factorial_calc(num):
    if num == 0:
        return 1
    else:
        return num * factorial_calc(num-1)   
    return 

if __name__ == '__main__':
    
    num=int(input("Input a number to compute the factiorial : "))
    print(factorial_calc(num))
