import _thread as thread
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog

root =Tk()

root.title('BCAW tool')
root.geometry('600x600')
root.resizable(False, False)
cwgt=Canvas(root,width=1500,height=800)
cwgt.grid()

Label(root, text="BCAWT :").place(x=10, y=470)
Label(root, text="      Automated tool for codon usage bias analysis for molecular\n").place(x=10, y=490)
####### loading bar
mpb = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
cwgt.create_window(45,430,window=mpb,anchor=NW)
mpb["maximum"] = 100

###############
####functions
###############
photo4 = PhotoImage(file = r"logo/True.png") 
photoimage4 = photo4.subsample(1, 1)


photo5 = PhotoImage(file = r"logo/done.png") 
photoimage5 = photo5.subsample(11, 11)


def Thread_run():
    thread.start_new_thread(But4, ())

def But1():
    global open_fasta
    open_fasta = filedialog.askopenfilename()
    label = StringVar()
    Label(root, image=photoimage4).place(x=210, y=55)

def But2():
    global save_folder
    save_folder = filedialog.askdirectory()
    label = StringVar()
    Label(root, image=photoimage4).place(x=210, y=155)


def But3():
    global ref_file
    ref_file = filedialog.askopenfilename()
    label = StringVar()
    Label(root, image=photoimage4).place(x=210, y=255)

def But4():
    global open_fasta
    global save_folder
    global ref_file
    label = StringVar()
    Label(root, textvariable=label).place(x=215, y=370)
    label.set(str("Running.."))

    ###
    from BCAWT import BCAWT0
    main_fasta_file = [open_fasta]
   
    try:
        if len (ref_file) != 0:
            ref_fasta_file = [ref_file]
            Auto = False
        else:
            ref_fasta_file = None
            Auto = True
    except:
        ref_fasta_file = None
        Auto = True

    if genetic_code.get() == "":
        pass
    else:
        genetic_code_ = int(genetic_code.get())
    mpb["value"] = 50
    BCAWT0.BCAW(main_fasta_file, save_path=save_folder, ref_fasta_file=ref_fasta_file, genetic_code_=1, Auto=Auto)
    mpb["value"] = 100

    ###

    Label(root, image=photoimage5).place(x=290, y=360)
    Label(root, image=photoimage4).place(x=320, y=360)

########
#Entry
########

tk.Label(root, text="Genetic Codes Number?").place(x=200, y=115)
genetic_code = tk.Entry(root)
genetic_code.place(x=365, y=115, width=60)

########
####
########
photo1 = PhotoImage(file = r"logo/fasta.png") 
photoimage1 = photo1.subsample(11, 11)

photo2 = PhotoImage(file = r"logo/savein.png") 
photoimage2 = photo2.subsample(11, 11)

photo3 = PhotoImage(file = r"logo/run.png") 
photoimage3 = photo3.subsample(25,15)
#####
but1=ttk.Button(cwgt,text='Open fasta file',width=15,command=But1, image = photoimage1, compound = RIGHT)
cwgt.create_window(20,50,window=but1,anchor=NW)

but2=ttk.Button(cwgt,text='   Save in    ',width=15,command=But2, image = photoimage2, compound = RIGHT)
cwgt.create_window(20,150,window=but2,anchor=NW)

but3=ttk.Button(cwgt,text='Open Reference',width=15,command=But3,  image = photoimage1, compound = RIGHT)
cwgt.create_window(20,250,window=but3,anchor=NW)

but4=ttk.Button(cwgt,text='Run',width=15,command=Thread_run, image = photoimage3, compound = RIGHT)
cwgt.create_window(20,350,window=but4,anchor=NW)


root.mainloop()
