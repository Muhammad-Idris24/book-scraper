from gui.app import ScraperApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()