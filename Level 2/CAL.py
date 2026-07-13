import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")
window.resizable(0, 0)

def press_num(num):
    text_in_box = entr_label.cget('text')
    
    # Feature 2: If the screen just has '0', replace it instead of appending (e.g., '7' instead of '07')
    if text_in_box == '0':
        if num == '.':
            entr_label.configure(text='0.')
        else:
            entr_label.configure(text=str(num))
    else:
        # Prevent double decimals in the same number entry
        if num == '.' and '.' in text_in_box:
            return
        entr_label.configure(text=text_in_box + str(num))

def press_op(operator):
    text_in_box = entr_label.cget('text')
    text_in_expr = expr_label.cget('text')
    
    # If they just finished a calculation, let them build onto the result
    if '=' in text_in_expr:
        text_in_expr = ''
        
    expr_label.configure(text=text_in_expr + text_in_box + " " + operator + " ")
    entr_label.configure(text='0') # Reset to 0 for the next number entry

def press_C():
    expr_label.configure(text='')
    entr_label.configure(text='0') # Default back to a clean 0

def press_eq():
    text_in_box = entr_label.cget('text')
    text_in_expr = expr_label.cget('text')

    if '=' in text_in_expr:
        text_in_expr = ''

    full_expression = text_in_expr + text_in_box
    expr_label.configure(text=full_expression + ' = ')

    try:
        result = eval(full_expression)
        
        # Clean up clean floats (e.g., display 5 instead of 5.0)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        entr_label.configure(text=str(result))
        
    # Feature 8 & Humanized Messages: Let the user know exactly what went wrong in plain English
    except ZeroDivisionError:
        entr_label.configure(text="Can't divide by zero!")
    except SyntaxError:
        entr_label.configure(text="Math error!")
    except Exception:
        entr_label.configure(text="Oops, invalid input!")

# --- GUI Setup ---
expr_label = tk.Label(window, text = '', bg = 'grey', width = 36, height= 3, borderwidth = 3, relief = 'ridge', anchor = tk.E)
expr_label.grid(column = 0, row = 0, columnspan = 5)

# Feature 2: Starting the main display at '0'
entr_label = tk.Label(window, text = '0', bg = 'grey', font = ('Arial bold', 15), width = 22, height= 3, borderwidth = 3, relief = 'ridge', anchor = tk.E)
entr_label.grid(column = 0, row = 1, columnspan = 5)

# --- Buttons Layout ---
tk.Button(text = ' 7 ', fg = 'black', bg = 'grey', command= lambda: press_num(7)).grid(row=2, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 8 ', fg = 'black', bg = 'grey', command= lambda: press_num(8)).grid(row=2, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 9 ', fg = 'black', bg = 'grey', command= lambda: press_num(9)).grid(row=2, column = 2, sticky= tk.NSEW)
tk.Button(text = ' / ', fg = 'black', bg = 'grey', command= lambda: press_op('/')).grid(row=2, column = 3, sticky= tk.NSEW)
tk.Button(text = ' C ', fg = 'black', bg = 'grey', command = press_C).grid(row=2, column = 4, rowspan= 2, sticky= tk.NSEW)

tk.Button(text = ' 4 ', fg = 'black', bg = 'grey', command= lambda: press_num(4)).grid(row=3, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 5 ', fg = 'black', bg = 'grey', command= lambda: press_num(5)).grid(row=3, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 6 ', fg = 'black', bg = 'grey', command= lambda: press_num(6)).grid(row=3, column = 2, sticky= tk.NSEW)
tk.Button(text = ' * ', fg = 'black', bg = 'grey', command= lambda: press_op('*')).grid(row=3, column = 3, sticky= tk.NSEW)

tk.Button(text = ' 1 ', fg = 'black', bg = 'grey', command= lambda: press_num(1)).grid(row=4, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 2 ', fg = 'black', bg = 'grey', command= lambda: press_num(2)).grid(row=4, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 3 ', fg = 'black', bg = 'grey', command= lambda: press_num(3)).grid(row=4, column = 2, sticky= tk.NSEW)
tk.Button(text = ' - ', fg = 'black', bg = 'grey', command= lambda: press_op('-')).grid(row=4, column = 3, sticky= tk.NSEW)
tk.Button(text = ' = ', fg = 'black', bg = 'grey', command= press_eq).grid(row=4, column = 4, rowspan= 2, sticky= tk.NSEW)

tk.Button(text = ' 0 ', fg = 'black', bg = 'grey', command= lambda: press_num(0)).grid(row=5, column = 0, columnspan = 2, sticky= tk.NSEW)
tk.Button(text = ' . ', fg = 'black', bg = 'grey', command= lambda: press_num('.')).grid(row=5, column = 2, sticky= tk.NSEW)
tk.Button(text = ' + ', fg = 'black', bg = 'grey', command= lambda: press_op('+')).grid(row=5, column = 3, sticky= tk.NSEW)

tk.mainloop()