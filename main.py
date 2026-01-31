import questionary
import subprocess

def main():
    user = input("Enter your UCF email (before @ucf.edu):")
    selected_option = questionary.select("What would you like to do?", choices=["What would you like to do?", "Upload a file", "Upload a folder", "Connect to Eustis"]).ask()
    if selected_option == "Upload a folder":
        folder_upload = input("Enter the path of the folder you want to upload: ")
        folder_eustis = input("Enter the path to store folder on eustis. '/' for root directory : ")
        result = subprocess.run(['scp', '-r', f"{folder_upload}" , f"{user}@eustis.eecs.ucf.edu:~{folder_eustis}"], capture_output=True, text=True)
        print("Uploaded Folder!" + result.stdout)
    elif selected_option == "Upload a file":
        file_upload = input("Enter the path of the file you want to upload: ")
        file_eustis = input("Enter the path to store file on eustis. '/' for root directory: ")
        result = subprocess.run(['scp', f"{file_upload}" , f"{user}@eustis.eecs.ucf.edu:~{file_eustis}"], capture_output=True, text=True)
        print("Uploaded file!" + result.stdout)
    elif selected_option == "Connect to Eustis":
        print("Connecting to Eustis...")
        subprocess.run(['ssh', f"{user}@eustis.eecs.ucf.edu"])

if __name__ == "__main__":
    main()
