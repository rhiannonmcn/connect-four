from pyfiglet import figlet_format
import colorama
from termcolor import cprint
import run as run
import validation as val


colorama.init(autoreset=True)


def blank_line():
    """
    Function to print off a blank line
    """
    print(' ')
    

def multiple_blank_lines():
    blank_line()
    blank_line()
    blank_line()
    blank_line()

def connect4_title():
    """
    Function to print off the connect 4 title
    """
    color = 'yellow'
    blank_line()
    
    cprint(figlet_format(' Connect            4 !         ', font = "banner3-D", justify = 'center'), color, attrs=['bold'])

def game_bar():
    """
    
    """
    blank_line()
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
    cprint(f'Player 1 : {val.player_one}                Player 2 : {val.player_two}'.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
    

def game_over_text():
    """
    
    """
    blank_line()
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['RED_HL'])
    cprint('GAME OVER!'.center(80), run.COLORS['WHITE'], run.COLORS['RED_HL'])
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['RED_HL'])