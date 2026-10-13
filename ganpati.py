import math

root = tk.Tk()
root.title("Ganpati Bappa Morya")
root.geometry("600x650")
root.configure(bg="#fff3d6")

canvas = tk.Canvas(
    root,
    width=600,
    height=650,
    bg="#fff3d6",
    highlightthickness=0
)
canvas.pack()

canvas.create_text(
    300, 40,
    text="Ganpati Bappa Morya",
    font=("Arial", 28, "bold"),
    fill="#d35400"
)

# Head
canvas.create_oval(
    180, 100, 420, 340,
    fill="#f4a261",
    outline="#c85a00",
    width=5
)

# Ears
canvas.create_oval(
    110, 160, 220, 300,
    fill="#f4a261",
    outline="#c85a00",
    width=4
)

canvas.create_oval(
    380, 160, 490, 300,
    fill="#f4a261",
    outline="#c85a00",
    width=4
)

# Eyes
canvas.create_oval(235, 175, 265, 205, fill="black")
canvas.create_oval(335, 175, 365, 205, fill="black")

# Trunk
canvas.create_arc(
    250, 190, 350, 320,
    start=270,
    extent=180,
    style=tk.ARC,
    width=18,
    outline="#c85a00"
)

# Body
canvas.create_oval(
    170, 320, 430, 570,
    fill="#f4a261",
    outline="#c85a00",
    width=5
)

# Modak
canvas.create_oval(
    250, 440, 350, 500,
    fill="#e9c46a",
    outline="#a66a00",
    width=3
)

# Diya
canvas.create_oval(
    220, 570, 380, 610,
    fill="#e76f51",
    outline="#9d3d25",
    width=3
)

# Flame
flame = canvas.create_oval(
    285, 515, 315, 575,
    fill="orange",
    outline="red",
    width=2
)

angle = 0

def animate():
    global angle

    x = 300 + math.sin(angle) * 8

    canvas.coords(
        flame,
        x - 15, 515,
        x + 15, 575
    )

    angle += 0.15

    root.after(50, animate)

animate()

root.mainloop()