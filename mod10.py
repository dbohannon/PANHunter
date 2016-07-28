#mod10 module to determine if suspected number is in valid PAN format
#obtained partial code from public sourcecode, written by E. Fulkerson at www.elifulkerson.com

def doubler(digit):
    "Double digit, add its digits together if they are >= 10"
    digit = int(digit)
    digit = digit * 2
    
    if digit < 0:
        print("Error!  digit < 0 sent: " + str(digit))
        sys.exit(1)

    if digit > 18:
        print("Error!  digit > 18 sent: " + str(digit))
        sys.exit(1)

    if digit < 10:
        return digit

    return digit - 9

def reverse(str):
    "Reverse the string str"
    buf = ""
    a = 0
    while (a < len(str)):
        a += 1
        buf += str[-a]
    return buf
    
def check(cc):
    "Given a cc number (string), will return True if it passes mod10 check, False otherwise"
    cc = reverse(cc)

    a = 0
    total = 0
    while (a < len(cc)):
           if (a % 2) == 1:
               total = total + doubler(cc[a])
           else:
               total = total + int(cc[a])
           a += 1

    if (total % 10) == 0:
        return True
    else:
        return False
