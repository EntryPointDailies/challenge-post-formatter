mission = input("Mission: ")
tactic = input("Tactic: ")
mod1 = input("Modifier 1: ")
mod2 = input("Modifier 2: ")
mod3 = input("Modifier 3: ")
print(mission," (",tactic,")","\n• ",mod1,"\n• ",mod2,"\n• ",mod3,sep="")

weight1 = ("Misplaced Gear","No Aegis Armor","Boarded Up","Fog","No Suppressors","No Safecracking")
weight2 = ("Weapon Scanners","No Scrambler","Bloodless","Unskilled","Small Arms Only","Criminal Arsenal","No Hybrid Classes","Cascade Arsenal","Flashbang Frenzy","Reinforced Doors","Heavy Bags","Armera Arsenal","No Equipment Bags","Reinforced Locks","Glass Cannon","Mandatory Headshots","No Interrogation","Extra Cameras","No Heavy Armor")
weight3 = ("Unintimidating","Weaker Medkits","Hidden UI","Faster Detection","Reinforced Cameras","Aegis Academy","Flashbang Revenge","One Shot","Hidden Detection Bars","No Lockpicks","Inexperienced","Fifteen Minutes","Less Health")
weight4 = ("No Explosives","Takedown Limit","Shield Swarm","Explosive Flashbangs","No Knockouts","No Moving Bodies","No Disguise","Explosive Revenge")


total_weight = 0

for cmod in [mod1,mod2,mod3]:
    if cmod in weight1:
        total_weight = total_weight + 1
    elif cmod in weight2:
        total_weight = total_weight + 2
    elif cmod in weight3:
        total_weight = total_weight + 3
    elif cmod in weight4:
        total_weight = total_weight + 4
    else:
        print("challenge doesn't exist?")
        total_weight = 99

if total_weight < 5.5:
    print("Green")
elif total_weight < 7.5:
    print("Blue")
elif total_weight < 9.5:
    print("Purple")
elif total_weight < 12.5:
    print("Red")
else:
    print("Invalid weight?")