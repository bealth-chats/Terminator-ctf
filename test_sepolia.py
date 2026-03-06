import urllib.request
import json
import time

RPC_URL = "https://ethereum-sepolia-rpc.publicnode.com"
TX_HASH = "0x5234faa7013f7d2ac9138c23a2d8d0f39bd7b1093b81f4abc5009548236cf228"

def rpc_call(method, params):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }

    req = urllib.request.Request(RPC_URL, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result
    except Exception as e:
        print(f"Error calling {method}: {e}")
        return None

tx = rpc_call("eth_getTransactionByHash", [TX_HASH])
print("Transaction:", tx)
