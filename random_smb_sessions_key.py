import hmac
import argparse
from binascii import unhexlify, hexlify
from Cryptodome.Cipher import ARC4
from Cryptodome.Hash import MD4

def generateEncryptedSessionKey(keyExchangeKey, exportedSessionKey):
    cipher = ARC4.new(keyExchangeKey)
    sessionKey = cipher.encrypt(exportedSessionKey)
    return sessionKey

# Argument parser setup
parser = argparse.ArgumentParser(description="Calculate the Random Session Key based on data from a PCAP (maybe).")
parser.add_argument("-u", "--user", required=True, help="User name")
parser.add_argument("-d", "--domain", required=True, help="Domain name")
parser.add_argument("-p", "--password", help="Password of User")
parser.add_argument("-m", "--ntlmhash", help="NTLM Hash of the User")
parser.add_argument("-n", "--ntproofstr", required=True, help="NTProofStr. This can be found in PCAP (provide Hex Stream)")
parser.add_argument("-k", "--key", required=True, help="Encrypted Session Key. This can be found in PCAP (provide Hex Stream)")
parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")

args = parser.parse_args()

# Upper Case User and Domain
user = str(args.user).upper().encode('utf-16le')
domain = str(args.domain).upper().encode('utf-16le')

# Choose between NTLM hash or password
if args.password:
    # Create NTLM hash of password using Cryptodome's MD4
    md4 = MD4.new()
    md4.update(args.password.encode('utf-16le'))
    ntlm_hash = md4.digest()
elif args.ntlmhash:
    # Use provided NTLM hash
    ntlm_hash = unhexlify(args.ntlmhash)
else:
    raise ValueError("You must provide either a password or an NTLM hash.")

# Calculate the ResponseNTKey
h = hmac.new(ntlm_hash, digestmod='md5')
h.update(user + domain)
respNTKey = h.digest()

# Use NTProofSTR and ResponseNTKey to calculate Key Exchange Key
NTproofStr = unhexlify(args.ntproofstr)
h = hmac.new(respNTKey, digestmod='md5')
h.update(NTproofStr)
KeyExchKey = h.digest()

# Calculate the Random Session Key by decrypting Encrypted Session Key with Key Exchange Key via RC4
RsessKey = generateEncryptedSessionKey(KeyExchKey, unhexlify(args.key))

# Output the results
if args.verbose:
    print("USER WORK: " + user.decode('utf-16le') + " " + domain.decode('utf-16le'))
    print("RESP NT:   " + hexlify(respNTKey).decode())
    print("NT PROOF:  " + hexlify(NTproofStr).decode())
    print("KeyExKey:  " + hexlify(KeyExchKey).decode())

print("Random SK: " + hexlify(RsessKey).decode())
