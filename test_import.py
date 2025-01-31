import sys
import subprocess

# Ensure setuptools is installed
try:
    import setuptools
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
finally:
    import pkg_resources

print(sys.path)
try:
    import dataengieneeringparsers 
    import pandas as pd
    
    print("Import successful!")
    if hasattr(dataengieneeringparsers, '__version__'):
        print(f"dataengieneeringparsers version: {dataengieneeringparsers} installed ")
    else:
        print("dataengieneeringparsers version: Not available")
    print(f"pandas version: {pd.__version__}")
except ImportError as e:
    print(f"Import failed: {e}")

# List all installed packages
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
print("Installed packages:")
for package in installed_packages_list:
    print(package)
