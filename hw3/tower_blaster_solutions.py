"""
HW3: Tower Blaster

This homework deals with the following topics:
 - lists
 - tuples

In this HW, we will be implementing the game Tower Blaster,
which is a game that involves re-arranging a group of bricks
in order to have an increasing sequence.

While Tower Blaster is often played with 2 human players,
we will keep this simple and just play the user versus the computer.
The user’s moves are decided by the user, by asking for input,
and the computer’s moves are decided by you, the programmer.

There is NO right answer for the section that asks you to program a
strategy for the computer.  All we want you to do is come up with a
reasonable enough strategy that ensures a human user does not always
beat the computer.  So, unlike your previous assignments, this one has
a creative component to it. 

"""

import random
import time

def setup_bricks():
     """Returns a tuple containing a main pile of 60 bricks
     and a discard pile containing 0 bricks."""
     
     print("Setting up bricks ...")

     main_pile = [i for i in range(1, 61)]
     discard_pile = []
     
     return main_pile, discard_pile

def shuffle(bricks):
     """Shuffles a pile of given bricks."""
     
     print("Shuffling bricks ...")

     random.shuffle(bricks)

def check_bricks(main_pile, discard):
     """Checks if there are any cards left in given main pile of bricks.

     If so, shuffles the discard pile and moves those bricks to the main pile.
     Then turns over the top card to be the start of the new discard pile.
     
     """

     #confirm main_pile has bricks
     if (len(main_pile) == 0):
          print("No bricks left in the main pile")
          
          #shuffle discard pile
          shuffle(discard)

          print("Copying discard to main ...")
          #copy all bricks in discard pile to main pile
          main_pile[:] = discard[:]

          #empty discard pile
          discard[:] = []

          #add top brick from main pile to discard pile
          add_brick_to_discard(get_top_brick(main_pile), discard)
    
def check_tower_blaster(tower):
     """Returns whether the given tower has stability.

     Stability means that the bricks are in perfect ascending order.
     
     """
     last_i = 61
     for i in range(len(tower) - 1, 0, -1):
          if (tower[i] > last_i):
               return False
          
          last_i = tower[i]
          
     return True

def get_top_brick(brick_pile):
     """Removes and returns the top brick of the given brick pile.

     Note: Brick piles are vertically oriented structures, with the top having index 0.
     
     """
     if (len(brick_pile) == 0):
          return None
     
     return brick_pile.pop(0)

def deal_initial_bricks(main_pile):
     """
     Deals bricks to the computer and user, taking from the top of the given
     main brick pile.

     The computer and the user each get 10 bricks.  The convention is to
     deal one brick to the computer, one to the user, one to the computer,
     one to the user, and so on.
     The computer is always the first person to get dealt to.

     Returns tuple continaing the computer's bricks, and the user's bricks.
     """
     print("Dealing bricks ...")

     computer_bricks = []
     user_bricks = []
     
     #deal 10 cards to computer and user
     for i in range(0, 10):
          #pop next brick off of main pile and give to computer and user
          computer_bricks.append(get_top_brick(main_pile))
          user_bricks.append(get_top_brick(main_pile))

     #reverse to display most recently dealt bricks on top (to the left)
     computer_bricks.reverse()
     user_bricks.reverse()
     
     return computer_bricks, user_bricks
    
def add_brick_to_discard(brick, discard):
     """Adds given brick to top of given discard pile.

     Note: Brick piles are vertically oriented structures, with the top having index 0.

     """
     
     discard.insert(0, brick)

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
     """Replaces the given brick to be replaced with the given new brick
     in the given tower.
     Check and make sure that the brick to be replaced is truly a brick in the tower.

     Adds the replaced brick to the given discard pile.
     
     """
     #confirm the brick to replace is in the pile
     if brick_to_be_replaced in tower:
          #get index
          index = tower.index(brick_to_be_replaced)
         
          #replace brick
          tower[index] = new_brick

          #add to discard
          add_brick_to_discard(brick_to_be_replaced, discard)

          return True
     
     else:
          
          return False

def computer_play(tower, main_pile, discard):
     """The computer's turn.

     The computer's strategy determines which brick to pick,
     from the given main pile or discard pile,
     and whether to use and add it to the given tower.
     
     """
     print('\nCOMPUTER\'S TURN')
     print('Computer\'s Tower', end = ': ')
     print(tower)
     
     new_brick, pile_type = computer_pick_brick(tower, main_pile, discard)
     use_brick = computer_use_brick(new_brick, tower, pile_type)

     if (use_brick == True):
          brick_to_replace = computer_check_brick_in_tower(new_brick, tower)
          success = find_and_replace(new_brick, brick_to_replace, tower, discard)
          
          if (success == True):
               print('The computer replaced', brick_to_replace, 'with', new_brick)

     print('Computer\'s Tower', end = ': ')
     print(tower)
     
     return tower
        
def see_top_brick_discard(discard):
     """Returns the top brick of the given brick pile, without removing it.

     Note: Brick piles are vertically oriented structures, with the top having index 0.
     
     """
     if (len(discard) == 0):
          return None
     
     top_discard_brick = discard[0]

     return top_discard_brick

def computer_pick_brick(tower, main_pile, discard):
     """The computer's strategy in determining which brick to pick,
     from the given main pile or discard pile.

     """
     
     top_discard_brick = see_top_brick_discard(discard)
     
     #check discard brick in tower
     potential_brick_to_replace = computer_check_brick_in_tower(top_discard_brick, tower)

     if (potential_brick_to_replace != None):
          new_brick = get_top_brick(discard)
          pile_type = 'discard'
          print('The computer picked', new_brick, 'from the discard pile')
     else:
          new_brick = get_top_brick(main_pile)
          pile_type = 'main'
          print('The computer picked', new_brick, 'from the main pile')

     return new_brick, pile_type
     
def computer_use_brick(new_brick, tower, pile_type):
     """The computer's strategy in determining whether to use the given new brick.

     A new brick from the discard pile must be used
     while a new brick from the main pile can be rejected.

     """
     #determine if computer will use the brick
     use_brick = False
     
     #selected from discard pile
     if (pile_type == 'discard'):
          use_brick = True
          
     #if selected from the main pile
     elif (pile_type == 'main'):

          #check main brick in tower
          potential_brick_to_replace = computer_check_brick_in_tower(new_brick, tower)

          if (potential_brick_to_replace == None):
               print('The computer rejected', new_brick)
          else:
               use_brick = True
               
     return use_brick


def computer_check_brick_in_tower(brick, tower):
     """The computer's strategy in determining if the given brick
     can reasonably be added to the given tower.

     Computer strategy:
     Splits all possible brick values (1 - 60) in half.
     Compares the given brick value to these two groups.
     - If it's <= half of all possible brick values (1 - 30),
     starts looking at the top (left) position of the tower
     since we want smaller numbers here.  Scans down (towards the right)
     until it find a reasonable brick to replace.
     For the very top (left-most) position, only considers bricks <= 15.
     - If it's > half of all possible brick values (31 - 60),
     start looking at the bottom (right) position of tower
     since we want bigger numbers here.  Scans up (towards the left)
     until it find a reasonable brick to replace.
     For the very bottom (right-most) position, only considers bricks >= 45. 

     Returns possible match, otherwise None.

     """

     #used to split possible brick values in half
     middle_split = 30

     #used to separate bricks with high values
     bottom_split = 45

     #used to separate bricks with low values
     top_split = 15

     #if the new brick value is <= half of all possible brick values,
     #start looking at the top (left) position of tower
     #we want smaller numbers here
     if (brick <= middle_split):

          start = 0
          end = len(tower) - 1
          increment = 1

     #if the new brick value is > half of all possible brick values,
     #start looking at the bottom (right) position of tower
     #we want bigger numbers here         
     elif (brick > middle_split):
          
          start = len(tower) - 1
          end = 0
          increment = -1

     for i in range(start, end, increment):
          #brick in bottom (right) position
          if (i == len(tower) - 1):
               if (brick > tower[i - 1]
                   #only consider new bricks with a high value for this position
                   and brick >= bottom_split
                   and brick > tower[i]):

                   return tower[i]
          #brick in some middle position
          elif (i > 0):
               replace = False

               #if new brick value is greater than the one above
               if (brick > tower[i - 1]):
                    #and its value is less than the one below
                    if (brick < tower[i + 1]):
                         #check the current brick value
                         #if it's greater than the one below
                         if (tower[i] > tower[i + 1]):
                              #replace it
                              replace = True
                         #else if the new brick value is greater than the current brick value
                         elif (brick > tower[i]):
                              #replace it
                              replace = True
                                   
               if (replace == True):
                    return tower[i]
                         
          #brick in top (left) position
          elif (i == 0):
               if (brick < tower[i + 1]
                   #only consider new bricks with a low value for this position
                   and brick <= top_split
                   and brick < tower[i]):

                    return tower[i]
                    
     return None

def user_start_play(tower, discard):
     """Starts the user's turn."""

     print('\nNOW IT\'S YOUR TURN!')
     print('Your Tower', end = ': ')
     print(tower)

     top_discard_brick = see_top_brick_discard(discard)
     print('The top brick on the discard pile is', top_discard_brick)

def user_end_play(tower):
     """Ends the user's turn."""
     
     print('Your Tower', end = ': ')
     print(tower)

def print_tower(tower):
     """Prints the given tower."""
     
     for i in tower:
          print()
          print('(', i, ')\t', sep = '', end = '')

          for j in range(1, i + 1):
               print('|', end = '')

     print('\n')

def print_about_the_game():
     """Prints information about the game."""
     
     print('Welcome to Tower Blaster, a game that '
           + 'involves re-arranging a group of bricks in order to have an '
           + 'increasing sequence.\n\nWhile Tower Blaster is often played '
           + 'with 2 human players, this version keeps it simple and just plays the '
           + 'user versus the computer. The user’s moves are decided by you '
           + '(the user) by asking for input and the computer’s moves are '
           + 'decided automatically, using its own logic.\n')
     
def print_directions():
     """Prints instructions."""
     
     print('\nInstructions:\nBuild a tower by placing bricks in numerical '
           + 'progression from low at the top (left of list) to high at the bottom '
           + '(right of list) of the tower.  Note: Towers are represented as lists, '
           + 'from top bricks (left of list) to bottom bricks (right of list).\n\n'
           + 'Finish your tower before your opponent (the computer) to win.  '
           + 'Replace the bricks in your tower so that they are in order.\n\nIf you '
           + 'do not want to use the known brick in the discard pile, try the mystery '
           + 'brick in the main pile.\n\nNote: If you choose a brick from the discard '
           + 'pile, you MUST place it in your tower.  If you choose a mystery brick from the '
           + 'main pile, you can reject it!\n')
     
def delay(secs = 1):
     """Delays the game by the given seconds value."""
     
     time.sleep(secs)
     
def main():

     print_about_the_game()
     input('Type any key to continue and play!')
     
     #create bricks
     main_pile, discard_pile = setup_bricks()
     delay()
     
     #shuffle main bricks
     shuffle(main_pile)
     delay()
     
     #deal 10 bricks to computer and user
     computer_bricks, user_bricks = deal_initial_bricks(main_pile)
     delay()
     
     #turn over top card and add to discard pile
     add_brick_to_discard(get_top_brick(main_pile), discard_pile)
        
     computer_won = False
     user_won = False
     game_over = False

     print('The computer goes first!')
     
     while (game_over == False):

          check_bricks(main_pile, discard_pile)
          
          #computer goes first
          computer_bricks = computer_play(computer_bricks, main_pile, discard_pile)

          #check if computer won
          computer_won = check_tower_blaster(computer_bricks)
          
          #user goes second
          user_start_play(user_bricks, discard_pile)

          #ask user to choose new brick from discard pile or main pile
          new_brick = None
          use_new_brick = False
          while (new_brick == None):
               pile_choice = input('Type \'D\' to take the discard brick, \'M\' for a mystery brick, or \'H\' for help\n')

               if (pile_choice.lower() == 'd'): #select from discard pile
                    new_brick = get_top_brick(discard_pile)
                    print('You picked', new_brick, 'from discard pile.')

                    #must use new brick from discard pile
                    use_new_brick = True
                                 
               elif (pile_choice.lower() == 'm'): #select from main pile 
                    new_brick = get_top_brick(main_pile)
                    print('You picked', new_brick, 'from main pile.')

                    #ask user to use or reject new brick
                    found_new_brick_choice = False
                    while (found_new_brick_choice == False):
                         use_new_brick_choice = input('Do you want to use this brick? Type \'Y\' or \'N\' to skip turn\n')
                         
                         if (use_new_brick_choice.lower() == 'n'):
                              found_new_brick_choice = True
                              print('You rejected', new_brick)
                              
                         elif (use_new_brick_choice.lower() == 'y'):
                              found_new_brick_choice = True

                              #will use new brick from main pile
                              use_new_brick = True

               elif (pile_choice.lower() == 'h'): #get help 
                    print_directions()

          #user using new brick
          if (use_new_brick == True):

               #ask user for brick to be replaced
               brick_to_be_replaced = None
               found_brick_to_be_replaced = False
               while (found_brick_to_be_replaced == False):
                    replace_choice = input('Where do you want to place this brick?  Type a brick number to replace in your tower.\n')

                    #check that for numeric value
                    if (replace_choice.isnumeric()):
                         brick_to_be_replaced = int(replace_choice)

                         #check if brick exists in user tower
                         if (brick_to_be_replaced in user_bricks):
                              found_brick_to_be_replaced = True

                    if (found_brick_to_be_replaced == False):
                         print('Sorry, that does not exist in your tower.  Please try again.')

               #replace brick in tower
               success = find_and_replace(new_brick, brick_to_be_replaced, user_bricks, discard_pile)
                    
               if (success == True):
                    print('You replaced', brick_to_be_replaced, 'with', new_brick)
                    
          user_end_play(user_bricks)

          #check if user won
          user_won = check_tower_blaster(user_bricks)
          
          if (user_won == True):
               print('You won!')
          elif (computer_won == True):
               print('Oh well ... the computer won!')

          game_over = computer_won or user_won
          
if __name__ == '__main__':
    main()
