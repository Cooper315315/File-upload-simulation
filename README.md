# README: Secure File Upload Demonstration

## 1. Discussion of the Chosen Question, Answer, and Conclusion

**Chosen question:**  
*"Is file extension validation alone sufficient to prevent malicious file uploads, or is content (magic bytes) validation also required?"*

**Discussion:**  
File upload vulnerabilities are a major attack vector in cyber-physical systems, as highlighted in the attached vulnerability table (see Controller 434: Unrestricted file upload)[1]. Many applications rely on file extension checks to restrict uploads to "safe" file types (e.g., `.jpg`, `.png`). However, research and industry best practices show that extension checks alone are not enough. Attackers can easily bypass these checks by renaming malicious files (e.g., uploading `shell.php` as `shell.jpg`), using double extensions (`image.jpg.php`), or exploiting poorly implemented filters[3][6].  
Magic bytes, or file signatures, are unique sequences at the start of files that indicate their true type[2][3]. Validating both extension and magic bytes ensures that the file's content matches its claimed extension, preventing many bypass techniques.

**Answer & Conclusion:**  
Extension validation alone is *not* sufficient to prevent malicious uploads. Magic bytes (content) validation is also required to reliably identify and block disguised or dangerous files[3][4]. The secure approach is to use a whitelist of allowed extensions *and* verify the file's magic bytes before accepting the upload.

---

## 2. Description of the Model Implemented

This project implements a **client-server model** using Python sockets to simulate file uploads in a CPS environment:

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
   - `controller.py` (server)
   - `client.py` (client)
   - Test files with various extensions and content (e.g., `.jpg`, `.php`, `.exe`). You can create a dummy `.php` file by saving `<?php echo "test"; ?>` as `test.php`.

2. **Start the Controller (Server):**
   - Open a terminal and run:
     ```
     python controller.py
     ```
   - When prompted, select:
     - `1` for Version 1.0 (extension check only, vulnerable)
     - `2` for Version 2.0 (extension + magic bytes check, secure)

3. **Start the Client:**
   - In a separate terminal, run:
     ```
     python client.py
     ```
   - Enter the path to a file you want to upload (e.g., `test.php`, `image.jpg`).

4. **Observe the Results:**
   - The controller terminal will display detailed information about each upload, including the security decision and reasons for rejection if applicable.
   - The client will display the server's response.
  
  ![Screenshot 2025-05-30 at 00 26 51](https://github.com/user-attachments/assets/c34d383f-801d-4589-9140-0dabf174c4e7)
![Screenshot 2025-05-30 at 00 26 33](https://github.com/user-attachments/assets/d9745a22-0f3d-4e7c-bd0f-2c5217e99091)
![Screenshot 2025-05-30 at 00 26 41](https://github.com/user-attachments/assets/9e8c4216-8349-4d9a-8a44-3be6d4d10c31)


**Demonstration:**  
- In Version 1.0, try uploading a `.php` file renamed as `.jpg`—it will be accepted (vulnerable).
- In Version 2.0, the same file will be rejected because the magic bytes do not match the `.jpg` signature.

---

**References:**  
- [1] Vulnerability Table (see attached image)  
- [2][3][4][6] Security best practices and magic bytes validation: see provided search results.

---

**Conclusion:**  
This project demonstrates that file extension validation alone is insufficient for secure file uploads. Magic bytes validation is essential to prevent attackers from bypassing filters and uploading malicious files.
