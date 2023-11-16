import socket
import threading

HOST = 'localhost'
PORT = 8080


# Get the command from the client and return the output
# For example: "get my ip" -> "ipconfig"
def handle_cmd(cmd):
    output = ""
    if cmd == "get my ip":
        output = "ipconfig /all@(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')"
    # if cmd = "check if ip is up":
        # output = "ping -n 1 " + ip


    return output

# Todo: Ask when do we need to close the connection to the client????????
# Todo: Do we need to close after each command or after the client disconnects????????
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        #Receive data from client (cmd in english)
        data = data.decode()

        if not data:
            break

        if data == "exit":
            conn.close()
            break
        out_cmd = handle_cmd(data) #Handle the data (cmd in bash/windows)
        conn.sendall(out_cmd) # Send data back to client (cmd in bash/windows)

    #TODO: Close connection to client


def start_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f"Server listening on {HOST}:{PORT}")

        #Wait for connections - (Multi-Client) # Main thread
        while True:
            conn, addr = s.accept() #Accept connection RON DAN
            client_thread = threading.Thread(target=handle_client, args=(conn, addr)) #Sending the connection to a thread
            client_thread.start()

if __name__ == "__main__":
    start_server()
