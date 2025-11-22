# email_config.py
# Email configuration for job alerts
# Update with your details to enable email notifications

# Enable/disable email alerts
EMAIL_ENABLED = True  # Set to True to enable email alerts

# Gmail SMTP settings (for Gmail users)
# For Gmail, you need to:
# 1. Enable 2-factor authentication
# 2. Generate an "App Password" at https://myaccount.google.com/apppasswords
# 3. Use the app password below (not your regular Gmail password)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Your email credentials
SENDER_EMAIL = "your_email@gmail.com"  # Your Gmail address
SENDER_PASSWORD = "your_app_password_here"  # Gmail App Password (16 characters)

# Where to send alerts
RECIPIENT_EMAIL = "your_email@gmail.com"  # Can be same as sender

# For other email providers, update SMTP settings:
# Outlook: smtp-mail.outlook.com, port 587
# Yahoo: smtp.mail.yahoo.com, port 587
# Custom domain: ask your email provider