# Before using the python code , pls ensure you have all the necessary libraries installed
import pandas as pd
from  tkinter import *
from pytube import *
# from pytube.compat import quote
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size=0
def progresscheck(chunk,file_handler,bytes_remaining):
    
    file_downloaded=(file_size-bytes_remaining)
    per=(file_downloaded/file_size)*100
    dbtn.config(text=f'{round(per,2)} % Downloaded')

def download():
    global file_size
    try:
        url=url_text.get()
        # changing btn text
        dbtn.config(text='Downloading')
        dbtn.config(state=DISABLED)
        path_to_save=askdirectory()
        if path_to_save is None:
            return
        
        yt=YouTube(url,on_progress_callback=progresscheck)
        a=yt.title
        print(a)
        stream = yt.streams.get_highest_resolution()
        print(stream)
        file_size=stream.filesize
        print(file_size)
        print(stream)
        stream.download(path_to_save,a)
        print('Downloading completed....')
        dbtn.config(text='Start downlaod')
        dbtn.config(state=NORMAL)
        showinfo('Downloaded','Downloading finished')
        url_text.delete(0,END)
    except Exception as e:
        print(e)

#starting new thread
def startthread():
        thread=Thread(target=download)
        thread.start()
tk=Tk()
# pdb.set_trace()
tk.geometry('600x400')
tk.title('Youtube downloader')
# you can add customize icon for your GUI application, same is done below
tk.iconbitmap(r'C:\Users\euakumn\OneDrive - Ericsson AB\Desktop\data analysis\youtube\youtube.ico')
file=PhotoImage(file=r'C:\Users\euakumn\OneDrive - Ericsson AB\Desktop\data analysis\youtube\youtube-icon.png')
heading_icon=Label(tk,image=file)
heading_icon.image=file
heading_icon.pack(side=TOP)
url_text=Entry(tk,font=('Comic Sans Ms',13),justify=CENTER)
url_text.pack(side=TOP,fill=X,padx=40)
dbtn=Button(tk,text='Start Download',font=('Candara',13),relief='raised',command=startthread)
dbtn.pack(side=TOP,pady=30)
tk.mainloop()