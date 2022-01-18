# iterate from end to start of list to remove zeros
def removeZeros(poly):
    for i in range(len(poly)-1,0,-1):
        if poly[i] == 0:
            poly.pop(i)
        else:
            break
    return poly

# add one polynomial to another
def addPoly(poly1,poly2):
    result = []
    for i in range(min(len(poly1),len(poly2)),max(len(poly1),len(poly2)),1): # compare the size of the 2 lists
        if min(len(poly1),len(poly2)) == len(poly2):
            poly2.append(0) # fill the empty space of smallest list with zeros
        else:
            poly1.append(0)
    for i in range(len(poly1)):
        result.append(poly1[i] + poly2[i]) # addition of the 2 lists of now same size
    return result

# multiply one polynomial to a const
def constPoly(poly,const):
    result = []
    for i in range(len(poly)):
        result.append(poly[i] * const) # multiplication
    return result

def factPoly(poly1,poly2):
    result = []
    poly1 = removeZeros(poly1)
    poly2 = removeZeros(poly2)
    for i in range(len(poly1)):
       for j in range(len(poly2)):
           result.append(poly1[i] * poly2[j])
    return result


# Test
liste = [0,1,2,3,4]
liste2 = [1,2,0,0,3,4,0]

print(addPoly(liste,liste2))
print(constPoly(liste,3))
print(factPoly(liste,liste2))
