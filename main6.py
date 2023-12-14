import tkinter as tk
from tkinter import filedialog

class PolicyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Complaint Master")
        self.master.geometry("250x150")

        # Screen 1
        self.screen1_frame = tk.Frame(master, bg="lightblue")
        tk.Button(self.screen1_frame, text="CREATE A NEW POLICY", command=self.show_screen2, bg="grey", fg="black").pack(pady=20)
        tk.Button(self.screen1_frame, text="START WITH EXISTING POLICY", command=self.show_screen3, bg="grey", fg="black").pack(pady=20)

        # Screen 2
        self.screen2_frame = tk.Frame(master, bg="lightblue")
        tk.Checkbutton(self.screen2_frame, text="A", bg="lightblue").pack()
        tk.Checkbutton(self.screen2_frame, text="B", bg="lightblue").pack()
        tk.Checkbutton(self.screen2_frame, text="C", bg="lightblue").pack()
        tk.Button(self.screen2_frame, text="NEXT", command=self.show_screen5, bg="green", fg="white").pack(pady=15)

        # Screen 3
        self.screen3_frame = tk.Frame(master, bg="lightblue")
        tk.Button(self.screen3_frame, text="UPLOAD FILES", command=self.upload_files, bg="grey", fg="black").pack(pady=30)
        tk.Button(self.screen3_frame, text="Continue", command=self.show_screen4, bg="green", fg="white").pack(pady=15)

        # Screen 4
        self.screen4_frame = tk.Frame(master, bg="lightblue")
        tk.Button(self.screen4_frame, text="REVIEW CHANGE", command=self.show_screen6, bg="grey", fg="black").pack(pady=50)
        tk.Button(self.screen4_frame, text="Next", command=self.show_screen6, bg="green", fg="white").pack(pady=15)

        # Screen 5
        self.screen5_frame = tk.Frame(master, bg="lightblue")
        tk.Button(self.screen5_frame, text="A", bg="grey", fg="white").pack(pady=20)
        tk.Button(self.screen5_frame, text="Harden Now", command=self.show_screen6, bg="grey", fg="black").pack(pady=20)

        # Screen 6
        self.screen6_frame = tk.Frame(master, bg="lightblue")
        tk.Button(self.screen6_frame, text="EXECUTION", command=self.show_screen7, bg="green", fg="white").pack(pady=40)

        # Screen 7
        self.screen7_frame = tk.Frame(master, bg="lightblue")
        tk.Label(self.screen7_frame, text="REPORT", bg="lightblue", fg="black").pack(pady=30)
        tk.Button(self.screen7_frame, text="Exit", command=self.master.destroy, bg="green", fg="white").pack()

        # Show initial screen
        self.show_screen1()

    def show_screen1(self):
        self.hide_all_screens()
        self.screen1_frame.pack(fill="both", expand=True)

    def show_screen2(self):
        self.hide_all_screens()
        self.screen2_frame.pack(fill="both", expand=True)

    def show_screen3(self):
        self.hide_all_screens()
        self.screen3_frame.pack(fill="both", expand=True)

    def show_screen4(self):
        self.hide_all_screens()
        self.screen4_frame.pack(fill="both", expand=True)

    def show_screen5(self):
        self.hide_all_screens()
        self.screen5_frame.pack(fill="both", expand=True)

    def show_screen6(self):
        self.hide_all_screens()
        self.screen6_frame.pack(fill="both", expand=True)

    def show_screen7(self):
        self.hide_all_screens()
        self.screen7_frame.pack(fill="both", expand=True)

    def hide_all_screens(self):
        screens = [self.screen1_frame, self.screen2_frame, self.screen3_frame,
                   self.screen4_frame, self.screen5_frame, self.screen6_frame, self.screen7_frame]
        for screen in screens:
            screen.pack_forget()

    def upload_files(self):
        file_path = filedialog.askopenfilename()
        print("Uploaded file:", file_path)

def main():
    root = tk.Tk()
    app = PolicyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
