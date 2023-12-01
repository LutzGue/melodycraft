import tkinter as tk
from tkinter import ttk

class EditableTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editable Table App")

        self.create_widgets()

    def create_widgets(self):
        # Create a ttk.Treeview as a table
        self.tree = ttk.Treeview(self.root, columns=("Name", "Age", "Country"), show="headings")

        # Set column headings
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Country", text="Country")

        # Set column widths
        self.tree.column("Name", width=100)
        self.tree.column("Age", width=50)
        self.tree.column("Country", width=100)

        # Example content in the table
        self.tree.insert("", "end", values=("John Doe", 30, "USA"))
        self.tree.insert("", "end", values=("Jane Smith", 25, "Canada"))
        self.tree.insert("", "end", values=("Bob Johnson", 40, "UK"))

        # Bind double-click event to the table
        self.tree.bind("<Double-1>", self.on_item_double_click)

        # Display the table
        self.tree.grid(row=0, column=0, padx=10, pady=10)

    def on_item_double_click(self, event):
        # Double-click on an item to start editing
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        col_index = int(column.split("#")[-1]) - 1
        cell_value = self.tree.item(item, "values")[col_index]

        # Create an Entry widget for editing
        entry = tk.Entry(self.tree, justify="center")
        entry.insert(0, cell_value)

        # Set the Entry as the current editor
        self.tree.item(item, text="", values=(), tags=("editing",))
        self.tree.editing_entry = entry
        self.tree.editing_id = item
        self.tree.editing_col = col_index

        # Place the Entry over the selected cell
        bbox = self.tree.bbox(item, column)
        entry.place(x=bbox[0], y=bbox[1], width=bbox[2]-bbox[0], height=bbox[3]-bbox[1])
        entry.focus_set()

        # Bind the Entry to the edit_save function
        entry.bind("<Return>", lambda e: self.edit_save(entry))

    def edit_save(self, entry):
        # Save the edited value and clean up
        new_value = entry.get()
        item = self.tree.editing_id
        col_index = self.tree.editing_col

        # Get the existing values
        values = list(self.tree.item(item, "values"))

        # Ensure values list is long enough
        while len(values) <= col_index:
            values.append("")

        # Update the value at the specified index
        values[col_index] = new_value

        # Update the tree with the new values
        self.tree.item(item, values=values, tags=())

        # Destroy the Entry widget
        entry.destroy()

def main():
    root = tk.Tk()
    app = EditableTableApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
