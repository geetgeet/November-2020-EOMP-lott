"""Class 1 Gabriel Moses"""
from tkinter import *
from tkinter import messagebox
#creating tkinter window
verWin =Tk()
verWin.geometry("600x300")
verWin.title("YOUR ARE ABOUT TO PLAY Ithuba LOTTO!")
verWin.config(bg="yellow")



#Verification function
def verify():
  name = name_e.get()
  age = age_en.get()
  email=email_e.get()

  """file=open('/home/user/Desktop/Ithuba lottery.txt','a')"""
  '''file.write("Player:"+ str(name_e.get())+"\n"+
             "Age:"+ str(age_en.get())+"\n"
             "E-mail:"+str(email_e.get())+"\n"+
             "Amount Payable:"
             )'''

#tr and except - for exceptions
  try:
    age = int(age)
    name=str(name)

#setting age restriction
    if (age >= 18) and (len(name)>=1):
      messagebox.showinfo("Message"," Age has been Verified")
      #Creating text document
      file=open('/home/user/Desktop/Ithuba lottery.txt','a')
      file.write("Player:"+ "*"+str(name_e.get())+"*"+"\n"+
             "Age:"+ str(age_en.get())+"\n"
             "E-mail:"+str(email_e.get())+"\n")
      file.close()

      verWin.withdraw()
      import lott_PLAY #Imprting the "lotto module"
    else:
      if len(name)<=0:
        messagebox.showinfo("Missing","Please Enter Your Name")
      else:
        messagebox.showinfo("Message","Hello there." +"\n"+"You are too Young to play Lotto.")
  except ValueError:
    messagebox.showerror("Error","Please enter your NAME and AGE.")








#creating widgets


lbl_name =Label(verWin, text = "What's your name?")
name_e = Entry(verWin)

lbl_age = Label(verWin, text ="What is your age?")
age_en = Entry(verWin)

verify_B = Button(verWin, text="Click to Play LOTTO",command=verify)
verify_B.configure(bg="green")

lbl_email=Label(verWin,text="Enter your E-mail")
email_e=Entry(verWin)


lbl_name.pack()
name_e.pack()
lbl_age.pack()
age_en.pack()
lbl_email.pack()
email_e.pack()
verify_B.pack()


verWin.mainloop()

#notr to self ____ possimbly try to append usersnums in a loop
