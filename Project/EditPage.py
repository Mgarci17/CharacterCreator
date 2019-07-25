"""
    Main edit character page
"""
from PageBase import Page
import Tkinter as Tk


class Load(Page):
    """
        Allow the user to edit their character
    """
    import Classes_and_Subclasses
    import Level_and_Attributes
    import Backgrounds

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Setting Default Class
        self.classes_var = Tk.StringVar()
        self.classes_var.set(self.Classes_and_Subclasses.available_classes[0])
        print(type(self.classes_var))
        self.subclasses_var = Tk.StringVar()
        self.subclasses_var.set(
            self.Classes_and_Subclasses.subclass_dict[
                self.Classes_and_Subclasses.available_classes[
                    self.Classes_and_Subclasses.available_classes.index(self.classes_var.get())]][0])
        # Setting Default Level and attributes
        self.level_var = Tk.IntVar()
        self.level_var.set(self.Level_and_Attributes.accepted_range[0])
        self.strength_var = Tk.IntVar()
        self.strength_var.set(self.Level_and_Attributes.accepted_range[0])
        self.dexterity_var = Tk.IntVar()
        self.dexterity_var.set(self.Level_and_Attributes.accepted_range[0])
        self.constitution_var = Tk.IntVar()
        self.constitution_var.set(self.Level_and_Attributes.accepted_range[0])
        self.wisdom_var = Tk.IntVar()
        self.wisdom_var.set(self.Level_and_Attributes.accepted_range[0])
        self.intelligence_var = Tk.IntVar()
        self.intelligence_var.set(self.Level_and_Attributes.accepted_range[0])
        self.charisma_var = Tk.IntVar()
        self.charisma_var.set(self.Level_and_Attributes.accepted_range[0])
        # Setting default background
        self.background_var = Tk.StringVar()
        self.background_var.set(self.Backgrounds.available_backgrounds[0])

        self.build_page()

    def find_subclasses(self, main_class):
        return self.Classes_and_Subclasses.subclass_dict[main_class]

    def build_page(self):
        NMELabel = Tk.Label(self, text='Name: ', fg='black')
        LVLLabel = Tk.Label(self, text='Level: ', fg='black')
        CLSLabel = Tk.Label(self, text="Class: ", fg='black')
        SLSLabel = Tk.Label(self, text="Subclass: ", fg='black')
        BKGLabel = Tk.Label(self, text='Background: ', fg='black')
        STRlabel = Tk.Label(self, text='STR: ', fg='red')
        DEXlabel = Tk.Label(self, text='DEX: ', fg='red')
        CONlabel = Tk.Label(self, text='CON: ', fg='red')
        WISlabel = Tk.Label(self, text='WIS: ', fg='red')
        INTlabel = Tk.Label(self, text='INT: ', fg='red')
        CHAlabel = Tk.Label(self, text='CHA: ', fg='red')

        user_nme_label = Tk.Entry(self)
        user_lvl_label = Tk.OptionMenu(self, self.level_var, *self.Level_and_Attributes.accepted_range)
        user_cls_label = Tk.OptionMenu(self, self.classes_var, *self.Classes_and_Subclasses.available_classes,
                                       command=self.update_subclass())
        user_sls_label = Tk.OptionMenu(self, self.subclasses_var,
                                       *self.Classes_and_Subclasses.subclass_dict[self.classes_var.get()])
        user_bkg_label = Tk.OptionMenu(self, self.background_var, *self.Backgrounds.available_backgrounds)
        user_str_label = Tk.OptionMenu(self, self.strength_var, *self.Level_and_Attributes.accepted_range)
        user_dex_label = Tk.OptionMenu(self, self.dexterity_var, *self.Level_and_Attributes.accepted_range)
        user_con_label = Tk.OptionMenu(self, self.constitution_var, *self.Level_and_Attributes.accepted_range)
        user_wis_label = Tk.OptionMenu(self, self.wisdom_var, *self.Level_and_Attributes.accepted_range)
        user_int_label = Tk.OptionMenu(self, self.intelligence_var, *self.Level_and_Attributes.accepted_range)
        user_cha_label = Tk.OptionMenu(self, self.charisma_var, *self.Level_and_Attributes.accepted_range)

        NMELabel.grid(row=0, column=0)
        user_nme_label.grid(row=0, column=1, sticky='W')
        LVLLabel.grid(row=1, column=0)
        user_lvl_label.grid(row=1, column=1, sticky='W')
        CLSLabel.grid(row=2, column=0)
        user_cls_label.grid(row=2, column=1, sticky='W')
        SLSLabel.grid(row=3, column=0)
        user_sls_label.grid(row=3, column=1)
        BKGLabel.grid(row=4, column=0)
        user_bkg_label.grid(row=4, column=1, sticky='W')

        STRlabel.grid(row=0, column=2)
        user_str_label.grid(row=0, column=3)
        DEXlabel.grid(row=1, column=2)
        user_dex_label.grid(row=1, column=3)
        CONlabel.grid(row=2, column=2)
        user_con_label.grid(row=2, column=3)
        WISlabel.grid(row=3, column=2)
        user_wis_label.grid(row=3, column=3)
        INTlabel.grid(row=4, column=2)
        user_int_label.grid(row=4, column=3)
        CHAlabel.grid(row=5, column=2)
        user_cha_label.grid(row=5, column=3)

    def update_subclass(self):

        # Still Does not work!!
        self.subclasses_var.set('')
        user_sls_label['menu'].delete(0, 'end')

        current_selection = self.classes_var.get()
        self.subclasses_var = self.Classes_and_Subclasses.subclass_dict[current_selection]

        for val in self.Classes_and_Subclasses.subclass_dict[current_selection]:
            user_sls_label.add_command(label=val, command=lambda v=self.subclasses_var, choice=val: v.set(choice))
        self.subclasses_var.set(
            self.Classes_and_Subclasses.subclass_dict[
                self.Classes_and_Subclasses.available_classes[
                    self.Classes_and_Subclasses.available_classes.index(current_selection)]][0])