import os
import webbrowser

# Set your desktop path
desktop = r"C:\Users\A\OneDrive\Desktop"

print("1. Create Folder")
print("2. Create File")
print("3. Send WhatsApp Message")
print("4. Shutdown PC")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    folder_name = input("Enter folder name: ")
    folder_path = os.path.join(desktop, folder_name)
    try:
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created on Desktop.")
    except FileExistsError:
        print("Folder already exists.")
    except Exception as e:
        print("Error:", e)

elif choice == "2":
    file_name = input("Enter file name (with extension, like test.txt): ")
    file_path = os.path.join(desktop, file_name)
    try:
        with open(file_path, 'w') as f:
            f.write("")
        print(f"File '{file_name}' created on Desktop.")
    except Exception as e:
        print("Error:", e)

elif choice == "3":
    phone = input("Enter the phone number with country code (e.g. +91XXXXXXXXXX): ")
    message = input("Enter your message: ")
    try:
        url = f"https://web.whatsapp.com//send?phone={phone}&text={message}"
        webbrowser.open(url)
        print("WhatsApp Web opened in your browser. Please press 'Enter' in chat to send the message manually.")
    except Exception as e:
        print("Could not open WhatsApp Web. Error:", e)

elif choice == "4":
    confirm = input("Are you sure you want to shutdown your PC? (yes/no): ")
    if confirm.lower() == "yes":
        print("Shutting down your PC...")
        os.system("shutdown /s /t 1")
    else:
        print("Shutdown canceled.")

else:
    print("Invalid choice. Please enter a number from 1 to 4.")