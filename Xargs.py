
def stu(*elements):
    print(elements)
    print(elements[0])

def add(*numbers):
    sum=0

    for x in numbers:
        sum=sum+x
    print(sum)

stu(101,"dfgh",3)
stu(1,2,3,4)

add(1,2,3)
add(1,2,3,4,5,6)
#https://www.youtube.com/watch?v=MuK3ggxQK9A&list=PLgH5QX0i9K3rz5XqMsTk41_j15_6682BN&index=39
#debug: https://www.youtube.com/watch?v=ClS458qN-1c&list=PLgH5QX0i9K3rz5XqMsTk41_j15_6682BN&index=40


