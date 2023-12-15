def stack(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.insert(0, new_element)
        return our_list
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
        return our_list
    else:
        print(f'The operation {operation} is invalid, please enter add or remove')

def queue(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
        return our_list
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
        return our_list
    else:
        print(f'The operation {operation} is invalid, please enter add or remove')

# Example usage
new_list = [1, 2, 3, 4]

print("Adding a new element to the stack")
new_list = stack(new_list, 'add', 0)
print(new_list)

print("Removing an element from the stack")
new_list = stack(new_list, 'remove')
print(new_list)

print("Adding new element to the queue")
new_list=queue(new_list,'add',5)
print(new_list)

print("Adding remove an element from the queue")
new_list=queue(new_list,'remove')
print(new_list)
