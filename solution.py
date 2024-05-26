# Dream Premier League (DPL)
# A match of DPL is going on. Team Aravali has a made score of 195 for 7 in 20 overs and the opponent 
# Team Shivalik is doing some analytics to find out what they need to do to win. You are the Data 
# Scientist of the Team Shivalik and you have been asked to help them.

# Problem 1
# Team Shivalik has stored the runs made by Team Aravali players in the following dictionary.
aravali ={"Dhoni":25, "Virat":31, "Pollard":11, "Rohit": 0, "Maxwell":12, "Sachin":59, "Sehwag":12}
list_of_players=[player for player in aravali.keys()]
# print(list_of_players)

# Problem 2
# By mistake, the runs made by Rohit was recorded as 0. 
# Your next task is to figure out how many runs were made by Rohit and update the dictionary
total_runs=195
sum_runs=[run for player,run in aravali.items()]
rohit_run=total_runs-sum(sum_runs)
aravali["Rohit"]=rohit_run
# print(aravali)

# Problem 3
# Your next task is to find out who scored the second highest runs in Team Aravali

maximum_runs=[(player,run) for player,run in aravali.items() if run == max([run for run in aravali.values()])]

# print(f"""Player who scored maximum run is {maximum_runs[0][0]} and 
# runs scored by him is {maximum_runs[0][1]}""")

# Problem 4
# Just out of curiosity, you want to find out the unique runs made by Team Aravali players.
unique_runs=set([runs for runs in aravali.values()])
# print(unique_runs)

# Problem 7
# Find out the runrate required for Team Shivalik to win (for 20 overs)
# Hint: Runrate is runs required per over to win the match

runs_to_win=196
overs=20
run_rate_required=runs_to_win/overs
# print (run_rate_required)

# Problem 8
# You have just received a secret message form your informant stating that some players of the 
# other team are into match fixing. You have to decode a message and inform authorities about it.
# You received a string "skdlfjnvuerhw qefnnaosfu qrhviudhfv wuirhv adknlkxjcier vafuvhkajn iuvhsf 
# vasuif KJSHFKJ aeuihvasf akjfhiufe" and index of "i" are going to be "no balls".

message = "skdlfjnvuerhw qefnnaosfu qrhviudhfv wuirhv adknlkxjcier vafuvhkajn iuvhsf vasuif KJSHFKJ aeuihvasf akjfhiufe"

# first_no_ball=message.index('i')

# print(first_no_ball)
c=0
for index in range(len(message)):
    if message[index]=='i':
        if c==0:
            print(f"first no ball is {index}")
            c+=1
        last_no_ball=index
print(f"last no ball is {last_no_ball}")

# for no_ball in message:
#     if no_ball=='i':
#         first_no_ball=message.index(no_ball)
#         print("first no ball is {first_no_ball}")
#         last_no_ball=message.index(no_ball)
# print("last no ball is {last_no_ball}")

# Problem 9
# You have given the information about fixing to the authorities and they are going to verify it during the match. But still you have to work on your strategy.
# It is in your hands to automate the decision on who goes on 4th position for batting depending on following criteria:
# if runs made by Team Shivalik is less than 50, Smith will play
# if runs are between 51 to 100 then Sir Jadeja will go
# if runs are above 100 then Hardik will play

target=int(input("Enter runs scored by Team Shivalik 78"))

if target<=50:
    print("Smith will play at number 4")
elif target>50 and target<=100:
    print("Sir Jadeja will play at number 4")
else:
    print("Hardik will play at number 4")