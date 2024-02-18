# txt-file-RSA-encryption-program
This is a python GUI application utilizing RSA cryptography to encrypt and decrypt text files.

*NOTE: THIS PROGRAM IS A PROOF OF CONCEPT WORK, USING RSA AS A FILE ENCRYPTION ALGORITHM, IT HAS IT'S FAULTS WHICH INCLUDE:*  
* *THE ENCRYPT AND DECRYPT CAN ONLY BE DONE WHLE THE PROGRAM IS RUNNING, CLOSURE OF THE PROGRAM WILL RESULT IN LOSS OF DATA*
* *THE SHRED FEATURE WILL PERMENANTLY DELETE A TEXT FILE*
******************************************************************************  
## How to use the program
### Prerequisites
* Have the latest python version :- Python 3.11.0 
* Have pip

*For MacOS and Linux:*  
Check by running the following in terminal:  
python --version Or  python3 --version

*For Windows:*  
Run the same above in cmd or powershell

### Have the following libraries installed:
* rsa
* ttkbootstrap
* ttkthemes

*For MacOS and Linux:*  
Install them by pasting the commands in the terminal  
pip install rsa ttkbootstrap ttkthemes
 
*For Windows:*  
Run the above in cmd or powershell


#### Running the program

To run the program, go to the location of the python file and open it in the terminal. Then run this command  
python Secure_File_Encryption.py  
Or  
python3 Secure_File_Encryption.py

You will be greated with this interface  
![image](https://github.com/samyboi16/txt-file-RSA-encryption-program/assets/95954618/aa1445ad-9d67-4de1-bc74-b9b6c4d09311)

Logging in  
By default, All the functionality of the program is disabled and needs a password to log in. The default password we have implemented is ‘purushu’. the password is hidden when typing in.

## Encryption  
Click on the encrypt button and choose your text file to encrypt. after the encryption is done a dialog box will be shown saying file is encrypted. The name of the encrypted file was the same as its original name.

## Decryption
For the decryption process, click on decrypt button and choose the encrypted file. After decryption a dialog box will appear saying file is decrypted.

## Singing and verifying  
This feature allows to signing and verifying files to see if there were any unauthorized tampering was done to the file.Signing is done before encryption and verification is done after decryption. Signing creates a SHA512 signature of the file. If any change was done to file, the verification process will yield invalid.

## Shredding file  
The shred button helps in deleting files from the program itself. Click on shred and select the file to be deleted.

## Creating a new file
Another feature of the program is to create a new text file within the program and save it at your desired location. Type out the message in the text box, click on Save decrypted content and choose where to save.
