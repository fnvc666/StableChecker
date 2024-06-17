import os
import time

import inquirer
from colorama import init, Fore, Style

import components
from utilits.accounts_reader import read_accounts_from_file


init()
g_text = Fore.LIGHTGREEN_EX
w_text = Fore.LIGHTWHITE_EX
r_text = Fore.LIGHTRED_EX
reset_text = Style.RESET_ALL

available_chains = ['ETH', 'BNB', 'ARB', 'OP']
available_coins = ['USDT', 'USDC', 'DAI']

chains = []
coins = []


def select_items():
    global chains, coins
    questions = [
        inquirer.Checkbox('chains',
                          message="Select chains",
                          choices=available_chains,
                          default=chains),
        inquirer.Checkbox('coins',
                          message="Select coins",
                          choices=available_coins,
                          default=coins)
    ]

    answers = inquirer.prompt(questions)

    chains = answers.get('chains', [])
    coins = answers.get('coins', [])

    print(w_text + 'Selected chains: ' + g_text + ', '.join(chains) + reset_text)
    print(w_text + 'Selected coins: ' + g_text + ', '.join(coins) + reset_text)


if __name__ == "__main__":
    print(w_text +
          'Available chains:\n' + g_text +
          ', '.join(available_chains)
          + reset_text)
    print(w_text +
          'Available coins:\n' + g_text +
          ', '.join(available_coins)
          + reset_text)

    select_items()

    print('Wait for 5 seconds...')
    time.sleep(5)
    os.system('cls')

    for account in read_accounts_from_file():
        print(w_text + f'ADDRESS : {account}' + reset_text)
        account = account.lower()
        for chain in chains:
            print(w_text + f'\nCHAIN : {chain}' + reset_text)
            component_chain = components.Chain(account, chain)
            for coin in coins:
                func_to_call = getattr(component_chain, coin.lower())
                if func_to_call() == 0:
                    print(r_text + f'{coin} : {func_to_call()}' + reset_text)
                else:
                    print(g_text + f'{coin} : {func_to_call()}' + reset_text)
        print('\n')
    input("Press Enter to close...")
