# email_config_example.py
# Email configuration for job alerts
# Copy this to email_config.py and fill in your details

# Enable/disable email alerts
EMAIL_ENABLED = True

# Gmail SMTP settings (for Gmail users)
# For Gmail, you need to:
# 1. Enable 2-factor authentication
# 2. Generate an "App Password" at https://myaccount.google.com/apppasswords
# 3. Use the app password below (not your regular Gmail password)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Your email credentials
SENDER_EMAIL = "your_email@gmail.com"  # Your Gmail address
SENDER_PASSWORD = "your_app_password_here"  # Gmail App Password (16 characters, NOT your regular password!)

# Where to send alerts
RECIPIENT_EMAIL = "your_email@gmail.com"  # Can be same as sender

# For other email providers, update SMTP settings:
# Outlook: smtp-mail.outlook.com, port 587
# Yahoo: smtp.mail.yahoo.com, port 587
# Custom domain: ask your email provider
