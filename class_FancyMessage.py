import os
import fancyprint as fp
msg = fp.FancyMessage()
crs = fp.Cursor()
name1 = " Miguelito Aguilar Cuesta "

name2 = " Miguelito Angel Aguilar Cuesta   Come, \" The highway if full of big cars going nowhere \
fast and folks are smoking anything that  will burn. \""

name3 = '''
        I should probably collect a list of the best
        romantic poems ever written, and maybe I will.
        This is not that. I mostly talk about writing
        books, but I noticed most of the other big
        writing sites actually get most of the their

        traffic from this keyword, because everybody
        is interested in romantic poetry! When you
        want to tell her how you feel, but do not
        have the words to express all that emotion...! 
'''

name4 = '''\
    +---------------------------------------------------+
    |    I should probably collect a list of the best   |
    |    romantic poems ever written, and maybe I will. |
    |    This is not that. I mostly talk about writing  |
    |    books, but I noticed most of the other big     |
    |    writing sites actually get most of the their   |
    +---------------------------------------------------+
    |   traffic from this keyword, because everybody    |
    |   is interested in romantic poetry! When you      |
    |   want to tell her how you feel, but do not       |
    |   have the words to express all that emotion...!  |
    +---------------------------------------------------+
'''

# Default Varibles
# bold = False           Values = True/False          
# fg = 4                 Values = from 0 to 255
# bg = 251               Values = from 0 to 255

# left_indent = 0        Values = depends on the width of the terminal
# right_indent = 0       Values = depends on the width of the terminal

# self.length = Length_bg.ALL_ROW   (All_ROW, ONLY_WORD)

#---------------------------------------------------------------------------------------
# self.lines = 1 
# self.adj_bg_lines_to_right_indent =  False    (False, True)
# self.adj_bg_msg_to_space_available = False    (False, True, None)

# msg.bold = True; msg.bg = 95; msg.fg = 0
# msg.left_indent = 8; msg.right_indent = 8    # it's for the string 
# msg.lines = 3                                # how many lines above and below the string

# msg.print_fancy_msg(name1)
# print("\n"); 
# msg.length = fp.Length_bg.ONLY_WORD          # type of bg
# msg.adj_bg_lines_to_right_indent =  True     # True adjs to space available
#                                              # when True, right_indent is considerd
#                                              # False adjs bg to the string width
# msg.adj_bg_msg_to_space_available = True     # True adjs string to space available
#                                              # when True right_indent is considerd
#                                              # False adjs bg to longest string width
#                                              # None adjs bg to string length
# Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# options when the string is presented in a form of paragraph type

# msg.print_fancy_msg(name1)


#---------------------------------------------------------------------------------------
# msg.bold = True; msg.bg = 95; msg.fg = 0
# msg.left_indent = 8; msg.right_indent = 8      # it's for the string 
# msg.lines = 3                                  # how many lines above and below the string

# msg.print_fancy_msg(name2)
# print("\n"); 
# msg.length = fp.Length_bg.ONLY_WORD            # type of bg
# msg.adj_bg_lines_to_right_indent =  True       # True adjs to space available
#                                                # when True, right_indent is considerd
#                                                # False adjs bg to the string width
# msg.adj_bg_msg_to_space_available = True       # True adjs string to space available
#                                                # when True right_indent is considerd
#                                                # False adjs bg to longest string width
#                                                # None adjs bg to string length
# Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# options when the string is presented in a form of paragraph type
# msg.print_fancy_msg(name2)


#---------------------------------------------------------------------------------------
# msg.bold = True; msg.bg = 95; msg.fg = 0
# msg.left_indent = 8; msg.right_indent = 8      # it's for the string 
# msg.lines = 2                                  # how many lines above and below the string

# msg.print_fancy_msg(name3)
# print("\n"); 
# msg.length = fp.Length_bg.ONLY_WORD            # type of bg
# msg.adj_bg_lines_to_right_indent =  False      # True adjs to space available
#                                                # when True, right_indent is considerd
#                                                # False adjs bg to the longest string width
# msg.adj_bg_msg_to_space_available = None       # True adjs string to space available
#                                                # when True right_indent is considerd
#                                                # False adjs bg to longest string width
#                                                # None adjs bg to string length
# # Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# # options when the string is presented in a form of paragraph type

# msg.print_fancy_msg(name3)


#---------------------------------------------------------------------------------------
msg.bold = True; msg.bg = 95; msg.fg = 0
msg.left_indent = 8; msg.right_indent = 18      # it's for the string 
msg.lines = 2                                  # how many lines above and below the string

msg.print_fancy_msg(name4)
print("\n"); 
msg.length = fp.Length_bg.ONLY_WORD            # type of bg
msg.adj_bg_lines_to_right_indent =  False      # True adjs to space available
                                               # when True, right_indent is considerd
                                               # False adjs bg to the longest string width
msg.adj_bg_msg_to_space_available = False       # True adjs string to space available
                                               # when True right_indent is considerd
                                               # False adjs bg to longest string width
                                               # None adjs bg to string length
# Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# options when the string is presented in a form of paragraph type

msg.print_fancy_msg(name4)