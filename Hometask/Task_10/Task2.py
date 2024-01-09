
with open(f'text.txt', 'w') as file:
    file.write(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore \n'
        'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut \n'
        'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse \n'
        'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \n'
        'culpa qui officia deserunt mollit anim id est laborum.'
    )


with open(f'text.txt', 'r') as input_file, open(f'text2.txt', 'w') as output_file:
    data = input_file.read()
    output_file.write(data.upper())
