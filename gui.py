import tkinter as tk
from tkinter import ttk
from tkinter import Canvas

class MelodyCraftGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MelodyCraft")

        self.create_widgets()

    def create_widgets(self):
        # Canvas für die Notenlinien und für das Zeichnen der Kurve
        self.canvas = Canvas(self.master, width=1000, height=200, bg='white')

        self.draw_staff()
        self.draw_measures()

        self.canvas.grid(row=0, column=0, columnspan=14, padx=10, pady=10)

        # Label und Entry für den Focal Point
        ttk.Label(self.master, text="Focal Point:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.focal_point_entry = ttk.Entry(self.master)
        self.focal_point_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Label und Entry für den ARC
        ttk.Label(self.master, text="ARC:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.arc_entry = ttk.Entry(self.master)
        self.arc_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Dropdown for the musical key
        ttk.Label(self.master, text="Key:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.key_var = tk.StringVar()
        self.key_combobox = ttk.Combobox(self.master, textvariable=self.key_var, values=[
            "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F", "C", "G", "D", "A", "E", "B", "F#", "C#"])
        self.key_combobox.set("C")  # Default key
        self.key_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Dropdown for the mode
        self.mode_var = tk.StringVar()
        self.mode_combobox = ttk.Combobox(self.master, textvariable=self.mode_var, values=["Major", "Minor"])
        self.mode_combobox.set("Major")  # Default mode
        self.mode_combobox.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        # Button zum Generieren der Melodie
        ttk.Button(self.master, text="Melodie generieren", command=self.generate_melody).grid(row=10, column=0, columnspan=2, pady=10)

        # Binden Sie die Mausereignisse an die Canvas
        self.canvas.bind("<B1-Motion>", self.draw_curve)

        # Initialisieren Sie die Kurvenpunkte
        self.curve_points = []

    def draw_staff(self):
        # Zeichnen Sie die fünf Linien des Notensystems
        for i in range(5):
            y = 30 + i * 30
            self.canvas.create_line(50, y, 950, y, fill='black')

    def draw_measures(self):
        # Zeichnen Sie die Taktstriche in das Notensystem
        for i in range(6):
            x = 50 + i * 100
            self.canvas.create_line(x, 30, x, 150, fill='blue')

    def draw_curve(self, event):
        x, y = event.x, event.y
        self.curve_points.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='black')

    def generate_melody(self):
        # Hier können Sie die Kurvenpunkte verwenden, um die Melodie zu generieren
        # Rufen Sie Ihre Melodiegenerator-Funktion mit den Kurvenpunkten als Parameter auf.
        
        focal_point = self.focal_point_entry.get()
        arc_txt = self.arc_entry.get()

        print(f"Focal Point: {focal_point}")
        print(f"ARC:: {arc_txt}")
        print("Kurvenpunkte:", self.curve_points)

def main():
    root = tk.Tk()
    app = MelodyCraftGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
