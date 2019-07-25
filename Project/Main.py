"""
    Main introductory file for use

"""
import Tkinter as Tk
import MainPage
import SkillsPage
import SpellsPage
import EditPage
import FeaturesPage


class MainView(Tk.Frame):
    def __init__(self, *args, **kwargs):
        Tk.Frame.__init__(self, *args, **kwargs)

        # Tk.Frame.__init__(self, *args, **kwargs)

        main_sheet = MainPage.Load(self)
        skills_sheet = SkillsPage.Load(self)
        spells_sheet = SpellsPage.Load(self)
        feature_sheet = FeaturesPage.Load(self)
        edit_sheet = EditPage.Load(self)

        button_frame = Tk.Frame(self)
        container = Tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        main_sheet.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        skills_sheet.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        spells_sheet.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        feature_sheet.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        edit_sheet.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Tk.Button(button_frame, text="Main", command=main_sheet.lift)
        b2 = Tk.Button(button_frame, text="Skills", command=skills_sheet.lift)
        b3 = Tk.Button(button_frame, text="Spells", command=spells_sheet.lift)
        b4 = Tk.Button(button_frame, text="Edit", command=edit_sheet.lift)
        b5 = Tk.Button(button_frame, text="Features", command=feature_sheet.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b5.pack(side="left")
        b4.pack(side="left")

        main_sheet.show()


root = Tk.Tk()
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.wm_geometry("400x400")
root.mainloop()
