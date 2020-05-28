"""Contains the Empath Character class"""

import json 
from botc import Townsfolk, Character
from ._utils import TroubleBrewing, TBRole

with open('botc/gamemodes/troublebrewing/character_text.json') as json_file: 
    character_text = json.load(json_file)[TBRole.empath.value.lower()]

class Empath(Townsfolk, TroubleBrewing, Character):
    """Empath:
    Each night, you learn how many of your 2 alive neighbors are evil.
    """
    
    def __init__(self):

        Character.__init__(self)
        TroubleBrewing.__init__(self)
        Townsfolk.__init__(self)

        self._desc_string = character_text[self.name]["description"]
        self._examp_string = character_text[self.name]["examples"]
        self._instr_string = character_text[self.name]["instruction"]
        self._lore_string = character_text[self.name]["lore"]

        self._art_link = "http://bloodontheclocktower.com/wiki/images/6/61/Empath_Token.png"
        self._wiki_link = "http://bloodontheclocktower.com/wiki/Empath"

        self._role_enum = TBRole.empath
