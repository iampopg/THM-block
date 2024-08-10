# Original 16-byte session ID in hexadecimal
session_id = input('Input Session id: ')

# Reverse the bytes
reversed_session_id = ''.join([session_id[i:i+2] for i in range(0, len(session_id), 2)][::-1])

# Trim to 8 bytes if needed
if len(reversed_session_id) > 16:
    reversed_session_id = reversed_session_id[:16]

print("8-byte Reversed Session ID:", reversed_session_id)

# Expected output: '4100000000100000'
