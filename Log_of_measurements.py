from tkinter import *
from tkinter import ttk
from tkinter import filedialog

"""WINDOW"""
window = Tk()
window.title('Measuring Diary')
window.geometry("700x700")

# Create a main Frame
main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)

# Create canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=TOP, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_srollbar = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
my_srollbar.pack(side=BOTTOM, fill=X)

# Configure The Canvas
my_canvas.configure(xscrollcommand=my_srollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that new frame to a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

""" TABLE """


def Data():
    """Creates a table with general data"""
    global k_box_list

    autor = Label(second_frame, text="© Mateusz Czyrzniak", font=('bold', 8))
    autor.grid(row=0, column=0)

    nazwa = Label(second_frame, text="LOG OF MEASUREMENTS WITH A STATIC GRAVIMETER", font=('bold', 15), pady=20)
    nazwa.grid(columnspan=13, row=0, column=1)

    # Observer
    observer_text = Label(second_frame, text="Observer :", font=('bold', 10))
    observer_text.grid(row=1, column=4)
    observer_input = StringVar()
    observer_box = Entry(second_frame, textvariable=observer_input)
    observer_box.grid(row=1, column=5)

    # Object
    object_text = Label(second_frame, text="Object :", font=('bold', 10))
    object_text.grid(row=1, column=6)
    object_input = StringVar()
    object_box = Entry(second_frame, textvariable=object_input)
    object_box.grid(row=1, column=7)

    # Time
    TU_text = Label(second_frame, text="TU :", font=('bold', 10))
    TU_text.grid(row=2, column=4)
    TU_input = StringVar()
    TU_box = Entry(second_frame, textvariable=TU_input)
    TU_box.grid(row=2, column=5)

    # Gravimetr
    graw_text = Label(second_frame, text="Gravimetr :", font=('bold', 10))
    graw_text.grid(row=3, column=4)
    graw_input = StringVar()
    graw_box = Entry(second_frame, textvariable=graw_input)
    graw_box.grid(row=3, column=5)

    # Constant K
    K_text = Label(second_frame, text="Constant K :", font=('bold', 10))
    K_text.grid(row=3, column=6)
    K_input = DoubleVar()
    K_box = Entry(second_frame, textvariable=K_input, bg="yellow")
    K_box.grid(row=3, column=7)
    k_box_list.append(K_box)

    # Line
    Linia_text = Label(second_frame, text="Line :", font=('bold', 10))
    Linia_text.grid(row=1, column=8)
    Linia_input = StringVar()
    Linia_box = Entry(second_frame, textvariable=Linia_input)
    Linia_box.grid(row=1, column=9)

    # Date
    date_text = Label(second_frame, text="Date :", font=('bold', 10))
    date_text.grid(row=2, column=8)
    date_input = StringVar()
    date_box = Entry(second_frame, textvariable=date_input)
    date_box.grid(row=2, column=9)


def Titles():
    """Column headers"""

    position2_text = Label(second_frame, text="Position", font=('bold', 8), relief='solid', width=18, bg="yellow")
    position2_text.grid(row=5, column=0, ipadx=10, ipady=10)

    T2_text = Label(second_frame, text="T [HH:MM]", font=('bold', 8), relief='solid', width=18, bg="yellow")
    T2_text.grid(row=5, column=1, ipadx=10, ipady=10)

    h_text = Label(second_frame, text="h [m]", font=('bold', 8), relief='solid', width=18, bg="yellow")
    h_text.grid(row=5, column=2, ipadx=10, ipady=10)

    observations2_text = Label(second_frame, text="Observations [dz]", font=('bold', 8), relief='solid', width=18,
                               bg="yellow")
    observations2_text.grid(row=5, column=3, ipadx=10, ipady=10)

    mean_text = Label(second_frame, text="Mean", font=('bold', 8), relief='solid', width=18)
    mean_text.grid(row=5, column=4, ipadx=10, ipady=10)

    gref_text = Label(second_frame, text="g_ref [mGal]", font=('bold', 8), relief='solid', width=18)
    gref_text.grid(row=5, column=5, ipadx=10, ipady=10)

    dgh_text = Label(second_frame, text="dg_h [mGal]", font=('bold', 8), relief='solid', width=18)
    dgh_text.grid(row=5, column=6, ipadx=10, ipady=10)

    ETC_text = Label(second_frame, text="ETC", font=('bold', 8), relief='solid', width=18, bg="yellow")
    ETC_text.grid(row=5, column=7, ipadx=10, ipady=10)

    grefpopr_text = Label(second_frame, text="g_refpopr [mGal]", font=('bold', 8), relief='solid', width=21)
    grefpopr_text.grid(row=5, column=8, ipady=10)

    dT_text = Label(second_frame, text="dT [h]", font=('bold', 8), relief='solid', width=18)
    dT_text.grid(row=5, column=9, ipadx=10, ipady=10)

    dTd_text = Label(second_frame, text="-dT*d [mGal]", font=('bold', 8), relief='solid', width=18)
    dTd_text.grid(row=5, column=10, ipadx=10, ipady=10)

    dryft_text = Label(second_frame, text="g_refpopr + dryft [mGal]", font=('bold', 8), relief='solid', width=18)
    dryft_text.grid(row=5, column=11, ipadx=10, ipady=10)

    dg_text = Label(second_frame, text="dg [mGal]", font=('bold', 8), relief='solid', width=18)
    dg_text.grid(row=5, column=12, ipadx=10, ipady=10)


def boxes():
    """creates line of boxes"""

    global row
    global st_number

    row += 3

    stan_input3 = StringVar()
    stan_input3_box = Entry(second_frame, textvariable=stan_input3, width=18)
    stan_input3_box.grid(row=row, column=0, ipadx=10)
    postion_list.append(stan_input3_box)

    T3 = StringVar()
    T3_box = Entry(second_frame, textvariable=T3, width=18)
    T3_box.grid(row=row, column=1, ipadx=10)
    time_list.append(T3_box)

    h3 = DoubleVar()
    h3_box = Entry(second_frame, textvariable=h3, width=18)
    h3_box.grid(row=row, column=2, ipadx=10)
    h_list.append(h3_box)

    ETC = DoubleVar()
    ETC_box = Entry(second_frame, textvariable=ETC, width=18)
    ETC_box.grid(row=row, column=7, ipadx=10)
    ETC_list.append(ETC_box)

    for i in range(0, 3):
        obs3 = DoubleVar()
        obs3_box = Entry(second_frame, textvariable=obs3, width=18)
        obs3_box.grid(row=row + i, column=3, ipadx=10)
        obs_list.append(obs3_box)

    mean_box = Entry(second_frame, width=21)
    mean_box.grid(row=row, column=4)
    mean_list_box.append(mean_box)

    gref_box = Entry(second_frame, width=21)
    gref_box.grid(row=row, column=5)
    g_ref_value_list_box.append(gref_box)

    dgh_box = Entry(second_frame, width=21)
    dgh_box.grid(row=row, column=6)
    dgh_value_list_box.append(dgh_box)

    g_ref_popr_box = Entry(second_frame, width=21)
    g_ref_popr_box.grid(row=row, column=8)
    g_ref_popr_value_list_box.append(g_ref_popr_box)

    dT_box = Entry(second_frame, width=21)
    dT_box.grid(row=row, column=9)
    dT_value_list_box.append(dT_box)

    dT_d_box = Entry(second_frame, width=21)
    dT_d_box.grid(row=row, column=10)
    dT_d_value_list_box.append(dT_d_box)

    d_ref_popr_dryft_box = Entry(second_frame, width=21)
    d_ref_popr_dryft_box.grid(row=row, column=11)
    d_ref_popr_dryft_value_list_box.append(d_ref_popr_dryft_box)

    dg_box = Entry(second_frame, width=21)
    dg_box.grid(row=row, column=12)
    dg_box_list_box.append(dg_box)

    st_number += 1


def del_Boxes():
    global n
    global st_number
    global row

    postion_list[-1].destroy()
    del postion_list[-1]
    time_list[-1].destroy()
    del time_list[-1]
    h_list[-1].destroy()
    del h_list[-1]
    ETC_list[-1].destroy()
    del ETC_list[-1]
    for i in range(-3, 0):
        obs_list[i].destroy()
        del obs_list[i]

    try:
        mean_list_box[-1].destroy()
        del mean_list_box[-1]
        g_ref_value_list_box[-1].destroy()
        del g_ref_value_list_box[-1]
        dgh_value_list_box[-1].destroy()
        del dgh_value_list_box[-1]
        g_ref_popr_value_list_box[-1].destroy()
        del g_ref_popr_value_list_box[-1]
        dT_value_list_box[-1].destroy()
        del dT_value_list_box[-1]
        dT_d_value_list_box[-1].destroy()
        del dT_d_value_list_box[-1]
        d_ref_popr_dryft_value_list_box[-1].destroy()
        del d_ref_popr_dryft_value_list_box[-1]
        dg_box_list_box[-1].destroy()
        del dg_box_list_box[-1]

    except:
        pass

    if row != 3:
        row -= 3
    if st_number != 0:
        st_number -= 1


""" FUNCTIONS """


def calculate_function():
    global st_number

    g_ref_value_list = []
    dgh_value_list = []
    g_ref_popr_value_list = []
    dT_value_list = []
    dT_d_value_list = []
    d_ref_popr_dryft_value_list = []
    mean_list = []
    dg_box_list = []

    n = 0

    # calculating the average
    for i in range(0, st_number):
        a = float(obs_list[n].get())
        b = float(obs_list[n + 1].get())
        c = float(obs_list[n + 2].get())
        if a != 0 and b != 0 and c != 0:
            mean = (a + b + c) / 3
        elif a != 0 and (b != 0 or c != 0):
            mean = (a + b + c) / 2
        elif b != 0 and (a != 0 or c != 0):
            mean = (a + b + c) / 2
        elif c != 0 and (a != 0 or b != 0):
            mean = (a + b + c) / 2
        else:
            mean = (a + b + c) / 1
        mean_list_box[i].delete(0, "end")
        mean_list_box[i].insert(0, mean)
        n += 3
        mean_list.append(mean)

    # calculating gref

    k = k_box_list[0].get()
    k = float(k)
    l = 0

    for z in range(0, st_number):
        gref = mean_list[l] * k
        g_ref_value_list.append(gref)
        g_ref_value_list_box[z].delete(0, "end")
        g_ref_value_list_box[z].insert(0, gref)
        l += 1

    # calculating dgh

    o = 0
    const_h = 0.3086

    for z in range(0, st_number):
        dgh = float(h_list[o].get()) * const_h
        dgh_value_list.append(dgh)
        dgh_value_list_box[z].delete(0, "end")
        dgh_value_list_box[z].insert(0, dgh)
        o += 1

    # g_ref_popr

    i = 0

    for z in range(0, st_number):
        g_ref_popr = dgh_value_list[i] + g_ref_value_list[i] + float(ETC_list[i].get())
        g_ref_popr_value_list_box[z].delete(0, "end")
        g_ref_popr_value_list_box[z].insert(0, g_ref_popr)
        g_ref_popr_value_list.append(g_ref_popr)
        i += 1

    # delta T

    i = 0
    try:
        for z in range(0, st_number):
            dT1 = float(time_list[0].get().split(':')[0]) + float(time_list[0].get().split(':')[1]) / 60
            dT2 = float(time_list[z].get().split(':')[0]) + float(time_list[z].get().split(':')[1]) / 60
            dT = dT2 - dT1
            dT_value_list_box[z].delete(0, "end")
            dT_value_list_box[z].insert(0, dT)
            dT_value_list.append(dT)
            i += 1

    except:

        comment.config(text='Wrong data format in T [HH:MM]', fg="red")
        return

    # -deltaT * dryft
    try:
        d = (g_ref_popr_value_list[st_number - 1] - g_ref_popr_value_list[0]) / dT_value_list[st_number - 1]

    except:
        comment.config(text='Add more postions (at least 2 in total)', fg="red")
        return

    i = 0
    for z in range(0, st_number):
        dT_d = -dT_value_list[i] * d
        dT_d_value_list_box[z].delete(0, "end")
        dT_d_value_list_box[z].insert(0, dT_d)
        dT_d_value_list.append(dT_d)
        i += 1

    # d_ref_popr_dryft

    i = 0
    z = 0
    for z in range(0, st_number):
        d_ref_popr_dryft = g_ref_popr_value_list[i] + dT_d_value_list[i]
        d_ref_popr_dryft_value_list_box[z].delete(0, "end")
        d_ref_popr_dryft_value_list_box[z].insert(0, d_ref_popr_dryft)
        d_ref_popr_dryft_value_list.append(d_ref_popr_dryft)
        i += 1

    # Done comment
    comment.config(text='Done', fg="green")

    # dg

    i = 0

    for z in range(0, st_number):
        dg = d_ref_popr_dryft_value_list[i + 1] - d_ref_popr_dryft_value_list[i]
        dg_box_list_box[z + 1].delete(0, "end")
        dg_box_list_box[z + 1].insert(0, dg)
        dg_box_list.append(dg)
        i += 1


def save_file():
    global st_number

    path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
    f = open(path, "w")
    f.write(
        "Headers\nPosition, T [HH:MM], h[m], Observations [dz], Mean, g_ref [mGal], dg_h [mGal], ETC, g_refpopr [mGal], dT [h], -dt*g [mGal], g_refpopr + dryft [mGal], dg [mGal]\n")
    for i in range(0, st_number):
        z = 0
        f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(postion_list[i].get(),
                                                                                      time_list[i].get(),
                                                                                      h_list[i].get(),
                                                                                      obs_list[z].get(),
                                                                                      obs_list[z + 1].get(),
                                                                                      obs_list[z + 2].get(),
                                                                                      mean_list_box[i].get(),
                                                                                      g_ref_value_list_box[i].get(),
                                                                                      dgh_value_list_box[i].get(),
                                                                                      ETC_list[i].get(),
                                                                                      g_ref_popr_value_list_box[
                                                                                          i].get(),
                                                                                      dT_value_list_box[i].get(),
                                                                                      dT_d_value_list_box[i].get(),
                                                                                      d_ref_popr_dryft_value_list_box[
                                                                                          i].get(),
                                                                                      dg_box_list_box[i].get()))
        z += 3
    f.close()


"""BUTTONS"""


def addLine():
    """Adding line button"""
    add_line_button = Button(second_frame,
                             text="Add line",
                             command=boxes, pady=5, width=15)
    add_line_button.grid(row=1, column=0)


def delLine():
    """Deleting line button"""
    del_line_button = Button(second_frame,
                             text="Delete last line",
                             command=del_Boxes, pady=5, width=15)
    del_line_button.grid(row=2, column=0)


def calculate():
    """Calculate button"""
    calculate_button = Button(second_frame,
                              text="Calculate",
                              command=calculate_function, pady=5, width=15)
    calculate_button.grid(row=1, column=1)


def saveFile():
    """Saves as txt"""
    calculate_button = Button(second_frame,
                              text="Save",
                              command=save_file, pady=5, width=15)
    calculate_button.grid(row=2, column=1)


""" VARIABLES """

# comments and errors label
comment = Label(second_frame, text='', font=('bold', 8), wraplength=100)
comment.grid(row=0, column=2)

# known variables
postion_list = []
obs_list = []
time_list = []
h_list = []
k_box_list = []
ETC_list = []

# serarching variables boxes lists
mean_list_box = []
g_ref_value_list_box = []
dgh_value_list_box = []
g_ref_popr_value_list_box = []
dT_value_list_box = []
dT_d_value_list_box = []
d_ref_popr_dryft_value_list_box = []
dg_box_list_box = []

st_number = 0
row = 3

"""START PROGRAM"""

Data()
Titles()
boxes()
addLine()
delLine()
calculate()
saveFile()

window.mainloop()