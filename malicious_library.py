def safe_function():
    print("This function is safe!")

# Mã độc 
def malicious_function():
    import os
    os.system("echo 'Bạn đã bị tấn công!' > hacked.txt")

malicious_function()
