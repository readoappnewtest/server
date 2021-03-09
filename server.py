import socket
import requests


data_record = {}
data_record['data'] = []

def search(text):
    a = text.decode("utf-8")
    end = 0
    n_n = 0
    last_n = 0
    http_method = ""#method like get
    http_host = ""#host omean main domain name
    http_user_agent = "" #user agent is browser name
    http_cookie = ""
    http_sub_file = ""
    #a = str(c.recv(1024).decode("utf-8"))
    while end == 0:
        #print("Staed..")
        n_n = a.find("\n",last_n+1)
        if n_n <0:
            print("One Packet Complete")
            end = 1
        else:
            data_record_txt = a[last_n:n_n]
            #print(a[last_n:n_n])
            if "HTTP/1" in data_record_txt:
                if "GET" in data_record_txt:
                    http_method="GET"
                elif "POST" in data_record_txt:
                    http_method= "POST"
                length_of_txt = len(data_record_txt)
                n_double_comma = data_record_txt.find("/")
                n_next_double_comma = data_record_txt.find(" ",n_double_comma+1)
                
                main_data_txt = data_record_txt[n_double_comma:n_next_double_comma]
                http_sub_file = main_data_txt
            elif "Host:" in data_record_txt:
                length_of_txt = len(data_record_txt)
                n_double_comma = data_record_txt.find(":")
                main_data_txt = data_record_txt[n_double_comma+2:length_of_txt-1]
                http_host = main_data_txt
            elif "User-Agent" in data_record_txt:
                length_of_txt = len(data_record_txt)
                n_double_comma = data_record_txt.find(":")
                main_data_txt = data_record_txt[n_double_comma+2:length_of_txt-1]
                http_user_agent = main_data_txt
            elif "Cookie" in data_record_txt:
                length_of_txt = len(data_record_txt)
                n_double_comma = data_record_txt.find(":")
                main_data_txt = data_record_txt[n_double_comma+2:length_of_txt-1]
                http_cookie = main_data_txt
            last_n = n_n
    main_json_data = {"host":""+str(http_host)+"","method":""+str(http_method)+"","user-agent":""+str(http_user_agent)+"","cookie":""+str(http_cookie)+"","sub_file":""+str(http_sub_file)+""}
    print(main_json_data)
def my_ip():
    url="https://api.my-ip.io/ip"
    data = requests.get(url,headers={"User-Agent":"Nasa"})
    #print(data)
    return str(data.text)
s = socket.socket()
port = 8080
host_ip = socket.gethostbyname("jeemainnoti.herokuapp.com")
s.bind(('0.0.0.0',port))
print("Socket Bind " +str(port)+"")
print(s)
s.listen(5)
print("Stated")
while True:
    try:
        c, addr = s.accept()
        print("Got Connetction form",addr)
        print(addr[0])
        #send_data = 
        #ad = b'HTTP/1.1 400 OK\r\nServer: nginx/1.6.2\r\nDate: Mon, 08 Mar 2021 15:15:21 GMT\r\nContent-Type: text/html\r\nContent-Length: 348\r\nLast-Modified: Sat, 20 Jul 2019 11:49:25 GMT\r\nConnection: close\r\nETag: "5d32ffc5-15c"\r\nAccess-Control-Allow-Origin: *\r\nAccept-Ranges: bytes\r\n\r\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>My html page</title>\n</head>\n<body>\n\n    <p>\n        Today is a beautiful day. We go swimming and fishing.\n    </p>\n    \n    <p>\n         Hello there. How are you?\n    </p>\n    \n</body>\n</html>\n\n'
        ad = b'HTTP/1.1 200 Ok \r\n\r\n<html><head><title>Hi Aryan Jaswal</title></head><body>Hi Man how are you</body>'
        c.send(ad)       
        #print(c.recv(1024))
        search(c.recv(1024))
        c.close()
    except:
        print("Error")

    
    
