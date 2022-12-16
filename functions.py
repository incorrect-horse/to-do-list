FILEPATH = 'files/todos.txt'

def get_todo_list(todo_list=FILEPATH):
    """ This is a doc string, for commenting code """
    with open(todo_list, 'r') as file_read:
        todo_read = file_read.readlines()
    return todo_read


def write_todo_list(todo_write, todo_list=FILEPATH):
    with open(todo_list, 'w') as file_write:
        file_write.writelines(todo_write)


#print(__name__)

if __name__ == "__main__":
    print(get_todo_list('files/todos.txt'))
elif __name__ == "functions":
    print(f"{__name__}.py imported")