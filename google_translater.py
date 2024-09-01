from tkinter import *
from tkinter import ttk,messagebox
from googletrans import Translator
import googletrans
import os

#corresponding functions:

def change_label():
    a=combo1.get()
    b=combo2.get()
    label1.configure(text=a)
    label2.configure(text=b) 
    root.after(1000,change_label)


def translate():
    def get_language_code(language_name):
        for code, name in language.items():
            if name.lower() == language_name.lower():  # Case-insensitive matching
                return code
        return None  # Return None if the language name is not found

    lang1_code = get_language_code(combo1.get())
    lang2_code = get_language_code(combo2.get())
    
    if not lang1_code or not lang2_code:
        messagebox.showerror("Error", "Please select valid languages")
        return

    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=lang1_code, dest=lang2_code)
    trans_text = trans_text.text
    text2.delete(1.0, END)
    text2.insert(END, trans_text)



if __name__ == '__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("Google Translator (code_with_Samya_edition)")
    root.geometry("1080x400")
    root.resizable(False,False)
    root.config(bg="grey40")

    #icon:
    icon_path = os.path.join(os.path.dirname(__file__), 'google_trans.ico')    # Set the GUI window's icon using the correct path
    root.wm_iconbitmap(icon_path)


    #arrow:
    arrow_image_path = os.path.join(os.path.dirname(__file__), 'arrow.png')
    arrow_image=PhotoImage(file=arrow_image_path)
    image_label=Label(root,image=arrow_image,width=140,background="grey40")
    image_label.place(x=465,y=15)

    language=googletrans.LANGUAGES
    languageV= list(language.values())


    #first combobox:
    combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r",width=10)
    combo1.place(x=160,y=20)
    combo1.set("english")

    label1=Label(root,text="English",font="segoe 30 bold",bg="white",width=18,bd=5,relief=SUNKEN,background="grey20",activebackground="grey80",foreground="yellow")
    label1.place(x=10,y=50)


    #second combobox:
    combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r",width=10)
    combo2.place(x=780,y=20)
    combo2.set("spanish")  # Set a valid default language

    label2=Label(root,text="English",font="segoe 30 bold",bg="white",width=18,bd=5,relief=SUNKEN,background="grey20",activebackground="grey80",foreground="yellow")
    label2.place(x=623,y=50)
    
     
    #first frame:
    f1=Frame(root,bg="black",bd=5)
    f1.place(x=10,y=118,width=440,height=210)

    text1=Text(f1,font="Robote 20",bg="grey50",relief=SUNKEN,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=200)


    #second frame:
    f2=Frame(root,bg="black",bd=5)
    f2.place(x=625,y=118,width=440,height=210)

    text2=Text(f2,font="Robote 20",bg="grey50",relief=SUNKEN,wrap=WORD)
    text2.place(x=0,y=0,width=430,height=200)

    #scroll bar:
    sc_bar1 = Scrollbar(f1)
    sc_bar1.pack(side="right", fill="y")

    sc_bar2 = Scrollbar(f2)
    sc_bar2.pack(side="right", fill="y")    

    sc_bar1.config(command=text1.yview) 
    sc_bar2.config(command=text2.yview)
    text1.config(yscrollcommand=sc_bar1.set)
    text2.config(yscrollcommand=sc_bar2.set)

    #translate button:
    translate_button=Button(root,font="segoe 12 bold",text="Translate",height=1,width=8,command=translate,background="grey20",activebackground="grey80",foreground="yellow",relief=SUNKEN)
    translate_button.place(x=495,y=200)
    
    change_label()
    root.mainloop()