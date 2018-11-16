# Lesson 6 writing .py files instead of jupyter notebooks

# IF RUNNING IN SPYDER SET BREAKPOINTS USING F12

import pandas as pd
import random

if __name__ == '__main__': # this line ensures we are in the main application
    
    data = pd.read_pickle('WellGenData.pkl')
    rani = random.randint(0, len(data))
    
    # Start your game here, replace enter some text with a question you want to ask the player
    game_over = False
    tries = 0
    while not game_over:
        tries += 1
        
        d = data.iloc[rani]
        wellcomp = d['WELL_COMP_NAME']
        wellauto = d['WELL_AUTO_NAME']
        wellcom = d['WELL_COMMON_NAME']
        wellname = wellcomp
        
        wn = input('Slightly miss arange this wellname {}: '.format(wellname)) # allows player to enter some text or a number
        print('You entered {}'.format(wn))
        
        data.fillna(value='Empty', inplace=True)
        
        subreplacements = {
          '-RD*': '',
          '_RD*': '',
          ' RD*': '',
          '-R*': '',
          '_R*': '',
          ' R*': '',
          '-': '',
          '_': '',
          ' ': '',
          'SECTION': '',
          'SEC': '',
          '/': ''
          }
    
        replacements = {
           'WELL_COMP_NAME': subreplacements,
           'WELL_AUTO_NAME': subreplacements,
           'WELL_COMMON_NAME': subreplacements,
        }
        
        data.replace(replacements, regex=True, inplace=True)
    
        # Check the input with an if statement
        if wn == '':
            print('Nothing given')
        else:
            
            temp = wn.replace(subreplacements)

            print('do something else')

        if tries == 5:
            game_over = True
            print('You took too long, game over')

        # Your task: make a 2-3 step text game with the starting code up above and have your neighbor try playing it