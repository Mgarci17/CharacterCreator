"""
    Main page in use for the GUI
"""
from PageBase import Page
import Tkinter as Tk


class Load(Page):

    character_separator = "#"

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        NMELabel = Tk.Label(self, text='Name: ', fg='black')
        LVLLabel = Tk.Label(self, text='Level: ', fg='black')
        CLSLabel = Tk.Label(self, text='Class: ', fg='black')
        BKGLabel = Tk.Label(self, text='Background: ', fg='black')
        STRlabel = Tk.Label(self, text='STR: ', fg='red')
        DEXlabel = Tk.Label(self, text='DEX: ', fg='red')
        CONlabel = Tk.Label(self, text='CON: ', fg='red')
        WISlabel = Tk.Label(self, text='WIS: ', fg='red')
        INTlabel = Tk.Label(self, text='INT: ', fg='red')
        CHAlabel = Tk.Label(self, text='CHA: ', fg='red')

        user_nme_label = Tk.Label(self, text=self.pull_variables("NME"), fg='black')
        user_lvl_label = Tk.Label(self, text=self.pull_variables("LVL"), fg='black')
        user_cls_label = Tk.Label(self, text=self.pull_variables("CLS"), fg='black')
        user_bkg_label = Tk.Label(self, text=self.pull_variables("BKG"), fg='black')
        user_str_label = Tk.Label(self, text=self.pull_variables("STR"), fg='black')
        user_dex_label = Tk.Label(self, text=self.pull_variables("DEX"), fg='black')
        user_con_label = Tk.Label(self, text=self.pull_variables("CON"), fg='black')
        user_wis_label = Tk.Label(self, text=self.pull_variables("WIS"), fg='black')
        user_int_label = Tk.Label(self, text=self.pull_variables("INT"), fg='black')
        user_cha_label = Tk.Label(self, text=self.pull_variables("CHA"), fg='black')

        hit_points = Tk.Label(self, text=self.pull_variables("HP"), fg='black')
        armor_class = Tk.Label(self, text=self.pull_variables('AC'), fg='black')
        max_hit_points = Tk.Label(self, text=self.pull_variables("MAXHP"), fg='black')
        hitPointLabel = Tk.Label(self, text="Hit Points: ", fg='black')
        maxHitPointLabel = Tk.Label(self, text='Max Hit Points: ', fg='black')
        armorClassLabel = Tk.Label(self, text='Armor Class: ', fg='black')

        saves_label= Tk.Label(self, text="Saves", fg='black')

        SPCLabel1 = self.make_space()
        # SPCLabel2 = self.make_space()
        SPCLabel3 = self.make_space()
        SPCLabel4 = self.make_space()
        SPCLabel5 = self.make_space()
        SPCLabel6 = self.make_space()
        SPCLabel7 = self.make_space()

        proficiency_label = Tk.Label(self, text='Proficiency: ', fg='black')
        user_prof_label = Tk.Label(self, text=self.pull_variables("PROF"), fg='black')
        experience_label = Tk.Label(self, text='XP: ', bg='orange3')
        user_xp_label = Tk.Label(self, text=self.pull_variables("XP"), bg='orange3')
        gold_label = Tk.Label(self, text='Gold: ', bg='goldenrod1')
        user_gold_label = Tk.Label(self, text=self.pull_variables("GOLD"), bg='goldenrod1')

        user_str_save_label = Tk.Label(self, text=self.pull_variables("STRSV"), fg='black')
        user_dex_save_label = Tk.Label(self, text=self.pull_variables("DEXSV"), fg='black')
        user_con_save_label = Tk.Label(self, text=self.pull_variables("CONSV"), fg='black')
        user_wis_save_label = Tk.Label(self, text=self.pull_variables("WISSV"), fg='black')
        user_int_save_label = Tk.Label(self, text=self.pull_variables("INTSV"), fg='black')
        user_cha_save_label = Tk.Label(self, text=self.pull_variables("CHASV"), fg='black')

        # Now start placing items into the frame
        NMELabel.grid(row=0, column=0)
        LVLLabel.grid(row=1, column=0)
        CLSLabel.grid(row=2, column=0)
        BKGLabel.grid(row=3, column=0)

        SPCLabel1.grid(row=4, column=0, columnspan=2)

        maxHitPointLabel.grid(row=5, column=0)
        armorClassLabel.grid(row=6, column=0)
        hitPointLabel.grid(row=7, column=0)

        # SPCLabel2.grid(row=8, column=0)

        STRlabel.grid(row=9, column=0)
        DEXlabel.grid(row=10, column=0)
        CONlabel.grid(row=11, column=0)
        WISlabel.grid(row=12, column=0)
        INTlabel.grid(row=13, column=0)
        CHAlabel.grid(row=14, column=0)

        user_nme_label.grid(row=0, column=1)
        user_lvl_label.grid(row=1, column=1)
        user_cls_label.grid(row=2, column=1)
        user_bkg_label.grid(row=3, column=1)

        SPCLabel3.grid(row=4, column=1)

        max_hit_points.grid(row=5, column=1)
        armor_class.grid(row=6, column=1)
        hit_points.grid(row=7, column=1)

        SPCLabel4.grid(row=8, column=1)

        user_str_label.grid(row=9, column=1, sticky='W')
        user_dex_label.grid(row=10, column=1, sticky='W')
        user_con_label.grid(row=11, column=1, sticky='W')
        user_wis_label.grid(row=12, column=1, sticky='W')
        user_int_label.grid(row=13, column=1, sticky='W')
        user_cha_label.grid(row=14, column=1, sticky='W')

        user_str_save_label.grid(row=9, column=2, sticky='W')
        user_dex_save_label.grid(row=10, column=2, sticky='W')
        user_con_save_label.grid(row=11, column=2, sticky='W')
        user_wis_save_label.grid(row=12, column=2, sticky='W')
        user_int_save_label.grid(row=13, column=2, sticky='W')
        user_cha_save_label.grid(row=14, column=2, sticky='W')

        proficiency_label.grid(row=0, column=2)
        SPCLabel5.grid(row=1, column=2)
        experience_label.grid(row=2, column=2)
        gold_label.grid(row=3, column=2)
        user_prof_label.grid(row=0, column=3)
        SPCLabel6.grid(row=1, column=3)
        user_xp_label.grid(row=2, column=3)
        user_gold_label.grid(row=3, column=3)

        saves_label.grid(row=8, column=2, sticky='W')

        SPCLabel7.grid(row=0, column=15, columnspan=3)

        weapon_header_label = Tk.Label(self, text='Weapon', font='bold', bg='indian red')
        attack_header_label = Tk.Label(self, text='Attack', font='bold', bg='indian red')
        damage_header_label = Tk.Label(self, text='Damage', font='bold', bg='indian red')

        weapon_header_label.grid(row=16, column=0)
        attack_header_label.grid(row=16, column=1)
        damage_header_label.grid(row=16, column=2)

    def make_space(self):
        return Tk.Label(self, text=self.character_separator * 11, bg='black')

    @staticmethod
    def pull_variables(attribute):
        attrib_dict = {"STR": 16,
                       "DEX": 14,
                       "CON": 14,
                       "WIS": 12,
                       "INT": 11,
                       "CHA": 10,
                       "NME": "David",
                       "LVL": 3,
                       "CLS": "Wiz",
                       "BKG": "Sage",
                       "STRSV": 3,
                       "DEXSV": 2,
                       "WISSV": 1,
                       "CONSV": 2,
                       "INTSV": 0,
                       "CHASV": 0,
                       "HP": 10,
                       "MAXHP": 40,
                       "AC": 15,
                       "PROF": 2,
                       "XP": 600,
                       "GOLD": 10
                       }
        return attrib_dict[attribute]
