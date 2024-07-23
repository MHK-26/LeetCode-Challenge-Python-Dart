
def isomorphicStrings(array1,array2):
   
    if(len(array1) != len(array2)):
      return False
    hashMap1,hashMap2 = {},{}
   
    for i in range(len(array1)):
        if  array1[i] not in  hashMap1:
            hashMap1[array1[i]]= array2[i]
        if  array2[i] not in  hashMap2:
            hashMap2[array2[i]]= array1[i]
        if hashMap1[array1[i]] != array2[i] or hashMap2[array2[i]] != array1[i]:
            return False
    

    return True








print(isomorphicStrings("green","abced"))