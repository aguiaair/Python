import urllib.request
import os
import zipfile
import time
print('''
    _______           _        _ _        __        __                ______    _                     _           __  __ _      
   / /_   _|         | |      | | |       \ \      / _|              |  ____|  | |                   | |         |  \/  ( )     
  | |  | |  _ __  ___| |_ __ _| | | ___ _ _| |    | |_ ___  _ __     | |__   __| |_   _  __ _ _ __ __| | ___     | \  / |/ ___  
 / /   | | | '_ \/ __| __/ _` | | |/ _ \ '__\ \   |  _/ _ \| '__|    |  __| / _` | | | |/ _` | '__/ _` |/ _ \    | |\/| | / __| 
 \ \  _| |_| | | \__ \ || (_| | | |  __/ |  / /   | || (_) | |       | |___| (_| | |_| | (_| | | | (_| | (_) |   | |  | | \__ \ 
  | ||_____|_| |_|___/\__\__,_|_|_|\___|_| | |    |_| \___/|_|       |______\__,_|\__,_|\__,_|_|  \__,_|\___/    |_|  |_| |___/ 
  _\_\___   ____                          /_/                                                                                   
 /_ |/ _ \ / __ \                                                                                                               
  | | | | | |  | |                                                                                                              
  | | | | | |  | |                                                                                                              
  | | |_| | |__| |                                                                                                              
  |_|\___/ \____/ _                                      _           _                                                          
 |  __ \     | | | |                                    (_)         | |                                                         
 | |__) |   _| |_| |__   ___  _ __       _ __  _ __ ___  _  ___  ___| |_ ___                                                    
 |  ___/ | | | __| '_ \ / _ \| '_ \     | '_ \| '__/ _ \| |/ _ \/ __| __/ __|                                                   
 | |   | |_| | |_| | | | (_) | | | |    | |_) | | | (_) | |  __/ (__| |_\__ \                                                   
 |_|    \__, |\__|_| |_|\___/|_| |_|    | .__/|_|  \___/| |\___|\___|\__|___/                                                   
         __/ |                          | |            _/ |                                                                     
        |___/                           |_|           |__/                                                                      


''')
print('Please Read: Hello, Welcome to the setup wizazrd for my python projects, this is an installer which fetches the latest version of my projects. Once you have run this once you wont need to do it again, inside the Year 10.py you can find update options!')
input('Press enter to continue...')
print('Grabbing link...')
url = 'http://fase2.tk/kingscollege/term_1/data.zip' 
filename = 'data.zip'  
print('Downloading...')
urllib.request.urlretrieve(url, filename)
print('Done!')
print('Preparing to unzip...')
zip_ref = zipfile.ZipFile('data.zip', 'r')
print('Unzipping...')
zip_ref.extractall()
zip_ref.close()
print('Done!')
print('Running setup in 2s...')
time.sleep(2)
deir=os.getcwd()
setup='python "' + deir +'/setup.py" install'
os.system(setup)
print('Setup complete!')
input()