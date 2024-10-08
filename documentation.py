import sys
import fancyprint as fp
lst = fp.FancyFormat()
#----------------------------------------------------------------------------------------------------------------------------------------------
# Difining all the clases
blue_msg  = fp.FancyMessage()  # for titles

green_msg = fp.FancyMessage()  # for subtitles
green_msg.bg_body = 2;  green_msg.fg_body = 0; green_msg.bold_body = True

dark_green_msg = fp.FancyMessage()
dark_green_msg.bg_body = 22; dark_green_msg.bold_body = True

purple_msg = fp.FancyMessage()
purple_msg.bg_body = 90; purple_msg.fg_body = 231

white_msg = fp.FancyMessage()
white_msg.bg_body = 231; white_msg.fg_body = 21; white_msg.bold_body = True

msg = fp.FancyMessage()   # Note
msg.right_indent = 5

simple_msg = fp.FancyFormat()


crs = fp.Cursor()

fst = fp.FontStyle() 
fst.bold = True; 
fst.fg = 0
fst.bg = 231
fst.indent = 2
fst.next_line = False

#----------------------------------------------------------------------------------------------------------------------------------------------
def adj_screen(y, x):
   if (fp.OS_Linux == True and fp.OS_Windows == False):   fp.resize(rows=y, cols=x) #fp.resize(44, 90)
   elif (fp.OS_Linux == False and fp.OS_Windows == True): fp.resize(rows=y, cols=x) #fp.resize(44, 90)
   else:                                                  pass

# Variables
ncols, nrows = fp.dimensions()
myrows = 90; mycols = 100
adj_screen(myrows, mycols)



screen_funs        = [[" Screen_Functions "],["clean"],["clear"],["erase"],["dimensions"], ["resize"]]

internal_functions = [[" Internal_Functions "],["ins_space"],["ins_newline"], ["ansi_colors"], ["terminal_bell"]]

help_classes       = [[" Help_Classes "],["Move"],["Align"],["Layout"],["Length"],["Style_Line"]]

classes_methods_fancyprint = [["Cursor",  "FontStyle",    "FancyMessage",        "FancyFormat"        ,"Draw"],
                              ["jumpTo",  "start_style",  "print_fancy_message", "print_fancy_format", "line"],
                              ["jumpxy",  "stop_style",   "print_fancy_note",    "reset_fancy_format", "arrow"],
                              ["moveTo",  "print_style",  "reset_fancy_message", "----",               "box"],
                              ["movexy",  "reset_style",  "reset_fancy_note",    "----",               "brakets"]]

# classes_methods_fancyprint = [["Cursor", "FontStyle",   "FancyMessage",    "FancyFormat",       ],
#                               ["jump",   "get_style",   "print_fancy_msg", "print_fancy_format" ],
#                               ["move",   "reset_style", "----",            "----",              ],
#                               ["gotoxy", "print_style", "----",            "----",              ],
#                               ["moveTo", "----",        "----",            "----",              ]]
#----------------------------------------------------------------------------------------------------------------------------------------------
# Welcome Message Function for fancyprint Module                                                                                              -
#----------------------------------------------------------------------------------------------------------------------------------------------
def Welcome_Message():
   welcome_msg = "Documentation For fancyprint Module....!"
   li = int(((mycols)-(len(welcome_msg)))/2)
   blue_msg.left_indent = li
   blue_msg.bold = True
   blue_msg.italic = True
   blue_msg.print_fancy_message(welcome_msg)
   fp.ins_newline()

   lst.bg_all_cell_header = False
   lst.bold_header = True
   lst.bg_header = 90; lst.fg_header = 231

   # lst.bg_header = 231; lst.fg_header = 90
   lst.italic_header = True
   
   lst.print_fancy_format(screen_funs)
   

   lst.adj_indent = 34
   crs.jumpTo(qty=8,direction=fp.Move.UP)
   lst.print_fancy_format(internal_functions)

   # lst.bg_header = 90; lst.fg_header = 231
   
   lst.adj_indent = 68
   crs.jumpTo(qty=7,direction=fp.Move.UP)
   lst.print_fancy_format(help_classes)


   lst.adj_indent = 2
   fp.ins_newline(3)


   blue_msg.length = fp.Length_bg.ONLY_WORD
   blue_msg.print_fancy_message("  Classes and Methods in fancyprint Module ")
   lst.msg_title = " Clasess ";         lst.bg_title = 90; lst.fg_title = 231
   lst.bold_title = True;               lst.align_title = fp.Align.LEFT
   lst.msg_footnote = "Methods";        lst.align_footnote = fp.Align.RIGHT
   lst.fg_footnote = 11;  lst.fg_data = 11
   lst.bg_all_cell_header = True

   lst.horizontal_separator_line_on = True
   lst.print_fancy_format(classes_methods_fancyprint,fp.Line_Style.SINGLE)
   fp.ins_newline(2)

   print("  To display help for specific function or method, just pass the name as a parameter\n    when running this script.")
   fp.ins_newline(1)
   fst.print_style(" Example 1:")
   print(" python documentation.py clean\n")
   #print(f" {fp.set_font(1,231,0)} Example 1: {fp.reset_font()} python documentation.py clean")
   fp.ins_newline(1)

   note=" Note: "
#                  20                  40                  60                  80   85   90
   message_note = '''
It is possible to display help for more than one function or method at the same    
time, it just need to be specified. If it's preferred, it can display all the      
methods for a specific class or a combination of them.'''
   blue_msg.length = fp.Length_bg.ALL_ROW
   blue_msg.bold = False
   blue_msg.note_msg = note
   blue_msg.position_note = 2
   blue_msg.bold_note = True
   blue_msg.print_fancy_note(body_msg=message_note)

   fp.ins_newline(1); fst.print_style(" Example 2: "); print(" python documentation.py clean terminal_bell get_style Cursor")
      
   fp.ins_newline(2); fst.print_style(" Example 3: "); print(" python documentation.py help_functions")
   
   fp.ins_newline(2)
   message = '''     
     In example 2, notice that we are calling a mix of functions, methods and a class.
  For the class, it will call all the methods that this class contains as shown in the
  tables above. Cursor Class contains four methos, jump, move, gotoxy, and moveTo and
  so on for the rest of the following classes.
 
  In example 3, we are calling help for all the functions that this class contains.

  It's possible to display the complete documentation by passing \"all\" as parameter.
'''
   blue_msg.left_indent = 2
   blue_msg.print_fancy_message(message)
   fp.ins_newline(2)
   blue_msg.length = fp.Length_bg.ONLY_WORD; 
   blue_msg.left_indent = li
   message = "  python documentation.py all  "
   blue_msg.print_fancy_message(message)
   
   blue_msg.length = fp.Length_bg.ALL_ROW   
   blue_msg.left_indent = 2
   lst.msg_title = "";        lst.msg_footnote = ""
   lst.fg_data = -1;          lst.adj_indent = 30
   lst.adj_top_margin = 2;    lst.adj_bottom_margin = 2
   # lst.print_fancy_format("Report Bugs \u2192 acma82@yahoo.com", fp.Line_Style.DOUBLE)
   lst.print_fancy_format("Bugs \u2192 acma.mex@gmail.com", fp.Line_Style.DOUBLE)


#---------------------------------------------------------------------------------------------------
#  Screen_Functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Screen_Functions():
   blue_msg.bold = True
   blue_msg.italic = True
   blue_msg.print_fancy_message("Screen Functions")
   Clean_Function()
   Clear_Function()
   Erase_Function()
   Dimensions_Function()
   Resize_Function()
   fp.ins_newline(3)
   message = "\u25CF Reference \u2192  00_screen_functions.py"
   dark_green_msg.print_fancy_message(message)


def Clean_Function():
   #------------------------------------------------------------------------------------------------
   # clean                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor to home.
      It uses ansi code.
   '''
   green_msg.print_fancy_message(screen_funs[1][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.clear()\n")

def Clear_Function():
   #------------------------------------------------------------------------------------------------
   # clear                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor  to home.
      It uses the system command.
   '''
   green_msg.print_fancy_message(screen_funs[2][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.clear()\n")

def Erase_Function():
   #------------------------------------------------------------------------------------------------
   # erase                                                                                         -
   #------------------------------------------------------------------------------------------------
   menssage = '''
      It cleans the terminal and the cursor remain in the same position.
      It uses ansi code.
   '''
   green_msg.print_fancy_message(screen_funs[3][0])
   print(menssage)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.erase()\n")

def Dimensions_Function():
   #------------------------------------------------------------------------------------------------
   # dimensions                                                                                    -
   #------------------------------------------------------------------------------------------------
   menssage ='''
      It returns the size of the actual terminal: cols, rows.
      '''
   green_msg.print_fancy_message(screen_funs[4][0])
   print(menssage)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}ncols, nrows = fp.dimensions()\n")

def Resize_Function():
   #------------------------------------------------------------------------------------------------
   # resize                                                                                        -
   #------------------------------------------------------------------------------------------------
   message = '''
      It resizes the terminal
         '''
   green_msg.print_fancy_message(screen_funs[5][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.resize(rows = n_rows, cols = n_cols)\n")

#---------------------------------------------------------------------------------------------------
#  internal_functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Internal_Functions():   
   blue_msg.print_fancy_message("Internal Functions")
   Ins_Space_Function()
   Ins_Newline_Function()
   Ansi_Color_Function()   
   Terminal_Bell_Function()
   message = "\u25CF Reference \u2192  01_ansi_colors.py"
   dark_green_msg.print_fancy_message(message)
   

def Ins_Space_Function():
   #------------------------------------------------------------------------------------------------
   # ins_space                                                                                     -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_message(internal_functions[1][0])
   message = f'''
      This function inserts x number of spaces between words.

               fancy_print.ins_space(x)

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp      
                  print("Hello"+fp.ins_space(20)+"There")

      {fp.set_font(1,231,90)} \u25CF Output {fp.reset_font()}  Hello                    There
      '''
   
   print(message)
   # print(f"{fp.ins_space(6)}{fp.set_font(1,231,90)} \u25CF Reference \u2192 ins_space.py {fp.reset_font()}\n")

def Ins_Newline_Function():
   #------------------------------------------------------------------------------------------------
   # ins_newline                                                                                   -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_message(internal_functions[2][0])
   message = f'''
      This function inserts x number of lines.

               fancy_print.ins_newline(x)

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  print("Python 3.12")
                  fp.ins_newline(2)
                  print("is amazing...!")
              
      {fp.set_font(1,231,90)} \u25CF Output {fp.reset_font()}  Python 3.12

               
                  is amazing...!
      '''
   print(message)
   

def Ansi_Color_Function():
   #------------------------------------------------------------------------------------------------
   # ansi_colors                                                                                -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_message(internal_functions[3][0]+": fancy_print contains 4 functions that make use of ansi code.")
   print("\n  bg colors available in the ansi code \n")

   for i in range(0, 16):
      for j in range(0, 16):
         code = str(i * 16 + j)
         sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
      print (u"\u001b[0m")
   
   fp.ins_newline(2)
   print("  fg colors available in the ansi code \n")
   for i in range(0, 16):
      for j in range(0, 16):
         code = str(i * 16 + j)
         sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
      print (u"\u001b[0m")
   
   print()

   purple_msg.print_fancy_msg("bg_ansi_colors(bool, int, int)")
   message = f''' 
      This function displays all background colors available in the fancyprint
      module. Three options for better visualization:
   
      1.- The option bold for the font (True/False).
      2.- The option fg to visualize the background colors with a specific foreground color.
      3.- The option n_line to insert lines between the colors.

      
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  fp.bg_ansi_colors(bold=1, fg=22, n_line=1)
   '''
   print(message)

   purple_msg.print_fancy_msg("fg_ansi_colors(bool, int, int)")
   message = f'''
      This function displays all foreground colors available in the fancyprint
      module. Two options for better visualization:
   
      1.- The option bold helps for font.
      2.- The option bg to visualize the foreground colors with a specific
          background color.
      3.- It insert lines to have space between them.

      
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  fp.fg_ansi_colors(bold=1, bg=22, n_line=1)
   '''
   print(message)

   purple_msg.print_fancy_msg("set_font() and reset_font()")

   message =f'''
      set_font() function changes the attributes of the font.
      reset_font() set font to its default attributes.
      
      Parameters with their default values:
      
      1) bold=False      4) italic=False         7) blinking=False      10) inverse=False
      2) bg=-1           5) underline=False      8) dim=False
      3) fg=-1           6) strike=False         9) hidden=False
      
      As you see there are many parameters to pass, if this is a littlle bit annoying, then use
      the FontStyle Class. Check the documentation for that class.

      The best way to use this function is only to pass the first 3 parameters as the example below.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  print(fp.set_font(1,11,21) + " Python is " + fp.set_font(0,1) +
                        " Wonderful." + fp.reset_font())

'''
   print(message)
   
   message = '''The range for colors goes from -1 to 256. 

to set the default color use -1 or 256 for bg and fg.

blinking might not work in all the OS. We use Red Hat Family.'''
   
   white_msg.print_fancy_note("Note:", message)

def Terminal_Bell_Function():
   #------------------------------------------------------------------------------------------------
   # terminal_bell                                                                                 -
   #------------------------------------------------------------------------------------------------
   message = f'''
      This function makes sound of the terminal bell.               

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  fp.terminal_bell()
      '''
   green_msg.print_fancy_message(internal_functions[4][0])
   print(message)
   fp.terminal_bell()

#---------------------------------------------------------------------------------------------------
# Help_Fucntions                                                                                   -
#---------------------------------------------------------------------------------------------------
def Help_Classes():
   blue_msg.print_fancy_message("Help Classes")
   Move_Class()
   Layout_Class()
   Length_Class()
   Style_Line_Class()

def Move_Class():
   #------------------------------------------------------------------------------------------------
   # Move                                                                                          -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_message(help_classes[1][0])
   message = f'''
      This class is used with the Cursor Class and it contains 4 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_space(10)}  fp.Move.RIGHT
      {fp.ins_space(10)}  fp.Move.LEFT
      {fp.ins_space(10)}  fp.Move.UP
      {fp.ins_space(10)}  fp.Move.DOWN
   
      Note: These options can be replaced for the original value as display below:

      {fp.ins_space(10)}  fp.Move.RIGHT  \u2192  \"right\"
      {fp.ins_space(10)}  fp.Move.LEFT   \u2192  \"left\"
      {fp.ins_space(10)}  fp.Move.UP     \u2192  \"up\"
      {fp.ins_space(10)}  fp.Move.DOWN   \u2192  \"down\"        

'''
   print(message)

def Align_Class():
   #------------------------------------------------------------------------------------------------
   # Align                                                                                         -
   #------------------------------------------------------------------------------------------------
   # Works with FancyFormat (print_fancy_format)
   # works with FancyMessage (print_fancy_note, print_fancy_header)
   green_msg.print_fancy_message(help_classes[2][0])
   message = f'''

      Aligns Class is used with the FancyFormat Class and FancyMessage Class.
      It contains 4 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_space(10)}  fp.Align.RIGHT
      {fp.ins_space(10)}  fp.Align.LEFT
      {fp.ins_space(10)}  fp.Align.CENTER
      {fp.ins_space(10)}  fp.Align.JUSTIFY
      
      Note: These options can be replaced for the original value as display below:

      {fp.ins_space(10)}  fp.Move.RIGHT    \u2192  \"right\"    \u2192  \"r\"
      {fp.ins_space(10)}  fp.Move.LEFT     \u2192  \"left\"     \u2192  \"l"
      {fp.ins_space(10)}  fp.Move.CENTER   \u2192  \"center\"   \u2192  \"c\"
      {fp.ins_space(10)}  fp.Move.JUSTIFY  \u2192  \"justify\"  \u2192  \"j\"
'''   
   print(message)

def Layout_Class():
   #------------------------------------------------------------------------------------------------
   # Layout                                                                                        -
   #------------------------------------------------------------------------------------------------
   # works with FancyFormat, range, set, setfrozen obj.set_layout = fp.Layout.VERTICAL
   # works with Draw (line, arrow)
   green_msg.print_fancy_message(help_classes[3][0])
   message = f'''
      
      Layout Class is used on FancyFormat only for the range, set, frozenset type of variables.
      Layout also is uded with Draw Class. It contains 2 options.
      
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_space(10)}  fp.Layout.HORIZONTAL
      {fp.ins_space(10)}  fp.Layout.VERTICAL
      
      Note: These options can be replaced for the original value as display below:

      {fp.ins_space(10)}  fp.Layout.HORIZONTAL   \u2192  \"horizontal\"
      {fp.ins_space(10)}  fp.Layout.VERTICAL     \u2192  \"vertical\"

'''
   print(message)
def Length_Class():
   #------------------------------------------------------------------------------------------------
   # Length                                                                                        -
   #------------------------------------------------------------------------------------------------
   # FancyMessage   
   green_msg.print_fancy_message(help_classes[4][0])
   message = f'''
   
      Length Class is used with FancyMessage Class and there 2 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_space(10)}  fp.Length.ALL_ROW
      {fp.ins_space(10)}  fp.Length.ONLY_WORD
            
'''
   print(message)

def Style_Line_Class():
   #------------------------------------------------------------------------------------------------
   # Style_Line                                                                                    -
   #------------------------------------------------------------------------------------------------
   # FancyFormat   
   green_msg.print_fancy_message(help_classes[5][0])
   message = f'''
   
      Style_Line Class is used with FancyFormat Class and Draw Class. There are 7 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_space(10)}  fp.Style_Line.CUSTOMIZED
      {fp.ins_space(10)}  fp.Style_Line.SINGLE
      {fp.ins_space(10)}  fp.Style_Line.SINGLE_BOLD
      {fp.ins_space(10)}  fp.Style_Line.SINGLE_HEAVY
      {fp.ins_space(10)}  fp.Style_Line.DOUBLE
      {fp.ins_space(10)}  fp.Style_Line.DASH
      {fp.ins_space(10)}  fp.Style_Line.SQR_BRACKETS
      {fp.ins_space(10)}  fp.Style_Line.NONE

      Note: These options can be replaced for the original value as display below:

      {fp.ins_space(10)}  fp.Style_Line.CUSTOMIZED     \u2192  \"customized\"  
      {fp.ins_space(10)}  fp.Style_Line.SINGLE         \u2192  \"single\"   
      {fp.ins_space(10)}  fp.Style_Line.SINGLE_BOLD    \u2192  \"single_bold\" 
      {fp.ins_space(10)}  fp.Style_Line.SINGLE_HEAVY   \u2192  \"single_heavy\"
      {fp.ins_space(10)}  fp.Style_Line.DOUBLE         \u2192  \"double\"
      {fp.ins_space(10)}  fp.Style_Line.DASH           \u2192  \"dash\"      
      {fp.ins_space(10)}  fp.Style_Line.SQR_BRACKETS   \u2192  \"sq_brackets\"
      {fp.ins_space(10)}  fp.Style_Line.NONE           \u2192  \"none\"
   '''
   print(message)


#---------------------------------------------------------------------------------------------------
# Cursor Class                                                                                     -
#---------------------------------------------------------------------------------------------------
def Cursor_Class():
   blue_msg.print_fancy_message("Cursor Class")
   JumpTo_Method()
   Jumpxy_Method()
   MoveTo_Method()
   Movexy_Method()  
   message = "This methods only works with the actual size of the terminal, if you try\
 to go beyond thesize of the terminal, it may not work properly."
   white_msg.print_fancy_note("Note:", message)

   message = "\u25CF Reference \u2192  02_Cursor_Move_Class.py"
   dark_green_msg.print_fancy_message(message)
   
def JumpTo_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[1][0])
   message = f'''
   
      jumpTo method is used to jump rows or columns for the cursor in the terminal.
      The difference between move and jump is that move return the code, while jump
      execute the code.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_space(10)}  crs = fp.Cursor()
      {fp.ins_space(10)}  crs.jumpTo(qty=2,  direction = fp.Move.DOWN);        print("I am down")
      {fp.ins_space(10)}  crs.jumpTo(qty=20, direction = "right");             print("I am right")
      {fp.ins_space(10)}  crs.jumpTo(1, fp.Move.UP);                           print("I am up")
      {fp.ins_space(10)}  crs.jumpTo(5, "down");                               print("GoodBye...!")

   '''
   print(message)


def Jumpxy_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[2][0])
   message = f'''
   
      jumpxy method is used to jump to especific coordinate on the terminal.
      The difference between jumpxy and movexy is that jumpxy execute the code
      while the movexy returns the code.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_space(10)}  crs = fp.Cursor()
      {fp.ins_space(10)}  crs.jumpToxy(0,0);     print("*** Start Here ***")
      {fp.ins_space(10)}  crs.jumpToxy(20, 5);   print("GoodBye...!")      

   '''
   print(message)


def MoveTo_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[3][0])
   message = f'''
   
      moveTo method is used to move rows or columns for the cursor in the terminal.
      The difference between move and jump is that move return the code, while jump
      execute the code.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_space(10)}  crs = fp.Cursor()
      '''
   
   message2 = '''                  print(f"{crs.moveTo(15,"right")} First One",  end="")

                  print(f"{crs.moveTo(15,"right")} Second One", end="")
            
                  print(f"{crs.moveTo(qty=20,direction="left")} Hello")
   
   '''
   print(message)
   print(message2)

def Movexy_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[4][0])
   message = f'''
   
      movexy method is used to move to especific coordinate on the terminal.
      The difference between jumpxy and movexy is that jumpxy execute the code
      while the movexy returns the code.


      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_space(10)}  crs = fp.Cursor()
   '''
   message2 = '''                  print(f"{crs.movexy(15,40)}hello again")

      '''
   print(message)
   print(message2)



#---------------------------------------------------------------------------------------------------
# FontStyle Class                                                                                  -
#---------------------------------------------------------------------------------------------------
def FontStyle_Class():
   blue_msg.print_fancy_message("FontStyle Class")
   font_style_options = [["bold","bg","fg","italic"],
                        ["dim","underline","blinking","inverse"],
                        ["hidden","strike","indent","next_line"]]
   lst.msg_title = "FontStyle Class Variables"
   lst.bg_header = -1; lst.fg_header = -1
   lst.print_fancy_format(font_style_options,fp.Line_Style.NONE)

   Start_Stop_Style_Method()
   Print_Style_Method()
   Reset_Style_Method()

   message = "\u25CF Reference \u2192  03_FontStyle_Class.py"
   dark_green_msg.print_fancy_message(message)

def Start_Stop_Style_Method():
   message = classes_methods_fancyprint[1][1] + " and "+ classes_methods_fancyprint[2][1]
   green_msg.print_fancy_message(message)
   message = f'''
   
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_space(10)}  fs = fp.FontStyle
      {fp.ins_space(10)}  fs.bg = 14
      {fp.ins_space(10)}  print(fs.start_style() + " FontStyle Class " + fs.stop_style())

   '''
   print(message)

def Print_Style_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[3][1])

   message = f'''
   
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_space(10)}  fs = fp.FontStyle
      {fp.ins_space(10)}  fs.bg = 14
      {fp.ins_space(10)}  fs.print_style(" FontStyle Class ")
      {fp.ins_space(10)}  print("  Normal Font...!")

   '''
   print(message)

def Reset_Style_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[4][1])
   message = f'''
   
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_space(10)}  fs = fp.FontStyle
      {fp.ins_space(10)}  fs.bg = 14
      {fp.ins_space(10)}  fs.print("  FontStyle Class ")
      {fp.ins_space(10)}  fs.reset_style()
      {fp.ins_space(10)}  fs.print("  Default Values ")

   '''
   print(message)



#---------------------------------------------------------------------------------------------------
# FancyMessage Class                                                                               -
#---------------------------------------------------------------------------------------------------
def FancyMessage_Class():
   blue_msg.print_fancy_message("FancyMessage Class")
   simple_msg.adj_top_margin = 1;                   simple_msg.align_title = fp.Align.JUSTIFY
   simple_msg.bg_title = 231;                       simple_msg.fg_title = 0
   simple_msg.msg_title = " Note Default Values "; simple_msg.bold_title = True

   # Note Default Values
   default_values = ["note_msg = \" Note: \" "]
   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)

   
   # Title Default Values
   simple_msg.msg_title = " Title Default Values "
   default_values = [["align_title = Align.LEFT"]]   
   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)


   # Body Default Values
   simple_msg.msg_title = " Body Default Values "
   default_values = [["bg_body     = 4",     "strike_body = False",    "underline_body = False"],
                  ["fg_body     = 231",   "italic_body = False",    "blinking_body  = False"],
                  ["dim_body    = False", "hidden_body = False",    "inverse_body   = False"],
                  ["bold_body   = False", "body_msg    = Body Msg", "help_lines     = False"]]
   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)


   # Footnote Default Values
   simple_msg.msg_title = " Footnote Default Values "
   default_values = ["align_footnote = Align.RIGHT"]

   # Indentation and Lines Default Values
   simple_msg.msg_title = " Default Indent and Line Values "
   default_values = [["left_indent  = 2 ", "bottom_lines = 1", "length = Length_bg.ALL_ROW"],
                       ["right_indent = 2",  "top_lines    = 1", "adj_bg_lines_to_right_indent  = False "],
                       [" "," ",                                 "adj_bg_msg_to_space_available = False"]] 
   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)
    
   
   
   



   Print_Fancy_Message_Method()
   Print_Fancy_Note_Method()
   Reset_Fancy_Message_Method()
   Reset_Fancy_Note_Method()

def Print_Fancy_Message_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[1][2])

def Print_Fancy_Note_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[2][2])

def Reset_Fancy_Message_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[3][2])

def Reset_Fancy_Note_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[4][2])

#----------------------------------------------------------------------------------------------------------------------------------------------
# Start the Documentation for fancyprint Module                                                                                               -
#----------------------------------------------------------------------------------------------------------------------------------------------
fp.clear()
ctrl = 0
cmdl_argv = []
for argv in sys.argv:
   cmdl_argv.append(argv.lower())

flag_screen_functions = False; flag_internal_functions=False; flag_help_classes = False
flag_cursor = False;           flag_font_style = False;   flag_fancy_message = False
flag_fancy_format = False;     flag_draw = False

if (len(cmdl_argv) == 1):
   Welcome_Message()

elif ("all" in cmdl_argv):  
   Screen_Functions()
   Internal_Functions()
   Help_Classes()
   Cursor_Class()
   FontStyle_Class()
   FancyMessage_Class()

   

else:
   blue_msg.bold = True
   blue_msg.italic = True
   for fun in cmdl_argv:
      if ("screen_functions" in fun):     Screen_Functions();    flag_screen_functions = True
      elif ("internal_functions" in fun): Internal_Functions();  flag_internal_functions = True
      elif ("help_classes" in fun):       Help_Classes();        flag_help_classes = True
      elif ("cursor" in fun):             Cursor_Class();        flag_cursor = True
      elif ("fontstyle" in fun):          FontStyle_Class();     flag_font_style = True
      elif ("fancymessage" in fun):       FancyMessage_Class();  flag_fancy_message = True
      

      elif ("clean" == fun and flag_screen_functions == False):           Clean_Function()
      elif ("clear" == fun and flag_screen_functions == False):           Clear_Function()
      elif ("erase" == fun and flag_screen_functions == False):           Erase_Function()
      elif ("dimensions" == fun and flag_screen_functions == False):      Dimensions_Function()
      elif ("resize" == fun and flag_screen_functions == False):          Resize_Function()
      

      elif ("ins_space" == fun and flag_internal_functions == False):     Ins_Space_Function()
      elif ("ins_newline" == fun and flag_internal_functions == False):   Ins_Newline_Function()
      elif ("terminal_bell" == fun and flag_internal_functions == False): Terminal_Bell_Function()
      elif ("ansi_colors" == fun and flag_internal_functions == False):   Ansi_Color_Function()


      elif ("move" == fun and flag_help_classes == False):                Move_Class()
      elif ("align" == fun and flag_help_classes == False):               Align_Class()
      elif ("layout" == fun and flag_help_classes == False):              Layout_Class()
      elif ("length" == fun and flag_help_classes == False):              Length_Class()
      elif ("style_line" == fun and flag_help_classes == False):          Style_Line_Class()

      
      elif ("jumpto" == fun and flag_cursor == False):                    JumpTo_Method()
      elif ("jumpxy" == fun and flag_cursor == False):                    Jumpxy_Method()
      elif ("moveto" == fun and flag_cursor == False):                    MoveTo_Method()
      elif ("movexy" == fun and flag_cursor == False):                    Movexy_Method()


      elif ("start_style" == fun and flag_font_style == False):           Start_Stop_Style_Method()
      elif ("stop_style"  == fun and flag_font_style == False):           Start_Stop_Style_Method()
      elif ("print_style" == fun and flag_font_style == False):           Print_Style_Method()
      elif ("reset_style" == fun and flag_font_style == False):           Reset_Style_Method()


      elif ("print_fancy_message" == fun  and flag_fancy_message == False):  Print_Fancy_Message_Method()
      elif ("print_fancy_note"    == fun  and flag_fancy_message == False):  Print_Fancy_Note_Method()
      elif ("reset_fancy_message" == fun  and flag_fancy_message == False):  Reset_Fancy_Message_Method()
      elif ("reset_fancy_note"    == fun  and flag_fancy_message == False):  Reset_Fancy_Note_Method() 


      else: pass
         

fp.ins_newline(3)
input("  Press Enter to Continue: ")
adj_screen(nrows, ncols)

# fp.clear()
# fp.clean()green_msg.print_fancy_message(screen_funs[5][0])