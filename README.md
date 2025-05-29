# File Upload Simulation 

## 1. Introduction and Question 
**Introduction:**  
"Unrestricted File Upload (CWE-434)" is a critical vulnerability identified in the previous group assignment. In this assignment, we will demonstrate 1) how a "Unrestricted File Upload" vulnerability and 2) how a secure content validation operates in a simulation enviroment.

Many application uses file extension checks to restrict malicious files upload. However, both research and industry practices have shown that this method is not an effective mechanism against malicious files upload. Attackers can bypass this checks by renaming extensions of the malicious files (e.g., from `shell.php` to `shell.jpg`) or using double extensions ((e.g., from `install.exe` to `install.exe.jpg`)
[3][6].  

A more sophisticated security procedure is required to tackle this issue. Hence, Magic Bytes validation (or file signatures) comes into play. Magic Bytes refers to a unique sequences of characters, and each file type has its own unique sequences (e.g. jpg: `FF` `D8`). This method validates both file extention and the magic bytes to ensure the content matches with its claimed extension, which effectively prevents bypassing techniques such as renaming extension and double extension.[2][3]

**Question:**  
*"Does content validation (magic bytes) enhance security effectiveness compared to extension validation alone? "*

Based on the ABCDE characteristics in function of security, this question is based on the A - elemment "Autonomy" because how the controller and client application runs independently. The controller validates and implements security procedures whilst the client uploads files to the system.

---

## 2. Description of the Model Implemented

This assignment uses Python sockets to create a file upload simulation in a CPS environment and it is done by the implementaion of **client-server model**.

- **Controller (Server):**
  - Prompts the user to select version 1.0 (vulnerable: extension check only) or version 2.0 (secure: extension + magic bytes check).
  - Receives files from the client and applies the selected validation strategy.
  - Logs detailed information about each upload, including file name, type, size, time, extension/magic bytes validation results, and the security decision.
  - In secure mode, rejects files whose content does not match their extension, demonstrating defense against common attack techniques (e.g., renaming `.php` to `.jpg`).

- **Client:**
  - Allows the user to select and upload a file to the controller.
  - Receives and displays the server's acceptance or rejection message.

This model allows users to observe and compare the outcomes of both validation strategies in a controlled environment.

---

## 3. Instructions on How to Execute the Code

**Prerequisites:**  
- Python 3.x installed on your system.

**Steps:**

1. **Download or create the following files:**
   - `controller4.py` (server)
   - `client4.py` (client)
   - Test files with various extensions and content (e.g., `.jpg`, `.php`, `.exe`). You can create a dummy `.php` file by saving `<?php echo "test"; ?>` as `test.php`.

2. **Start the Controller (Server):**
   - Open a terminal and run:
     ```
     python controller4.py
     ```
   - When prompted, select:
     - `1` for Version 1.0 (extension check only, vulnerable)
     - `2` for Version 2.0 (extension + magic bytes check, secure)

3. **Start the Client:**
   - In a separate terminal, run:
     ```
     python client4.py
     ```
   - Enter the path to a file you want to upload (e.g., `test.php`, `image.jpg`).

4. **Observe the Results:**
   - The controller terminal will display detailed information about each upload, including the security decision and reasons for rejection if applicable.
   - The client will display the server's response.
   - Demonstration commands are listed below
     ```
     /Users/cooperli/Desktop/M6_coding/Deadpool.png
     /Users/cooperli/Desktop/M6_coding/1mb.exe
     /Users/cooperli/Desktop/M6_coding/sample.php
     /Users/cooperli/Desktop/M6_coding/1mb.exe.jpg
     /Users/cooperli/Desktop/M6_coding/1mb.jpg
     ```
  
![Screenshot 2025-05-30 at 00 26 33](https://github.com/user-attachments/assets/d9745a22-0f3d-4e7c-bd0f-2c5217e99091)
![Screenshot 2025-05-30 at 00 26 41](https://github.com/user-attachments/assets/9e8c4216-8349-4d9a-8a44-3be6d4d10c31)


**Demonstration:**  
- In Version 1.0, try uploading a `.php` file renamed as `.jpg`—it will be accepted (vulnerable).
- In Version 2.0, the same file will be rejected because the magic bytes do not match the `.jpg` signature.

---
**Conclusion:**  
Extension validation alone is *not* sufficient to prevent malicious uploads. Magic bytes (content) validation is also required to reliably identify and block disguised or dangerous files[3][4]. The secure approach is to use a whitelist of allowed extensions *and* verify the file's magic bytes before accepting the upload.

**References:**  
- [1] Vulnerability Table (see attached image)  
- [2][3][4][6] Security best practices and magic bytes validation: see provided search results.

---

**Conclusion:**  
This project demonstrates that file extension validation alone is insufficient for secure file uploads. Magic bytes validation is essential to prevent attackers from bypassing filters and uploading malicious files.
