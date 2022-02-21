# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#versie 2 nav waardevolle feedback Niels

# Wie scoren er in deze wedstrijd?
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

# In welke minuuut wordt er gescoord?
goal_0 = 32
goal_1 = 54

#scorers = (player1  +  goal0), (player2  +  goal1)
scorers = player_1 + ' ' + str(goal_0) + ', ' + player_2 +  ' ' + str(goal_1)

report = f'{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute'
print(report)

player = 'Ronald Koeman'

first_name = player[:player.find(" ")]         # generiek, willekeurige first_name werkt
print(first_name)

#last_name
last_name = player [player.find(" ")+1:]       # generiek, willekeurige last_name werkt
print(last_name)
last_name_len = len(last_name)
print(last_name_len)

#name_short = player[0] + ". " + last_name     # eenvoudige versie
name_short = f'{first_name [:1]}. {last_name}' # met f-strings - variabelen
print(name_short)

chant = (first_name + "! ") * (len(first_name) - 1) + (first_name + "!")
#chant = (first_name + "! ") * len(first_name)
#chant = chant.rstrip()
print(chant)
print(len(chant))
good_chant = (chant[-1] != " ") # uitkomst = True

