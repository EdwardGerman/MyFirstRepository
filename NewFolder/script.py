import requests


# Write to file
def write_file(dao, text):
    if type(text) is not str or type(dao) is not str:
        print('I eat only a lists or strings')
        raise TypeError

    try:
        with open(dao, 'x') as file:
            file.write(text)
    except FileExistsError:
        for x in range(5):
            mark_overwrite = input('File exists. Do you want overwrite this file? (y/n): ')
            if mark_overwrite in ['y', 'Y']:
                with open(dao, 'w') as file:
                    file.write(text)
                    break
            elif mark_overwrite in ['n', 'N']:
                print('No so no')
                break
            else:
                print(f'Incorrect input: "{mark_overwrite}".')
        else:
            print('No so no')


# =============================================================================
def main():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()

    string_to_write = ''
    for json_dict in data:
        text_block = json_dict['title'].capitalize() + '\n'
        for sentence in json_dict['body'].split('\n'):
            text_block += (sentence.capitalize() + '. ')
        text_block += '\n\n'
        string_to_write += text_block

    print(string_to_write)
    write_file('structured_response.txt', string_to_write)

if __name__ == "__main__":

    main()
