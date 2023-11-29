from django.core.mail import send_mail, BadHeaderError


def send_email(email, os, city, country):
    message = f"""

        Dear {email},

        We recently detected a new login activity from {country},{city} and {os} OS.

        If you initiated these changes, you can disregard this email. However, if you did not make these changes or suspect unauthorized access, please take the following steps:

        1. Change your password immediately using the account recovery process.
        2. Review and update your account security settings.
        3. Check for any connected apps or devices that you do not recognize and revoke access if necessary.
        4. Enable two-factor authentication for an extra layer of security.

        If you have any concerns or need further assistance, please visit our support page.

        Thank you for your prompt attention to this matter.

        Sincerely,
        The Addissytems Team
    """
    try:
        send_mail('Security Alert', message, 'jegisew21@gmial.com', ['degisew.mengist21@gmail.com'])
    except BadHeaderError:
        print("Bad Header Error!")