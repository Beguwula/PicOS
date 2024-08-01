import uos

def exists(directory_path):
    try:
        uos.stat(directory_path)
        return True
    except OSError:
        return False

# Example usage:
'''
directory_path = "/path"
if directory_exists(directory_path):
    print(f"The directory {directory_path} exists.")
else:
    print(f"The directory {directory_path} does not exist.")
'''
