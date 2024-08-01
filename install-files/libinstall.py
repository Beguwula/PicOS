import uos

def exists(path):
    try:
        uos.stat(path)
        return True
    except OSError:
        return False

# Example usage:
'''
path = "/path"
if exists(path):
    print(f"The directory {path} exists.")
else:
    print(f"The directory {path} does not exist.")
'''
