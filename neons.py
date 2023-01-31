from web3 import Web3
import json
import requests
import time

web3 = Web3(Web3.HTTPProvider('https://canto.slingshot.finance/'))

# Contract Address
address = '0x157B312d199031afC82D77a34269D3Da51436afd'
abi = json.loads('[{"type":"event","name":"AuctionBid","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"address","name":"sender","internalType":"address","indexed":false},{"type":"uint256","name":"value","internalType":"uint256","indexed":false},{"type":"bool","name":"extended","internalType":"bool","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionCreated","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"uint256","name":"startTime","internalType":"uint256","indexed":false},{"type":"uint256","name":"endTime","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionExtended","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"uint256","name":"endTime","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionMinBidIncrementPercentageUpdated","inputs":[{"type":"uint256","name":"minBidIncrementPercentage","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionReservePriceUpdated","inputs":[{"type":"uint256","name":"reservePrice","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionSettled","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"address","name":"winner","internalType":"address","indexed":false},{"type":"uint256","name":"amount","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionTimeBufferUpdated","inputs":[{"type":"uint256","name":"timeBuffer","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":true},{"type":"address","name":"newOwner","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"Paused","inputs":[{"type":"address","name":"account","internalType":"address","indexed":false}],"anonymous":false},{"type":"event","name":"Unpaused","inputs":[{"type":"address","name":"account","internalType":"address","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"nounId","internalType":"uint256"},{"type":"uint256","name":"amount","internalType":"uint256"},{"type":"uint256","name":"startTime","internalType":"uint256"},{"type":"uint256","name":"endTime","internalType":"uint256"},{"type":"address","name":"bidder","internalType":"address payable"},{"type":"bool","name":"settled","internalType":"bool"}],"name":"auction","inputs":[]},{"type":"function","stateMutability":"payable","outputs":[],"name":"createBid","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"duration","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"initialize","inputs":[{"type":"address","name":"_nouns","internalType":"contract INounsToken"},{"type":"address","name":"_weth","internalType":"address"},{"type":"uint256","name":"_timeBuffer","internalType":"uint256"},{"type":"uint256","name":"_reservePrice","internalType":"uint256"},{"type":"uint8","name":"_minBidIncrementPercentage","internalType":"uint8"},{"type":"uint256","name":"_duration","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"minBidIncrementPercentage","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"contract INounsToken"}],"name":"nouns","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"pause","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"paused","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"renounceOwnership","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"reservePrice","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setMinBidIncrementPercentage","inputs":[{"type":"uint8","name":"_minBidIncrementPercentage","internalType":"uint8"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setReservePrice","inputs":[{"type":"uint256","name":"_reservePrice","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setTimeBuffer","inputs":[{"type":"uint256","name":"_timeBuffer","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"settleAuction","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"settleCurrentAndCreateNewAuction","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"timeBuffer","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"transferOwnership","inputs":[{"type":"address","name":"newOwner","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"unpause","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"weth","inputs":[]}]')

contract = web3.eth.contract(address=address, abi=abi)
PRIVATE_KEY = ""
chain_id = web3.eth.chain_id
# Your Address
caller = ""

while True:
    try:
        auction = contract.functions.auction().call()
        noun_id = auction[0]
        current_bid = auction[1]
        nonce = web3.eth.getTransactionCount(caller)
        print(auction)
        print("Current bid in Canto: " + str(current_bid / 1000000000000000000))

        y = str(noun_id)
        url = "https://api2.alto.build/subgraphs/name/canto/froggie"
        payload="{\"query\":\"{\\n  noun(id: " + y +") {\\n    id\\n    seed {\\n      background\\n      body\\n      accessory\\n      head\\n      glasses\\n      __typename\\n    }\\n    owner {\\n      id\\n      __typename\\n    }\\n    __typename\\n  }\\n}\",\"variables\":null,\"extensions\":{\"headers\":null}}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept': 'application/json, multipart/mixed',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://api2.alto.build/subgraphs/name/canto/froggie/graphql?query=^%^7B^%^0A++noun^%^28id^%^3A+41^%^29+^%^7B^%^0A++++id^%^0A++++seed+^%^7B^%^0A++++++background^%^0A++++++body^%^0A++++++accessory^%^0A++++++head^%^0A++++++glasses^%^0A++++++__typename^%^0A++++^%^7D^%^0A++++owner+^%^7B^%^0A++++++id^%^0A++++++__typename^%^0A++++^%^7D^%^0A++++__typename^%^0A++^%^7D^%^0A^%^7D^%^0A',
            'content-type': 'application/json',
            'Origin': 'https://api2.alto.build',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        seed = json.loads(response.text)['data']['noun']['seed']
        print(seed)
        body_seed = seed['body']

        # 120 Canto for non-rare
        MAX_BID = 120000000000000000000

        if body_seed == 1:
            # Bid for NEO up to 1.5k Canto
            MAX_BID = 1500000000000000000000

        if auction[4] == caller or current_bid > MAX_BID:
            print("Top bidder or above max price... Sleeping")
            time.sleep(8)
            
        else:
            my_bid = 100000000000000000000
            if current_bid != 0:
                # Beat top bid by 3 Canto
                my_bid = current_bid+3000000000000000000
            print("Bidding: " + str(my_bid / 1000000000000000000 ))
            call_function = contract.functions.createBid(noun_id).buildTransaction({
                "chainId": chain_id,
                'gas': 110000,
                "from": caller,
                "nonce": nonce,
                'maxFeePerGas': 7260000000000,
                'maxPriorityFeePerGas': 148806250000,
                "value": my_bid
            })
            signed_txn = web3.eth.account.sign_transaction(
            call_function, private_key=PRIVATE_KEY)
            txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            res = web3.eth.wait_for_transaction_receipt(txn_hash)
            print(res)
            time.sleep(8)
    except:
        print("prob too many request")
        time.sleep(5)
