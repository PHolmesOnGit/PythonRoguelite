
class Armor:
    def __init__(self):
        self.items = ["Mirror Armor", "Spiked Armor", "Hardened Oak Plates", "Armor of the Square Table",
                      "Purified Robes", "Thick Burlap Garb", "Empress Nauhra's Chain Mail Set", "Adventurer's Set",
                      "Royal Robes", "Alchemist's Cloak", "Meteorite Armor"]
        self.items_lore = {
            "Mirror Armor": "Forged with bright silver and obsidian chunks, this armor protects it's wearer from magic"
                            "and the elements.",
            "Spiked Armor": "Steel armor covered with spiked nails, this armor hurts foes who attack it's wearer.",
            "Hardened Oak Plates": "Hand carved by Amara, these sturdy plates offer decent protection without"
                                   "restricting movement",
            "Armor of the Square Table": "Heavy Iron Armor designed for the Knights of the Square Table, only the "
                                         "strongest of weapons can hit this armor without breaking",
            "Purified Robes": "Robes washed in boiling Gayuma, this practice is said to protect the robes from all "
                              "diseases and increase its softness. Warm, Cozy, and practical",
            "Thick Burlap Garb": "Makeshift clothes created from thick pieces of burlap and tied with ropes, plenty of"
                                 "pockets and holes to hide weapons and stolen gold",
            "Empress Naurha's Chain Mail Set": "An ornate robe lined with mythril chain mail, an heirloom worn by an "
                                               "ancient empress with immense power.",
            "Adventurer's Set": "This has everything one could need! A large backpack to store all your supplies,"
                                "extra space for ingredients and potions, decent steel armor plates, and a warm "
                                "cloak",
            "Royal Robes": "Fine Robes of cotton, lined with gold fibers, this robe commands authority, and radiates"
                           "confidence and respect.",
            "Alchemist's Cloak": "A dark leather armor set with a black cloak to match. The insides of the cloak are"
                                 "lined with multiple slots for potions, and a large pocket that contains all the "
                                 "devices necessary for brewing on the go.",
            "Meteorite Armor": "No one knows how this armor was made, it is far to heavy for any normal person to wear."
                               "But old fables tell of a god-like warrior, who could wield this armor with ease, and "
                               "used it to conquer the Great Demon King that threatened to destroy this world."
        }
        self.stats = {
            "Mirror Armor": {
                "type": "medium",
                "physical_reduction": .05,
                "magic_reduction": .60,
                "status_reduction": 0,
                "speed_penalty": 0,
            },
            "Spike Armor": {
                "type": "heavy",
                "physical_reduction": .20,
                "magic_reduction": .20,
                "status_reduction": .10,
                "speed_penalty": 0,
            },
            "Hardened Oak Plates": {
                "type": "medium",
                "physical_reduction": .15,
                "magic_reduction": .15,
                "status_reduction": .20,
                "speed_penalty": 0,
            },
            "Armor of the Square Table": {
                "type": "heavy",
                "physical_reduction": .35,
                "magic_reduction": .35,
                "status_reduction": .10,
                "speed_penalty": 0,
            },
            "Purified Robes": {
                "type": "light",
                "physical_reduction": .10,
                "magic_reduction": .10,
                "status_reduction": .50,
                "speed_penalty": 0,
            },
            "Thick Burlap Garb": {
                "type": "light",
                "physical_reduction": .10,
                "magic_reduction": .20,
                "status_reduction": 0,
                "speed_penalty": 0,
            },
            "Empress Naurha's Chain Mail Set": {
                "type": "medium",
                "physical_reduction": .25,
                "magic_reduction": .25,
                "status_reduction": .25,
                "speed_penalty": 0,
            },
            "Adventurer's Set": {
                "type": "light",
                "physical_reduction": .15,
                "magic_reduction": .15,
                "status_reduction": .10,
                "speed_penalty": 0,
            },
            "Royal Robes": {
                "type": "light",
                "physical_reduction": .05,
                "magic_reduction": .20,
                "status_reduction": 0,
                "speed_penalty": 0,
            },
            "Alchemist's Cloak": {
                "type": "medium",
                "physical_reduction": .10,
                "magic_reduction": .40,
                "status_reduction": 0,
                "speed_penalty": 0,
            },
            "Meteorite Armor": {
                "type": "heavy",
                "physical_reduction": .60,
                "magic_reduction": .60,
                "status_reduction": .50,
                "speed_penalty": 0,
            },
        }
