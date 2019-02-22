# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data) 
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
#desired_batsman = 'SC Ganguly'
def get_delivers_faced_first_inning(desired_batsman,data):
    count =0
    first_innings_deliveries =data['innings'][0]['1st innings']['deliveries']
    #print(first_innings_deliveries)
    for delivery_faced in first_innings_deliveries:
        for delivery_number, delivery_info in delivery_faced.items():
            batsman= delivery_info['batsman']
            if batsman == desired_batsman:
               count+=1
    return count

print(get_delivers_faced_first_inning('SC Ganguly',data))


#  Who was man of the match and how many runs did he scored ?
player_of_match =data['info']['player_of_match'][0]
#print(player_of_match)
runs = 0
first_innings_deliveries =data['innings'][0]['1st innings']['deliveries']
for delivery_faced in first_innings_deliveries:
    for delivery_number,delivery_info in delivery_faced.items(): 
        if delivery_info['batsman'] == player_of_match:
                runs = runs + delivery_info['runs']['batsman']
    

print('The man of the match was ',player_of_match)
print('he scored',runs,'runs')
#  Which batsman played in the first inning?
batsman_list = []
first_innings_deliveries =data['innings'][0]['1st innings']['deliveries']
for delivery_faced in first_innings_deliveries:
    for delivery_number,delivery_info in delivery_faced.items():
        batsman_list.append(delivery_info['batsman'])

print(set(batsman_list)) 

# Which batsman had the most no. of sixes in first inning ?
sixes = []
first_innings_deliveries =data['innings'][0]['1st innings']['deliveries']
for delivery_faced in first_innings_deliveries:
    for delivery_number,delivery_info in delivery_faced.items():
        if delivery_info['runs']['batsman']==6:
           sixes.append(delivery_info['batsman'])

from collections import Counter
batsman_sixes = Counter(sixes)
print(batsman_sixes)
max_val =0 
max_val=max(batsman_sixes,key =batsman_sixes.get)
print(max_val)

# Find the names of all players that got bowled out in the second innings.
second_inning_bowled_out = []
second_innings_deliveries =data['innings'][1]['2nd innings']['deliveries']
for delivery_faced in second_innings_deliveries:
    for delivery_number,delivery_info in delivery_faced.items():
        try:
            if delivery_info['wicket']['kind'] == 'bowled':
               second_inning_bowled_out.append(delivery_info['batsman'])
        except:
            pass

print('the players are bowled in second innings are',second_inning_bowled_out)


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_first_innings = [delivery_info 
                        for deliveries in first_innings_deliveries
                        for delivery_number,delivery_info in deliveries.items()
                        if 'extras' in delivery_info]

print(extras_first_innings)


# Code ends here


