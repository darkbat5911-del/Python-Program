# # # mylist = [0,1,2,3,4]
# # # sum = 0
# # # # count = 0
# # # # for x in mylist:
# # # #     if x<=0:
# # # #         count +=1
# # # # print(count)
# # # # for x in mylist:
# # # #     if x%2 != 0:
# # # #         sum= sum +x
# # # # print(sum)

# # n = int(input("Number"))
# # for x in range(1,11):
# #     if x == 5: 
# #         continue
# #     t = n * x 
# #     print(t)

# MyDict = {
#     "name" : "Hiren",
#     "Age" : 25,
#     "City" : "Ahmedabad" 
# }

# for x in MyDict:
#     print(x)

number = [1,-2,3,-4,5,6,-7,-8,9,10]
positive_number_count = 0
for x in number:
    if x>0:
        positive_number_count += 1 