import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Frame) :

    def __init__(self, container, controller, windowType, *args, **kwargs) :
        super().__init__(container, *args, **kwargs)

        self.controller = controller
        self.pixelSizes = (500,500)
        self.defaultImg1 = ImageTk.PhotoImage(Image.new("RGB", self.pixelSizes, color="gray"))
        self.windowType = windowType

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        self.container = ttk.Frame(self,style="InnerBackgorund.TFrame")
        self.container.grid(row=0, column=0)

        self.clearWindow()

        self.createWidgets()


    def setLoadType(self) :
        try :
            self.loadType = self.controller.executerFrame.getFileType()
        except :
            self.loadType = None

    def clearWindow(self) :

        try :
            self.controller.toggleBarFrame.disableButtons()
        except :
            pass

        self.cleaner = ttk.Label(
            self.container,
            image=self.defaultImg1
        )
        self.cleaner.grid(row=0, columnspan=3, padx=15)

    def loadFile(self) :

        if (self.loadType == "bmp" or self.loadType == "png" or self.loadType == "bin") :
            self.loadImage()
            self.controller.toggleBarFrame.enableButtons()
        elif (self.loadType == "txt") :
            self.loadText()
        else :
            print("Window type is not supported, try -> png,bmp,txt,bin")
            exit()
        self.controller.startButton["state"] = "normal"

    def loadImage(self, foundPath=None, img=None) :

        try :
            if (img != None) :
                self.inputImg = ImageTk.PhotoImage(img)
                self.pWindow["image"] = self.inputImg
                self.pWindow.grid(row=0, columnspan=3, padx=15)
                self.pWindow.tkraise()
        except :
            pass
        try :
            if (foundPath != None) :
                self.inputImg = ImageTk.PhotoImage(Image.open(foundPath).resize(self.pixelSizes))
            else :
                self.inputImg = ImageTk.PhotoImage(Image.open(self.controller.inputFilePath).resize(self.pixelSizes))
            self.pWindow["image"] = self.inputImg
            self.pWindow.grid(row=0, columnspan=3, padx=15)
            self.pWindow.tkraise()
        except :
            pass
    def loadText(self, foundPath=None) :
        try :
            if (foundPath != None) :
                file = open(foundPath)
            else :
                file = open(self.controller.inputFilePath)
            str = ""
            for line in file :
                str+=line
            self.tWindow.delete("1.0", "end")
            self.tWindow.insert("1.0", str)
            self.tWindow.tkraise()
        except :
            pass
    def allowButtons(self) :
        for child in self.container.winfo_children() :
            child["state"] = "normal"

    def disableButtons(self) :
        for child in self.container.winfo_children() :
            child["state"] = "disabled"

    def createButtons(self) :

        self.loadButton = ttk.Button(
            self.container,
            text = "Load File",
            command=self.loadFile,
            cursor = "hand2",
            state="disabled",
            style="Normal.TButton"
        )
        self.loadButton.grid(row=1, column=0, sticky="E", padx=15, pady=15)

        self.clearButton = ttk.Button(
            self.container,
            text = "Clear Canvas",
            command=self.clearWindow,
            cursor = "hand2",
            state="disabled",
            style="Normal.TButton"
        )
        self.clearButton.grid(row=1, column=1, sticky="E", padx=15, pady=15)

    def createWidgets(self) :

        self.setLoadType()

        self.createButtons()

        if (self.windowType == "in") :

            if (self.loadType in ("bmp","png")):
                self.pWindow = ttk.Label(
                    self.container,
                    image=self.defaultImg1
                )
                self.pWindow.grid(row=0, columnspan=3, padx=15)
            elif (self.loadType == "txt") :
                self.tWindow = tk.Text(
                    self.container,
                    height = 31,
                    width=62
                )
                self.tWindow.grid(row=0, columnspan=3, padx=15)
            else :
                pass
        else : #self.windowType == "out"

            if (self.loadType == "txt") :
                self.tWindow = tk.Text(
                    self.container,
                    height = 31,
                    width=62
                )
                self.tWindow.grid(row=0, columnspan=3, padx=15)
            elif (self.loadType == "bin") :
                self.pWindow = ttk.Label(
                    self.container,
                    image=self.defaultImg1
                )
                self.pWindow.grid(row=0, columnspan=3, padx=15)
                self.tWindow = tk.Text(
                    self.container,
                    height = 31,
                    width=62
                )
                self.tWindow.grid(row=0, columnspan=3, padx=15)
            else :
                pass

    def display_color_channel(self, channel, foundPath=None):
        try :

            path = foundPath or self.controller.inputFilePath

            if (channel == "gray") :
                img_rgb = Image.open(path).resize(self.pixelSizes)
                img_grayscale = img_rgb.convert('L')
                self.ref = img_grayscale
                self.loadImage(img_grayscale)
                return
            elif channel == 'red':
                channel_index = 0
            elif channel == 'green':
                channel_index = 1
            else :
                channel_index = 2


            img_rgb = Image.open(path).resize(self.pixelSizes)

            image_array = np.array(img_rgb)

            n_rows = image_array.shape[0]
            n_cols = image_array.shape[1]
            for row in range(n_rows):
                for col in range(n_cols):
                    for rgb in range(3):
                        if (rgb != channel_index):
                            image_array[row][col][rgb] = 0
            pil_img = Image.fromarray(np.uint8(img_array))

            self.photo_ref = pil_img
            self.loadImage(pil_img)

        except :
            pass
