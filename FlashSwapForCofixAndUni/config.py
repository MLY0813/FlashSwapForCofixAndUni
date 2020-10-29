from web3 import Web3

SETTING = {
    "ROPSTEN_URL": "XXX",
    "MAINNET_URL": "XXX",
    "CONTRACT_ADDRESS": "XXX",
    "WALLET_PRIVATEKEY": "XXX",
    "WALLET_ADDRESS": "XXX",
    "ETH_SPAN": [1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900]
}

w3 = Web3(Web3.HTTPProvider(SETTING["MAINNET_URL"]))


def sendTransation(tx_dic):
    nonce = w3.eth.getTransactionCount(SETTING["WALLET_ADDRESS"])
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=SETTING["WALLET_PRIVATEKEY"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)


def sendTransationWithMoreGas(tx_dic, gwei):
    nonce = w3.eth.getTransactionCount(SETTING["WALLET_ADDRESS"])
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice + w3.toWei(gwei, 'gwei')
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=SETTING["WALLET_PRIVATEKEY"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)
