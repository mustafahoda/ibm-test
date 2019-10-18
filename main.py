import logging

def div_by_3(int):
    if int % 3 == 0:
        return True
    else:
        return False

def div_by_5(int):
    if int % 5 == 0:
        return True
    else:
        return False

def fizz_buzz(start, end):

    for i in range(start,end):
        msg = f"{i}"

        if div_by_3(i):
            msg = "Fizz"
            if div_by_5(i) == 0:
                msg = msg + " Buzz"
        elif div_by_5(i) == 0:
            msg = "Buzz"

        print (msg)



if __name__ == "__main__":
    fizz_buzz(1, 100)
