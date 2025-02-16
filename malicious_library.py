# malicious_library.py
def safe_function():
    print("This function is safe!")

# Mã độc được chèn vào mà không ai hay biết
def malicious_function():
    import os
    os.system("echo 'Bạn đã bị tấn công!' > hacked.txt")

# Khi thư viện được import, mã độc tự chạy
malicious_function()
