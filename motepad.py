from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Motepad:
    window = Tk()
    menu_bar = Menu(window)
    textarea = Text(window)
    height=800
    width=400
    my_txt_file=""

    def __init__(self, **kwargs):
        self.height=kwargs['ht']
        self.width=kwargs['wd']
        scrwd=self.window.winfo_screenwidth()
        scrht=self.window.winfo_screenheight()
        left = (scrwd / 2) - (self.width / 2)
        top = (scrht / 2) - (self.height / 2)

        self.window.geometry('%dx%d+%d+%d' % (self.width, self.height, left, top))
        self.window.title("New-Motepad")
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        self.textarea.grid(sticky=N+S+E+W)
        self.menu_bar.add_command(label="New",command=self.newfile)
        self.menu_bar.add_command(label="Open", command=self.openfile)
        self.menu_bar.add_command(label="Save",command=self.savefile)
        self.window.config(menu=self.menu_bar)

    def newfile(self):
        self.window.title("Untitled -Motepad")
        self.my_txt_file=""
        self.textarea.delete(1.0,END)
    def savefile(self):
        ans=askokcancel("Save","Save now?")
        if ans is True:
            if self.my_txt_file=="":
                self.my_txt_file=asksaveasfilename(initialfile="tmp.txt",defaultextension="*.txt",filetypes=[("All","*.*"),("txt","*.txt")])
                mycontent=open(self.my_txt_file,"w")
                mycontent.write(self.textarea.get(1.0,END))
                mycontent.close()
                self.window.title(os.path.basename(self.my_txt_file)+"- Motepad")
            else:
                overwrite=askyesno("Overwrite","replace exising file? this cannot be undone")
                if overwrite is True:
                    mycontent=open(self.my_txt_file,"w")
                    mycontent.write(self.textarea.get(1.0,END))
                    mycontent.close()
                else:
                    self.my_txt_file=""
                    self.savefile()
    def openfile(self):
        self.my_txt_file=askopenfilename(defaultextension="*.txt",filetypes=[("All","*.*"),("txt","*.txt")])
        file_content=open(self.my_txt_file,"r")
        self.textarea.delete(1.0,END)
        self.textarea.insert(1.0,file_content.read())
        file_content.close()
        self.window.title(os.path.basename(self.my_txt_file)+"- Motepad")
    def run(self):
        self.window.mainloop()

notepad=Motepad(ht=800,wd=400)
notepad.run()
