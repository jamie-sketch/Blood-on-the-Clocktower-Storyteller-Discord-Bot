"""Contains the Scarlet Woman Character class"""

import json 
from botc import Minion, Character
from ._utils import TroubleBrewing, TBRole

with open('botc/gamemodes/troublebrewing/character_text.json') as json_file: 
    character_text = json.load(json_file)[TBRole.scarletwoman.value.lower()]

class ScarletWoman(Minion, TroubleBrewing, Character):
    """Scarlet Woman:
    If there are 5 or more players alive & the Demon dies, you become the Demon.
    """

    def __init__(self):
        
        Character.__init__(self)
        TroubleBrewing.__init__(self)
        Minion.__init__(self)

        self._desc_string = character_text[self.name]["description"]
        self._examp_string = character_text[self.name]["examples"]
        self._instr_string = character_text[self.name]["instruction"]
        self._lore_string = character_text[self.name]["lore"]
        
        self._art_link = "http://bloodontheclocktower.com/wiki/images/7/7c/Scarlet_Woman_Token.png"
        self._wiki_link = "http://bloodontheclocktower.com/wiki/Scarlet_Woman"

        self._role_enum = TBRole.scarletwoman
