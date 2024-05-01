import tkinter as tk
from startpage import StartPage

def main():
    # Run App
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
