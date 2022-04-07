#coding:utf-8
import os
import time


splash1 = """
    +----------------------------------+
    | Masscan2Httpx2Nuclei             |
    +----------------------------------+
    | by mbskter                       |
    +----------------------------------+
"""
print(splash1)



os.system('masscan -iL ip.txt -p1-65535  -oL masscan.txt --rate=2000')
while True:
    if os.path.exists("masscan.txt"):
        break
    else:
        time.sleep(1)
if os.path.getsize("masscan.txt") == 0:
    splash3 = """
    +----------------------------------+
    | 无端口开放，程序已退出!          |
    +----------------------------------+
    """
    print(splash3)
    exit()
else :
    splash4 = """
    +----------------------------------+
    | Masscan扫描结果解析并调用httpx   |
    +----------------------------------+
    """
    print(splash4)
    masscanfile = open("masscan.txt", "r")
    masscanfile.seek(0)
    for line in masscanfile:
        if line.startswith("#"):
            continue
        if line.startswith("open"):
            line = line.split(" ")
            with open("masscanconvert.txt", "a") as f:
                f.write(line[3]+":"+line[2]+"\n")
                f.close()
    masscanfile.close()
if os.path.exists("masscan.txt"):
    os.system('./httpx -l masscanconvert.txt -nc -o httpxresult.txt')
    os.remove("masscan.txt")
    splash2 = """
    +----------------------------------+
    | Httpx is done !                  |
    +----------------------------------+
    """
    print(splash2)
else:
    splash5 = """
    +----------------------------------+
    | 未发现解析后的masscan端口结果    |
    +----------------------------------+
    """
    print(splash5)
    exit()
if os.path.exists("httpxresult.txt"):
    os.system('./nuclei -l httpxresult.txt -s medium,high,critical -o nucleiresult.txt')
    os.remove("httpxresult.txt")
    os.remove("masscanconvert.txt")
else:
    print("扫描结果未发现http协议")
    exit()
if os.path.exists("nucleiresult.txt"):
    splash6 = """
    +----------------------------------+
    | 扫描完成。请查看nucleiresult.txt |
    +----------------------------------+
    """
    print(splash6)
else:
    splash7 = """
    +----------------------------------+
    | 未发现中高危漏洞                 |
    +----------------------------------+
    """
    print(splash7)
    exit()
