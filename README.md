# rl_tracker v.3.0

Understanding All_Ids_RLTN_RankedMMR_csv.py (RLTN MMR Scanning Program)

-----------------------------------
1.0 STEP ONE - SETUP
-----------------------------------

Script uses a file named [ all_platforms_ids.csv ] to get the platforms and Ids of players.

  *This csv contains two columns, column A for platform and B for id

  *Fill this file with that data and save it in the same location as the script

  *Always replace the data in here to check for new batches



1.1 csv issues, fixes and prevention
------------------------------------

1)The program is opening a CSV file [ all_platforms_ids.csv ] with column A as the platform and columns B as the ID. Column one(plaform) reads the following codes: steam, xbl, xbox, xboxlive, psn, play, playstation, epic. Other codes dont work.

2)Sometimes this file can trigger an error if it thinks there's data in blank spaces.
CSV Error: Phantom data happens when a new set is copy/pasted into a column (columns) and the new set is smaller than the previous one.

FIX: Make sure you select all blank rows and delete the data even when nothing appears in those rows.

3)Make sure that all data in this csv is formatted as text and not numbers. Steam ids (numbers) can become truncated. Usually this truncation does not cause any errors but it is better to prevent any possible issues.


-----------------------------------
2.0 STEP TWO - Python Script Check
-----------------------------------

  *Open with Sublime or a Python Editor

  *base_url is the URL that is being used to get the rank.

  *That URLs last word is the number for the season. At the moment it is 16 for Season 2 Free to play. 

[CHANGES TO BASE_URL IS ONLY EDIT ALLOWED WITHOUT POSSIBLE CORRUPTION]



-----------------------------------
3.0 STEP THREE - Run the script
-----------------------------------

1) Run All_Ids_RLTN_RankedMMR_csv.py on the command line (or PowerShell)

2) The program also asks for the rank mode. The only rank modes available are 2s (Doubles Ranked) and 3s (Standard Ranked).



-----------------------------------
3.0 STEP THREE - "Scanning MMRs for 3s..."
-----------------------------------

  *If you can read a message that says "Scanning MMRs for ...", then its working.

  *Keep in mind that scanning for 450 entries will take around 12-15 min.

  *When done, the program will show a message saying '"Done.. open to_save_file_all_mmr.csv".



-----------------------------------
4.0 STEP FOUR - Created or overwritten
-----------------------------------

  *The file created by the program is called [ to_save_file_all_mmr.csv ]

  *It will be OVERWRITTEN everytime the program runs.

  *It is located in the same directory as the script and the csv with the plaform/ids of players.



4.1 MAKE SURE to open this file thru and already opened Excel file.
-------------------------------------------------------------------

1)Go to a blank sheet in Excel

2)Go to Data > From Text > Find to_save_file_all_mrr.csv in your computer

3)Tranfer and select Delimited Data - Next

4)Delimiters, checkmark on comma - Next

5)Make sure that the column with the ids is TEXT and not GENERAL. - Finish

6)Choose destination  - OK


*IF your want to keep that data save this new Excel file with a different name*


-----------------------------------
5.0 STEP FIVE - Data Cleanup
-----------------------------------

  *Check some ranks manually to validate data.

  *Error names appear in the Rank columns if there was an error.

  *Suggestion: Matches played is also a good way to asses if the rank is reliable.