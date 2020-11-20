from blurses import Blurses
from example_pages import pages

def menu(window, menu):
    title = ['Blurses Example']
    description = '''Welcome to the Blurses example app.
    Blurses is an easy to use Curses framework that allows for
    efficient formatting, program structure, and positioning.

    Select instructions for more information.'''

    mode = 0
    while mode == 0:
        window.clear()
        window.update()
        window.draw(title, top=0, left=2)
        window.wrap(description, width=80, vcenter=True, left=10)
        window.draw(menu(), bottom=5, left=5)
        mode = menu.input(window.getch())
    return mode


def instructions(window, menu):
        
    press = 'Press enter to continue: '

    for page in pages: 
        key = 0
        while key != 10:
            window.clear()
            window.update()
            window.wrap(page, width=90, left=5, top=5)
            window.wrap(press, left=5, bottom=5)

            key = window.getch()
    
    return 0

def pause(window, menu):

    description = '''The window object also features pause() and 
    resume() methods in order to temporarily return the application to
    a regular terminal mode: SKIP SKIP

    window.pause() SKIP
    # Do stuff SKIP
    window.resume()'''

    press = 'Press enter to pause the application and return to the terminal.'

    key = 0
    while key != 10:
        window.clear()
        window.update()
        window.wrap(description, width=90, left=5, top=5)
        window.wrap(press, left=5, bottom=5)

        key = window.getch()
    window.pause()
    print('Blurses has been paused.\n')
    tl = input('Enter text to display in the top left: ')
    tr = input('Enter text to display in the top right: ')
    bl = input('Enter text to display in the bottom left: ')
    br = input('Enter text to display in the bottom right: ')
    window.resume()
    description = 'Blurses has resumed!'
    press = 'Press enter to return to the main menu.'
    key = 0
    while key != 10:
        window.clear()
        window.update() 
        window.wrap(description, width=90, left=5, top=5)
        window.wrap(press, left=5, bottom=5)
        window.wrap(tl, top=0, left=0)
        window.wrap(tr, top=0, right=0)
        window.wrap(bl, bottom=0, left=0)
        window.wrap(br, bottom=0, right=0)
        
        key = window.getch()
    return 0


blurses = Blurses()
blurses.bind('', menu)
blurses.bind('Instructions', instructions)
blurses.bind('Pause and Resume', pause)
blurses.run()
