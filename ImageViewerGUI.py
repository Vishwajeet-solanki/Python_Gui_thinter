from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog


def fileClick(clicked):
    # Define the function you want to call when the filebrowser button (Open) is clicked.
    # This function should pop-up a dialog for the user to select an input image file.
    global imgName
    imgName=filedialog.askopenfilename(initialdir="D:\SWELAB\Assignment_4\Python_Tkinter_Assignment\data\imgs", title="Select Image File", filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"),))
    if imgName:
        # Set the file path to the entry widget.
        e.delete(0, END)
        a = imgName.replace(
            "D:\SWELAB\Assignment_4\Python_Tkinter_Assignment\data\imgs/", "")
        e.insert(0, a)
    
    if len(imgName) == 0 :
        return
    origImg = Image.open(imgName)
    origImg = origImg.resize((400,400),Image.LANCZOS)
    photoImg= ImageTk.PhotoImage(origImg)
    label = Label(root, image = photoImg)
    label.image = photoImg
    label.grid(row=1, column=0 ,columnspan=3)
    # To have a better clarity, please check out the sample video.


def process(clicked, captioner, classifier):
    # This function will produce the required output when 'Process' button is clicked.
    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.

    try : 
        if len(imgName) == 0 :
            print("Choose an image first!")
            return
    except : 
        print("Choose an image first!")
        return
	
    if clicked.get() == "CAPTIONING" : # If captioner is choosen from drop-down
        cap = captioner(imgName, 3)
        ans = "Top 3 captions:\n\n"
        ans += (cap[0]+"\n"+cap[1]+"\n"+cap[2])
        Output.config(text=ans)
        print(ans)
    else : # If classifier is choosen from drop-down
        output=classifier(imgName)
        ans = "3 Main Classes:\n\n"
        ans += (output[0][1]+" - " + str(output[0][0]) + "\n"+output[1][1] +
                 " - " + str(output[1][0])+"\n"+output[2][1]+" - " + str(output[2][0]))
        Output.config(text=ans)
        print(ans)
        # print(output)
        
if __name__ == '__main__':
    # Complete the main function preferably in this order:
    # Instantiate the root window.
    root=Tk()
    # Provide a title to the root window.
    root.title("IMAGE PROCESSOR")
    # Instantiate the captioner, classifier models.
    captioner = ImageCaptioningModel()
    classifier = ImageClassificationModel()
    #OPTIONS
    options = ["CAPTIONING", "CLASSIFICATION"]
    clicked = StringVar()
    clicked.set(options[0])
    e = Entry(root, width=70)
    e.grid(row=0,column=0)

    # Declare the file browsing button.
    openbutton = Button(root ,text="Open", command=partial(fileClick, clicked))
    openbutton.grid(row =0,column =1)
    # Declare the drop-down button.
    dropDown = OptionMenu(root, clicked, *options)
    dropDown.grid(row=0, column=2)
    # Declare the process button.
    myButton = Button(root, text="Process", padx = 5, command=partial(process, clicked ,captioner, classifier))
    myButton.grid(row=0, column=3)
    # Declare the output label.
    Output = Label(root, text="", relief='solid')
    Output.grid(row=1, column=4)
    root.mainloop()


