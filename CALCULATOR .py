######_________________________________Claculator_________________________________#######
#########################################################################################

from tkinter import *

root=Tk()

root.title("CALCULATOR")

root.geometry("300x400+300+300")
root.resizable(0,0)

######________________________________Functioning of Bottons______________________#######
#########################################################################################

var = ""
first_var = 0
operator = ""

def click1():
       global var
       var = var + '1'
       data.set(var)

def click2():
       global var
       var = var + '2'
       data.set(var)

def click3():
       global var
       var = var + '3'
       data.set(var)

def click4():
       global var
       var = var + '4'
       data.set(var)

def click5():
       global var
       var = var + '5'
       data.set(var)

def click6():
       global var
       var = var + '6'
       data.set(var)

def click7():
       global var
       var = var + '7'
       data.set(var)

def click8():
       global var
       var = var + '8'
       data.set(var)

def click9():
       global var
       var = var + '9'
       data.set(var)

def click0():
       global var
       var = var + '0'
       data.set(var)

def click_dot():
       global var
       var = var + '.'
       data.set(var)

######__________________________Functioning of operators__________________________########
##########################################################################################

def add():
       global first_var
       global operator
       global var
       if(var==""):
              data.set("Error,null value")
       else:
              first_var = float(var)
              operator = "+"
              var = var + "+"
              data.set(var)
       

def subtract():
       global first_var
       global operator
       global var
       if(var==""):
              data.set("Error,null value")
       else:
              first_var = float(var)
              operator = "-"
              var = var + "-"
              data.set(var)


def multiply():
       global first_var
       global operator
       global var
       if(var==""):
              data.set("Error,null value")
       else:
              first_var = float(var)
              operator = "x"
              var = var + "x"
              data.set(var)


def divide():
       global first_var
       global operator
       global var
       if(var==""):
              data.set("Error,null value")
       else:
              first_var = float(var)
              operator = "/"
              var = var + "/"
              data.set(var)

def percent():
       global first_var
       global operator
       global var
       if(var==""):
              data.set("Error,null value")
       else:
              first_var = float(var)
              operator = "%"
              var = var + "%"
              data.set(var)

def C():
       global first_var
       global operator
       global var
       var = ""
       first_var = 0
       operator = ""
       data.set(var)

def CE():
       global first_var
       global operator
       global var
       first_var = (var.split(operator)[0])
       data.set(first_var)
       var = first_var
       
#####____________________________________Print Final Result___________________######
####################################################################################
       
def result():
       global first_var
       global var
       global operator
       var2 = var
       if operator == '+':
              second_var = float((var2.split("+")[1]))
              final_ans = first_var + second_var
              data.set(final_ans)
              var = str(final_ans)

       elif operator == '-':
              second_var = int((var2.split('-')[1]))
              final_ans = first_var - second_var
              data.set(final_ans)
              var = str(final_ans)
              
       elif operator == 'x':
              second_var = float((var2.split('x')[1]))
              final_ans = first_var * second_var
              data.set(final_ans)
              var = str(final_ans)
              
       elif operator == '/':
              second_var = float((var2.split('/')[1]))
              if(second_var == 0):
                     data.set("Error,Divide by 0")
                     first_var = ""
                     var = ""
                     #data.set(var)
              else:
                     final_ans = float(first_var / second_var)
                     data.set(final_ans)
                     var = str(final_ans)

       elif operator == '%':
              final_ans = first_var/100  
              data.set(final_ans)
              var = str(final_ans)



#####_________________Frame1 for lable___________######
#######################################################
              
data = StringVar()

lbl = Label(root,text = "lable",textvariable = data,fg = "White",bg = "#000000",font = ("verdana",15),anchor = SE,relief = GROOVE,border = 0)
lbl.pack(expand = True,fill = "both")

#####_________________Frame Button row 5_________######
#######################################################

F5 = Frame(root,bg="#000000")
F5.pack(expand = True, fill = 'both')

b13 = Button(F5,text="%",command = percent,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b13.pack(side = LEFT,expand = True, fill = "both")

b14 = Button(F5,text="CE",command = CE,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b14.pack(side = LEFT,expand = True, fill = "both")

b15 = Button(F5,text="C",command = C,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b15.pack(side = LEFT,expand = True, fill = "both")

#####_________________Frame Button row 1_________######
#######################################################

F1 = Frame(root,bg="#000000")
F1.pack(expand = True, fill = 'both')

b1 = Button(F1,text="7",command = click7,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b1.pack(side = LEFT,expand = True, fill = "both")

b2 = Button(F1,text="8",command = click8,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b2.pack(side = LEFT,expand = True, fill = "both")

b3 = Button(F1,text="9",command = click9,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b3.pack(side = LEFT,expand = True, fill = "both")

b4 = Button(F1,text="+",command = add,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b4.pack(side = LEFT,expand = True, fill = "both")

#####_________________Frame Button row 2_________######
#######################################################

F2 = Frame(root,bg="#000000")
F2.pack(expand = True, fill = 'both')

b5 = Button(F2,text="4",command = click4,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b5.pack(side = LEFT,expand = True, fill = "both")

b6 = Button(F2,text="5",command = click5,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b6.pack(side = LEFT,expand = True, fill = "both")

b7 = Button(F2,text="6",command = click6,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b7.pack(side = LEFT,expand = True, fill = "both")

b8 = Button(F2,text="-",command = subtract,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b8.pack(side = LEFT,expand = True, fill = "both")

#####_________________Frame Button row 3_________######
#######################################################

F3 = Frame(root,bg="#000000")
F3.pack(expand = True, fill = 'both')

b9 = Button(F3,text="1",command = click1,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b9.pack(side = LEFT,expand = True, fill = "both")

b10 = Button(F3,text="2",command = click2,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b10.pack(side = LEFT,expand = True, fill = "both")

b11 = Button(F3,text="3",command = click3,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b11.pack(side = LEFT,expand = True, fill = "both")

b12 = Button(F3,text="x",command = multiply,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b12.pack(side = LEFT,expand = True, fill = "both")


#####_________________Frame Button row 4_________######
#######################################################

F4 = Frame(root,bg="#000000")
F4.pack(expand = True, fill = 'both')

b9 = Button(F4,text=".",command = click_dot,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b9.pack(side = LEFT,expand = True, fill = "both")

b10 = Button(F4,text="0",command = click0,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b10.pack(side = LEFT,expand = True, fill = "both")

b11 = Button(F4,text="=",command = result,fg = "White",bg = "IndianRed4",font = ("verdana",22),relief = GROOVE,border = 0)
b11.pack(side = LEFT,expand = True, fill = "both")

b12 = Button(F4,text="/",command = divide,fg = "White",bg = "#000000",font = ("verdana",22),relief = GROOVE,border = 0)
b12.pack(side = LEFT,expand = True, fill = "both")


root.mainloop()

######################################################################################################################
########################################       DIWAKER PRASHAR       #################################################
######################################################################################################################

