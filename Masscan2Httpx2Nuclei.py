#coding:utf-8
import os
import time
import argparse

def biaoti():
    splash1 = """
        +----------------------------------+
        | Masscan2Httpx2Nuclei             |
        +----------------------------------+
        | by mbskter                       |
        +----------------------------------+
    """
    print(splash1)

def args():
    parser = argparse.ArgumentParser(description='Masscan2Httpx2Nuclei')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-p', '--port', help='port', required=True)
    parser.add_argument('--rate', '--rate', help='rate', required=True)
    args = parser.parse_args()
    return args

def check_args(args):
    if not os.path.exists(args.input):
        print('input file not exists')
        exit()
    if not args.port:
        print('port not exists')
        exit()
    if not args.rate:
        print('rate not exists')
        exit()
    return args

def masscan2httpx2nuclei(args):
    args = check_args(args)
    input_file = args.input
    port = args.port
    rate = args.rate
    os.system('masscan -iL ' + input_file + ' -p' + port + ' -oL masscan.txt --rate ' + rate)

def masscan2httpx2nuclei_main():
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


def main():
    biaoti()
    masscan2httpx2nuclei(args())
    masscan2httpx2nuclei_main()

if __name__ == '__main__':
    main()
    exit()
