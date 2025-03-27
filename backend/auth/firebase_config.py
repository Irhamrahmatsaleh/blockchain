import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth

# Muat variabel dari .env
load_dotenv()

# Ambil path file credentials dari .env
firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS")

# Inisialisasi Firebase Admin SDK (hanya jika belum)
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials_path)
    firebase_admin.initialize_app(cred)

# Untuk penggunaan di file lain
firebase_auth = auth
