import tkinter as tk
import webbrowser

def open_links():
    # Get all text from the text box
    links = text_box.get("1.0", tk.END).strip().split("\n")

    for link in links:
        link = link.strip()
        if link:
            webbrowser.open_new_tab(link)

# Create main window
root = tk.Tk()
root.title("Bug Hunting - Bulk Link Opener")
root.geometry("600x400")

# Label
label = tk.Label(root, text="Paste URLs (one per line):", font=("Arial", 12))
label.pack(pady=5)

# Big text box
text_box = tk.Text(root, height=15, width=70)
text_box.pack(pady=10)

# Button
open_button = tk.Button(
    root,
    text="Open Links",
    command=open_links,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
open_button.pack(pady=10)

# Run the app
root.mainloop()
