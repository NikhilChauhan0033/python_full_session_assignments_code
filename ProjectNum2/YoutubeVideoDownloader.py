# pytube is not working bcz youtube make many changies that we use another library
# install this library using this command 'pip install yt-dlp'
# yt-dlp stand for YouTube - Download, Like a Pro

import os  #os: Used to run system commands (yt-dlp).
import tkinter as tk
from tkinter import messagebox

def download_video():
    url = entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube video URL!")
        return

    status_label.config(text="🔄 Downloading...", fg="blue") #config update the properties of widgets dynamically 
    t.update_idletasks()

    try:
        # Use yt-dlp to download the video
        os.system(f'yt-dlp "{url}"')
        status_label.config(text="✅ Download Complete!", fg="green")
    except Exception as e:
        status_label.config(text="❌ Download Failed", fg="red")
        messagebox.showerror("Error", str(e))

# GUI setup
t = tk.Tk()
t.title("🎥 YouTube Video Downloader")
t.geometry("600x600")
t.resizable(False, False)

tk.Label(t, text="Enter YouTube Video URL:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(t, font=("Arial", 12), width=50)
entry.pack(pady=5)

tk.Button(t, text="Download", font=("Arial", 12), command=download_video).pack(pady=10)

status_label = tk.Label(t, text="", font=("Arial", 12))
status_label.pack()

t.mainloop()


# simple way [out will be in terminal]
# import os

# url = input("Enter the YouTube video URL: ").strip()
# os.system(f'yt-dlp "{url}"')


# using pytube 'pip install pytube'

# from pytube import YouTube

# try:
#     url = input("Enter YouTube video URL: ").strip()
#     yt = YouTube(url)

#     print(f"Title: {yt.title}")
#     print("Downloading...")

#     video = yt.streams.get_highest_resolution()
#     video.download()

#     print("✅ Download complete!")

# except Exception as e:
#     print("❌ Error:", e)



# without try and except
# from pytube import YouTube

# # Ask user for the video URL
# url = input("Enter the YouTube video URL: ")

# # Create YouTube object
# yt = YouTube(url)

# # Get the highest resolution stream
# video = yt.streams.get_highest_resolution()

# # Download the video
# video.download()

# print("Download completed successfully!")
