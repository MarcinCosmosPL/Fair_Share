import tkinter as tk
from functions import *
from Communicators import *

#necessary variables
cost = 0 #cost - to be stored in int - lowest currency units (gr = 0.01 pln) and displayed using MoneyFormat()
FandClist = [] #friends and contributions list - to be filled with tuples of names and abs amounts (in lowest curr - gr)

#window and its adjustments
window = tk.Tk()
window.title(Title)
window.geometry("500x550")
window.columnconfigure([0,1], weight=1, minsize=100)
window.rowconfigure(0, weight=1, minsize=100)
window.rowconfigure([1,3], weight=1, minsize=200)
window.rowconfigure(2, weight=1, minsize=10)

###creating left upper frame with widgets to take the cost
frm_cost_taker = tk.Frame(relief = tk.RAISED, borderwidth=5)

def func_cost_taker(): #function for cost taking button
    global cost
    costGiven = entry_cost_taker.get()
    costGivenCent = entry_cost_cent_taker.get()
    if costGiven.isnumeric() and (costGivenCent.isnumeric() or costGivenCent == '') and len(costGivenCent)<=2:
        if len(costGivenCent) == 2:
            cost = grFormat(costGiven,costGivenCent)
        elif len(costGivenCent) == 1:
            cost = grFormat(costGiven, costGivenCent+"0")
        elif len(costGivenCent) == 0:
            cost = grFormat(costGiven, costGivenCent + "00")
        if cost == 0:
            lbl_cost_display["text"] = noGivenCost
        else:
            lbl_cost_display["text"] = costIs.format(str(MoneyFormat(cost))) ## OUR GOAL
    else:
        lbl_cost_display["text"] = costError

#widgets definitions
lbl_cost_taker = tk.Label(master = frm_cost_taker, text = costButtonLabel)
entry_cost_taker = tk.Entry(master = frm_cost_taker, justify = tk.RIGHT, width=10)
lbl_cost_comma = tk.Label(master = frm_cost_taker, text = ",")
entry_cost_cent_taker = tk.Entry(master = frm_cost_taker, width=5)
btn_cost_taker = tk.Button(master = frm_cost_taker, text = costButtonAction, command = func_cost_taker)

#widgets allingment
lbl_cost_taker.grid(row=0, column=0, columnspan=3)
entry_cost_taker.grid(row=1, column=0)
entry_cost_taker.insert(0,"0")
lbl_cost_comma.grid(row=1, column=1)
entry_cost_cent_taker.grid(row=1, column=2)
entry_cost_cent_taker.insert(0,"00")
btn_cost_taker.grid(row=2, column=0, columnspan=3)

frm_cost_taker.grid(row=0, column=0)

###creating right upper label to display the cost
lbl_cost_display = tk.Label(master=window, relief=tk.SUNKEN, text=noGivenCost, borderwidth=5)

lbl_cost_display.grid(row=0, column=1, sticky="news")

###creating left middle frame to take the names and contributions
frm_FandC = tk.Frame(relief = tk.RAISED, borderwidth=5)

#buttons functions
def func_Fandc_insert():
    global FandClist
    person = entry_FandC_name.get()
    contr = entry_FandC_contr.get()
    contrCent = entry_FandC_contr_cent.get()
    if person and contr.isnumeric() and (contrCent.isnumeric() or contrCent=="") and len(contrCent)<=2:
        entry_FandC_name.delete(0, tk.END)
        if len(contrCent) == 2: #perfect situation
            FandClist.append((person,grFormat(contr, contrCent)))
            lbl_FandC_display["text"] = FandCDisplayer(FandClist)
        if len(contrCent) == 1:
            FandClist.append((person, grFormat(contr, contrCent+'0')))
            lbl_FandC_display["text"] = FandCDisplayer(FandClist)
        if contrCent == "":
            FandClist.append((person, grFormat(contr, contrCent+'00')))
            lbl_FandC_display["text"] = FandCDisplayer(FandClist)
    else: #warning text
        if not(lbl_FandC_display["text"].endswith(FandCerror)):
            lbl_FandC_display["text"]+='\n'+FandCerror

def func_Fandc_remove():
    global FandClist
    person = entry_FandC_name.get()
    for FandC in FandClist[::-1]: #reverse the list - if we have two same names, it will remove the lat one
        if FandC[0] == person:
            FandClist.remove(FandC)
            break
    if FandClist:
        lbl_FandC_display["text"] = FandCDisplayer(FandClist)
    else:
        lbl_FandC_display["text"] = noGivenFandC

def func_Fandc_clear(): #not yet alligned
    global FandClist
    FandClist = []
    lbl_FandC_display["text"] = noGivenFandC

#widget definitions
lbl_FandC = tk.Label(master = frm_FandC, text = give_FandC)
lbl_FandC_name = tk.Label(master = frm_FandC, text = personName)
entry_FandC_name = tk.Entry(master = frm_FandC, width=15)
lbl_FandC_contr = tk.Label(master = frm_FandC, text = personContribution)
entry_FandC_contr= tk.Entry(master = frm_FandC, width=10, justify = tk.RIGHT)
entry_FandC_contr.insert(0, "0")
lbl_FandC_comma = tk.Label(master = frm_FandC, text = ",")
entry_FandC_contr_cent = tk.Entry(master = frm_FandC, width=5)
entry_FandC_contr_cent.insert(0, "00")
btn_FandC_insert = tk.Button(master = frm_FandC, text = insert, command = func_Fandc_insert)
btn_FandC_remove = tk.Button(master = frm_FandC, text = remove, command = func_Fandc_remove)
btn_FandC_clear = tk.Button(master = frm_FandC, text = clear, command = func_Fandc_clear)

#widgets allingment
lbl_FandC.grid(row=0, column=0, columnspan=5)
lbl_FandC_name.grid(row=1, column=0)
entry_FandC_name.grid(row=1, column=1, columnspan=4, sticky="w")
lbl_FandC_contr.grid(row=2, column=0)
entry_FandC_contr.grid(row=2, column=1, sticky="w")
lbl_FandC_comma.grid(row=2, column=3, sticky="w")
entry_FandC_contr_cent.grid(row=2, column=4, sticky="w")
btn_FandC_insert.grid(row=3, column=0, columnspan=5, sticky="we")
btn_FandC_remove.grid(row=4, column=0, columnspan=5, sticky="we")
btn_FandC_clear.grid(row=5, column=0, columnspan=5, sticky="we")

frm_FandC.grid(row=1, column=0)

###creating right middle label to display list of people and their contributions
lbl_FandC_display = tk.Label(master=window, relief=tk.SUNKEN, text=noGivenFandC, borderwidth=5)
lbl_FandC_display.grid(row=1, column=1, sticky="news")

###lower button to run the process
#but first its command
def func_Fair_Share():
    if cost == 0 and not FandClist:
        lbl_Fair_Share_display["text"] =  noCostOrPersonForShare
    elif cost == 0 and FandClist:
        lbl_Fair_Share_display["text"] =  noCostForShare
    elif cost != 0 and not FandClist:
        lbl_Fair_Share_display["text"] =  noPersonForShare
    else: #GOAL!!!!!!!!!!!!!!!!!!!!!
        lbl_Fair_Share_display["text"] = fairDivider(cost, FandClist)

btn_Fair_Share = tk.Button(master=window, relief =tk.RAISED, text = run_Fair_Share, command = func_Fair_Share)
btn_Fair_Share.grid(row=2, column=0, columnspan=3, sticky="news")

###lowest label to display results
lbl_Fair_Share_display = tk.Label(master=window, relief=tk.SUNKEN, text='', borderwidth=5)
lbl_Fair_Share_display.grid(row=3, column=0, columnspan=3, sticky="news")

window.mainloop()