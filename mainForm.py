from tkinter import *

fields = (
    "Age",
    "Gender",
    "AirPollution",
    "AlcoholUse",
    "DustAllergy",
    "OccupationalHazards",
    "GeneticRisk",
    "ChronicLungDisease",
    "BalancedDiet",
    "Obesity",
    "Smoking",
    "PassiveSmoker",
    "ChestPain",
    "CoughingofBlood",
    "Fatigue",
    "WeightLoss",
    "ShortnessofBreath",
    "Wheezing",
    "SwallowingDifficulty",
    "ClubbingofFingerNails",
    "FrequentCold",
    "DryCough",
    "Snoring")

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def submitCall(e, r):
    opls=""

    for s in fields:
        opls+=('"'+s+'",')

    opls=opls[0:-1]
    opls+="\n"

    for s in fields:
        opls+=('"'+e[s].get()+'",')

    opls=opls[0:-1]
    opls+="\n"

    print(opls,sep="")

    r.destroy()
    return


if __name__ == '__main__':
    root = Tk()
    root.title("Lung Cancer Prediction")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: submitCall(e, root)))
    b1 = Button(root, text='Submit',
                command=(lambda e=ents: submitCall(e, root)))
    b1.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
