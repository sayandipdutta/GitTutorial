import shutil
import sys

def check_disk_usage(disk, min_GB, min_percent):
    """Returns True it there us enough free disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate percentage of free disk space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    print(f"Available disk space: {gigabytes_free:.2f} GB ({percent_free:.2f}%)")
    if percent_free < min_percent or gigabytes_free < min_GB:
        return False
    return True

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_root_full():
        print("Root partition full.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)
    
print("Everything OK!")
sys.exit(1)
