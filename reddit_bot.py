#A reddit bot that automatically responds after recognizing the triggered phase in a subreddit

# import the modules
import praw
import random
import time

# creating an authorized reddit instance
reddit = praw.Reddit(
    client_id="//your client Id",
    client_secret="//your client secret id,
    user_agent="<console:MB:1.0>",
    username="//reddit_username",
    password="//Password")

# the subreddit where the bot is to be live on
subreddit=reddit.subreddit("//put the name of subreddit where you want your bot live on")

#Random replies you want your bot to reply
#Non_fiction_books = ["Read Shoe-dog by Phil knight" ,
 #                   "Read We Should All Be Feminists by Chimamanda Ngozi Adichie",
  #                  "Read Why I am an atheist is an incredibly thought provoking book by - Bhagat Singh", 
   #                "Read Ikigai",
    #                "Read Rich Dad Poor Dad by Robert T. Kiyosaki",
     #               "Read The 5 AM Club by Robin Sharma" ] 

for submission in subreddit.hot(limit=300): #limit is the number of posts you want ur bot to react on
    #print('********************')
    #print(submission.title)
    
    # check every comment in the subreddit
    for comment in submission.comments:
        if hasattr(comment,"body"):
            if " //phrase to trigger the bot " in comment.body: # phrase to trigger the bot
                print('-------------------------')
                print(comment.body)
                random_index=random.randint(0, len(Non_fiction_books)-1)
                comment.reply(Non_fiction_books[random_index])
                time.sleep(600)#time between two bot replies in seconds