def deletion_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 == 0:
        return len2
    if len2 == 0:
        return len1

  
    #E line lo last characters equal unnaya leva ani chustundi,okavela equal itey delete cheyalsina avasaram ledu 
    if str1[-1] == str2[-1]:
        #e return valla last charcters exclude avtai
        return deletion_distance(str1[:-1], str2[:-1])

 #e line work avtadi last character same kakapotey
 #dentlo last character of str1 ni remove chesi str2 tho compare chey
 #orginal str2 with short str1
 #and last character of str2 ni remove chesi str 1 tho compare chey,here original str1 and short str 2
 #min :evvi 2 values ni compare chesi min value tiskuntundi
    return 1 + min(deletion_distance(str1[:-1], str2), deletion_distance(str1, str2[:-1]))


str1 = input("enter 1st one")
str2 = input("enter 2nd one")
result = deletion_distance(str1, str2)
print("Deletion Distance:", result)
