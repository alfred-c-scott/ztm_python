try:
    with(open('sad.txt', mode='r')) as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print(f'file does not exist {err}')
except IOError as err:
    print(f'IO error {err}')
