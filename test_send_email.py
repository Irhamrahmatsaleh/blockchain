from backend.auth.email_verification import send_verification_email

# Ganti dengan email kamu sendiri untuk uji coba
recipient = "sintaci734@gmail.com"
link = "https://neutron.app/verify?token=abc123"

send_verification_email(recipient, link)
