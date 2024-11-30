# Automatic_emails

This repository contains a Python application that automatically sends email recaps of orders. It allows you to upload a CSV file with order details and send emails to recipients with product lists and quantities. Be careful, don't use it mindlessly or you will spam hundreds of poor Pépin orderers...

## Application Overview

- **Easy-to-use Interface**: No coding is required to use the application. Simply download the `.exe` file for Windows (or other versions for Mac/Linux) and run the program.
- **Upload CSV**: The user can upload a CSV file containing order details, and the app will send emails to the recipients based on the provided information.
- **Automatic Email Sending**: The app uses Gmail's SMTP to send emails with the order summary.

### App Link
You can download the application for Windows [here](https://drive.google.com/file/d/1kzxuW6yr_VZ8rYVQA2_hQc_boW5nK19g/view?usp=drive_link) and for Mac [here](https://drive.google.com/file/d/1SA9vIMJNTLyPxSx5zj0Mq1Hn0U4orqMb/view?usp=drive_link). Simply download the file to start using it!

## Usage

1. **Download and Run the App**:  
   Just download the `.exe` file (for Windows) or .app (for Mac) (sorry Linux users you can update the build.yml file if you want your own app but it is at your own risks in regards to packages compatibility, I didn't test it.). No coding or installation is required.

2. **Upload CSV**:  
   Click on the "Upload CSV" button to select your CSV file containing the order details. The file should have columns for the customer's name, email address, order date, and product details.

3. **Send Emails**:  
   Once the CSV file is uploaded, click on the "Send Emails" button. The app will automatically send emails to the addresses listed in the file, containing the order recaps. Once the progress bar reaches 100%, the sending process should be done, you can close the window.


## How to Modify the Code (For Developers only, don't bother reading that if coding disgusts you)

While the application is easy to use without any coding, you might need to modify the code in some cases, such as changing the Gmail application password, or changing the message sent. Here's how you can do it:

### Changing the Gmail Application Password

To change the Gmail application password, go to:  
[Google App Passwords](https://myaccount.google.com/u/1/apppasswords?rapt=AEjHL4MCJFoY8wj1is5Gvna4Nd1mTUJJ9MaIYLDpG2w7fAatDz7UB3zVuufK-TfDzoRgMkK4BX1dfp-lkcV4ecENa6QpMS2WyN0mhjf0b9C4FaMGypH9AjA)

**Important**: The application password is reset every time the Gmail account password for Pépin changes. It is annoying... 

Once you've generated the new application password, you can start the fun part : coding and crying because of packages incompatibility (I hate PyQT5-Qt5).
Start by cloning the repository (you will probably need some tokens, ask ChatGPT in case of errors). 

### Rebuilding the Application

If you need to modify the code (e.g., changing the Gmail password as mentioned), follow these steps to rebuild the `.exe` (Windows) and the '.app' (MacOS):

1. **Create a New Conda Environment**:
   It's highly recommended to create a new environment to avoid unnecessary package installations. I like to use conda environments. If you have miniconda downloaded on your computer (which you should all have #les_cours_de_sip), you can follow these steps to create an env called pepin_env (python 3.10 might be outdated one day... The packages compatibility is very important to create the Mac version of the app. I really recommand you to stick to requirements versions for as long as possible) :
   
   ```bash
   conda create -n pepin_env python=3.10
   conda activate pepin_env
   pip install -r requirements.txt

2. **Do your modifications**:
   Update the code as you wish (for instance the password in the Python code (line 70 in `mails_Pépin_app.py`)). Try to run your code bedore trying to push it please.

3. **Rebuild the Application**:
   Navigate to the folder containing your Python script (mails_Pépin_app.py) and the logo_pepin_icon.ico using bash.

   ```bash
   pyinstaller --onefile --windowed --icon=logo_pepin_icon.ico mails_Pépin_app.py

This will generate an .exe file if you are using a Windows in the dist folder, which can be shared with others. It is your new app.

4. **Create the .app (MacOS) or .exe Application**
   Here comes the fun part if by absolute horror you had to touch the requirements.txt file. You need to push your modifications. The build will then begin in "Actions". If everything runs smoothly the built will appear in Artifacts. You can download it and keep the mails_Pépin_app.app.
   If you are usig a Mac, you create the *windows* app by doing the same process, but before pushing you need to update the l10 of build.yml.

6. **Upload the new apps on the drive**
   Upload your two new files on the Pépin drive, so everyone can use you new app, just by downloading it ! (You might need to ask the VPépin to do it if you don't have the email password.)
   It's very important to always keep the 2 versions updated, so the users of every types of devices will be able to reuse your app.


And if you think that this README is way too long, and you need help with the code, you can try to contact me at louisa.arfib@gmail.com.

