# This file is used to automatically convert older GooFit code
# that uses the old lineshapes format to the new lineshapes format
# by automatically finding/replacing.

import fileinput
import re

def replace_all_lineshapes(text, lineshapeRepls):
    for oldEnum, newClassName in lineshapeRepls.iteritems():
        if re.search("new Lineshape.*,\s*"+oldEnum+"\s*,", text): 
            text = re.sub("new Lineshape", "new "+newClassName, text)
            text = re.sub(oldEnum+"\s*,\s*", "", text)
    return text

def main():
    # build dict with data needed for converting
    # key = old LS enum, value = new lineshape class
    lineshapeRepls = {
    'LS::ONE' : 'Lineshapes::One',
    'LS::BW' : 'Lineshapes::RBW',
    'LS::Lass' : 'Lineshapes::LASS',
    'LS::Lass_M3' : 'Lineshapes::GLASS',
    'LS::nonRes' : 'Lineshapes::NonRes',
    'LS::Bugg' : 'Lineshapes::Bugg',
    'LS::Bugg3' : 'Lineshapes::Bugg3',
    'LS::Flatte' : 'Lineshapes::Flatte',
    'LS::SBW' : 'Lineshapes::SBW'
    }
    
    # open file
    fileName = input("Full path to file: ")
    print 'Updating lineshapes in file ' + fileName + '...'
    fileToModify = fileinput.FileInput(fileName, inplace=True, backup='.bak')
    
    # replace
    for line in fileToModify:
        print replace_all_lineshapes(line, lineshapeRepls),
        
    # close file
    fileToModify.close()
    print 'Done.'
        
if __name__ == "__main__": main()
