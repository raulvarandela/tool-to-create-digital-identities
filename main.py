# Author: Raul Varandela
# Date: 22/07/22
# Description: Main file for the project.

import twitter 
import mastodon_app 
import instagram
import sys

def main(argv):

    if len(argv) < 3:
        print(" You need to pass the name of the social network as an argument and the name of the fuction to execute. \n\n Possible social networks are: \n \t - twitter \n \t - mastodon \n \t - instagram \n\n Possible functions are: \n \t - publishText (only mastodon and twitter) \n \t - publishPhoto \n \t - publishStory (instagram only) \n \t - boost (only mastodon and twitter) \n \t - replyComments \n \t - publishComment \n \t - like \n \t - followUsers \n \t - followBack \n \n Example: python3 main.py twitter publishText\n")
        return

    if argv[1] != "twitter" and argv[1] != "instagram" and argv[1] != "mastodon":
        print("The social network you passed is not valid.")
        return

    if argv[1] == "twitter" :
        twitter.main(argv[2])
    elif argv[1] == "instagram":
        instagram.main(argv[2])
    elif argv[1] == "mastodon" :
        mastodon_app.main(argv[2])

    print ('Done!')
    



if __name__ == "__main__":
    main(sys.argv)