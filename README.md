# Masscan2Httpx2Nuclei&xray
masscan全端口扫描==>httpx探测WEB服务==>nuclei&xray漏洞扫描
`解放双手`
# 环境准备 
- 自备nuclei\httpx\xray_linux_amd64放脚本同目录(文件名请保持不变)
- 自备masscan python3环境
- 将要扫描的资产放在ip.txt里面
- python3 Masscan2Httpx2Nuclei.py -i ip.txt -p 1-65535 --rate 2000
- nuclei默认只扫描medium,high,critical级别，方便打野，如有其他需求请自行更新
- **睡一觉**
## 没啥技术含量的脚本，能用就行
![1657119439056](https://user-images.githubusercontent.com/62868358/177580861-48afa816-20bd-40fc-8ea1-aa776669a370.png)

# 关于
* **[masscan](https://github.com/robertdavidgraham/masscan)**
* **[httpx](https://github.com/projectdiscovery/httpx/releases/)**
* **[nuclei](https://github.com/projectdiscovery/nuclei/releases)**
* **[xray](https://github.com/chaitin/xray/releases/tag/1.8.4)**
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=mbskter/Masscan2Httpx2Nuclei&type=Date)](https://star-history.com/#mbskter/Masscan2Httpx2Nuclei&Date)
