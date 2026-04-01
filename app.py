import streamlit as st
from pathlib import Path
import shutil
import os
import stat


# Fix permission issue
def handle_remove_readonly(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


st.title("📁 File Management System")

menu = st.sidebar.selectbox("Choose Operation", [
    "Create Folder", "View Files/Folders", "Rename Folder", "Delete Folder",
    "Create File", "Read File", "Update File", "Delete File"
])


# 🔹 Create Folder
if menu == "Create Folder":
    name = st.text_input("Enter folder name")
    if st.button("Create"):
        Path(name).mkdir(exist_ok=True)
        st.success("Folder created successfully")


# 🔹 View Files
elif menu == "View Files/Folders":
    files = list(Path.cwd().rglob("*"))
    for f in files:
        st.write(f)


# 🔹 Rename Folder
elif menu == "Rename Folder":
    old = st.text_input("Old folder name")
    new = st.text_input("New folder name")
    if st.button("Rename"):
        p = Path(old)
        if p.exists():
            p.rename(new)
            st.success("Renamed successfully")
        else:
            st.error("Folder not found")


# 🔹 Delete Folder
elif menu == "Delete Folder":
    name = st.text_input("Folder to delete")
    if st.button("Delete"):
        p = Path(name)
        if p.exists():
            shutil.rmtree(p, onerror=handle_remove_readonly)
            st.success("Deleted successfully")
        else:
            st.error("Folder not found")


# 🔹 Create File
elif menu == "Create File":
    name = st.text_input("File name")
    content = st.text_area("Content")
    if st.button("Create File"):
        with open(name, "w") as f:
            f.write(content)
        st.success("File created")


# 🔹 Read File
elif menu == "Read File":
    name = st.text_input("File name")
    if st.button("Read"):
        if Path(name).exists():
            with open(name, "r") as f:
                st.text(f.read())
        else:
            st.error("File not found")


# 🔹 Update File
elif menu == "Update File":
    name = st.text_input("File name")
    option = st.selectbox("Option", ["Append", "Overwrite"])

    content = st.text_area("Content")

    if st.button("Update"):
        if Path(name).exists():
            mode = "a" if option == "Append" else "w"
            with open(name, mode) as f:
                f.write(content)
            st.success("Updated successfully")
        else:
            st.error("File not found")


# 🔹 Delete File
elif menu == "Delete File":
    name = st.text_input("File name")
    if st.button("Delete"):
        p = Path(name)
        if p.exists():
            p.unlink()
            st.success("Deleted successfully")
        else:
            st.error("File not found")