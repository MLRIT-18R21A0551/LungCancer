import subprocess
from tkinter import *

fields = (
    "Age",
    "Gender",
    "AirPollution",
    "Alcoholuse",
    "DustAllergy",
    "OccuPationalHazards",
    "GeneticRisk",
    "chronicLungDisease",
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


#SUBMIT
def submitCall(e, r):
    opls=""

    for s in fields:
        opls+=('"'+s+'",')

    opls+='"Level"'
    opls+='\n"P777",'
    opls='"PatientId",'+opls

    for s in fields:
        opls+=('"'+e[s].get()+'",')

    opls+="\n"

    # print(opls,sep="")

    f = open("./prediction/Test.csv", "w")
    f.write(opls)
    f.close()
    f=open("p.txt",'w')
    subprocess.run("./predict.sh", shell = True, stdout=f)
    f.close()

    f=open("p.txt",'r')

    r.destroy()

    r = Tk()
    r.title("Lung Cancer Prediction")
    t=Text(r)
    t.pack()
    sf = f.read()
    t.insert(END, sf[-40:-19]+"\n"+sf[-17:-1])
    r.mainloop()

    return


if __name__ == '__main__':
    root = Tk()
    root.title("Lung Cancer Prediction")
    ents = makeform(root, fields)
    # root.bind('<Return>', (lambda event, e=ents: submitCall(e, root)))
    b1 = Button(root, text='Submit',
                command=(lambda e=ents: submitCall(e, root)))
    b1.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
