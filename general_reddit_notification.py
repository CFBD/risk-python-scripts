import pandas as pd
import praw

reddit = praw.Reddit(client_id='CLIENT_ID',
                    client_secret='CLIENT_SECRET',
                    user_agent='User-Agent: web:APP_NAME:vAPP_VERSION (by /u/USERNAME)',
                    username='USERNAME',
                    password='PASSWORD')

# requires a populated CSV file with a 'player' column
df = pd.read_csv('./players.csv')
players = list(df['player'])

successfully_messaged = [] #initializes empty list for users successfully messaged
failed_to_message = [] #empty list for users not messaged


for player in players:
    try:
        reddit.redditor(player).message('Join TEAM Risk today!', '''
Greeetings {0}!

&nbsp;

PLACE_MESSAGE_HERE

&nbsp;

You will receive no further messages from us. Hope you join us!

TEAM Risk Leadership
        '''.format(player))
        print(player + ' messaged successfully!')
        successfully_messaged = successfully_messaged + [player]
    except:
        print("Error in messaging user " + player)
        failed_to_message = failed_to_message + [player]

# output successes and failures to separate text files
with open('successes.txt', 'w') as f:
    for item in successfully_messaged:
        f.write("%s\n" % item)

with open('failures.txt', 'w') as f:
    for item in failed_to_message:
        f.write("%s\n" % item)