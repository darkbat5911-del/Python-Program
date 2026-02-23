# Normal 

# def even_generate(limit):
#     for i in range(2, limit+1,2):
#         print(i)
# even_generate(5)

# yield

def even_genera(l):
    for i in range(2, l+1,2):
        yield i
for num in even_genera(95):
    print(num)
    