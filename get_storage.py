import urllib.request
import json
import time

RPC_URL = "https://ethereum-sepolia-rpc.publicnode.com"
CONTRACT_ADDRESS = "0x539173EE242B78467f29d723637ce156027Db65a"

for slot in range(10):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getStorageAt",
        "params": [CONTRACT_ADDRESS, hex(slot), "latest"],
        "id": 1
    }

    req = urllib.request.Request(RPC_URL, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8')).get('result', '')
            print(f"Slot {slot}: {result}")

            # Decode hex properly
            hex_data = result[2:] if result.startswith("0x") else result
            if hex_data:
                try:
                    # Strip null bytes at the beginning/end
                    ascii_data = bytes.fromhex(hex_data).replace(b'\x00', b'').decode('utf-8', errors='ignore')
                    print(f"  ASCII: {ascii_data}")
                except Exception as e:
                    print(f"  Could not decode as ascii: {e}")
    except Exception as e:
        print(f"Error at slot {slot}: {e}")
    time.sleep(0.5)
