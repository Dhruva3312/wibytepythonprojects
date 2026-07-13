import tkinter as tk


def calculate():
    start = start_station.get()
    stop = stop_station.get()

    # Check if the user forgot to select a station
    if not start or not stop:
        farelabel.configure(
            text="Please select both a start and stop station first.", fg="red"
        )
        return
    else:
        farelabel.configure(fg="black")

    # Figure out which lines the stations belong to
    if start in stn_sL:
        start_line = stn_sL
    else:
        start_line = stn_pL

    if stop in stn_sL:
        stop_line = stn_sL
    else:
        stop_line = stn_pL

    if start_line is stop_line:
        # Stations are on the same line
        n_stops = abs(start_line.index(start) - start_line.index(stop))
    else:
        # Stations are on different lines, routing through WiByte
        n_stops = start_line.index(start) - start_line.index("WiByte")
        n_stops = abs(n_stops) + abs(
            stop_line.index("WiByte") - stop_line.index(stop)
        )

    fare = n_stops * 20
    farelabel.configure(text="Your total fare is INR " + str(fare))


window = tk.Tk()
window.title("WiByte Metro Map")
window.configure(bg="Darkgreen")
window.geometry("600x650+10+0")

c = tk.Canvas(window, width=550, height=500)
c.pack()

stn_sL = [
    "SpriteLand",
    "GoNGlide",
    "Costumes",
    "Broadcast",
    "WiByte",
    "Cloning",
    "MyBlocks",
]
stn_pL = [
    "EscapeChar",
    "WhileLoop",
    "WiByte",
    "IfElifElse",
    "Range",
    "Dictionary",
    "TurtlePark",
]

r_stn = 6


# Clean function to draw the lines with square stations instead of circles
def draw_metro_line(stn_list, init_pos, step, label_offset, clr):
    x_s = init_pos[0]
    y_s = init_pos[1]
    x_step = step[0]
    y_step = step[1]

    for stn in stn_list:
        if stn != stn_list[-1]:
            c.create_line(x_s, y_s, x_s + x_step, y_s + y_step, fill=clr)

        # Drawing squares instead of circles
        c.create_rectangle(
            x_s - r_stn,
            y_s - r_stn,
            x_s + r_stn,
            y_s + r_stn,
            fill=clr,
            outline=clr,
        )
        c.create_text(
            x_s + label_offset[0],
            y_s + label_offset[1],
            text=stn,
            fill=clr,
            font=("Helvetica 6 bold"),
        )

        x_s = x_s + x_step
        y_s = y_s + y_step


# Render the two metro lines
draw_metro_line(stn_sL, [50, 200], [70, 0], [0, 30], "DarkOrange")
draw_metro_line(stn_pL, [330, 40], [0, 70], [35, 0], "blue")

# Filter out the interchange station for the selection lists
all_stations = stn_sL + stn_pL
all_stations.remove("WiByte")

c.create_text(30, 250, text="Start")
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x=30, y=270)

c.create_text(240, 250, text="Stop")
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(window, stop_station, *all_stations)
drop_stop.place(x=240, y=270)

button = tk.Button(text="Calculate Fare", command=calculate)
button.pack(pady=10)

farelabel = tk.Label(window, text="Select your route", font=("Helvetica 12 bold"))
farelabel.pack(pady=10)

tk.mainloop()