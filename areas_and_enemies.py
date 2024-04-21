

class Bosses:
    def __init__(self):
        self.final_boss = ["Demon King"]
        self.blightwater_bosses = ["Tormet, Punishment of the Damned", "Alphis, Greed's Servant", "Ancient Basilisk",
                                   "Maven, Thief Queen"]
        self.castillion_bosses = ["Knight Tord, The Iron Lancer", "Knight Eduardo, The Iron Knight",
                                "Knight Acrius, The Iron Executor", "King Radahn"]
        self.taj_dunhi_bosses = ["Mahendra, Corrupted Monk", "Akuma, Force of Light", "Phantom of Empress Naurha"]
        self.cagayan_bosses = ["Amara, The Outcast", "The Shadow Dragon", "The Forger of Myth"]

        self.move_sets = {
            # Each boss should have 6 moves, 2 attack, 2 defensive, 2 curse
            "Torment, Punishment of the Damned": {
                "Soul Siphon": {
                    "dmg": 10,
                    "type": "curse",
                    "steal": 10,
                },
                "Hellfire": {
                    "dmg": 20,
                    "type": "Curse",
                },
                "Soul Shield": {
                    "block": 17,
                    "type": "defensive",
                },
                "Soul Drain": {
                    "block": 10,
                    "type": "defensive",
                    "steal": 10,
                },
                "Chain Whip": {
                    "dmg": 12,
                    "type": "slash",
                },
                "Soul Crush": {
                    "dmg": 15,
                    "type": "slash",
                },
            },
            "Alphis, Greed's Servant": {
                "Gold Rush": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Golden Shower": {
                    "dmg": 20,
                    "type": "slash",
                },
                "Gold Armor": {
                    "block": 15,
                    "type": "defensive",
                },
                "Gold Shield": {
                    "block": 20,
                    "type": "defensive",
                },
                "Gold Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
                "Golden Touch": {
                    "dmg": 5,
                    "type": "curse",
                    "steal": 5,
                },
            },
            "Ancient Basilisk": {
                "Petrify": {
                    "dmg": 10,
                    "type": "curse",
                },
                "Venomous Bite": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Stone Skin": {
                    "block": 20,
                    "type": "defensive",
                },
                "Stone Gaze": {
                    "block": 15,
                    "type": "defensive",
                },
                "Tail Whip": {
                    "dmg": 10,
                    "type": "slash",
                },
                "Venomous Spit": {
                    "dmg": 15,
                    "type": "curse",
                },
            },
            "Maven, Thief Queen": {
                "Dagger Throw": {
                    "dmg": 10,
                    "type": "slash",
                },
                "Backstab": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Smoke Bomb": {
                    "block": 15,
                    "type": "defensive",
                },
                "Shadow Step": {
                    "block": 20,
                    "type": "defensive",
                },
                "Steal": {
                    "dmg": 5,
                    "type": "curse",
                    "steal": 5,
                },
                "Thief's Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
            },
            "Knight Tord, The Iron Lancer": {
                "Lance Thrust": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Shield Bash": {
                    "dmg": 10,
                    "type": "slash",
                    "stagger": .8,
                },
                "Iron Shield": {
                    "block": 20,
                    "type": "defensive",
                },
                "Iron Wall": {
                    "block": 15,
                    "type": "defensive",
                },
                "Iron Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Iron Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
            },
            "Knight Eduardo, The Iron Knight": {
                "Sword Slash": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Iron Fist": {
                    "dmg": 10,
                    "type": "slash",
                    "stagger": .8,
                },
                "Iron Shield": {
                    "block": 20,
                    "type": "defensive",
                },
                "Iron Wall": {
                    "block": 15,
                    "type": "defensive",
                },
                "Iron Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Iron Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
            },
            "Knight Acrius, The Iron Executor": {
                "Executioner's Blade": {
                    "dmg": 20,
                    "type": "slash",
                },
                "Iron Fist": {
                    "dmg": 10,
                    "type": "slash",
                    "stagger": .8,
                },
                "Iron Shield": {
                    "block": 20,
                    "type": "defensive",
                },
                "Iron Wall": {
                    "block": 15,
                    "type": "defensive",
                },
                "Iron Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Iron Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
            },
            "King Radahn": {
                "Royal Slash": {
                    "dmg": 20,
                    "type": "slash",
                },
                "Upheaval": {
                    "dmg": 15,
                    "type": "blunt",
                    "stagger": .8,
                },
                "Royal Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
                "Royal Decree": {
                    "dmg": 15,
                    "type": "curse",
                },
                "Royal Guard": {
                    "block": 15,
                    "type": "defensive",
                },
                "Royal Will": {
                    "health": 20,
                    "type": "defensive",
                },
            },
            "Mahendra, Corrupted Monk": {
                "Palm Strike": {
                    "dmg": 10,
                    "type": "blunt",
                },
                "Cursed Palm": {
                    "dmg": 15,
                    "type": "curse",
                },
                "Corrupted Aura": {
                    "dmg": 10,
                    "type": "curse",
                },
                "Corrupted Blessing": {
                    "health": 10,
                    "type": "defensive",
                },
                "Corrupted Will": {
                    "health": 15,
                    "type": "defensive",
                },
                "Corrupted Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
            },
            "Akuma, Force of Light": {
                "Light Strike": {
                    "dmg": 10,
                    "type": "blunt",
                },
                "Light Burst": {
                    "dmg": 15,
                    "type": "blunt",
                },
                "Light Shield": {
                    "block": 15,
                    "type": "defensive",
                },
                "Light Wall": {
                    "block": 20,
                    "type": "defensive",
                },
                "Light Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Light Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
            },
            "Phantom of Empress Naurha": {
                "Spectral Slash": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Spectral Slam": {
                    "dmg": 12,
                    "type": "blunt",
                    "stagger": .8,
                },
                "Spectral Wall": {
                    "block": 15,
                    "type": "defensive",
                },
                "Spectral Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Spectral Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
                "Spectral Decree": {
                    "dmg": 15,
                    "type": "curse",
                },
            },
            "Amara, The Outcast": {
                "Shadow Strike": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Shadow Wall": {
                    "block": 15,
                    "type": "defensive",
                },
                "Shadow Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Shadow Rend": {
                    "dmg": 30,
                    "type": "slash",
                },
                "Shadow Decree": {
                    "dmg": 15,
                    "type": "curse",
                },
                "Shadow Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
            },
            "The Shadow Dragon": {
                "Shadow Breath": {
                    "dmg": 20,
                    "type": "blunt",
                },
                "Shadow Claw": {
                    "dmg": 15,
                    "type": "slash",
                },
                "Shadow Wall": {
                    "block": 15,
                    "type": "defensive",
                },
                "Shadow Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Shadow Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
                "Shadow Decree": {
                    "dmg": 15,
                    "type": "curse",
                },
            },
            "The Forger of Myth": {
                "Mythical Strike": {
                    "dmg": 20,
                    "type": "slash",
                },
                "Mythical Wall": {
                    "block": 15,
                    "type": "defensive",
                },
                "Mythical Will": {
                    "health": 10,
                    "type": "defensive",
                },
                "Mythical Curse": {
                    "dmg": 10,
                    "type": "curse",
                },
                "Mythical Decree": {
                    "dmg": 15,
                    "type": "curse",
                },
                "Mythical Rend": {
                    "dmg": 30,
                    "type": "slash",
                },
            },
            "Demon King": {
                "Demon Strike": {
                    "dmg": 25,
                    "type": "slash",
                },
                "Demon Wall": {
                    "block": 20,
                    "type": "defensive",
                },
                "Demon Will": {
                    "health": 15,
                    "type": "defensive",
                },
                "Demon Curse": {
                    "dmg": 35,
                    "type": "curse",
                },
                "Demon Decree": {
                    "dmg": 25,
                    "type": "curse",
                },
                "Demon Rend": {
                    "dmg": 50,
                    "type": "pierce",
                },
            },
        }


class Enemies:
    def __init__(self):
        self.blightwater_pool = ["Thief", "Land Shark", "Witch", "Corrupt Officer", "Pirate Captain"]
        self.castillion_pool = ["Evil Jester", "Legionare", "Castillion Calvary", "Royal Guard", "Giant Bear"]
        self.taj_dunhi_pool = ["Apocalypse Herald", "Poacher",  "King Cobra", "Taj Dunhi Soldier", "Warrior Monk"]
        self.cagayan_pool = ["Tree Spider", "Dragon Hatchling", "Forest Sentinel", "Storm Bringer", "Cloud Spirit"]
        self.move_sets = {
            "Thief": {
                "Shank": {
                    "dmg": 5,
                    "steal": 5,
                    "type": "slash",
                },
                "Distraction": {
                    "dmg": 0,
                    "type": "curse",
                    "steal": 15,
                },
                "Please don't hurt me I won't take you're money I swear": {
                    "block": 10,
                    "type": "defensive",
                },
            },
            "Land Shark": {
                "Bite": {
                    "dmg": 15,
                    "type": "peirce",
                },
                "Tail Slam": {
                    "dmg": 6,
                    "type": "blunt",
                    "stagger": 0.2,
                },
                "Submerge": {
                    "type": "defensive",
                    "juke": 3,
                },
                "Tidal Wave": {
                    "type": "curse",
                    "dmg": 10,
                    "weak": 1
                },
            },
            "Witch": {
                "Poison Mist": {
                    "weak": 1,
                    "poison": 5,
                    "type": "curse",
                },
                "Fire Blast": {
                    "type": "curse",
                    "dmg": 10,
                    "no_heal": 1,
                },
                "Spawn Rat": {
                    "type": "summon",
                },
                "Hex Shield": {
                    "type": "defensive",
                    "block": 15,
                },
            },
            "Corrupt Officer": {
                "Bludgeon": {
                    "dmg": 8,
                    "type": "blunt"
                },
                "Tase": {
                    "type": "curse",
                    "stagger": .5
                },
                "Shield": {
                    "type": "defensive",
                    "dmg_red": .4,
                    "block": 5,
                },
            },
            "Pirate Capitan": {
                "Blunderbuss": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Scimitar Slash": {
                    "type": "slash",
                    "dmg": 8
                },
                "Pommel": {
                    "type": "blunt",
                    "dmg": 8
                },
                "Plank Shield": {
                    "type": "defensive",
                    "block": 12,
                },
            },
            "Evil Jester": {
                "Juggle": {
                    "type": "slash",
                    "dmg": 6,
                },
                "Laughing Gas": {
                    "type": "curse",
                    "dmg": 5,
                    "stagger": .5,
                },
                "Dance of Death": {
                    "type": "slash",
                    "dmg": 10,
                },
                "Jester's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Legionare": {
                "Sword Strike": {
                    "type": "slash",
                    "dmg": 8,
                },
                "Shield Bash": {
                    "type": "blunt",
                    "dmg": 6,
                    "stagger": .5,
                },
                "Spear Thrust": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Legionare's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Castillion Calvary": {
                "Lance Charge": {
                    "type": "peirce",
                    "dmg": 10,
                },
                "Trample": {
                    "type": "blunt",
                    "dmg": 6,
                    "stagger": .5,
                },
                "Sword Slash": {
                    "type": "slash",
                    "dmg": 8,
                },
                "Calvary Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Royal Guard": {
                "Sword Strike": {
                    "type": "slash",
                    "dmg": 8,
                },
                "Shield Bash": {
                    "type": "blunt",
                    "dmg": 6,
                    "stagger": .5,
                },
                "Spear Thrust": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Royal Guard's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Giant Bear": {
                "Claw Swipe": {
                    "type": "slash",
                    "dmg": 10,
                },
                "Bite": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Roar": {
                    "type": "curse",
                    "stagger": 1,
                },
                "Bear Hug": {
                    "type": "blunt",
                    "dmg": 8,
                },
            },
            "Apocalypse Herald": {
                "Fireball": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Ice Shard": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Lightning Bolt": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Apocalypse Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Poacher": {
                "Bow Shot": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Trap": {
                    "type": "curse",
                    "stagger": .5,
                },
                "Knife Throw": {
                    "type": "slash",
                    "dmg": 8,
                },
                "Poacher's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
           "King Cobra": {
                "Bite": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Tail Whip": {
                    "type": "blunt",
                    "dmg": 6,
                    "stagger": .5,
                },
                "Venom Spit": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Cobra's Hood": {
                    "type": "defensive",
                    "block": 10,
                },
           },
            "Taj Dunhi Soilder": {
                "Sword Strike": {
                    "type": "slash",
                    "dmg": 8,
                },
                "Shield Bash": {
                    "type": "blunt",
                    "dmg": 6,
                    "stagger": .5,
                },
                "Spear Thrust": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Taj Dunhi Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Warrior Monk": {
                "Staff Strike": {
                    "type": "blunt",
                    "dmg": 8,
                },
                "Palm Strike": {
                    "type": "blunt",
                    "dmg": 6,
                    "stagger": .5,
                },
                "Kick": {
                    "type": "blunt",
                    "dmg": 8,
                },
                "Monk's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Tree Spider": {
                "Bite": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Web": {
                    "type": "curse",
                    "stagger": .5,
                },
                "Venom Spit": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Spider's Web": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Dragon Hatchling": {
                "Claw Swipe": {
                    "type": "slash",
                    "dmg": 10,
                },
                "Bite": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Fire Breath": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Dragon Scale": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Forest Sentinel": {
                "Root Strike": {
                    "type": "blunt",
                    "dmg": 8,
                },
                "Vine Whip": {
                    "type": "blunt",
                    "dmg": 6,
                    "stagger": .5,
                },
                "Thorn Shot": {
                    "type": "peirce",
                    "dmg": 8,
                },
                "Sentinel's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Storm Bringer": {
                "Lightning Strike": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Wind Slash": {
                    "type": "slash",
                    "dmg": 8,
                },
                "Thunder Clap": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Storm Bringer's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
            "Cloud Spirit": {
                "Gust": {
                    "type": "blunt",
                    "dmg": 8,
                },
                "Rain": {
                    "type": "curse",
                    "stagger": .5,
                },
                "Lightning Strike": {
                    "type": "curse",
                    "dmg": 10,
                },
                "Cloud Spirit's Shield": {
                    "type": "defensive",
                    "block": 10,
                },
            },
        }

