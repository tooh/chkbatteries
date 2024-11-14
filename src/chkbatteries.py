#!/usr/bin/env python3
import subprocess
import smtplib
from email.mime.text import MIMEText

# Function to get the battery level of the Magic Mouse
def get_magic_mouse_battery_level():
    try:
        result = subprocess.run(
            ["ioreg", "-r", "-c", "AppleDeviceManagementHIDEventService"],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        # Find the battery level in the output
        for line in output.split("\n"):
            if '"BatteryPercent"' in line:
                # Extract the battery level value
                battery_level = int(line.split('=')[-1].strip())
                return battery_level
    except subprocess.CalledProcessError as e:
        print(f"Error running ioreg command: {e}")
        return None

# Function to send an email notification
def send_email(subject, body, to_email,cc_email ,from_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Cc"] = cc_email

    recipients = [to_email] + [cc_email]

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, recipients, msg.as_string())

# Function to display a macOS notification
def show_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])

# Main function to check battery level, show notification, and send email if below threshold
def main():
    battery_level = get_magic_mouse_battery_level()
    if battery_level is not None:
        print(f"Magic Mouse Battery Level: {battery_level}%")
        threshold = 20  # Set your desired threshold
        if battery_level < threshold:
            subject = "Magic Mouse Battery Alert"
            body = f"Warning: Your Magic Mouse battery level is at {battery_level}%. Please recharge it soon."
            to_email = "florijn.peter@gmail.com" 
            cc_email = "peterflorijn.uyexd@sync.omnigroup.com"
            from_email = "p.florijn@chello.nl"
            smtp_server = "smtp.ziggo.nl"
            smtp_port = 587
            smtp_username = "p.florijn@chello.nl"
            smtp_password = "AZvaElvt"

            show_notification("Magic Mouse Battery Alert", f"Battery level is at {battery_level}%. Sending email...")
            send_email(subject, body, to_email,cc_email, from_email, smtp_server, smtp_port, smtp_username, smtp_password)
            print("Low battery email sent.")
        else:
            print("Battery level is sufficient.")
    else:
        print("Unable to retrieve battery level.")

if __name__ == "__main__":
    main()

