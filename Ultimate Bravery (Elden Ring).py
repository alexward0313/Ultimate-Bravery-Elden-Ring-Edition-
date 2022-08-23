from tkinter import *
import time
import random
from PIL import Image, ImageTk

#Ultimate Bravery (Elden Ring) is where a user can press random and the program will give the user a completely random build to use in Elden Ring

weapons = ["Broadsword", "Cane Sword", "Carian Knight's Sword", "Coded Sword", "Crystal Sword", "Grafted Blade Greatsword", "Starscourge Greatsword", 
"Bloodhound’s Fang", "Blasphemous Blade", "Treespear", "Rivers of Blood", "Margott’s Cursed Sword", "Moonveil", "Dark Moon Greatsword", "Sword Of Night And Flame", 
"Carian Regal Scepter", "Lusat's Glintstone Staff", "Meteorite Staff", "The Prince Of Death’s Staff", "Godslayer’s Seal", "Dragon Communion Seal", "Erdtree Seal", 
"Bastard's Stars", "Axe Of Godfrey", "Serpent-Hunter", "Torch", "Torchpole", "Forked Hatchet", "Briar Greatshield", "Rickety Shield", "none"]

helmets = ["Vagabond Knight Helm", "Knight Helm", "Godrick Knight Helm", "Carian Knight Helm", "Cleanrot Helm", "Prisoner Iron Mask", "Pumpkin Helm", "White Mask", "Radahn’s Redmane Helm", 
"Veteran’s Helm", "Black Wolf Mask", "Radiant Gold Mask", "Silver Tear Mask", "Pumpkin Helmet", "Octopus Head", "Scarab Hats", "Mushroom Head", "Envoy Crown", "Queen's Crescent Crown", 
"Godskin Apostle Hood", "Jar", "Albinauric Mask", "Twinsage Glintstone Crown", "Azur's Glintstone Crown", "Mushroom Crown", "Lusat's Glintstone Crown", "none"]

armorsets = ["Twinned Armor Set", "Carian Knight Set", "Cleanrot Set", "Bull-Goat Set", "Lionel's Set", "Banished Knight Set", "Malenia's Set", "Black Knife Set", "War Surgeon Set", 
"Spellblade Set", "Queen Of The Full Moon Set", "Haligtree Knight Set", "Land Of Reeds Set", "Mushroom Set", "Drake Knight Set", "none"]

talismans = ["Great-Jar's Arsenal", "Marika's Soreseal", "Flock's Canvas Talisman", "Godfrey Icon", "Roar Medallion", "Bull-Goat's", "Green Turtle", "Graven-Mass", "Cerulean Amber", 
"Radagon Icon", "Magic Scorpion", "Crimson Amber", "Radagon's Scarseal", "Erdtree's Favor", "Radagon's Soreseal", "Rotten Winged Sword Insignia", "Shard of Alexander", 
"Godskin Swaddling Cloth", "Lord of Blood’s Exultation", "Daedicar’s Woe", "Longtail Cat Talisman", "Ancestral Spirit’s Horn", "Shabriri’s Woe", "Companion Jar", "Assassin’s Cerulean Dagger", "none"]

spells = ["Glintstone Pebble", "Magic Glintblade", "Carian Slicer", "Rock Sling", "Comet Azur", "Rennala's Full Moon", "Ranni's Dark Moon", "Carian Greatsword", "Glintstone Icecrag", 
"Eternal Darkness", "Carian Retaliation", "Great Ocular Bubble", "Meteorite", "Gravity Well", "Founding Rain of Stars", "Ancient Death of Rancor", "Starlight", "Shatter Earth", 
"Magma Shot", "Magic Downpour", "Gavel of Haima", "Briars of Punishment", "Lightning Spear", "Golden Vow", "Erdtree Heal", "Bloodflame Blade", "Rotten Breath", "Giantsflame Take Thee", 
"Frenzied Burst", "The Flame of Frenzy", "Scouring Black Flame", "Smarag's Glintstone Breath", "Flame Grant Me Strength", "Flame of the Fell God", "Protection of the Erdtree", "Poison Mist", 
"Bloodflame Talons", "Heal", "Swarm of Flies", "Lansseax's Glaive", "Urgent Heal", "Wrath of Gold", "Death Lightning", "Immutable Shield", "Pest Threads", "Reject", "none"]

ashes = ["Bloodhound's Step", "Seppuku", "Flame of Redmanes", "Lion's Claw", "Hoarfrost Stomp", "Bloody Slash", "Spinning Strikes", "Storm Blade", "Mighty Shot", "Sacred Blade", "Carian Greatsword", 
"Hoarah Loux's Earthshaker", "The Glintblade Phalanx", "Thunderbolt", "Gravitas", "Carian Grandeur"]

spirits = ["Lone Wolf Ashes", "Radahn Soldiers", "Bloodhound Knight Floh", "Banished Knight Oleg", "Nightmaiden and Swordstress Puppets", "Latenna the Albinauric", "Lhutel the Headless", 
"Dung Eater Puppet", "Black Knife Tiche", "Mimic Tear"]

def ultimate_bravery():
    wr1 = random.choice(weapons)
    wr2 = random.choice(weapons)
    wr3 = random.choice(weapons)
    weapon1.config(text = wr1)
    weapon2.config(text = wr2)
    weapon3.config(text = wr3)

    asr = random.choice(armorsets)
    armorset.config(text = asr)

    talr1 = random.choice(talismans)
    talr2 = random.choice(talismans)
    talr3 = random.choice(talismans)
    talr4 = random.choice(talismans)
    talisman1.config(text = talr1)
    talisman2.config(text = talr2)
    talisman3.config(text = talr3)
    talisman4.config(text = talr4)

    splr1 = random.choice(spells)
    splr2 = random.choice(spells)
    spell1.config(text = splr1)
    spell2.config(text = splr2)

    ashr = random.choice(ashes)
    ash.config(text = ashr)

    sprr = random.choice(spirits)
    spirit.config(text = sprr)

    helr = random.choice(helmets)
    helmet.config(text = helr)





screen = Tk()
title = screen.title("Ultimate Bravery (Elden Ring)")
canvas = Canvas(screen, width = 700, height = 950)
canvas.pack()


weapon1 = Label(screen, text = "Weapon 1", font = ("Ariel", 25))
canvas.create_window(350, 50, window = weapon1)

weapon2 = Label(screen, text = "Weapon 2", font = ("Ariel", 25))
canvas.create_window(350, 100, window = weapon2)

weapon3 = Label(screen, text = "Weapon 3", font = ("Ariel", 25))
canvas.create_window(350, 150, window = weapon3)

helmet = Label(screen, text = "Helmet", font = ("Ariel", 25))
canvas.create_window(350, 200, window = helmet)

armorset = Label(screen, text = "Armor Set", font = ("Ariel", 25))
canvas.create_window(350, 250, window = armorset)

talisman1 = Label(screen, text = "Talisman 1", font = ("Ariel", 25))
canvas.create_window(350, 300, window = talisman1)

talisman2 = Label(screen, text = "Talisman 2", font = ("Ariel", 25))
canvas.create_window(350, 350, window = talisman2)

talisman3 = Label(screen, text = "Talisman 3", font = ("Ariel", 25))
canvas.create_window(350, 400, window = talisman3)

talisman4 = Label(screen, text = "Talisman 4", font = ("Ariel", 25))
canvas.create_window(350, 450, window = talisman4)

spell1 = Label(screen, text = "Spell 1", font = ("Ariel", 25))
canvas.create_window(350, 500, window = spell1)

spell2 = Label(screen, text = "Spell 2", font = ("Ariel", 25))
canvas.create_window(350, 550, window = spell2)

ash = Label(screen, text = "Ashes of War", font = ("Ariel", 25))
canvas.create_window(350, 600, window = ash)

spirit = Label(screen, text = "Spirit Ashes", font = ("Ariel", 25))
canvas.create_window(350, 650, window = spirit)

go = Button(screen, text = "Ultimate Bravery", width = 25, height = 2, font = ("Times New Roman", 25), command = ultimate_bravery)
canvas.create_window(350, 800, window = go)


screen.mainloop()
