from backend.core.crypto.keys import (
    generate_key_pair,
    private_key_to_pem,
    public_key_to_pem,
    load_private_key,
    load_public_key
)

def main():
    print("🔐 [1] Generate key pair...")
    private_key, public_key = generate_key_pair()

    print("📄 [2] Convert to PEM format...")
    private_pem = private_key_to_pem(private_key)
    public_pem = public_key_to_pem(public_key)

    print("\n--- PRIVATE KEY ---")
    print(private_pem)
    print("--- PUBLIC KEY ---")
    print(public_pem)

    print("🔁 [3] Load keys back from PEM...")
    loaded_priv = load_private_key(private_pem)
    loaded_pub = load_public_key(public_pem)

    print("✅ Keys loaded successfully. Test complete!")

if __name__ == "__main__":
    main()
