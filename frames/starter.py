import tkinter as tk
import tkinter.font as font
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class Executer(ttk.Frame) :

    def __init__(self, container, controller, *args, **kwargs) :
        super().__init__(container, *args, **kwargs)

        self.controller = controller

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        self.createWidgets()

        self.levelSelectionCombobox.bind("<<ComboboxSelected>>", self.setLevel)
        self.modeSelectionCombobox .bind("<<ComboboxSelected>>", self.setMode )

    def createWidgets(self) :

        ttk.Label(self,text = "1-)").grid(row=0, column=0, padx=5, ipady = 1)
        self.fileInputButton = ttk.Button(
            self,
            text = "Select File",
            command = self.getPath,
            cursor = "hand2",
            state="normal"
        )
        self.fileInputButton.grid(row=0, column=1, sticky="E", ipady = 1)

        ttk.Label(self,text = "2-)").grid(row=0, column=2, padx=5, ipady = 1)
        self.levelSelectionCombobox = ttk.Combobox(
            self,
            width=6,
            state = "disabled"
        )
        self.levelSelectionCombobox.grid(row=0, column=3, sticky="E", ipady = 6)

        ttk.Label(self,text = "3-)").grid(row=0, column=4, padx=5, ipady = 1)
        self.modeSelectionCombobox = ttk.Combobox(
            self,
            width=14,
            values = ("Compression", "Decompression"),
            state = "disabled"
        )
        self.modeSelectionCombobox.grid(row=0, column=5, sticky="E", ipady = 6)

    def getPath(self) :

        filePath = filedialog.askopenfilename(
            title = "Select an image file",
            filetypes = [("png files", "*.png"),("txt files", "*.txt"),("bin files", "*.bin")]
        )

        if filePath == "":
            messagebox.showinfo("Warning", "You must select an image or a file to continue !")
        else :
            self.controller.inputFilePath = filePath
            fileType = self.getFileType()

            self.levelSelectionCombobox["values"] = ("Level 1", "Level 2", "Level 3", "Level 4", "Level 5")
            self.modeSelectionCombobox ["values"] = ("Compression", "Decompression")

            self.levelSelectionCombobox["state"] = "normal"

            if (fileType in ("bmp","png")) :
                self.levelSelectionCombobox["values"] = ("Level 2", "Level 4")
                self.modeSelectionCombobox["values"] = "Compression"
            elif (fileType == "txt") :
                self.levelSelectionCombobox["values"] = ("Level_1")
                self.modeSelectionCombobox["values"] = "Compression"
            elif (fileType == "bin") :
                self.modeSelectionCombobox["values"] = "Decompression"
                self.levelSelectionCombobox["values"] = ("Level 1", "Level 2", "Level 4")
                self.levelSelectionCombobox["state"] = "normal"
                self.modeSelectionCombobox["state"]  = "normal"

            self.fileInputButton["text"] = f"File : \"{self.getFileName()}.{self.getFileType()}\""
            #self.fileInputButton["state"] = "disabled"

    def setLevel(self, event) :
        self.controller.proccesLevel = self.levelSelectionCombobox.get()
        self.modeSelectionCombobox["state"]  = "normal"

    def setMode(self, event) :

        self.controller.proccesMode = self.modeSelectionCombobox.get()


        if (self.controller.proccesMode == "Compression") :
            self.controller.inputWindowFrame.clearWindow()
            self.controller.inputWindowFrame.createWidgets()
            self.controller.inputWindowFrame.allowButtons()

            self.controller.outputWindowFrame.clearWindow()
            self.controller.outputWindowFrame.disableButtons()

        elif (self.controller.proccesMode == "Decompression") :
            self.controller.outputWindowFrame.clearWindow()
            self.controller.outputWindowFrame.createWidgets()
            self.controller.outputWindowFrame.allowButtons()

            self.controller.inputWindowFrame.clearWindow()
            self.controller.inputWindowFrame.disableButtons()
        #self.modeSelectionCombobox["state"]  = "disabled"

    def getFileType(self) :
        return self.controller.inputFilePath[(self.controller.inputFilePath.find("."))+1:]

    def getFileName(self) :
        return self.controller.inputFilePath[self.controller.inputFilePath.rfind("/")+1:self.controller.inputFilePath.find(".")]

    def getBoundaryPath(self) :
        return self.controller.inputFilePath[:(self.controller.inputFilePath.rfind("/"))]+"/"
