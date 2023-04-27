from StrangeContainer import StrangeContainer


inf = '\tadd <key> [key, ...] - add one or more elements to the container'\
      '\n\tremove <key> - delete key from container'\
      '\n\tfind - <key> [key, ...] - check if the element is presented in the container'\
      '\n\tlist - print all elements of container'\
      '\n\tgrep <regex> - check the value in the container by regular expression'\
      '\n\tsave - save container to file'\
      '\n\tswitch - switches to another user' \


def start_task2():
    user = input('Enter a username: ')
    container = StrangeContainer(user)

    print('\nSuccess!'
          '\n"info" or "i" for more information!\n')

    current = True
    while current:
        command, elements = user_input()
        current = current_command(command, elements, container)


def user_input():
    command_input = input('>> ').split(maxsplit=1)
    command = command_input[0]
    elements = str()

    if len(command_input) > 1:
        elements = command_input[1]

    return command, elements


def current_command(command, elements, container: StrangeContainer):
    match command:
        case 'add':
            element = elements.split()
            for i in element:
                container.add(i)
        case 'remove':
            if elements in container.list():
                container.remove(elements)
            else:
                print(f'Element {elements} not found')
        case 'find':
            element = elements.split()
            for i in element:
                el = container.find(i)
                if el:
                    print(f'Element "{el}" found')
                else:
                    print(f'Element "{el}" not found')
        case 'list':
            print(container.list())
        case 'grep':
            element = container.grep(elements)
            if len(element) != 0:
                print('Found values: ', element)

        case 'save':
            container.save()

        case 'load':
            path = input('Enter path:')
            container.load_from_file(path)
        case 'switch':
            answer = input('Do you want save container before exit? (y/n) ')
            if answer == 'y':
                container.save()
            container.switch(elements)
            answer = input('Do you want load container before exit? (y/n) ')
            if answer == 'y':
                container.load()

        case 'info' | 'i':
                    print(f'INFO:\n{inf}')
        case 'stop':
            answer = input('Do you want save container before exit? (y/n) ')
            if answer == 'y':
                container.save()
            return False
        case _:
            print(f'There is no such command: {command}')

    return True