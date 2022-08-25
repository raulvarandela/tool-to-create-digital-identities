# author: Raúl Varandela Marra
# date: 25/08/2022
# description: This script is used to execute the tasks of the project

USER = 'raul'

#mastodon
*/15 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon publishText #no tira
*/60 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon publishPhoto #idem
*/30 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon boost # no tira por el propio metodo
30 15 * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon replyComments #no tira
*/60 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon publishComment
*/10 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon like
0 15 * * 1 /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon followUsers
30 20 * * 1 /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon followBack #no funciona en metodo en sí
0 15 1 * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py mastodon createAccount #no tira

#twitter
*/15 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter publishText #no tira
*/60 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter publishPhoto #no tira
*/30 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter boost
30 15 * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter replyComments #no tira
*/60 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter publishComment #no tira
*/10 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter like
0 15 * * 1 /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter followUsers
30 20 * * 1 /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py twitter followBack

#instagram, no tira ni uno
0 */4 * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py instagram publishPhoto
0 */3 * * *  /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py instagram publishStory
30 15 * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py instagram replyComments
*/60 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py instagram publishComment
*/10 * * * * /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py instagram like
0 15 * * 1 /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py instagram followUsers
30 20 * * 1 /usr/bin/python3 /home/$USER/tool-to-create-digital-identities/main.py instagram followBack
