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
  - User can select 2 different versions. Version 1.0 is a vulnerable application using only extension checking, whereas Version 2.0 is a secure version using both extension check and magic bytes validation.
  - Both version receive files from the client side and apply security validations.
  - Upon each upload, the controller outputs important information including receiving date & time, file name, file type, file size and whether the file is successfully uploaded or rejected due to security checks.
  - In secure version (v2.0), common techniques such as renaming and double extension will not work because the file content does not match with its content extension.

- **Client:**
  - User can upload files to the controller via the client side
  - The client outputs a message and inform users whether the server accepts or rejects the file.

This client vs controller model demonstrates how different extension validation methods interact with normal and potential harmful file types in a controlled environment.

---

## 3. Instructions

**Prerequisites:**  
- Install Python 3.x on your system.

**Steps:**
1. **Download the following files:**
   - `controller4.py` (server)
   - `client4.py` (client)
   - Test files with various extensions including image file (`.png`), executable (`.exe`) and Hypertext Preprocessor (`.php`).

2. **Start the Controller (Server):**
   - Open a terminal and change to the directory where the downloaded python files are located:
     ```
     cd [INSERT PATH HERE]
     ```
   - Run the python file:
     ```
     python controller4.py
     ```
   - When prompted, select:
     - `1` for Version 1.0 (Vulnerable: extension check only)
     - `2` for Version 2.0 (Secure: extension + magic bytes check)
       
![Screenshot 2025-05-30 at 00 20 44](https://github.com/user-attachments/assets/c4c7a749-23b3-4a33-a675-2b497c76a549)

4. **Start the Client:**
   - Open a separate terminal and change the directory, run:
     ```
     cd [INSERT PATH HERE]
     ```
   - Run the python file:
     ```
     python client4.py
     ```
   - Enter the path to a file you want to upload (e.g., `sample.php`, `image.png`).
     
     For example:
     
     ```
     /Users/cooperli/Desktop/M6_coding/Deadpool.png
     ```
    - Demonstration commands used in section 5 are listed below:
     ```
     /Users/cooperli/Desktop/M6_coding/Deadpool.png
     /Users/cooperli/Desktop/M6_coding/1mb.exe
     /Users/cooperli/Desktop/M6_coding/sample.php
     /Users/cooperli/Desktop/M6_coding/1mb.exe.jpg
     /Users/cooperli/Desktop/M6_coding/1mb.jpg
     ```

5. **Observe the Results:**
   - The controller terminal will display detailed information about each upload, including the security decision and reasons for rejection if applicable.
   - The client will display the server's response.
  
**Demonstration:**  
- In Version 1.0, try uploading a `.php` file renamed as `.jpg`—it will be accepted (vulnerable).
- In Version 2.0, the same file will be rejected because the magic bytes do not match the `.jpg` signature.

---
**Conclusion:**  
Extension validation alone is insufficient to prevent malicious uploads as it can be easily bypassed by renaming and double extension. By implementing magic bytes validation and extension validation together, the application can effectively identify true file's extension and reject disgusied malicious files. [3][4]

**References:**  
- [1] Vulnerability Table (see attached image)  
- [2][3][4][6] Security best practices and magic bytes validation: see provided search results.


