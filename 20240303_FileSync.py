#| Implement a file syncing algorithm for two computers over a low-bandwidth network.
#| What if we know the files in the two computers are mostly the same?

import os
import hashlib

#-----------------#
# Define Function #
#-----------------#

def compute_file_signature(file_path, chunk_size=1024):
    """Compute the signature of a file by hashing each chunk."""
    signatures = []
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_hash = hashlib.sha256(chunk).hexdigest()
            signatures.append(chunk_hash)
    return signatures

def compute_delta(local_signatures, remote_signatures, file_path, chunk_size=1024):
    """Compute the delta between local and remote file based on signatures."""
    delta = []
    with open(file_path, 'rb') as f:
        for i, local_sig in enumerate(local_signatures):
            if i >= len(remote_signatures) or local_sig != remote_signatures[i]:
                # Chunk has changed or does not exist on remote
                f.seek(i * chunk_size)
                chunk = f.read(chunk_size)
                delta.append((i, chunk))
    return delta

def apply_delta(file_path, delta, chunk_size=1024):
    """Apply the delta to the file."""
    new_file_contents = []
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    for index, chunk in delta:
        position = index * chunk_size
        new_file_contents.append(file_contents[:position])
        new_file_contents.append(chunk)
        file_contents = file_contents[position+chunk_size:]
    new_file_contents.append(file_contents) # Append the remaining part of the file
    with open(file_path, 'wb') as f:
        for part in new_file_contents:
            f.write(part)

# Example usage
local_file_path = 'path/to/local/file'
remote_file_path = 'path/to/remote/file'

# Step 1: Compute signatures for both files
local_signatures = compute_file_signature(local_file_path)
remote_signatures = compute_file_signature(remote_file_path)

# Step 2: Compute the delta between local and remote files
delta = compute_delta(local_signatures, remote_signatures, local_file_path)

# Step 3: Apply the delta to the remote file (simulate by applying to a copy for demonstration)
apply_delta(remote_file_path, delta)
