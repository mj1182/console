#!/usr/bin/python3

import npyscreen
import subprocess

# This application class serves as a wrapper for the initialization of curses
# and also manages the actual forms of the application

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())
        self.registerForm("GitAdd", GitAdd())

# This form class defines the display that will be presented to the user.

class MainForm(npyscreen.Form):
    def create(self):
        self.action = self.add(npyscreen.TitleText, name = "action", value= "" )

        self.myDepartment = self.add(npyscreen.TitleSelectOne, max_height=9,
                                name='Department',
                                values = ['Department 1', 'Department 2', 'Department 3', 'Department 3', 'Department 3'],
                                scroll_exit = True  # Let the user move out of the widget by pressing the down arrow instead of tab.  Try it without
                                                    # to see the difference.
                                )

    def afterEditing(self):
        if self.action.value == "add":
            self.parentApp.setNextForm("GitAdd")
            self.parentApp.retorno = "entro"
        else:
            self.parentApp.retorno = self.action.value
            self.parentApp.setNextForm( None )

class GitAdd(npyscreen.Form):
    def create(self):
        self.files = self.files = self.add(npyscreen.TitleMultiSelect, max_height=20,
                                name='Department',
                                values = [],
                                scroll_exit = True  # Let the user move out of the widget by pressing the down arrow instead of tab.  Try it without
                                                    # to see the difference.
                                )

    def beforeEditing(self):
        path = "/home/m/proyectos/compraloahi/"
        resultados = subprocess.check_output( ["git", "status", "--porcelain"], cwd=path ).splitlines()
        self.files.values = resultados

    def afterEditing(self):
        cmd = "git add"

        for file in self.files.values:
            cmd += " " + str(file, "utf-8")

        self.parentApp.retorno = cmd

        self.parentApp.setNextForm(None)




if __name__ == '__main__':
    TA = MyTestApp()
    TA.run()

    print(TA.retorno)
