# 파일명 : net.py



def find_net_id(ip, sm):
    net_id = []
    for i1, i2 in zip(ip, sm):
        item = str(int(i1) & int(i2))
        net_id.append(item)
    return ".".join(net_id)

def sm_to_prefix(sm):
    prefix = ""
    for item in sm:
        prefix += bin(int(item))[2:]
    return prefix.count("1")

def find_bit(ip):
    ip_bit = ""
    for i in ip:
        bit = bin(int(i))[2:]
        ip_bit += f"{bit:>08}"
    ip_bit = f"{ip_bit:0<32}"
    
    i = 0
    ip = ""
    for x in range(0, 4):
        i += 8
        ip += str(int(ip_bit[i-8: i], 2)) + "."
    return ip.strip(".")

def find_br_id(ip, prefix):
    ip_bit = ""
    for i in ip:
        bit = bin(int(i))[2:]
        ip_bit += f"{bit:>08}"
    ip_bit = f"{ip_bit[:prefix]:0<32}"
    ip = ""
    for i in range(0, 32, 8):
        ip += str(int(ip_bit[i:i+8], 2)) + "."
    return ip.strip(".")


ip = input("ip 주소 : ").split(".")
sm = input("subnetmask : ").split(".")
net_id = find_net_id(ip, sm)
prefix = sm_to_prefix(sm)
ip_bit = find_bit(ip)
br_ip = find_br_id(ip, prefix)
print(f"network id : {net_id}")
print(f"prefix : {prefix}")
print(f"ip bit : {ip_bit}")
print(f"br_ip : {br_ip}")
