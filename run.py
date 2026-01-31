import questionary
import subprocess


def run():
    print("Welcome to UCF Eustis CLI!")
    user = input("Enter your UCF email (before @ucf.edu):")

    while True:
        selected_option = questionary.select("What would you like to do?",
                                             choices=["Upload a file", "Upload a folder", "Connect to Eustis",
                                                      "Exit"]).ask()

        if selected_option == "Upload a folder":
            folder_upload = input("Enter the path of the folder you want to upload: ")
            folder_eustis = input("Enter the path to store folder on eustis. '/' for root directory : ")
            result = subprocess.run(['scp', '-r', f"{folder_upload}", f"{user}@eustis.eecs.ucf.edu:~{folder_eustis}"],
                                    capture_output=True, text=True)
            print("Uploaded Folder!" + result.stdout)
        elif selected_option == "Upload a file":
            file_upload = input("Enter the path of the file you want to upload: ")
            file_eustis = input("Enter the path to store file on eustis. '/' for root directory: ")
            result = subprocess.run(['scp', f"{file_upload}", f"{user}@eustis.eecs.ucf.edu:~{file_eustis}"],
                                    capture_output=True, text=True)
            print("Uploaded file!" + result.stdout)
        elif selected_option == "Connect to Eustis":
            print("Connecting to Eustis...")
            subprocess.run(['ssh', f"{user}@eustis.eecs.ucf.edu"])
        elif selected_option == "Exit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        exit(0)
