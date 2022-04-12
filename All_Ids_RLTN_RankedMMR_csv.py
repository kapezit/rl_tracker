#Epic added in platforms. CSV should have "epic" in the columns when Epic is the platform.

import csv
import requests
import random
import time
from playwright.sync_api import sync_playwright
import json

#data = open('C:/Users/shero/MMR/all_platforms_ids.csv')
data = open('all_platforms_ids.csv')

ids_data = csv.reader(data)

id_table = list(ids_data)


#PLEASE READ BELOW ------------------------------------------------------

#base_url variable should be changed depending on season ...profile/{}/{}/segments/playlist?season=add-in-here-the-season-number
#add-in-here-the-season-numer = 13,14,15
#Season 1 after Free to Play = season 15
#Season 4 FTP = 18..  Season 5 = 19

#first {} and second {} are platform and id that are automatically grabbed from the csv first and second column.
#Possible error caused by CSV file: program might be trying to get data from blanks spaces in the table.
#Fix CSV error: Make sure to Clean the data from blank cells in the table.


#PLEASE READ ABOVE ------------------------------------------------------

#BASE_URL variable BELOW. Just the last number in the URL to match your desired season. Other changes can break the program.

base_url = 'https://api.tracker.gg/api/v2/rocket-league/standard/profile/{}/{}/segments/playlist?season=19'

#BASE_URL variable ABOVE. Just the last number in the URL to match your desired season. Other changes can break the program.



file_to_output = open('to_save_file_all_mmr.csv','w',newline='')

csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(["Platform","Player ID","Rank","Total Games Played","Playlist Check","Season Check"])


playlist_mode = ""

print(" ")
print("---------------------------------")
print("Rocket League MMR Check Program")
print("---------------------------------")
print(" ")

while playlist_mode not in ["2s","3s"]:
	playlist_mode = input("Are you looking to check MMR for Ranked 2s or 3s? Type 2s or 3s as your answer:")
	print(" ")

print(" ")
print("Scanning MMRs for {}...".format(playlist_mode))



def barfing_url():
    """causes random delay"""
    secs = random.choice(range(4,35))
    time.sleep(secs)


def mmr_program_errors(error_type):
    csv_writer.writerow([line[0],line[1],error_type,"Not found","Not found","Not found"])



def ranked_mmr(platform,account_id,base_url,game_mode):
    """needs import csv and import requests ::: platform such as steam, id, url for json file, game_mode as 3s"""
    
    json_object = "{}"
    

#for i in range for the barfing_url() to run a max of 3 times, this is to call again to the server when there is a 503 error
    for i in range(3):
        try:
            # To get around cloudflare protection, we need to spoof a real browser
            # TODO: maybe need to only launch this once and then just do requests
            with sync_playwright() as p:
                # Webkit is fastest to start and hardest to detect
                browser = p.webkit.launch(headless=True)
                page = browser.new_page()
                page.goto(base_url.format(platform,account_id))
                # Use evaluate instead of `content` not to import bs4 or lxml
                webdata = page.evaluate('document.querySelector("pre").innerText')

            json_object = json.loads(webdata)
            break
        except Exception as e:
            print(e)
            print(webdata)
            print("barfing on " + base_url.format(platform,account_id))

            if webdata == "<Response [503]>":
                
                if i == 2:
                    mmr_program_errors("503 - 3 attempts")
                else:
                    barfing_url()
            
            else:
                mmr_program_errors(webdata)
                break


    playlist_id_number = 0


    if game_mode == "2s":

        playlist_id_number = 11

    elif game_mode == "3s":
        playlist_id_number = 13



    if "errors" not in json_object:
        
        data_list = json_object["data"]
        
        if 'platformInfo' not in data_list:
            playlist_found = False
            
            for items in data_list:
                
                if items['attributes']['playlistId'] == playlist_id_number:
                    playlist_found = True
                    csv_writer.writerow([line[0],line[1], items['stats']['rating']['displayValue'],items['stats']['matchesPlayed']['displayValue'],str(items['metadata']['name']),items['attributes']['season']])

            if playlist_found == False:
                mmr_program_errors("Playlist not found")

        else:
            mmr_program_errors("Wrong json file")

    else:
    	mmr_program_errors("Player ID not found")



for line in id_table[1:]:

	if line[0].lower() == "steam":

		if  line[1].isdigit():
			ranked_mmr("steam",line[1],base_url,playlist_mode)

		else:
			mmr_program_errors("Not Steam")


	elif line[0].lower() == "xbl" or line[0].lower() == "xbox" or line[0].lower() == "xboxlive":

		if line[1].isdigit() == False:
			ranked_mmr("xbl",line[1],base_url,playlist_mode)
			
		else:
			mmr_program_errors("Not XBL")


	elif line[0].lower() == "epic":

		if line[1].isdigit() == False:
			ranked_mmr("epic",line[1],base_url,playlist_mode)
			
		else:
			mmr_program_errors("Not Epic")


	elif line[0].lower() == "psn" or line[0].lower() == "play" or line[0].lower() == "playstation":

		if line[1].isdigit() == False:
			ranked_mmr("psn",line[1],base_url,playlist_mode)

		else:
			mmr_program_errors("Not PSN")

	
	else:
		mmr_program_errors("Platform not recognized")



file_to_output.close()


print("Done. Open file to_save_file_all_mmr.csv.")