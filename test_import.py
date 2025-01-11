import sys
print(sys.path)
try:
    import dataengieneeringparsers 
    
    print("Import successful!")
except ImportError as e:
    print(f"Import failed: {e}")
