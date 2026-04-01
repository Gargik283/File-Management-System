from pathlib import Path
import shutil
import os
import stat


# 🔧 Fix for Windows permission error
def handle_remove_readonly(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def create_folder():
    try:
        folder_name = input("Enter folder name: ")
        p = Path(folder_name)
        p.mkdir(exist_ok=True)
        print("Folder created successfully")
    except Exception as err:
        print(f"Error: {err}")


def read_file_folder():
    p = Path.cwd()
    items = list(p.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def update_folder():
    try:
        read_file_folder()
        old_name = input("Enter folder name to rename: ")
        p = Path(old_name)

        if p.exists() and p.is_dir():
            new_name = input("Enter new folder name: ")
            p.rename(new_name)
            print("Folder renamed successfully")
        else:
            print("Folder does not exist")
    except Exception as err:
        print(f"Error: {err}")


def delete_folder():
    try:
        read_file_folder()
        name = input("Enter folder name to delete: ")
        p = Path(name)

        if p.exists() and p.is_dir():
            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":
                shutil.rmtree(p, onerror=handle_remove_readonly)
                print("Folder deleted successfully")
            else:
                print("Cancelled")
        else:
            print("Folder does not exist")
    except Exception as err:
        print(f"Error: {err}")


def create_file():
    try:
        name = input("Enter file name (with extension): ")
        p = Path(name)

        if not p.exists():
            data = input("Enter file content: ")
            with open(name, "w") as fs:
                fs.write(data)
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as err:
        print(f"Error: {err}")


def read_file():
    try:
        read_file_folder()
        name = input("Enter file name to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(name, "r") as fs:
                print("\nFile Content:\n", fs.read())
        else:
            print("File does not exist")
    except Exception as err:
        print(f"Error: {err}")


def update_file():
    try:
        read_file_folder()
        name = input("Enter file name to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("\n1. Rename file")
            print("2. Append content")
            print("3. Overwrite content")

            try:
                choice = int(input("Choose option: "))
            except ValueError:
                print("Invalid input")
                return

            if choice == 1:
                new_name = input("Enter new file name: ")
                if not Path(new_name).exists():
                    p.rename(new_name)
                    print("File renamed successfully")
                else:
                    print("File with new name already exists")

            elif choice == 2:
                data = input("Enter content to append: ")
                with open(name, "a") as fs:
                    fs.write(" " + data)
                print("Content appended")

            elif choice == 3:
                data = input("Enter new content: ")
                with open(name, "w") as fs:
                    fs.write(data)
                print("Content overwritten")

            else:
                print("Invalid choice")

        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error: {err}")


def delete_file():
    try:
        read_file_folder()
        name = input("Enter file name to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully")
        else:
            print("File does not exist")
    except Exception as err:
        print(f"Error: {err}")


# 🔥 MAIN MENU
print("\n==== FILE MANAGEMENT SYSTEM ====")
print("1. Create Folder")
print("2. View Files/Folders")
print("3. Rename Folder")
print("4. Delete Folder")
print("5. Create File")
print("6. Read File")
print("7. Update File")
print("8. Delete File")

try:
    choice = int(input("\nEnter your choice: "))
except ValueError:
    print("Invalid input")
    exit()

if choice == 1:
    create_folder()
elif choice == 2:
    read_file_folder()
elif choice == 3:
    update_folder()
elif choice == 4:
    delete_folder()
elif choice == 5:
    create_file()
elif choice == 6:
    read_file()
elif choice == 7:
    update_file()
elif choice == 8:
    delete_file()
else:
    print("Invalid choice")