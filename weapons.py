
class Weapons:
    def __init__(self):
        self.weapons_list = ["Twin Forged Katanas", "Great Sword of the Square Table", "Gayuma Infused Dagger",
                             "Mythril Staff", "Great Axe of the Square Table", "Great Spear of the Square Table",
                             "Torment's Whip", "Serpent's Sickle", "Peregrine's Claws", "Shadow Dragon's Halberd",
                             "Chains of the Damned", "Dragon's Scale"]
        self.weapons_lore = {
            "Twin Forged Katanas": "These twin blades were made by an old blacksmith that took pity on Amara,"
                                   "They are perfectly symmetrical, in shape and weight, allowing for perfect balance.",
            "Great Sword of the Square Table": "Wielded by Knight Eduardo of the Square Table, as heavy as it is sharp"
                                               "this sword can split armored foes in two with a single swing.",
            "Gayuma Infused Dagger": "Alphis stole this prototype dagger from a renown scientist. It's crafted from "
                                     "steel and Gayuma fibers, and shines with a faint green glow.",
            "Mythril Staff": "A heavy staff with a round blunt tip at the top, designs like this"
                             " are common among the Samar Monks, but one cast in mythril is very rare. A relic of the "
                             "mosque Akuma worshipped in, it was given to him after he pledged to defend his people.",
            "Great Axe of the Square Table": "Wielded by Knight Acrius of the Square Table, a brutal weapon, the blunt"
                                             "force alone is enough to dent nearly all metal, and it come with a razor"
                                             "sharp edge.",
            "Great Spear of the Square Table": "A huge iron lance wielded by Knight Tord of the Square Table, the blade"
                                               "is over a meter long, with the lance standing at a staggering 3 meters,"
                                               "few things could withstand a charge from this great spear.",
            "Torment's Whip": "A black leather whip with a metal flail on the tip, victims of this whip are left with"
                              "excruciating pain, severe bleeding, and permanent scars, if they live...",
            "Serpent's Sickle": "A ritual weapon used by the Serpent's Servants, the curved point of this scythe is"
                                "resembled after the Ancient Basilisk, to whom which it's followers worship",
            "Peregrine Claws": "Short, fast, and extremely sharp, these twin swords are attached at the wrist, and act"
                               "as an extension of the wearers arms. Fast and deadly is the preferred style of these"
                               "weapons.",
            "Shadow Dragon's Halberd": "A golden halberd gifted by the shadow dragon to those he deems worthy, an "
                                       "ancient legend says when wielders of this halberd die, their souls arise from "
                                       "the earth with glorious light, and form a new star in the heavens",
            "Chains of the Damned": "Burning chains, cursed with the infernal flame of the Demon King, blows from"
                                    "these chains instantly corrode skin and flesh, and "
                                    "prevent the area from ever healing.",
            "Dragon's Scale": "A scale from one of the great dragons, retrofitted into a shield. No earthly metals can"
                              "peirce the scale and its light weight allows it be used as a powerful blunt weapon."

        }

        self.move_sets = {
            "Twin Forged Katanas": {
                "Expert Slash": {
                    "info": "Slice both katanas down in front of you at the target. High crit chance.",
                    "dmg": 10,
                    "type": "slash",
                    "crit": .20,
                },
                "Handle Bash": {
                    "info": "Slam the handle of one of the katanas into the target. High crit chance.",
                    "dmg": 8,
                    "type": "blunt",
                    "crit": .20,
                },
                "Piercing Stab": {
                    "info": "Lunge one of the katanas forward into the target. High crit chance.",
                    "dmg": 8,
                    "type": "pierce",
                    "crit": .20,
                },
                "Defensive Stance": {
                    "info": "Hold the katanas in front of you, guarding yourself",
                    "block": 20,
                    "dmg_red": .00,
                    "type": "defensive",
                },
            },
            "Great Sword of the Square Table": {
                "Overhead Slam": {
                    "info": "Bring the sword over and slice down the target with a heavy force. Small stagger chance.",
                    "dmg": 15,
                    "type": "slash",
                    "crit": .05,
                    "stagger": .10,
                },
                "Sprinting Bash": {
                    "info": "Rush the target and bash them with the pommel of the sword. High stagger chance",
                    "dmg": 10,
                    "type": "blunt",
                    "crit": .05,
                    "stagger": .20,
                },
                "Practiced Combo": {
                    "info": "Slash the target with a series of blows. Strong damage, no crit or stagger chance.",
                    "dmg": 20,
                    "type": "slash",
                    "crit": 0,
                    "stagger": 0,
                },
                "Guard Counter": {
                    "info": "Parry the targets attack, and strike them back with a quick slash",
                    "dmg": 8,
                    "type": "defensive",
                    "dmg_red": .45,
                    "block": 0,
                },

            },
            "Gayuma Infused Dagger": {
                "Sneaky Stab": {
                    "info": "Aim a quick stab at the targets neck. Builds up bleed",
                    "dmg": 5,
                    "type": "peirce",
                    "crit": .10,
                    "bleed": 5,
                },
                "Flurry": {
                    "info": "Overwhelm your foe with multiple slashes. Low damage, strong bleed",
                    "dmg": 3,
                    "type": "slash",
                    "crit": .10,
                    "bleed": 10,
                },
                "Dagger Throw": {
                    "info": "Hurl your dagger at the target and pull it back out. Builds up bleed",
                    "dmg": 10,
                    "type": "peirce",
                    "crit": .15,
                    "bleed": 2,
                },
                "Juke": {
                    "info": "Dodge a targets attack, higher damage attack more likely to dodge.",
                    "type": "defensive",
                    "dodge": 1.8,
                    "dmg_red": 0,
                    "block": 0,
                },
            },
            "Mythril Staff": {
                "Barrage": {
                    "info": "Pummel your target with a series of blows, high damage with a small stagger chance",
                    "dmg": 16,
                    "type": "blunt",
                    "stagger": .15,
                },
                "Trip": {
                    "info": "Swing at the targets legs, low damage with a high stagger chance",
                    "dmg": 6,
                    "type": "blunt",
                    "stagger": .50,
                },
                "Precision": {
                    "info": "Strike your target with a brutal smash, decent damage and decent crit chance",
                    "dmg": 12,
                    "type": "blunt",
                    "crit": .15,
                },
                "Parry": {
                    "info": "Parry your opponents attack, chance to block all damage and small chance to stagger",
                    "dmg_red": .45,
                    "stagger": .05,
                    "type": "defensive",
                },
            },
            "Great Axe of the Square Table": {
                "Chop": {
                    "info": "Swing your greataxe in a wide sweeping move at the target.",
                    "dmg": 10,
                    "type": "slash",
                    "bleed": 2,
                },
                "Flat Bash": {
                    "info": "Bash the target with the flat side of the axe",
                    "dmg": 12,
                    "type": "blunt",
                    "stagger": .15,
                },
                "Terminate": {
                    "info": "Attempt to execute your target, instantly killing them.",
                    "dmg": "either 0 or 100% of enemy health, chance increases as enemy health gets lower",
                    "type": "execute",
                },
                "Hold": {
                    "info": "Shield yourself with the greataxe, and block the targets attack.",
                    "block": 20,
                    "type": "defensive"
                },
            },
            "Great Spear of the Square Table": {
                "Spear Rush": {
                    "info": "Rush your target at high speed and skewer them, good damage and small stagger chance.",
                    "dmg": 15,
                    "type": "pierce",
                    "stagger": .10,
                },
                "Cleave": {
                    "info": "Slice your spear widely in front of you all the target.",
                    "dmg": 10,
                    "type": "slash",
                },
                "Pole Drive": {
                    "info": "Ram the spear up to the sky at your target, good damage adn high stagger chance.",
                    "dmg": 10,
                    "type": "pierce",
                    "stagger": 20,
                },
                "Reversal": {
                    "info": "use your enemies momentum against them, blocks damage and has chance to stagger",
                    "type": "defensive",
                    "dmg_red": .30,
                    "stagger": .10,
                },
            },
            "Torment's Whip": {
                "Infect": {
                    "info": "Whip your target brutally, causing intense bleed and infection",
                    "dmg": 2,
                    "type": "slash",
                    "bleed": 8,
                    "infect": 1,
                },
                "Onslaught": {
                    "info": "Wildly strike your target multiple times. Can crit and builds up bleed.",
                    "dmg": 8,
                    "crit": .40,
                    "bleed": 2,
                    "type": "slash",
                },
                "Trip": {
                    "info": "Whip at the target's legs, low damage, causes bleed, and a chance to stagger",
                    "dmg": 3,
                    "bleed": 3,
                    "stagger": .20,
                    "type": "slash",
                },
                "Disarm": {
                    "info": "Attempt to disarm your target by yoinking their weapon with your whip.",
                    "type": "defensive",
                    "disarm": .33,
                },
            },
            "Serpent's Sickle": {
                "Wound": {
                    "info": "Hook into your target with the barbed edge of the sickle and rip it out.",
                    "dmg": 10,
                    "bleed": 2,
                    "weak": 1,
                    "type": "pierce",
                },
                "Scar": {
                    "info": "Slash your target, leaving thin and deep scars",
                    "type": "slash",
                    "dmg": 8,
                    "bleed": 2,
                },
                "Ritual": {
                    "info": "Summon the power of the serpent to bite your opponent, crippling them and causing bleed",
                    "dmg": 0,
                    "type": "curse",
                    "weak": 2,
                    "bleed": 5,
                },
                "Defend": {
                    "info": "Block the target's attack, reducing the damage taken",
                    "type": "defensive",
                    "dmg_red": .33,
                },
            },
            "Peregrine Claws": {
                "Claw": {
                    "info": "Rapidly strike your opponent twice.",
                    "dmg": 6,
                    "crit": .20,
                    "attacks": 2,
                    "type": "slash",
                },
                "6 Edged Stab": {
                    "info": "Peirce your target with the claws. Small execute chance.",
                    "dmg": 6,
                    "execute": .05,
                    "type": "Peirce",
                },
                "Rampage": {
                    "info": "Assault your target with a flurry of attacks. Attacks 5 times, low damage, high crit.",
                    "dmg": 3,
                    "attacks": 5,
                    "type": "slash",
                    "crit": .33,
                },
                "Finesse": {
                    "info": "Juke your target, blocking some damage taken and reducing damage.",
                    "type": "defensive",
                    "block": 5,
                    "dmg_red": .40,
                },
            },
            "Shadow Dragon's Halberd": {
                "Cripple": {
                    "info": "Stab your target with the end of the halberd, strong damage and builds bleed",
                    "dmg": 15,
                    "type": "pierce",
                    "bleed": 4,
                },
                "Cut Down": {
                    "info": "Heave the halberd across the target. strong damage and bleed, chance to stagger",
                    "dmg": 12,
                    "bleed": 5,
                    "stagger": .15,
                    "type": "slash",
                },
                "Rend": {
                    "info": "Call upon the might of the shadow dragon to rend your opponents, increasing bleed by 50%. "
                            "if a targets bleed build up is greater than 40% of their health, they are executed.",
                    "dmg": 0,
                    "bleed_mod": .5,
                    "type": "spell",
                },
                "Become Ethereal": {
                    "info": "Use the power of the shadow dragon to become invincible for two turns, "
                            "but unable to deal damage",
                    "type": "defensive",
                    "immune": 2,
                },
            },
            "Chains of the Damned": {
                "Flail": {
                    "info": "Whip your target with the chains, weakens and prevents healing",
                    "dmg": 8,
                    "type": "slash",
                    "weak": 1,
                    "no_heal": 1,
                },
                "Serrate": {
                    "info": "drag the serrated edges of the chains across the target, weakens and causes extreme bleed.",
                    "dmg": 0,
                    "bleed": 13,
                    "type": "slash",
                    "weak": 1,
                },
                "Erupt": {
                    "info": "Slam the chains on the ground in front of the target, causing a volcanic rupture that "
                            "burns the target.",
                    "dmg": 12,
                    "no_heal": 1,
                    "type": "spell",
                },
                "Disarm": {
                    "info": "Attempt to disarm your target by yoinking their weapon with the chains.",
                    "type": "defensive",
                    "disarm": .33,
                },

            },
            "Dragon's Scale": {
                "Shield Bash": {
                    "info": "Crush the target with a forceful push of the shield, decent damage and stagger chance.",
                    "dmg": 10,
                    "stagger": .33,
                    "type": "blunt"
                },
                "Denting Blows": {
                    "info": "Pummel the target with a series of bashes.",
                    "dmg": 3,
                    "attacks": 3,
                    "stagger": .20,
                    "type": "blunt",
                },
                "Guillotine": {
                    "info": "Attempt to execute the target, chance is higher if target is staggered.",
                    "dmg": 1,
                    "type": "peirce",
                    "execute": .05,
                    "stagger_modifier": .50,
                },
                "Protect": {
                    "info": "Raise the shield in front of you, blocking the targets attack.",
                    "type": "defensive",
                    "block": 45
                }

            }
        }


