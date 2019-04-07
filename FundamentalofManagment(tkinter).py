from tkinter import *

def functionalStructure():
    global TopManager
    global totalDepartments
    totalDepartments = IntVar(root)
    Label(root,text="Head", bg = "BLACK", fg = "white").place(x = 600, y = 240)
    TopManager = Entry(root, bg = "cyan")
    TopManager.place(x=660, y=240)
    show = Button(root, text="Submit", command=showFunctionalStructure, bg = "cyan", activebackground = "CYAN")
    show.place(x=700, y=600)
    Button(root, text="New Window", command=dropMenu, bg = "cyan", activebackground = "CYAN").place(x=600, y=600)
    choices = {1, 2, 3, 4,5,6,7,8}
    totalDepartments.set("Functional Departments")
    numOfDepartments = OptionMenu(root, totalDepartments, *choices)
    numOfDepartments.place(x=600, y= 270)
    totalDepartments.trace('w', enterDepNames)
    numOfDepartments.config(bg = "cyan", fg = "BLACK", activebackground = "CYAN")
    numOfDepartments["menu"].config(bg="CYAN")

def enterDepNames(*args):
    global depLst
    n = totalDepartments.get()
    depLst = []
    x = 580
    y = 310
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "Department "+ a, bg = "black", fg = "white").place(x=x, y=y)
        depLst.append(Entry(root, bg = "cyan"))
        depLst[i].place(x=x+80, y=y)
        y += 20


def showFunctionalStructure():
    root.title('Functional Structure')
    canvas = Canvas(root, bg="black")  
    canvas.pack(expand=YES, fill=BOTH)
    size = 4 * len(TopManager.get())
    Label(canvas, text=TopManager.get(), fg='black', bg='cyan').place(x=663-size,y = 100)
    canvas.create_line(663,110,663,160, fill = 'white')
    Button(root, text="New Window", command=dropMenu, bg = "cyan", activebackground = "CYAN").place(x=600, y=700)
    n = totalDepartments.get()
    if n == 1:
        xAxis = 663
        l = 0
    else:
        canvas.create_line(80,160,1266,160, fill = 'white')
        l = 1186/(n-1)
        xAxis = 80
    for  i in range(0, n):
        size = 4 * len(depLst[i].get())
        canvas.create_line(xAxis,160,xAxis,220,fill = 'white')
        Label(canvas, text=depLst[i].get(), fg='black', bg='cyan').place(x=xAxis-size,y = 220)
        canvas.create_line(xAxis,240,xAxis,320,fill = 'white')
        Label(canvas, text=depLst[i].get()+" Manager", fg='black', bg='cyan').place(x=xAxis-size,y =320)
        canvas.create_line(xAxis,340,xAxis,420, fill = 'white')
        Label(canvas, text=depLst[i].get()+" Assistant Manager", fg='black', bg='cyan').place(x=xAxis-size,y = 420)
        canvas.create_line(xAxis,440,xAxis,520, fill = 'white')
        Label(canvas, text=depLst[i].get()+" Officer", fg='black', bg='cyan').place(x=xAxis-size,y = 520)
        xAxis += l    
def enterCountriesName(*args):
    global conLst
    global cdLst
    n = totalCountries.get()
    conLst = []
    cdLst = []
    x = 580
    z = 850
    y = 350
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "Country "+a, bg = "black", fg = "white").place(x=x, y=y)
        conLst.append(Entry(root, bg = "cyan"))
        conLst[i].place(x=x+80, y=y)
        Label(root,text= "Country Director "+a, bg = "black", fg = "white").place(x=z-25, y=y)
        cdLst.append(Entry(root, bg = "cyan"))
        cdLst[i].place(x=z+80, y=y)
        y += 20
    
def enterCitiesName(*args):
    global depLst1
    global ciLst
    m = totalCountries.get()
    n = m * totalCities.get()
    depLst1 = []
    ciLst = []
    z = 580
    x = 850
    y = 440
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "City "+a, bg = "black", fg = "white").place(x=z, y=y)
        ciLst.append(Entry(root, bg = "cyan"))
        ciLst[i].place(x=z+80, y=y)
        Label(root,text= "Department "+a, bg = "black", fg = "white").place(x=x, y=y)
        depLst1.append(Entry(root, bg = "cyan"))
        depLst1[i].place(x=x+80, y=y)
        y += 20
    
    
def showDivisionalStructure():
    root.title('Divisional Structure')
    canvas = Canvas(root, bg="black")   
    canvas.pack(expand=YES, fill=BOTH)  
    size1 = 4 * len(TopManager.get())
    Label(canvas, text=TopManager.get(), fg='black', bg='cyan').place(x=663-size1,y = 100)
    canvas.create_line(663,110,663,160, fill = 'white')
    Button(root, text="New Window", command=dropMenu, bg = "cyan", activebackground = "CYAN").place(x=600, y=700)
    n = totalCities.get()
    m = totalCountries.get()
    if m == 1:
        xAxis1 = 663
        l = 0
    else:
        canvas.create_line(300,160,1066,160,fill = 'white')
        l = 766/(m-1)
        xAxis1 = 300
    for i in range(0, m):
        size1 = 4 * len(conLst[i].get())
        canvas.create_line(xAxis1,160,xAxis1,220,fill = 'white')
        Label(canvas, text=conLst[i].get(),fg='black', bg='cyan').place(x=xAxis1-size1,y = 220)
        canvas.create_line(xAxis1,230,xAxis1,290,fill = 'white')
        size1 = 4 * len(cdLst[i].get())
        Label(canvas, text=cdLst[i].get(), fg='black', bg='cyan').place(x=xAxis1-size1,y = 290)
        canvas.create_line(xAxis1,300,xAxis1,350,fill = 'white')
        if n == 1:
            xAxis = xAxis1
            c = 0
        else:
            canvas.create_line(xAxis1-150,350,xAxis1+100,350,fill = 'white')
            c = 250/(n-1)
            xAxis = xAxis1-150
        for  i in range(0, n):
            size2 = 4 * len(ciLst[i].get())
            canvas.create_line(xAxis,350,xAxis,420,fill = 'white')
            Label(canvas, text=ciLst[i].get(), fg='black', bg='cyan').place(x=xAxis-size2,y = 420)
            size2 = 4 * len(depLst1[i].get())
            canvas.create_line(xAxis,430,xAxis,490,fill = 'white')
            Label(canvas, text=depLst1[i].get(), fg='black', bg='cyan').place(x=xAxis-size2,y = 490)
            canvas.create_line(xAxis,500,xAxis,560,fill = 'white')
            Label(canvas, text=depLst1[i].get()+" Manager", fg='black', bg='cyan').place(x=xAxis-size2,y =560)
            canvas.create_line(xAxis,570,xAxis,610,fill = 'white')
            Label(canvas, text=depLst1[i].get()+" Assistant Manager", fg='black', bg='cyan').place(x=xAxis-size2,y = 610)
            canvas.create_line(xAxis,600,xAxis,660,fill = 'white')
            Label(canvas, text=depLst1[i].get()+" Officer", fg='black', bg='cyan').place(x=xAxis-size2,y = 660)
            xAxis += c
        xAxis1 += l 
    
def divisionalStructure():
    global TopManager
    global totalCountries
    global totalCities
    totalCities = IntVar(root)
    totalCountries = IntVar(root)
    Label(root,text="Head", bg = "BLACK", fg = "white").place(x = 620, y = 240)
    TopManager = Entry(root, bg = "cyan")
    TopManager.place(x=660, y=240)
    show = Button(root, text="Submit", command=showDivisionalStructure, bg = "cyan", activebackground = "CYAN")
    show.place(x=700, y=700)
    Button(root, text="New Window", command=dropMenu, bg = "cyan", activebackground = "CYAN").place(x=600, y=700)
    choices1 = {1, 2, 3}
    totalCountries.set("Number of Countries")
    numOfCountries = OptionMenu(root, totalCountries, *choices1)
    numOfCountries.place(x=600, y=270)
    totalCountries.trace('w', enterCountriesName)
    numOfCountries.config(bg = "cyan", fg = "BLACK", activebackground = "CYAN")
    numOfCountries["menu"].config(bg="CYAN")
    choices2 = {1, 2,3}
    totalCities.set("Number of Cities")
    numOfCities = OptionMenu(root, totalCities, *choices2)
    numOfCities.place(x=600, y= 310)
    totalCities.trace('w', enterCitiesName)
    numOfCities.config(bg = "cyan", fg = "BLACK", activebackground = "CYAN")
    numOfCities["menu"].config(bg="CYAN")
    
       
        
def checkOption(*args):
    if structure.get() == "Functional Structure":
        functionalStructure()
    elif structure.get() == "Divisional Structure":
        divisionalStructure()        
        
def dropMenu():
    global root
    root = Tk()
    global structure
    root.config(bg = "black")
    totalDepartments = 0
    structure = StringVar(root)
    root.title('Fundamental of Management')
    root.geometry('1366x768')
    listStructure = {"Functional Structure", "Divisional Structure"}
    structure.set('Structure')
    menu = OptionMenu(root, structure, *listStructure)
    menu.config(bg = "cyan", fg = "BLACK", activebackground = "CYAN")
    menu["menu"].config(bg="CYAN")
    structure.trace('w', checkOption)
    menu.place(x = 600,y=200)
    root.mainloop()
dropMenu()