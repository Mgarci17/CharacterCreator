"""
    Skills page in use for the GUI
"""
from PageBase import Page
import Tkinter as Tk


class Load(Page):
    acrobatics = 'acrobatics'
    athletics = 'athletics'
    animal_handle = 'animal handling'
    arcana = 'arcana'
    deception = 'deception'
    history = 'history'
    intimidation = 'intimidation'
    insight = 'insight'
    investigation = 'investigation'
    medicine = 'medicine'
    nature = 'nature'
    perception = 'perception'
    performance = 'performance'
    persuasion = 'persuasion'
    religion = 'religion'
    sleight_hand = 'sleight of hand'
    stealth = 'stealth'
    survival = 'survival'

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.acrobatics_var = Tk.IntVar()
        self.athletics_var = Tk.IntVar()
        self.animals_var = Tk.IntVar()
        self.arcana_var = Tk.IntVar()
        self.deception_var = Tk.IntVar()
        self.history_var = Tk.IntVar()
        self.intimidation_var = Tk.IntVar()
        self.insight_var = Tk.IntVar()
        self.investigation_var = Tk.IntVar()
        self.medicine_var = Tk.IntVar()
        self.nature_var = Tk.IntVar()
        self.perception_var = Tk.IntVar()
        self.persuasion_var = Tk.IntVar()
        self.performance_var = Tk.IntVar()
        self.religion_var = Tk.IntVar()
        self.soh_var = Tk.IntVar()
        self.stealth_var = Tk.IntVar()
        self.survival_var = Tk.IntVar()

        acrobatics_box = Tk.Checkbutton(self, variable=self.acrobatics_var, text=self.acrobatics.upper())
        athletics_box = Tk.Checkbutton(self, variable=self.athletics_var, text=self.athletics.upper())
        animal_handling_box = Tk.Checkbutton(self, variable=self.animals_var, text=self.animal_handle.upper())
        arcana_box = Tk.Checkbutton(self, variable=self.arcana_var, text=self.arcana.upper())
        deception_box = Tk.Checkbutton(self, variable=self.deception_var, text=self.deception.upper())
        history_box = Tk.Checkbutton(self, variable=self.history_var, text=self.history.upper())
        intimidation_box = Tk.Checkbutton(self, variable=self.intimidation_var, text=self.intimidation.upper())
        insight_box = Tk.Checkbutton(self, variable=self.insight_var, text=self.insight.upper())
        investigation_box = Tk.Checkbutton(self, variable=self.investigation_var, text=self.investigation.upper())
        medicine_box = Tk.Checkbutton(self, variable=self.medicine_var, text=self.medicine.upper())
        nature_box = Tk.Checkbutton(self, variable=self.nature_var, text=self.nature.upper())
        perception_box = Tk.Checkbutton(self, variable=self.perception_var, text=self.perception.upper())
        performance_box = Tk.Checkbutton(self, variable=self.performance_var, text=self.performance.upper())
        persuasion_box = Tk.Checkbutton(self, variable=self.persuasion_var, text=self.persuasion.upper())
        religion_box = Tk.Checkbutton(self, variable=self.religion_var, text=self.religion.upper())
        sleight_of_hand_box = Tk.Checkbutton(self, variable=self.soh_var, text=self.sleight_hand.upper())
        stealth_box = Tk.Checkbutton(self, variable=self.stealth_var, text=self.stealth.upper())
        survival_box = Tk.Checkbutton(self, variable=self.survival_var, text=self.survival.upper())

        acrobatics_box.grid(row=0, column=0, sticky='W')
        athletics_box.grid(row=1, column=0, sticky='W')
        animal_handling_box.grid(row=2, column=0, sticky='W')
        arcana_box.grid(row=3, column=0, sticky='W')
        deception_box.grid(row=4, column=0, sticky='W')
        history_box.grid(row=5, column=0, sticky='W')
        intimidation_box.grid(row=6, column=0, sticky='W')
        insight_box.grid(row=7, column=0, sticky='W')
        investigation_box.grid(row=8, column=0, sticky='W')
        medicine_box.grid(row=9, column=0, sticky='W')
        nature_box.grid(row=0, column=1, sticky='W')
        perception_box.grid(row=1, column=1, sticky='W')
        performance_box.grid(row=2, column=1, sticky='W')
        persuasion_box.grid(row=3, column=1, sticky='W')
        religion_box.grid(row=4, column=1, sticky='W')
        sleight_of_hand_box.grid(row=5, column=1, sticky='W')
        stealth_box.grid(row=6, column=1, sticky='W')
        survival_box.grid(row=7, column=1, sticky='W')

        acro_label = Tk.Label(self, text="+{}".format(self.get_skills(self.acrobatics)))
        athl_label = Tk.Label(self, text="+{}".format(self.get_skills(self.athletics)))

    def get_skills(self, skill):
        # The get() will return a 0 for an unchecked skill and a 1 for a checked skill

        skills_dict = {'acrobatics': self.acrobatics_var.get(),
                       'athletics': self.athletics_var.get(),
                       'animal handling': self.animals_var.get(),
                       'arcana': self.arcana_var.get(),
                       'deception': self.deception_var.get(),
                       'history': self.history_var.get(),
                       'intimidation': self.intimidation_var.get(),
                       'insight': self.insight_var.get(),
                       'investigation': self.investigation_var.get(),
                       'medicine': self.medicine_var.get(),
                       'nature': self.nature_var.get(),
                       'perception': self.perception_var.get(),
                       'performance': self.performance_var.get(),
                       'persuasion': self.persuasion_var.get(),
                       'religion': self.religion_var.get(),
                       'sleight of hand': self.soh_var.get(),
                       'stealth': self.stealth_var.get(),
                       'survival': self.survival_var.get()}
        return skills_dict[skill]