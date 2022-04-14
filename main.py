import json


def searchByFile(filename):
    data = json.load(open(f'{filename}.json'))

    search_parameters = data[0].keys()

    print(f'\n________Selected File: {filename}________\n')
    while True:
        search_input = input(
            '\nPress 1 to View All Possible Search Parameters\n(Type Quit to Exit, Type Back to Go Back to Previous Menu)\nEnter Your Choice: ')
        if search_input == '1':
            for index, parameter in enumerate(search_parameters):
                print(f'{index + 1}: {parameter}')
            print()
        elif search_input in search_parameters:
            # Searching Value
            search_result = searchByValue(search_input, data)
            results_count = len(search_result)
            if results_count:
                print(f'\n{results_count} Results Found!\n')
                for index, result in enumerate(search_result):
                    # Not needed for only 1 result value
                    if results_count != 1:
                        print(f'\nData No: {index + 1}\n')
                    for parameter in search_parameters:
                        print(f'{parameter}: {result[parameter]}')
                print()
            else:
                print('-- No Results Could be Found!\n')
        elif search_input.lower() == 'back':
            print('-- Going Back...')
            break
        elif search_input.lower() == 'quit':
            print('\n________Thanks for using the Search Software!________\n')
            exit(0)
        else:
            print('-- Wrong Search Parameter!\n')


def searchByValue(search_input, data):
    search_value = input('Enter Search Value: ')
    print('-- Searching...\n')
    result = [value for value in data if str(value[search_input]) == search_value]
    return result


if __name__ == '__main__':
    print('______Welcome to The Search Software (by Hasham)______\n\n')
    while True:
        filename = ''
        choice = input('Where do you want to Search?\n1. Users\n2. Tickets\n3. Organizations\n(Type Quit to Exit)\nEnter Choice: ')
        if choice == '1':
            filename = 'users'
        elif choice == '2':
            filename = 'tickets'
        elif choice == '3':
            filename = 'organizations'
        elif choice.lower() == 'quit':
            print('\n________Thanks for using the Search Software!________\n')
            exit(0)
        else:
            print('-- No Record Found By This File Name!')

        searchByFile(filename)



