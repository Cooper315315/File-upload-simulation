import socket
import os
from datetime import datetime

# Allowed extensions and magic bytes for validation
ALLOWED_EXTENSIONS = {
    '.jpg':  b'\xff\xd8\xff',                # JPEG
    '.jpeg': b'\xff\xd8\xff',                # JPEG
    '.png':  b'\x89PNG',                     # PNG
    '.gif':  b'GIF',                         # GIF
    '.bmp':  b'BM',                          # BMP
    '.tiff': b'II*\x00',                     # TIFF (Intel)
    '.tif':  b'II*\x00',                     # TIFF (Intel)
    '.webp': b'RIFF',                        # WEBP
    '.pdf':  b'%PDF',                        # PDF
    '.txt':  b'',                            # TXT
    '.csv':  b'',                            # CSV
    '.doc':  b'\xd0\xcf\x11\xe0',            # Old MS Word
    '.docx': b'PK\x03\x04',                  # DOCX
    '.xls':  b'\xd0\xcf\x11\xe0',            # Old MS Excel
    '.xlsx': b'PK\x03\x04',                  # XLSX
    '.ppt':  b'\xd0\xcf\x11\xe0',            # Old MS PowerPoint
    '.pptx': b'PK\x03\x04',                  # PPTX
    '.zip':  b'PK\x03\x04',                  # ZIP
    '.rar':  b'Rar!',                        # RAR
    '.7z':   b'7z\xbc\xaf\x27\x1c',          # 7z
    '.gz':   b'\x1f\x8b',                    # GZIP
    '.mp3':  b'ID3',                         # MP3
    '.wav':  b'RIFF',                        # WAV
    '.mp4':  b'\x00\x00\x00',                # MP4
    '.mov':  b'\x00\x00\x00',                # MOV
    '.avi':  b'RIFF',                        # AVI
}

def get_extension(filename):
    return os.path.splitext(filename)[1].lower()

def validate_extension(filename):
    ext = get_extension(filename)
    return ext in ALLOWED_EXTENSIONS

def validate_magic_bytes(filename, content):
    ext = get_extension(filename)
    magic = ALLOWED_EXTENSIONS.get(ext, None)
    if magic is None:
        return False
    if not magic:  # For .txt, .csv, etc.
        return True
    return content.startswith(magic)

def handle_client(conn, mode):
    try:
        # Receive filename length and filename
        filename_len_bytes = conn.recv(4)
        if not filename_len_bytes or len(filename_len_bytes) < 4:
            return
        filename_len = int.from_bytes(filename_len_bytes, 'big')
        filename = conn.recv(filename_len).decode()
        # Receive file size and content
        file_size_bytes = conn.recv(8)
        if not file_size_bytes or len(file_size_bytes) < 8:
            return
        file_size = int.from_bytes(file_size_bytes, 'big')
        content = b''
        while len(content) < file_size:
            chunk = conn.recv(min(4096, file_size - len(content)))
            if not chunk:
                break
            content += chunk

        ext_valid = validate_extension(filename)
        magic_valid = validate_magic_bytes(filename, content)
        ext = get_extension(filename)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Security validation logic based on version
        if mode == "v1.0":
            if ext_valid:
                validation_result = "Extension validation: File accepted. (VULNERABLE MODE)"
                accepted = True
            else:
                validation_result = "Extension validation: File rejected! (VULNERABLE MODE)"
                accepted = False
        elif mode == "v2.0":
            if ext_valid and magic_valid:
                validation_result = "Extension + magic bytes validation: File accepted. (SECURE MODE)"
                accepted = True
            else:
                validation_result = "Extension + magic bytes validation: File rejected! (SECURE MODE)"
                accepted = False
        else:
            validation_result = "Unknown validation mode."
            accepted = False

        # Output detailed info to terminal
        print("\n[Controller] === File Upload Event ===")
        print(f"Time received     : {now}")
        print(f"File name         : {filename}")
        print(f"File type         : {ext if ext else 'Unknown'}")
        print(f"File size         : {file_size} bytes")
        print(f"Extension allowed : {'Yes' if ext_valid else 'No'}")
        print(f"Magic bytes valid : {'Yes' if magic_valid else 'No'}")
        print(f"Validation mode   : {mode}")
        print(f"Security result   : {validation_result}")
        print("[Controller] =========================\n")

        conn.sendall(validation_result.encode())
    except Exception as e:
        print(f"[Controller] Error: {e}")
    finally:
        conn.close()

def start_server(mode, host='127.0.0.1', port=9002):
    print(f"[Controller] Starting on {host}:{port} in mode {mode}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print("[Controller] Waiting for client connection...")
        while True:
            try:
                conn, addr = s.accept()
                print(f"[Controller] Connected by {addr}")
                handle_client(conn, mode)
            except Exception as e:
                print(f"[Controller] Connection handling error: {e}")

if __name__ == "__main__":
    print("Select application version:")
    print("1) Version 1.0 (Vulnerable: extension check only)")
    print("2) Version 2.0 (Secure: extension + magic bytes check)")
    version = ""
    while version not in ["1", "2"]:
        version = input("Enter 1 or 2: ").strip()
    mode = "v1.0" if version == "1" else "v2.0"
    start_server(mode)
