# ;==========================================
# ; Title:  Selenium Connection Bot
# ; Author: Prabal Jain
# ; Year: 2021
# ; rel: Beta W/o GUI
# ;==========================================
import openpyxl_operation
from graphical_script import guibuild

username = "yourmail@gmail.com"
commaseparated = "Field1;Field2;Field3"
password = "Yourpassword"

connection_mess = ''
#upto pages is just to let the script know for how many pages you want it ti execute
upto_page = 1



## Just to add some colors in text
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    guibuild()