# SMB3 Traffic Decryption Toolkit

This toolkit consists of two Python scripts designed to assist in decrypting SMB3-encrypted traffic captured in a PCAP file:

1. **random_smb_session_key.py**: Calculates the session key required to decrypt SMB3 traffic.
2. **reversed_session_id.py**: Reverses the session ID found in a PCAP file, as the reversed session ID is necessary for the decryption process.

## Requirements

- Python 3.x
- Cryptodome library (`pycryptodome`)

Install dependencies using pip:

```bash
pip install pycryptodomex
```

## random_smb_session_key.py
This script calculates the session key required to decrypt SMB3 traffic. It supports using either the NTLM hash or the password of the user.

### Arguments
-u, --user: (Required) The username (e.g., eshellstrop).
-d, --domain: (Required) The domain name (e.g., WORKGROUP).
-p, --password: (Optional) The password of the user. Either this or the NTLM hash must be provided.
-m, --ntlmhash: (Optional) The NTLM hash of the user. Either this or the password must be provided.
-n, --ntproofstr: (Required) The NTProofStr (found in the PCAP as a hex stream).
-k, --key: (Required) The encrypted session key (found in the PCAP as a hex stream).
-v, --verbose: (Optional) Increase output verbosity for debugging purposes.

## Usage 
### Calculate the session key using NTLM hash
```bash
python random_smb_session_key.py -u {username} -d {domain} -m {password ntlm hash} -n {ntproofstr key} -k {encrypted session key}

```

### Calculate the session key using the Password:
```bash
python random_smb_session_key.py -u {username} -d {domain} -p {MyPassword123} -n { key} -k {encrypted session key}

```

## reversed_session_id.py
This script takes a session ID found in a PCAP file and reverses it, producing the correct 8-byte session ID in hexadecimal format needed for decryption.

# Usage
Simply run the script with the session ID:

```bash
python reversed_session_id.py 
```
This will output the reversed session ID needed for decryption.

## Credit

Original scripts and inspiration:
- [Decrypting SMB3 Traffic with a PCAP ](https://medium.com/maverislabs/decrypting-smb3-traffic-with-just-a-pcap-absolutely-maybe-712ed23ff6a2) 
- [djalilayed's GitHub Repository](https://github.com/djalilayed/)






