# Automatic_emails

This repository contains a Python application that automatically sends email recaps of orders. It allows you to upload a CSV file with order details and send emails to recipients with product lists and quantities. Be careful, don't use it mindlessly or you will spam hundreds of poor Pépin orderers...

## Application Overview

- **Easy-to-use Interface**: No coding is required to use the application. Simply download the `.exe` file for Windows (or other versions for Mac/Linux) and run the program.
- **Upload CSV**: The user can upload a CSV file containing order details, and the app will send emails to the recipients based on the provided information.
- **Automatic Email Sending**: The app uses Gmail's SMTP to send emails with the order summary.

### App Link
You can download the application for Windows [here](https://drive.google.com/file/d/1kzxuW6yr_VZ8rYVQA2_hQc_boW5nK19g/view?usp=drive_link). Simply download the file to start using it!

## Usage

1. **Download and Run the App**:  
   Just download the `.exe` file (for Windows) or the appropriate file for Mac/Linux. No coding or installation is required.

2. **Upload CSV**:  
   Click on the "Upload CSV" button to select your CSV file containing the order details. The file should have columns for the customer's name, email address, order date, and product details.

3. **Send Emails**:  
   Once the CSV file is uploaded, click on the "Send Emails" button. The app will automatically send emails to the addresses listed in the file, containing the order recaps. Once the progress bar reaches 100%, the sending process should be done, you can close the window.

## How to Modify the Code (For Developers)

While the application is easy to use without any coding, you might need to modify the code in some cases, such as changing the Gmail application password, or changing the message sent. Here's how you can do it:

### Changing the Gmail Application Password

To change the Gmail application password, go to:  
[Google App Passwords](https://myaccount.google.com/u/1/apppasswords?rapt=AEjHL4MCJFoY8wj1is5Gvna4Nd1mTUJJ9MaIYLDpG2w7fAatDz7UB3zVuufK-TfDzoRgMkK4BX1dfp-lkcV4ecENa6QpMS2WyN0mhjf0b9C4FaMGypH9AjA)

**Important**: The application password is reset every time the Gmail account password for Pépin changes. It is annoying... 

Once you've generated the new application password, update the password in the Python code (line 70 in `mails_Pépin_app.py`).

### Rebuilding the Application

If you need to modify the code (e.g., changing the Gmail password as mentioned), follow these steps to rebuild the `.exe` (Windows) or corresponding files for Mac/Linux:

1. **Create a New Conda Environment**:
   It's highly recommended to create a new environment to avoid unnecessary package installations. I like to use conda environments. If you have miniconda downloaded on your computer (which you should all have #les_cours_de_sip), you can follow these steps to create an env called pepin_env (3.11 might be outdated one day, to be honest the python version isn't that important, just don't use a very recent one to avoid packages incompatibilities) :
   
   ```bash
   conda create -n pepin_env python=3.11
   conda activate pepin_env
   pip install -r requirements.txt

2. **Rebuild the Application**:
   Navigate to the folder containing your Python script (mails_Pépin_app.py) and the logo_pepin_icon.ico using bash.

   ```bash
   pyinstaller --onefile --windowed --icon=logo_pepin_icon.ico mails_Pépin_app.py

This will generate an .exe file if you are using a Windows in the dist folder, which can be shared with others. It is your new app.

