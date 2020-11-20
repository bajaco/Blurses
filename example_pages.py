pages = [

    '''Blurses is very easy to use. First import: SKIP SKIP
    
    from blurses import Blurses SKIP SKIP 

    After importing, you need to define the behavior of
    your application. This is done by creating a function for every section.
    Think of how many entries you want to have on your main menu, and
    create a function for each. The first function will not be included
    in the menu. It is ideal to make this your main menu function: 
    SKIP SKIP
    def menu(window, menu): 
    SKIP SKIP 
    Note that the function requires two arguments, window and menu.
    These are objects supplied by Blurses that allow you to
    position elements and define behavior. All functions used with
    Blurses must have window and menu arguments.''',

    

    '''Now that we have our menu function it's time to
    create some elements to display. There are two options: SKIP SKIP
    window.draw() - This accepts a list of strings. Alternatively any element of
    the list can instead be a tuple, containing the string, and a render
    mode. To use a render mode, you will have to import curses. SKIP SKIP
    window.wrap() - This is the same as draw, except it accepts a string 
    or tuple instead
    of a list of strings or tuples. The wrap function displays just like draw
    but provides word-wrapping so the string fits the window. Note that this
    ignores all newline characters, so to go to a new line type 'skip' in all 
    capital letters. To skip a line type 'skip' in uppercase twice. Optionally set
    the width as a percentage of the terminal width. For example, width=80
    will ensure that words are wrapped such that the longest lines are only
    80% as wide as the terminal.''',

    

    '''Both window.draw() and window.wrap() also except optional
    positioning arguments: SKIP SKIP

    top - Set percentage distance from top of terminal window. SKIP
    left - Set percentage distance from left side of terminal window. SKIP
    bottom - Set percentage distance from bottom of terminal window. SKIP
    right - Set percentage distance from right side of terminal window. SKIP
    vcenter - Vertically center the element if set to True SKIP
    hcenter - Horizontally center the element if set to True SKIP SKIP

    For example to take a string called text and position it
    vertically centered, and 5% from the left edge of the window: SKIP SKIP
    window.wrap(text, vcenter=True, left=5) SKIP SKIP
    Now, if we only want it to span 90% of the window's width
    we could use: SKIP SKIP
    window.wrap(text, width=90, vcenter=True, left=5) SKIP SKIP
    This would allow for a 5% buffer on both sides of the text block.''',

    

    '''However, before positioning anything you need to call
    two methods on the window object: SKIP SKIP
    window.clear() SKIP
    window.update() SKIP SKIP
    These are pretty self-explanatory. clear() clears the window, and update()
    refreshes the window's internal data regarding size. SKIP SKIP
    Within our menu function we want to display our some text and our
    menu. To do this we will put our code in a while loop. (In order for Blurses
    to be responsive, all drawing must be performed within a loop contingent on
    window.getch or similar. This is because terminal resize sends a key or char.) 
    First: SKIP SKIP
    mode = 0 SKIP SKIP
    Then, SKIP SKIP
    while mode == 0: SKIP SKIP''',

    

    '''Within our while loop we will clear, update, and draw.
    SKIP SKIP
    window.clear() SKIP
    window.update() SKIP
    window.wrap(description, width=80, vcenter=True, left=10) SKIP
    window.draw(menu(), left=5, bottom=5) SKIP SKIP
    Note the menu object is drawn in the draw method like anything else,
    it must simply be supplied as a callable: menu() not menu. SKIP SKIP''',


    '''We will also include code to break out of the loop: SKIP SKIP
    mode = menu.input(window.getch()) SKIP SKIP
    This takes character input from the window, passes it to the menu,
    which passes it to mode. Note, the output from the menu will correspond
    to the selected menu option's function. So if the first menu option is
    selected, 1 is returned, corresponding to function 1. Our menu is function
    0, so we can return this number to go to the selected menu option: SKIP SKIP
    return mode SKIP SKIP
    Note, all functions used with Blurses must return an int. Normally this will
    be 0, which signals a return to the main menu.''',

    

    '''Great. Now we simply need to add our functions with Blurses.
    For instance, say we have a menu() function, and an instructions() function:
    SKIP SKIP
    blurses = Blurses() SKIP
    blurses.bind('invisible', menu) SKIP
    blurses.bind('Instructions, instructions) SKIP SKIP
    The first function is set to the name invisible. You can set it to whatever
    you want. Since the first function is assumed to be the main menu, it does
    not matter what you call it, because it will not be displayed in the menu.
    SKIP SKIP
    Now, in order to run our application, we simply use: SKIP SKIP
    blurses.run() SKIP SKIP''',

    '''Note that the Exit menu option is automatically defined. You simply need
    to define the functions you need and bind them. SKIP SKIP

    That's it! You should now have a working application. Please see Pause and Resume for 
    more features'''
    ]

    

