from web3 import Web3
from data.config import rpc


class Chain:

    def __init__(self, address, chain):
        self.address = Web3.to_checksum_address(address)
        self.chain = chain
        self.web3 = Web3(Web3.HTTPProvider(rpc[self.chain]['rpc']))

    def usdt(self):
        usdt_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function",
            },
        ]
        usdt_contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(rpc[self.chain]['usdt_contract_address']),
            abi=usdt_abi)
        balance = usdt_contract.functions.balanceOf(self.address).call()
        return balance / 10 ** 6

    def usdc(self):
        usdc_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function",
            },
        ]
        usdc_contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(rpc[self.chain]['usdc_contract_address']),
            abi=usdc_abi)
        balance = usdc_contract.functions.balanceOf(self.address).call()
        return balance / 10 ** 6

    def dai(self):
        dai_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function",
            },
        ]
        dai_contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(rpc[self.chain]['dai_contract_address']),
            abi=dai_abi)
        balance = dai_contract.functions.balanceOf(self.address).call()
        return balance / 10 ** 18
