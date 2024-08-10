# SMB3 Traffic Decryption Toolkit

This toolkit consists of two Python scripts designed to assist in decrypting SMB3-encrypted traffic captured in a PCAP file:

1. **random_smb_session_key.py**: Calculates the session key required to decrypt SMB3 traffic.
2. **reversed_session_id.py**: Reverses the session ID found in a PCAP file, as the reversed session ID is necessary for the decryption process.

## Requirements

- Python 3.x
- Cryptodome library (`pycryptodome`)

Install dependencies using pip:

```bash
pip install pycryptodome
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
```
python random_smb_session_key.py -u {username} -d {domain} -m {password ntlm hash} -n {ntproofstr key} -k {encrypted session key}

```

### Calculate the session key using the Password:
```
python random_smb_session_key.py -u {username} -d {domain} -p {MyPassword123} -n { key} -k {encrypted session key}

```

## reversed_session_id.py
This script takes a session ID found in a PCAP file and reverses it, producing the correct 8-byte session ID in hexadecimal format needed for decryption.

# Usage
Simply run the script with the session ID:

```
python reversed_session_id.py -
```
This will output the reversed session ID needed for decryption.

## Example Workflow
Reverse the Session ID:

First, reverse the session ID using reversed_session_id.py.
Calculate the Session Key:

Use random_smb_session_key.py with either the NTLM hash or password and other required parameters to obtain the session key.
Decrypt SMB3 Traffic in Wireshark:

Use the session key and the reversed session ID to decrypt SMB3 traffic in Wireshark.
This toolkit provides a straightforward method for decrypting SMB3 traffic using a combination of session key extraction and session ID reversal. Ensure all dependencies are installed and the necessary arguments are correctly provided when running the scripts.

go
Copy code

You can now copy and paste the entire content directly into your `README.md` file.








