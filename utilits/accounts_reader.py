def read_accounts_from_file():
    with open('addresses.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]