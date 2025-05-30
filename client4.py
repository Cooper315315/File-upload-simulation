import socket
import os

def send_file(filename, host='127.0.0.1', port=9002):
    with open(filename, 'rb') as f:
        content = f.read()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # Send filename length and filename
        s.sendall(len(os.path.basename(filename)).to_bytes(4, 'big'))
        s.sendall(os.path.basename(filename).encode())
        # Send file size and content
        s.sendall(len(content).to_bytes(8, 'big'))
        s.sendall(content)
        # Receive response
        response = s.recv(1024)
        print(f"[Client] Controller response: {response.decode()}")

if __name__ == "__main__":
    print("Enter path to file to upload (or 'exit' to quit):")
    while True:
        fname = input("> ").strip()
        if fname.lower() == 'exit':
            break
        if not os.path.isfile(fname):
            print("File does not exist.")
            continue
        send_file(fname)
