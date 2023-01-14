import socket #Library sockets



def get():
    target = "google.com"#Example

    #Code
    final = socket.gethostbyname(target)
    print(f"Ip is {final}, Simple code made for beginners")


get()

