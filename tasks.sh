#!/bin/bash

$USER = 'raul'

#mastodon
*/15 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon publishText
*/60 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon publishPhoto
*/30 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon boost
30 15 * * * python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon replyComments
*/60 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon publishComment
*/10 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon like
0 15 * * 1 python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon followUsers
30 20 * * 1 python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon followBack
0 15 1 * * python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon createAccount

#twitter
*/15 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py twitter publishText
*/60 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py twitter publishPhoto
*/30 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py twitter boost
30 15 * * * python3 /home/$USER/tool-to-create-digital-identities/main.py twitter replyComments
*/60 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py twitter publishComment
*/10 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py twitter like
0 15 * * 1 python3 /home/$USER/tool-to-create-digital-identities/main.py twitter followUsers
30 20 * * 1 python3 /home/$USER/tool-to-create-digital-identities/main.py twitter followBack

#instagram
0 */4 * * * python3 /home/$USER/tool-to-create-digital-identities/main.py instagram publishPhoto
0 */3 * * *  python3 /home/$USER/tool-to-create-digital-identities/main.py instagram publishStory
30 15 * * * python3 /home/$USER/tool-to-create-digital-identities/main.py instagram replyComments
*/60 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py instagram publishComment
*/10 * * * * python3 /home/$USER/tool-to-create-digital-identities/main.py instagram like
0 15 * * 1 python3 /home/$USER/tool-to-create-digital-identities/main.py instagram followUsers
30 20 * * 1 python3 /home/$USER/tool-to-create-digital-identities/main.py instagram followBack
