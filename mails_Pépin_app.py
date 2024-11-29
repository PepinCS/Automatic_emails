import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QProgressBar, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
import pandas as pd
import yagmail
import re

class EmailApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pépin mail automatique")
        self.setGeometry(300, 200, 800, 600)

        # Widgets
        self.label = QLabel(f"Télécharger le fichier CSV de la perm'. \nAttention à verser le fichier donné par lydia non modifié (avant la transformation en excel). \nN'oublie pas de cliquer sur 'Envoyer les mails' après avoir chargé le csv.")
        self.label.setAlignment(Qt.AlignCenter)
        self.upload_button = QPushButton("Charger le csv")
        self.send_button = QPushButton("Envoyer les emails")
        self.send_button.setEnabled(False)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)


        # Layout
        layout = QVBoxLayout()
        spacer_top = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)  # Add a spacer at the top
        layout.addItem(spacer_top)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.send_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.progress_bar, alignment=Qt.AlignCenter)
        self.progress_bar.setMinimumWidth(300)  # Set a larger minimum width
        self.progress_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        spacer_bottom = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)  # Add a spacer at the bottom
        layout.addItem(spacer_bottom)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Signals
        self.upload_button.clicked.connect(self.upload_csv)
        self.send_button.clicked.connect(self.send_emails)

        self.df = None  # To store the loaded CSV

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                # Read only the first line
                first_line = csvfile.readline()
                # Replace double double-quotes with single quotes and remove quotes at the start and end
                cleaned_line = first_line.replace('""', '"').strip('"').rstrip('"')
                cleaned_line = cleaned_line[:-2]
                cleaned_line = re.sub(r'"([^"]*)"', lambda match: match.group(0).replace(',', ' '), cleaned_line)
                
            column_names = [name.strip() for name in cleaned_line.split(',')]
            self.df = pd.read_csv(file_path,
                 skipinitialspace=True,
                 header=None,  # Don't use the first row as the header
                 names=column_names,
                 engine='python')
            self.df = self.df.drop(0).reset_index(drop=True)
            self.label.setText(f"Loaded: {file_path.split('/')[-1]}\nN'oublie pas d'appuyer sur le bouton Envoyer les emails")
            self.send_button.setEnabled(True)

    def send_emails(self):
        if self.df is not None:
            yag = yagmail.SMTP('pepin.centralesupelec@gmail.com', 'nozn vlua dhar fesg')

            row_count = len(self.df)
            
            for index, row in self.df.iterrows():
                # Extract personal information
                name = row['Nom'] + " " + row['Prénom']
                email = row['Adresse email']
                date= row['Date de paiement']

                # Create a list of products and their quantities (ignore the first 4 columns)
                products = row[4:-3]  # Skip the first 4 columns (personal details, amount and order date)
                product_list = [f"{product}: {int(float(quantity))}" for product, quantity in products.items() if pd.notna(quantity)]


                # Create the email subject and contents
                subject = f"[Pépin] Récapitulatif de ta commande du {date}"
                contents = f"Bonjour {name},\n\nVoici le récapitulatif de ta commande du {date}:\n"
                contents += "\n".join(product_list)
                contents += "\n\nMerci pour ta commande !"
                contents += "\n\nA mercredi !"
                contents += "\nPépin"
                contents +="\n\n\nCe mail est envoyé automatiquement. Merci de ne pas répondre à cette adresse mail, elle n'est que très rarement consultée ! "
                contents +="Si tu as une question ou remarque n'hésite pas à contacter la personne qui t'envoie les mails Pépin chaque semaine !"

                # Send the email
                yag.send(to=email, subject=subject, contents=contents)
                print(f"Email envoyé à {name} ({email})")
                
                progress = int(((index + 1) / row_count) * 100)
                self.progress_bar.setValue(progress)

            self.label.setText("Emails sent successfully!")

# Main application loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailApp()
    window.show()
    sys.exit(app.exec_())
