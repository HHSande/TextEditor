from appJar import gui
import os.path

fil = None
save_path = 'TxtFiles'
knownFile = False
currentFile = ""


def readFile(target):

    txt = ""
    for line in target:
        txt += line

    return txt


def createFile():
    return os.path.join(save_path, app.stringBox("Create file", "Enter the time of the file", parent=None) + ".txt")


def press(btn):
    global fil
    if btn == "Save":
        if currentFile == "":
            filNavn = createFile()
            fil = open(filNavn, 'w+')
        else:
            fil = open(currentFile, 'w')


        fil.write(app.getTextArea("t1"))

    elif btn == "Cancel":

        app.stop(event=None)

    elif btn == "Open":
        try:
            global currentFile

            fil = open(app.openBox(title=None, dirName=save_path, fileTypes=None, asFile=False, parent=None), "r")
            currentFile = os.path.join(save_path, os.path.basename(fil.name))

            read = readFile(fil)

            app.clearTextArea(title="t1", callFunction=None)
            app.setTextArea(title="t1", text=read, end=False, callFunction=False)

            global knownFile
            knownFile = True

        except IOError:
            print("Cancelled pressed")

    elif btn == "New File":
        filNavn = createFile()
        fil = open(filNavn, 'a+')
        press("Open")


app = gui()
app.setSize(400, 400)
app.addTextArea("t1")
app.addButtons(["Save", "Open", "New File", "Cancel"], press)
app.go()
