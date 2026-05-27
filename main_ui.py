import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# „Õ«Ê·… «·« ’«· »«·„Õ—ﬂ «·”—Ì dn35_core
try:
    import dn35_core
except ModuleNotFoundError:
    messagebox.showerror(
        "Erreur SystËme", 
        "Le moteur sÈcurisÈ (dn35_core) est introuvable.\n"
        "Veuillez vous assurer que le fichier .so est dans le mÍme dossier."
    )
    sys.exit(1)

class GenDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GEN-D : Next-Gen Encryption Engine")
        self.root.geometry("550x400")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.selected_file_path = ""

        # Styles
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, text="?? GEN-D ENCRYPTION SYSTEM", 
            font=("Arial", 16, "bold"), fg="#ff9900", bg="#1e1e1e"
        )
        title_label.pack(pady=15)

        # File Selection Frame
        file_frame = tk.LabelFrame(self.root, text=" ?? SÈlection du Fichier ", fg="#ffffff", bg="#1e1e1e", font=("Arial", 10))
        file_frame.pack(fill="x", padx=20, pady=10)

        self.file_label = tk.Label(file_frame, text="Aucun fichier sÈlectionnÈ", fg="#aaaaaa", bg="#1e1e1e", wraplength=480, anchor="w")
        self.file_label.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        browse_btn = tk.Button(file_frame, text="Parcourir...", command=self.browse_file, bg="#ff9900", fg="#ffffff", activebackground="#cc7a00", font=("Arial", 9, "bold"), bd=0, padx=10)
        browse_btn.pack(side="right", padx=10, pady=10)

        # Credentials Frame
        cred_frame = tk.LabelFrame(self.root, text=" ?? SÈcuritÈ & Authentification ", fg="#ffffff", bg="#1e1e1e", font=("Arial", 10))
        cred_frame.pack(fill="x", padx=20, pady=10)

        # Key Entry
        tk.Label(cred_frame, text="ClÈ d'authentification :", fg="#ffffff", bg="#1e1e1e").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.key_entry = tk.Entry(cred_frame, show="*", width=30, bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=1)
        self.key_entry.grid(row=0, column=1, padx=10, pady=10)

        # PIN Entry
        tk.Label(cred_frame, text="Code PIN (4 chiffres) :", fg="#ffffff", bg="#1e1e1e").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.pin_entry = tk.Entry(cred_frame, show="*", width=10, bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=1)
        self.pin_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Action Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=20)

        self.encrypt_btn = tk.Button(btn_frame, text="Chiffrer le Fichier", command=self.encrypt_action, bg="#0066cc", fg="#ffffff", activebackground="#004c99", font=("Arial", 11, "bold"), bd=0, padx=15, pady=8)
        self.encrypt_btn.pack(side="left", padx=15)

        self.decrypt_btn = tk.Button(btn_frame, text="Restaurer l'Origine", command=self.decrypt_action, bg="#28a745", fg="#ffffff", activebackground="#1e7e34", font=("Arial", 11, "bold"), bd=0, padx=15, pady=8)
        self.decrypt_btn.pack(side="right", padx=15)

        # Footer
        footer = tk.Label(self.root, text="PropriÈtÈ Intellectuelle ProtÈgÈe ó ModËle GEN-D 2026", font=("Arial", 8, "italic"), fg="#555555", bg="#1e1e1e")
        footer.pack(side="bottom", pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_file_path = file_path
            self.file_label.config(text=os.path.basename(file_path), fg="#00ff00")

    def validate_inputs(self):
        if not self.selected_file_path:
            messagebox.showwarning("Attention", "Veuillez sÈlectionner un fichier d'abord.")
            return False
        if not self.key_entry.get():
            messagebox.showwarning("Attention", "Veuillez entrer la clÈ d'authentification.")
            return False
        if not self.pin_entry.get() or not self.pin_entry.get().isdigit():
            messagebox.showwarning("Attention", "Veuillez entrer un code PIN valide (chiffres uniquement).")
            return False
        return True

    def encrypt_action(self):
        if self.validate_inputs():
            # Â‰« «·ﬂÊœ ﬂÌ ’· œÌ—Ìﬂ  »«·„Õ—ﬂ «·”—Ì œÌ«·ﬂ dn35_core
            # ﬂÌ„—— ·ÌÂ «·„·›° «·„› «Õ° Ê«·‹ PIN
            try:
                # «› —«÷ «”„ «·œ«·… œ«Œ· «·‹ .so ÂÌ encrypt_file
                #  –ﬂ—  »œÌ·Â« ≈–« ﬂ«‰  «·œ«·… „”„Ì… ‘Ì Õ«Ã… √Œ—Ï Ê”ÿ «·‹ pyx «·ﬁœÌ„
                success = dn35_core.encrypt_file(self.selected_file_path, self.key_entry.get(), self.pin_entry.get())
                if success:
                    messagebox.showinfo("SuccËs", "Fichier chiffrÈ avec succËs via l'architecture DN-35gmx !")
                else:
                    messagebox.showerror("Echec", "Erreur lors du chiffrement. VÈrifiez vos accËs.")
            except AttributeError:
                # ≈Ì·« ﬂ«‰  «·œ«·… „”„Ì… »‘ﬂ· „Œ ·›° «·”Ì” „ €«Ì⁄ÿÌ —”«·…  Ã—Ì»Ì…
                messagebox.showinfo("Mode DÈmo", "Action de chiffrement reÁue par le noyau DN-35gmx.")

    def decrypt_action(self):
        if self.validate_inputs():
            try:
                # «› —«÷ «”„ «·œ«·… œ«Œ· «·‹ .so ÂÌ decrypt_file
                success = dn35_core.decrypt_file(self.selected_file_path, self.key_entry.get(), self.pin_entry.get())
                if success:
                    messagebox.showinfo("SuccËs", "Fichier restaurÈ avec succËs dans son format natif !")
                else:
                    messagebox.showerror("Echec", "ClÈ ou code PIN incorrect.")
            except AttributeError:
                messagebox.showinfo("Mode DÈmo", "Action de restauration reÁue par le noyau DN-35gmx.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GenDApp(root)
    root.mainloop()