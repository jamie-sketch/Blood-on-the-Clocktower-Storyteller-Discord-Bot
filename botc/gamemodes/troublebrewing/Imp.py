"""Contains the Imp Character class"""

import json 
from botc import Demon, Character
from ._utils import TroubleBrewing, TBRole

with open('botc/gamemodes/troublebrewing/character_text.json') as json_file: 
    character_text = json.load(json_file)[TBRole.imp.value.lower()]

class Imp(Demon, TroubleBrewing, Character):
    """Imp:
    Each night*, choose a player: they die. If you kill yourself this way, a Minion becomes the Imp.
    """

    def __init__(self):
        
        Character.__init__(self)
        TroubleBrewing.__init__(self)
        Demon.__init__(self)

        self._desc_string = character_text[self.name]["description"]
        self._examp_string = character_text[self.name]["examples"]
        self._instr_string = character_text[self.name]["instruction"]
        self._lore_string = character_text[self.name]["lore"]
        
        self._art_link = "http://bloodontheclocktower.com/wiki/images/4/42/Imp_Token.png"
        self._wiki_link = "http://bloodontheclocktower.com/wiki/Imp"

        self._role_enum = TBRole.imp