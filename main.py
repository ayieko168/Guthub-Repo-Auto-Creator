from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MainDesign import *
from cridentialsDialog import *
import requests, os

class CridentialsApp(QDialog):

    def __init__(self):

        super().__init__()
        self.crUi = Ui_Dialog()
        self.crUi.setupUi(self)
        

        self.crUi.showButton.clicked.connect(self.showPass)
        self.crUi.doneButton.clicked.connect(self.doneCMD)

    def showPass(self):

        print("show pass")
        if self.crUi.passwordEntry.echoMode():  # if normal...
            self.crUi.passwordEntry.setEchoMode(QtGui.QLineEdit.Normal)
            self.crUi.showButton.setText("hide")
        else:
            self.crUi.passwordEntry.setEchoMode(QtGui.QLineEdit.Password)
            self.crUi.showButton.setText("show")


    def getCridentials(self):

        credentials = []

        u = self.crUi.userNameEntry.text()
        p = self.crUi.passwordEntry.text()
        credentials.append(u)
        credentials.append(p)
        credentials = tuple(credentials)

        return credentials
    
    def run(self):

        self.show()
        self.exec_()

    def doneCMD(self):

        self.getCridentials()
        self.close()

class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.searchDirectoryButton.clicked.connect(self.searchDirectoryCMD)
        self.ui.createButton.clicked.connect(self.createRepoCMD)

    def searchDirectoryCMD(self):

        foundDirPath = QFileDialog.getExistingDirectory()
        dircetoryName = foundDirPath.split("\\")[-1].title().replace(" ", "-")

        # AUTO FILL FIELDS
        self.ui.searchDirectoryEntry.setText(foundDirPath)
        self.ui.repoNameEntry.setText(dircetoryName)
        
    def createRepoCMD(self):

        print("create repo...")

        # Get the credentials for github login...
        print("getting credentials...")
        crid = CridentialsApp()
        crid.run()
        user, _pass = crid.getCridentials()

        # get repoDetails ie name, commit massage etc
        print("getting repo Deatails...")
        reponame, repoPath, commitMess = self.getRepoDetails()

        # write REDAdme file
        print("Writting ReadMe file...")
        readmePath = repoPath + "\\README.md"
        with open(readmePath, "w") as rm:
            readmeTextContent = self.ui.readmeText.toPlainText()
            rm.write(readmeTextContent)

        # Create the repository github API
        print("creating reop from github API")
        repodata = r'{"name":"***"}'.replace("***", reponame)
        response = requests.post('https://api.github.com/user/repos', data=repodata, auth=(user, _pass))
        responceJson = response.json()

        # Initialize, Add, Commit and push all the repo files
        command = f"cd \"{repoPath}\" && git init && git add -A && git commit -m \"{commitMess}\" && git remote add origin https://github.com/{user}/{reponame}.git && git push -u origin master"
        os.system(command)
        
        # print("responceJson = ", responceJson)
        print("Done.\n\n")

    def getRepoDetails(self):

        ui = self.ui

        commitMassage = ui.commitMessageText.toPlainText()
        repoName = ui.repoNameEntry.text()
        repoDirectory = ui.searchDirectoryEntry.text()

        return (repoName, repoDirectory, commitMassage)


if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()
