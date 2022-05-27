from frames import Executer, ToggleBar, Window

import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_THIRD = "#29384f"
COLOUR_FOURTH = "#29385f"
COLOUR_LIGHT_BACKGROUND = "#29384f"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"

class GUI(tk.Tk) :

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)

        """ STYLES """
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("LightBackground.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("DarkBackground.TFrame", background=COLOUR_SECONDARY)
        style.configure("LittleDarkBackground.TFrame", background=COLOUR_THIRD)
        style.configure("InnerBackgorund.TFrame", background=COLOUR_FOURTH)

        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure("DarkText.TLabel", background=COLOUR_LIGHT_BACKGROUND, foreground=COLOUR_DARK_TEXT,font="Courier 38")
        style.configure("LightText.TLabel", background=COLOUR_PRIMARY, foreground=COLOUR_LIGHT_TEXT,)

        style.configure("Normal.TButton", background=COLOUR_SECONDARY, foreground=COLOUR_LIGHT_TEXT, bordercolor="black", borderwidth=5, relief="solid", font=("Segoe UI", 9, "bold"))

        style.configure("Gray.TButton",     background = COLOUR_SECONDARY, foreground = "gray", bordercolor="gray", borderwidth=5, relief="solid",   font=("Segoe UI", 9, "bold"))
        style.configure("Red.TButton",      background = COLOUR_SECONDARY, foreground = "red", bordercolor="red", borderwidth=5, relief="solid",    font=("Segoe UI", 9, "bold"))
        style.configure("Green.TButton",    background = COLOUR_SECONDARY, foreground = "green", bordercolor="green", borderwidth=5, relief="solid",  font=("Segoe UI", 9, "bold"))
        style.configure("Blue.TButton",     background = COLOUR_SECONDARY, foreground = "blue", bordercolor="blue", borderwidth=5, relief="solid",   font=("Segoe UI", 9, "bold"))

        style.map("Normal.TButton", background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)])

        # Main app window is a tk widget, so background is set directly
        self["background"] = COLOUR_PRIMARY
        """ STYLES """

        self.proccesMode = None
        self.proccesLevel = None
        self.inputFilePath = None

        self.title("Huffman Coding")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        pageContainer = ttk.Frame(self,style="DarkBackground.TFrame")
        pageContainer.grid(row=0, column=0, padx=30, pady=30)

        self.executerFrame = Executer(pageContainer, self, style="InnerBackgorund.TFrame")
        self.executerFrame.grid(row=0, column=0, columnspan=2)

        self.inputWindowFrame = Window(pageContainer,self, "in")
        self.inputWindowFrame.grid(row=1,column=0)

        self.outputWindowFrame = Window(pageContainer,self, "out")
        self.outputWindowFrame.grid(row=1,column=1)

        self.startButton = ttk.Button(pageContainer, text="Start !", style="Normal.TButton", state="disabled", command=self.applyHuffman)
        self.startButton.grid(row=2, column=0, columnspan=2)

        self.toggleBarFrame = ToggleBar(pageContainer, self, style="InnerBackgorund.TFrame")
        self.toggleBarFrame.grid(row=3, column=0, columnspan=2)


        for child in pageContainer.winfo_children() :
            child.grid_configure(padx=15, pady=15)

    def applyHuffman(self) :

        if ("1" in self.proccesLevel) :
            from levels.level1 import HuffmanCoding

            input_path  = self.inputFilePath
            binary_path = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + ".bin"
            txt_path = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + ".txt"

            h = HuffmanCoding(txt_path)

            if (self.proccesMode == "Compression") :
                h.compress()
                inputFilePath = self.inputFilePath
                self.inputWindowFrame.clearWindow()
                self.inputWindowFrame.loadText(inputFilePath)
            elif (self.proccesMode == "Decompression") :
                h.decompress(binary_path)
                inputFilePath = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + "_decompressed.txt"
                self.outputWindowFrame.clearWindow()
                self.outputWindowFrame.loadText(inputFilePath)

        elif (self.proccesLevel == "Level 2") :
            from levels.level2 import HuffmanCoding

            input_path  = self.inputFilePath
            binary_path = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + ".bin"
            png_path = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + ".png"

            h = HuffmanCoding(png_path)

            if (self.proccesMode == "Compression") :
                h.compress()
                inputFilePath = self.inputFilePath
                self.inputWindowFrame.clearWindow()
                self.inputWindowFrame.loadImage(inputFilePath)
            elif (self.proccesMode == "Decompression") :
                h.decompress(binary_path)
                inputFilePath = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + "_decompressed.png"
                self.outputWindowFrame.clearWindow()
                self.outputWindowFrame.loadImage(inputFilePath)

        elif (self.proccesLevel == "Level 3") :
            pass

        elif (self.proccesLevel == "Level 4") :
            from levels.level4 import HuffmanCoding

            input_path  = self.inputFilePath
            binary_path = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + ".bin"
            png_path = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + ".png"

            h = HuffmanCoding(png_path)

            if (self.proccesMode == "Compression") :
                h.compress()
                inputFilePath = self.inputFilePath
                self.inputWindowFrame.clearWindow()
                self.inputWindowFrame.loadImage(inputFilePath)
            elif (self.proccesMode == "Decompression") :
                h.decompress(binary_path)
                inputFilePath = self.executerFrame.getBoundaryPath() + self.executerFrame.getFileName() + "_decompressed.png"
                self.outputWindowFrame.clearWindow()
                self.outputWindowFrame.loadImage(inputFilePath)

        elif (self.proccesLevel == "Level 5") :
            pass

root = GUI()
root.mainloop()
