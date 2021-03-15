
#Imprting modules
from tkinter import *
import random
from tkinter import messagebox
from datetime import date

#creating Tkinter window
win=Tk()
win.config(bg="teal")
win.geometry("580x380")
win.title("Ithuba lottery."+"-"+ "LOTTERY DRAW" )

today = date.today()



#Random number generate
def select():
    counter=0
    lottonums=[] #Defines lotto number
    while counter<=6:
        lott=random.randint(1,49)
        if lott not in lottonums:
            if counter ==6:
                break
            lottonums.append(lott) #appending the generated numbers
            counter+=1
            lottonums.sort() #sorting it in assending order

            """
    for i in range (0,6): # looops for 6 times
        lott=random.randint(1,49)  #sets a restriction in the range numbers generate inn
        if lott not in lottonums:
            lottonums.append(lott)# adds the generated numbers to the lottonums
            lottonums.sort() #sorts it in accending order"""
# Try and except for error handling
    try:
        mynums=[] #defines user numbers
        #get the numbers from the entries
        num=[int(num_en1.get()),int(num_en2.get()),int(num_en3.get()),int(num_en4.get()),int(num_en5.get()),int(num_en6.get())]
        if int(num_en1.get()) >49 or int(num_en1.get())<1:
            messagebox.showinfo("Message", "Please enter number within range of 1-49.(check entry 1",icon="error")
        if int(num_en2.get()) > 49 or int(num_en2.get())<1:
            messagebox.showinfo("Message", "Please enter number within range of 1-49.(check entry 2",icon="error")
        if int(num_en3.get()) > 49 or int(num_en3.get())<1:
            messagebox.showinfo("Message", "Please enter number within range of 1-49.(check entry 3",icon="error")
        if int(num_en4.get()) > 49 or int(num_en4.get())<1:
            messagebox.showinfo("Message", "Please enter number within range of 1-49.(check entry 4",icon="error")
        if int(num_en5.get()) > 49 or int(num_en5.get())<1:
            messagebox.showinfo("Message", "Please enter number within range of 1-49.(check entry 5",icon="error")
        if int(num_en6.get()) > 49 or int(num_en6.get())<1:
            messagebox.showinfo("Message", "Please enter number within range of 1-49.(check entry 6",icon="error")



        mynums.append(num)
        num.sort()
        mynums=num

        if len(set(mynums))<6:
            messagebox.showerror("Important message","Please enter numbers or check for duplicates")

        else:
            messagebox.showinfo("Message","Your numbers are:"+"\n"+ str(mynums)+"\n"+"(Click check Result to continue)")
    except ValueError:
            messagebox.showinfo("Message","Please Enter Valid number(s)")


    #Result Funcrion: to check and compare the numbers'''
    def result():
        drawres_b.configure(bg="yellow")
        try:
            #
            if len(mynums)==0:#using length because if list is empty it should displar an error
                raise ValueError
            correct=set(mynums) & set(lottonums)
            #Applies to all underneith
            #THE CORRECT NUMBERS COMPARISON
            if len(correct) ==0:
                messagebox.showinfo("Message","You have 0 NUMBER COREECT ,\n Try Again. ")
                file=open('/home/user/Desktop/Ithuba lottery.txt','a')
                file.write(
                            "Amount Payable:0"+"\n"
                           "Date Played:"+str(today)+"\n"
                            "PLAYER NUMBERS:"+str(mynums)+"\n"
                            "LOTTO NUMBERS"+str(lottonums)+"\n"

             )
                file.close()

            elif len(correct) ==1:
                messagebox.showinfo("Message","You have 1 NUMBER COREECT ,\n Lucky Guess. \n *GET 2 NUMBERS TO WIN A PRIZE*")
                file=open('/home/user/Desktop/Ithuba lottery.txt','a')
                file.write("Amount Payable:0"+"\n"
                           "Date Played:"+str(today)+"\n"
                           "PLAYER NUMBERS:"+str(mynums)+"\n"
                            "LOTTO NUMBERS"+str(lottonums)+"\n"
             )
                file.close()


            elif len(correct) ==2:
                messagebox.showinfo("Message","You have 2 NUMBER COREECT ,\n Well done ")
                messagebox.showinfo("Congradulations!!","Congradulations!! You have won R20")
                file=open('/home/user/Desktop/Ithuba lottery.txt','a')
                file.write("Amount Payable:R20"+"\n"
                           "Date Played:"+str(today)+"\n"
                           "PLAYER NUMBERS:"+str(mynums)+"\n"
                            "LOTTO NUMBERS"+str(lottonums)+"\n"
             )
                file.close()


            elif len(correct) ==3:
                messagebox.showinfo("Message","You have 3 NUMBER COREECT ,\n Great Job. ")
                messagebox.showinfo("Congradulations!!","Congradulations!! You have won R100.50")
                file=open('/home/user/Desktop/Ithuba lottery.txt','a')
                file.write(
                            "Amount Payable:R100.50"+"\n"
                           "Date Played:"+str(today)+"\n"
                            "PLAYER NUMBERS:"+str(mynums)+"\n"
                            "LOTTO NUMBERS"+str(lottonums)+"\n"
             )
                file.close()

            elif len(correct) ==4:
                messagebox.showinfo("Message","You have 4 NUMBER COREECT ,\n Excellent! ")
                messagebox.showinfo("Congradulations!!","Congradulations!! You have won R2,384.00")
                file=open('/home/user/Desktop/Ithuba lottery.txt','a')
                file.write(
                            "Amount Payable:R2,384.00"+"\n"
                           "Date Played:"+str(today)+"\n"
                            "PLAYER NUMBERS:"+str(mynums)+"\n"
                            "LOTTO NUMBERS"+str(lottonums)+"\n"
             )
                file.close()

            elif len(correct) ==5:
                messagebox.showinfo("Message","You have 5 NUMBER COREECT ,\n Brilliant ")
                messagebox.showinfo("Congradulations!!","Congradulations!! You have won R8,584.00")
                file=open('/home/user/Desktop/Ithuba lottery.txt','a')
                file.write(
                            "Amount Payable:R 8,584.00"+"\n"+"\n"+
                           "Date Played:"+str(today)+"\n"
                            "PLAYER NUMBERS:"+str(mynums)+"\n"
                            "LOTTO NUMBERS"+str(lottonums)+"\n"
             )
                file.close()

            elif len(correct) ==6:
                messagebox.showinfo("Message","You have 6 NUMBER COREECT ,\n JACKPOT!!! ")
                messagebox.showinfo("Congradulations!!","Congradulations!! You have won R10, 000 000.00")
                file=open('/home/user/Desktop/Ithuba lottery.txt','a')
                file.write(
                            "Amount Payable:R 10,000 000.00"+"\n"+
                           "Date Played:"+str(today)+"\n"
                            "PLAYER NUMBERS:"+str(mynums)+"\n"
                            "LOTTO NUMBERS"+str(lottonums)+"\n"
             )
                file.close()
            else:
                messagebox.showerror("Error" ,"Please enter & draw numbers befor requesting result.")


            if len(correct)==0:
                lbl_lotto.config(text="Your numbers are:"+str(mynums)+"\n"
                             "The lotto numbers are:"+str(lottonums)+"\n"
                             "You guessed 0 numbers correct"+"\n"+"Today's date:"+str(today))


#to display the answers/output

            lbl_lotto.config(text="Your numbers are:"+str(mynums)+"\n"
                             "The lotto numbers are:"+str(lottonums)+"\n"+
                             "You guessed" +"**"+str(len(correct))+"**"+"number(s) correct"+"\n"
                             "Your lucky number(s) are:"+str(correct)+"\n"+
                             "Today's date:"+str(today))
            #change the button colour
            drawres_b.configure(bg="red")



#TO DISPLAY ERROR
        except ValueError:
             messagebox.showerror("Error","Please enter numbers before Draw and Request Results")
    if len(lottonums)<6:
            messagebox.showerror("Error","Sorry Something went Wrong, Please try again")
    drawres_b=Button(win,text="Lotto Result",command=result)
    drawres_b.grid(row=8,column=1)
#reset function
def reset():
    lbl_lotto.config(text= str(""))
    num_en1.delete(0,END)
    num_en2.delete(0,END)
    num_en3.delete(0,END)
    num_en4.delete(0,END)
    num_en5.delete(0,END)
    num_en6.delete(0,END)
    mynums=[]

#exit finction
def exit():
    leave= messagebox.askyesno("Are you done","Are you sure you want to EXIT?")
    if leave == True:
        win.destroy()

    else:
        messagebox.showinfo("Message","Feel free to try again.")


#creating widgets
exit_b=Button(win,text="Exit",command=exit)
exit_b.grid(row=14,column=3)


lbl_main=Label(win,text="Enter your numbers")
lbl_main.grid(row=0,column=1)
lbl_placeholder=Label(win,text="                        ")
lbl_placeholder.config(bg="teal")
lbl_placeholder.grid(row=0,column=2)

num_en1=Entry(win,width=8)
num_en1.grid(row=1,column=1)

num_en2=Entry(win,width=8)
num_en2.grid(row=2,column=1)


num_en3=Entry(win,width=8)
num_en3.grid(row=3,column=1)


num_en4=Entry(win,width=8)
num_en4.grid(row=4,column=1)


num_en5=Entry(win,width=8)
num_en5.grid(row=5,column=1)


num_en6=Entry(win,width=8)
num_en6.grid(row=6,column=1)


draw_b=Button(win,text="Draw",command=select)
draw_b.grid(row=7,column=1)


lbl_lotto=Label(win,text="", width=40,height=5)
lbl_lotto.configure(bg="yellow")
lbl_lotto.grid(row=12,column=3)

reset_b=Button(win, text="Reset",command=reset)
reset_b.grid(row=13,column=3)



win.mainloop()




