import tkinter as tk
import random
import pygame


def generate_key():

    try:
        input_word = input_entry.get().upper()
        
        if not input_word or len(input_word) != 6 or not input_word.isalpha():
            key_display.config(state=tk.NORMAL)
            key_display.delete(1.0, tk.END)
            key_display.config(state=tk.DISABLED)
            error_label.config(text="Error: Input must be a 6-letter word.")
            return None
        
        first_block = ''.join(random.sample(input_word, 3))

        second_block = ''.join([str((ord(c) - ord('A') + 1) % 10) for c in input_word])

        third_block = ''.join(random.sample(input_word, 3))


        key = f"{first_block}-{second_block}-{third_block}"
        
        error_label.config(text="")
        return key
    except ValueError as e:
        error_label.config(text=f"Error: {e}")
        return None


def on_generate_click():

    key = generate_key()
    
    if key:
        key_display.config(state=tk.NORMAL)
        key_display.delete(1.0, tk.END)
        key_display.insert(tk.END, key)
        key_display.config(state=tk.DISABLED)


        animate_color_change(key_display, "black", "red", 100)


def play_music():

    pygame.mixer.init()
    pygame.mixer.music.load("dark_souls_3_theme.mp3")
    pygame.mixer.music.play(-1)


def animate_color_change(widget, start_color, end_color, steps, step=0):

    r1, g1, b1 = widget.winfo_rgb(start_color)
    r2, g2, b2 = widget.winfo_rgb(end_color)
    
    r = int(r1 + (r2 - r1) * step / steps)
    g = int(g1 + (g2 - g1) * step / steps)
    b = int(b1 + (b2 - b1) * step / steps)
    
    widget.config(fg=f"#{r:04x}{g:04x}{b:04x}")
    
    if step < steps:
        widget.after(50, animate_color_change, widget, start_color, end_color, steps, step + 1)


#GUI
root = tk.Tk()
root.title("Dark Souls 3 Key generator")

try:
    img = tk.PhotoImage(file="dark_souls_3.png")
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except FileNotFoundError:
    print("Error: dark_souls_3.png not found. Please place the image in the same directory.")
    root.destroy()
    exit()


input_label = tk.Label(root, text="Enter a 6-letter word:", bg="black", fg="white", font=("system", 10))
input_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

input_entry = tk.Entry(root, width=25, font=("system", 12))
input_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

generate_button = tk.Button(root, text="Generate Key", command=on_generate_click, bg="black", fg="white", font=("system", 10))
generate_button.place(relx=0.5, rely=0.42, anchor=tk.CENTER)

error_label = tk.Label(root, text="", bg="black", fg="red", font=("system", 8))
error_label.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

key_label = tk.Label(root, text="Generated Key:", bg="black", fg="white", font=("system", 10))
key_label.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

key_display = tk.Text(root, width=25, height=1, font=("system", 12), state=tk.DISABLED)
key_display.place(relx=0.5, rely=0.58, anchor=tk.CENTER)


root.geometry("1280x720")
root.resizable(False, False)


if __name__ == "__main__":
    play_music()
    root.mainloop()