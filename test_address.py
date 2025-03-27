from backend.core.crypto.keys import generate_key_pair
from backend.wallet.address import generate_address, is_valid_address

def main():
    print("🔐 Generate key pair...")
    priv, pub = generate_key_pair()

    print("📬 Generate address from public key...")
    addr = generate_address(pub)
    print("✅ Address:", addr)

    print("🧪 Valid address?", is_valid_address(addr))

if __name__ == "__main__":
    main()
