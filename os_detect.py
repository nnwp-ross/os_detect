import os
import platform

# Check OS name
os_name = os.name  # Returns 'nt' for Windows, 'posix' for Unix-like systems
os_platform = platform.system() # Returns 'Windows', 'Linux', 'Darwin' (macOS)
os_version = platform.version()
detail_info = platform.platform()
os_release = platform.release()

# Print OS name
print(f"OS Name: {os_name}")
print(f"OS Platform: {os_platform}")
print(f"OS Version: {os_version}")
print(f"Detail Info: {detail_info}")
print(f"OS Release: {os_release}")


'''
# Additional checks
if os_name == 'nt':
    print("Running on Windows")
elif os_name == 'posix':
    # More specific checks for Unix-like systems
    if 'darwin' in platform.system().lower():
        print("Running on macOS")
    else:
        print("Running on Linux or another Unix-like OS")
'''