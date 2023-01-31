from web3 import Web3
import json
import time

web3 = Web3(Web3.HTTPProvider('https://canto.slingshot.finance/'))
web3.eth.get_block('latest')

address = '0x157B312d199031afC82D77a34269D3Da51436afd'
abi = json.loads('[{"type":"event","name":"AuctionBid","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"address","name":"sender","internalType":"address","indexed":false},{"type":"uint256","name":"value","internalType":"uint256","indexed":false},{"type":"bool","name":"extended","internalType":"bool","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionCreated","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"uint256","name":"startTime","internalType":"uint256","indexed":false},{"type":"uint256","name":"endTime","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionExtended","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"uint256","name":"endTime","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionMinBidIncrementPercentageUpdated","inputs":[{"type":"uint256","name":"minBidIncrementPercentage","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionReservePriceUpdated","inputs":[{"type":"uint256","name":"reservePrice","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionSettled","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256","indexed":true},{"type":"address","name":"winner","internalType":"address","indexed":false},{"type":"uint256","name":"amount","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"AuctionTimeBufferUpdated","inputs":[{"type":"uint256","name":"timeBuffer","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":true},{"type":"address","name":"newOwner","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"Paused","inputs":[{"type":"address","name":"account","internalType":"address","indexed":false}],"anonymous":false},{"type":"event","name":"Unpaused","inputs":[{"type":"address","name":"account","internalType":"address","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"nounId","internalType":"uint256"},{"type":"uint256","name":"amount","internalType":"uint256"},{"type":"uint256","name":"startTime","internalType":"uint256"},{"type":"uint256","name":"endTime","internalType":"uint256"},{"type":"address","name":"bidder","internalType":"address payable"},{"type":"bool","name":"settled","internalType":"bool"}],"name":"auction","inputs":[]},{"type":"function","stateMutability":"payable","outputs":[],"name":"createBid","inputs":[{"type":"uint256","name":"nounId","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"duration","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"initialize","inputs":[{"type":"address","name":"_nouns","internalType":"contract INounsToken"},{"type":"address","name":"_weth","internalType":"address"},{"type":"uint256","name":"_timeBuffer","internalType":"uint256"},{"type":"uint256","name":"_reservePrice","internalType":"uint256"},{"type":"uint8","name":"_minBidIncrementPercentage","internalType":"uint8"},{"type":"uint256","name":"_duration","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"minBidIncrementPercentage","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"contract INounsToken"}],"name":"nouns","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"pause","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"paused","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"renounceOwnership","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"reservePrice","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setMinBidIncrementPercentage","inputs":[{"type":"uint8","name":"_minBidIncrementPercentage","internalType":"uint8"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setReservePrice","inputs":[{"type":"uint256","name":"_reservePrice","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setTimeBuffer","inputs":[{"type":"uint256","name":"_timeBuffer","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"settleAuction","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"settleCurrentAndCreateNewAuction","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"timeBuffer","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"transferOwnership","inputs":[{"type":"address","name":"newOwner","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"unpause","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"weth","inputs":[]}]')

contract = web3.eth.contract(address=address, abi=abi)
PRIVATE_KEY = ""
chain_id = web3.eth.chain_id
caller = ""

while True:
    try:
        auction = contract.functions.auction().call()
        noun_id = auction[0]
        current_bid = auction[1]
        nonce = web3.eth.getTransactionCount(caller)
        print(auction)
        print("Current bid in Canto: " + str(current_bid / 1000000000000000000))

        if auction[4] == caller or current_bid > 120000000000000000000:
            print("Top bidder or above max price... Sleeping")
            time.sleep(8)
            
        else:
            my_bid = 100000000000000000000
            if current_bid != 0:
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