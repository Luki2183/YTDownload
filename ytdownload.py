import os
import msvcrt

# full menu with options and stuff
# pasek pobierania

def cls():
    return os.system('cls')

def mainmenu():
    while True:
        cls()
        print('\t\tYTDownload')
        print('  Youtube Videos:')
        print('    [1] Video with options')
        print('    [2] Audio-Only with options')
        print('    [3] Quick Video (always highiest quality)')
        print('    [4] Quick Audio-Only (always highiest quality)')
        print('  Youtube Playlist:')
        print('    [5] All Videos from playlist (always highiest quality)')
        print('    [6] All Audio-Only from playlist (always highiest quality)')
        print('  Other:')
        print('    [7] Login Credentials')
        print('    [8] Exit')
        print('Enter a menu option in the keyboard [1, 2, 3, 4, 5, 6, 7, 8]')
        menu = int(msvcrt.getch())
        if menu == 1:
            break
        elif menu == 2:
            break
        elif menu == 3:
            videomenu()
            continue
        elif menu == 4:
            break
        elif menu == 5:
            break
        elif menu == 6:
            break
        elif menu == 7:
            break
        elif menu == 8:
            break

def videomenu():
    while True:
        cls()
        print('\t\tYTDownload')
        print('  Quick Video (always highiest quality)')
        menu = input('Please insert Youtube link(type "back" to go back):')
        if menu == 'back':
            break
            cls()
        else:
            cls()
            print('Called function to download video with highest quality!')
            back = input('Would you like to download again(Y/n):')
            if back == 'Y' or back == 'y':
                continue
            elif back == 'n':
                break
            else:
                break

def audiomenu():
    cls()
    return

mainmenu()