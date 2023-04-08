def hello():
    print('Hello')

hello()

def pack(el1,el2,el3):
    return [el1,el2,el3]

print(pack(1,2,3))


def eat_lunch(lunch_list):
    if lunch_list == []:
        print('Lunch box is empty!')
    else:
        print(f'First I eat {lunch_list[0]}')
        for i in lunch_list[1:]:
            print(f'Next I eat {i}')


lunch_list = ['apple', 'pie', 'cookie']
eat_lunch(lunch_list)
