# Lesson 6 writing .py files instead of jupyter notebooks

# IF RUNNING IN SPYDER SET BREAKPOINTS USING F12

import pandas as pd
import random
from sys import stdout
from time import sleep
import re

if __name__ == '__main__': # this line ensures we are in the main application
    
    raw = pd.read_pickle('WellGenData.pkl')
    df = raw.copy()
    rani = random.randint(0, len(df))
    
    # Start your game here, replace enter some text with a question you want to ask the player
    game_over = False
    tries = 0
    while not game_over:
        tries += 1
        
        d = df.iloc[rani]
        wellcomp = d['WELL_COMP_NAME']
        wellcommon = d['WELL_COMMON_NAME']
        wellauto = d['WELL_AUTO_NAME']
        
        wellname = wellcomp
        
        input_wn = input('Slightly alter this wellname {}: '.format(wellname)) # allows player to enter some text or a number
        
        think = ['Thinking','.','.','.']
        for i in range(len(think)):
            print(think[i], sep=' ', end='', flush=True)
            sleep(1)
        print('\n')
        
        #Clean Master Reference
        df.fillna(value='EMPTY', inplace=True)
        df.apply(lambda x: x.astype(str).str.upper())
        subreplacements = {
          '-RD*': '',
          '_RD*': '',
          ' RD*': '',
          '-R*': '',
          '_R*': '',
          ' R*': '',
          '-ST*': '',
          '_ST*': '',
          ' ST*': '',
          'SECTION': '',
          'SEC': ''
          }
        replacements = {
           'WELL_COMP_NAME': subreplacements,
           'WELL_COMMON_NAME': subreplacements,
           'WELL_AUTO_NAME': subreplacements,
        }
        df.replace(replacements, regex=True, inplace=True)
        df['WELL_COMP_NAME'].apply(
                lambda x: re.sub('[^0-9a-zA-Z]+', '', x))
        df['WELL_COMMON_NAME'].apply(
                lambda x: re.sub('[^0-9a-zA-Z]+', '', x))
        df['WELL_AUTO_NAME'].apply(
                lambda x: re.sub('[^0-9a-zA-Z]+', '', x))
    
        # Check the input with an if statement
        if input_wn == '':
            print('Nothing given')
        else:
            
            temp_wn = input_wn.upper()
            for k,v in subreplacements.items():
                if k in input_wn:
                    temp_wn = temp_wn.replace(k,v)
            temp_wn = re.sub('[^0-9a-zA-Z]+', '', temp_wn)

            comp_check = df['WELL_COMP_NAME'][df['WELL_COMP_NAME'].str.contains(temp_wn)]
            common_check = df['WELL_COMMON_NAME'][df['WELL_COMMON_NAME'].str.contains(temp_wn)]
            auto_check = df['WELL_AUTO_NAME'][df['WELL_AUTO_NAME'].str.contains(temp_wn)]

            if not comp_check.empty:
                print('Well Comp Match:')
                for indx, val in comp_check.iteritems():
                    print (indx, val)
               
            elif not common_check.empty:
                print('Well Common Match:')
                for indx, val in common_check.iteritems():
                    print (indx, val)    
                
            elif not auto_check.empty:
                print('Well Auto Match:')
                for indx, val in auto_check.iteritems():
                    print (indx, val)
                
            else:
                print('No Match')

            game_over = True
            print('Game Over')

        if tries == 5:
            game_over = True
            print('You took too long, Game Over')

        # Your task: make a 2-3 step text game with the starting code up above and have your neighbor try playing it