# WAP to check if a list contains a pallindrome of elements or not. 

nums = list(map(int, input("Enter numbers: ").split()))

if(nums == nums[::-1]):  #nums[::-1} --> it reverses the list
    print("Pallindrome")
else:
    print("Not a pallindrome")
