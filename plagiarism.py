from tkinter import*
from difflib import SequenceMatcher

def plagcheck():
    first1=firstfile.get()
    first2=secfile.get()

    fil1=open('file1.txt','w')
    fil2=open('file2.txt','w')
    fil1.write(first1)
    fil2.write(first2)
    fil1.close()
    fil2.close()
    
    fil1=open('file1.txt','r')
    fil2=open('file2.txt','r')
    u=fil1.read()
    v=fil2.read()
    similarity= SequenceMatcher(None,u,v).ratio()
    
    output.set(similarity*100)
    fil1.close()
    fil2.close()

window=Tk()
window.geometry("600x300")
window.title("Nitin's Plagiarism Detector")
window.config(bg="pink")

Label(window,text="Plagiarism detector",font="impack 15 bold",bg="purple",fg="white").pack(fill="x")

file1_txt=Label(text="File 1 content:")
file2_txt=Label(text="File 2 content:")
file1_txt.place(x=15,y=70)
file2_txt.place(x=400,y=70)
firstfile=StringVar()
secfile=StringVar()

first_file_entry=Entry(textvariable=firstfile,width=30)
sec_file_entry=Entry(textvariable=secfile,width=30)

first_file_entry.place(x=15,y=90)
sec_file_entry.place(x=400,y=90)


button=Button(window,text="Calculate",command=plagcheck,width="10",bg="purple",fg="white")
button.place(x=250,y=140)

x=Label(window,text="Plag Result (%)",font="impack 14 bold",bg="purple",fg="pink")
x.place(x=215,y=200)

output=StringVar()
Entry(window,textvariable=output,font="impack 15 bold",bg="pink",bd=0,width=25).place(x=260,y=250)
mainloop()