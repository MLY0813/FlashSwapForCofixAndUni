from web3 import Web3
from config import SETTING
from config import w3


abi = """[{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"components":[{
"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"number",
"type":"uint256"}],"internalType":"struct Account.Info","name":"account","type":"tuple"},{"internalType":"bytes",
"name":"data","type":"bytes"}],"name":"callFunction","outputs":[],"stateMutability":"nonpayable","type":"function"},
{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"initiateFlashLoan","outputs":[],
"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"moreETH","outputs":[],
"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount",
"type":"uint256"}],"name":"setCofixETHSapn","outputs":[],"stateMutability":"nonpayable","type":"function"},
{"inputs":[{"internalType":"address","name":"_cofixRouter","type":"address"}],"name":"setCofixRouter","outputs":[],
"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount",
"type":"uint256"}],"name":"setNestPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{
"internalType":"address","name":"_newMan","type":"address"}],"name":"setSuperMan","outputs":[],
"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_uniRouter",
"type":"address"}],"name":"setUniRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{
"internalType":"uint256","name":"amount","type":"uint256"}],"name":"turnOutETH","outputs":[],
"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token",
"type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"turnOutToken","outputs":[],
"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},
{"stateMutability":"payable","type":"receive"},{"inputs":[],"name":"getCofixETHSapn","outputs":[{
"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],
"name":"getCofixRouter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view",
"type":"function"},{"inputs":[],"name":"getETHBalance","outputs":[{"internalType":"uint256","name":"",
"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNestPrice","outputs":[{
"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],
"name":"getSuperMan","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view",
"type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"getTokenBalance",
"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
{"inputs":[],"name":"getUniRouter","outputs":[{"internalType":"address","name":"","type":"address"}],
"stateMutability":"view","type":"function"}] """

contractObj = w3.eth.contract(address=Web3.toChecksumAddress(SETTING["CONTRACT_ADDRESS"]), abi=abi)


def initiateFlashLoan(ethAmount):
    tx_dix = contractObj.functions.initiateFlashLoan(ethAmount).buildTransaction({
        'from': SETTING["WALLET_ADDRESS"],
        'gas': 1200000
    })
    return tx_dix


