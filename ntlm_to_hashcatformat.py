import re


def get_input(prompt, required=True):
    """Get user input with optional validation"""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field is required. Please enter a value.")


def transform_to_hashcat_format():
    """
    Interactive script for collecting NTLMv2 data and transform to Hashcat format:
    User::Domain:Server Challenge:HMAC-MD5 (NTProofStr):NTLMv2Response
    """

    print("\n" + "=" * 60)
    print("NTLMv2 to Hashcat Format Converter")
    print("=" * 60)
    print("\nPlease enter the following NTLMv2 fields:\n")

    # Collect each field individually
    user = get_input("Username (User): ")
    domain = get_input("Domain: ")
    challenge = get_input("Server Challenge (8-byte hex): ")
    ntproof = get_input("HMAC-MD5 (NTProofStr) (16-byte hex): ")
    ntlmv2 = get_input("NTLMv2Response (full blob): ")

    # Validate hex fields
    hex_fields = {
        'Challenge': challenge,
        'NTProofStr': ntproof,
        'NTLMv2Response': ntlmv2
    }

    for field_name, value in hex_fields.items():
        if value and not re.match(r'^[a-fA-F0-9]+$', value):
            print(f"\n⚠️  Warning: '{field_name}' contains non-hex characters. Surely invalid.")
            confirm = input(f"Continue anyway? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Exiting...")
                return

    # Construct Hashcat format
    # Format: User::Domain:ServerChallenge:NTProofStr:NTLMv2Response
    hashcat_format = f"{user}::{domain}:{challenge}:{ntproof}:{ntlmv2}"

    # Display results
    print("\n" + "=" * 60)
    print("✅ Hashcat Format (Mode 5600 - NetNTLMv2):")
    print("=" * 60)
    print("\n" + hashcat_format + "\n")
    print("=" * 60)

    # Option to save to file
    save = input("\nSave to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Filename (default: hashcat_ntlmv2.txt): ").strip()
        if not filename:
            filename = "hashcat_ntlmv2.txt"

        try:
            with open(filename, 'w') as f:
                f.write(hashcat_format + '\n')
            print(f"✅ Saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")

    # Copy to clipboard option (if pyperclip is installed)
    try:
        import pyperclip
        copy = input("\nCopy to clipboard? (y/n): ").strip().lower()
        if copy == 'y':
            pyperclip.copy(hashcat_format)
            print("✅ Copied to clipboard!")
    except ImportError:
        pass

    print("\n" + "=" * 60)
    print("Hashcat command example:")
    print(f"hashcat -m 5600 -a 0 {filename if save == 'y' else 'hash.txt'} wordlist.txt")
    print("=" * 60)


def main():
    try:
        transform_to_hashcat_format()
    except KeyboardInterrupt:
        print("\n\nExited by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
