from web3 import Web3
import time
from config import INFURA_URL, AMOUNT_ETH, GAS_LIMIT, GAS_PRICE_GWEI, CHAIN_ID, DELAY_SECONDS

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.is_connected():
    print("Failed to connect to Base network")
    exit()

def read_wallets(filename):
    sender_address = None
    sender_private_key = None
    receivers = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            sender_address, sender_private_key = lines[0].strip().split(',')
            sender_address = w3.to_checksum_address(sender_address)
            receivers = [w3.to_checksum_address(line.strip()) for line in lines[1:] if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        exit()
    except IndexError:
        print("Error: wallets.txt must have at least one sender and one receiver")
        exit()
    except ValueError:
        print("Error: First line of wallets.txt must be in format 'address,private_key'")
        exit()
    except Exception as e:
        print(f"Error reading wallets file: {e}")
        exit()
    return sender_address, sender_private_key, receivers

def send_eth(sender_address, sender_private_key, receiver_address, amount_wei):
    try:
        nonce = w3.eth.get_transaction_count(sender_address)
        tx = {
            'nonce': nonce,
            'to': receiver_address,
            'value': amount_wei,
            'gas': GAS_LIMIT,
            'gasPrice': w3.to_wei(GAS_PRICE_GWEI, 'gwei'),
            'chainId': CHAIN_ID
        }
        signed_tx = w3.eth.account.sign_transaction(tx, sender_private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"Transaction sent to {receiver_address} - Tx Hash: {w3.to_hex(tx_hash)}")
        return True
    except Exception as e:
        print(f"Error sending to {receiver_address}: {e}")
        return False

def main():
    amount_wei = w3.to_wei(AMOUNT_ETH, 'ether')
    sender_address, sender_private_key, receivers = read_wallets('wallets.txt')
    print(f"Sending from: {sender_address}")
    success_count = 0
    total_receivers = len(receivers)
    for receiver_address in receivers:
        print(f"\nSending {AMOUNT_ETH} ETH to {receiver_address}")
        if send_eth(sender_address, sender_private_key, receiver_address, amount_wei):
            success_count += 1
            time.sleep(DELAY_SECONDS)
        print(f"Progress: {success_count}/{total_receivers} completed")
    print(f"\nFinished! Successfully sent to {success_count} out of {total_receivers} receivers")

if __name__ == "__main__":
    sender_address, _, receivers = read_wallets('wallets.txt')
    balance = w3.eth.get_balance(sender_address)
    required = w3.to_wei(AMOUNT_ETH * len(receivers), 'ether') + w3.to_wei(0.0001, 'ether')
    if balance < required:
        print(f"Insufficient balance: {w3.from_wei(balance, 'ether')} ETH available, "
              f"{w3.from_wei(required, 'ether')} ETH required")
    else:
        main()
