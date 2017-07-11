# coding: latin-1
# Above line for sorting special characters (like )
# Simple Sorting Thingy (integers and floats)
def printL(ul):
    out = "List: "
    out += str(ul[0])
    for i in range(1,len(ul)):
        out += ", "
        out += str(ul[i])
    return out

def sort(ul):
    for i in range(len(ul)):
        min = ul[i]
        for j in range(i,len(ul)):
            if ul[j] < min:
                min = ul[j]
                temp = ul[i]
                ul[i] = min
                ul[j] = temp
        print printL(ul)
    return ul

list = [9,7,5,3,1,2,8,4,6]
print printL(list)
sort(list)

print printL(list)