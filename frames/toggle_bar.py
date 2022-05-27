import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from PIL import Image, ImageTk

class ToggleBar(ttk.Frame) :
    def __init__(self, container, controller, *args, **kwargs) :
        super().__init__(container, *args, **kwargs)

        self.controller = controller

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        self.filterContainer = ttk.Frame(self, style="DarkBackground.TFrame")
        self.filterContainer.grid(row=0, column=0, rowspan=2, columnspan=1, padx=50, sticky="W")

        self.resultsContainer = ttk.Frame(self, style="DarkBackground.TFrame")
        self.resultsContainer.grid(row=0, column=1, rowspan=2, columnspan=1, padx=50, sticky="E")


        self.createFilterButtons()
        self.createResultLabels()

        self.disableButtons()

    def createFilterButtons(self) :

        originalImageButton = ttk.Button(
            self.filterContainer,
            text="Original",
            style="Normal.TButton"
        )
        originalImageButton.grid(row = 0, column = 0)

        grayImageButton = ttk.Button(
            self.filterContainer,
            text="Gray",
            style="Gray.TButton",
            #command = lamda : self.controller.inputWindowFrame.display_color_channel("gray")
        )
        grayImageButton.grid(row = 0, column = 1)

        redImageButton = ttk.Button(
            self.filterContainer,
            text="Red",
            style="Red.TButton",
            #command = lamda : self.controller.inputWindowFrame.display_color_channel("red")
        )
        redImageButton.grid(row = 0, column = 2)

        greenImageButton = ttk.Button(
            self.filterContainer,
            text="Green",
            style="Green.TButton",
            #command = lamda : self.controller.inputWindowFrame.display_color_channel("green")
        )
        greenImageButton.grid(row = 0, column = 3)

        greenImageButton = ttk.Button(
            self.filterContainer,
            text="Blue",
            style="Blue.TButton",
            #command = lamda : self.controller.inputWindowFrame.display_color_channel("blue")
        )
        greenImageButton.grid(row = 0, column = 4)

        for child in self.filterContainer.winfo_children() :
            child.grid_configure(padx=10, pady=10)

    def createResultLabels(self) :

        self.entropy = tk.Label(self.resultsContainer, text="Entropy = None")
        self.entropy.grid(row=0, column=2)

        self.averageCodeLength = tk.Label(self.resultsContainer, text="Average Code Length = None")
        self.averageCodeLength.grid(row=0, column=3)

        self.difference = tk.Label(self.resultsContainer, text="Difference = None")
        self.difference.grid(row=0, column=4)

        self.inputImageSize = tk.Label(self.resultsContainer, text="Input Image Size = None")
        self.inputImageSize.grid(row=1, column=2)

        self.compressedImageSize = tk.Label(self.resultsContainer, text="Compressed Image Size = None")
        self.compressedImageSize.grid(row=1, column=3)

        self.compressionRatio = tk.Label(self.resultsContainer, text="compression Ratio = None")
        self.compressionRatio.grid(row=1, column=4)

        for child in self.resultsContainer.winfo_children() :
            child.grid_configure(padx=15, pady=5)

    def enableButtons(self) :
        for child in self.filterContainer.winfo_children() :
            child["state"] = "normal"

    def disableButtons(self) :
        for child in self.filterContainer.winfo_children() :
            child["state"] = "disabled"
