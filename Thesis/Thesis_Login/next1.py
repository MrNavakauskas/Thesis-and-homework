import tkinter as tk
from tkinter import messagebox
import next2


class FirstWin:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg="light blue", height=600, width=800)  # background
        self.frame.pack(fill="both", expand="true", anchor="c")
        master.geometry("600x300")
        master.resizable(0, 0)
        master.title("Course work is dedicated to the lecturer Mr.Stasius Čivilius")
        master.iconbitmap(r'1.ico')

        frame_login = tk.Frame(master, bg="light grey", relief="groove", bd=2)  # login details / buttons...
        frame_login.place(rely=0.30, relx=0.17, height=120, width=400)
        title_style = {"font": ("Trebuchet MS Bold", 12), "background": "light grey"}
        label_title = tk.Label(frame_login, title_style, text="Login")
        label_title.grid(row=0, column=1, columnspan=1)
        text_styles = {"font": ("Verdana", 8), "background": "light grey", "foreground": "black"}
        label_user = tk.Label(frame_login, text_styles, text="           User name:")
        label_user.grid(row=1, column=0)
        label_pw = tk.Label(frame_login, text_styles, text="           Password:")
        label_pw.grid(row=2, column=0, sticky="E")

        entry_user = tk.Entry(frame_login, width=35)
        entry_user.grid(row=1, column=1)
        entry_pw = tk.Entry(frame_login, width=35, show="*")
        entry_pw.grid(row=2, column=1)

        btn_login = tk.Button(frame_login, text="Log in", width=10, command=lambda: log_in())
        btn_login.place(rely=0.68, relx=0.36)
        btn_signup = tk.Button(frame_login, text="Sign up",  width=10, command=lambda: SignUp())
        btn_signup.place(rely=0.68, relx=0.60)

        def log_in():
            username = entry_user.get()
            password = entry_pw.get()
            confirmation = confirm(username, password)
            if confirmation:
                tk.messagebox.showinfo("You have successfully logged in",
                                       "It's nice to see you back  {}".format(username))
                next2.SqlLangas(master)
#                gsql.root.mainloop()

            else:
                tk.messagebox.showerror("Please pay attention!",
                                        "The username or password you entered is incorrect")

        def confirm(username, password):
            # Checks the text file for a username/password combination.
            try:
                with open("psw.txt", "r") as psw:
                    for line in psw:
                        line = line.split(",")
                        if line[1] == username and line[3] == password:
                            return True
                    return False
            except FileNotFoundError:
                print("Please register first ")
                return False

        # def registruotis():
        #     e.SqlLangas(master)


class SignUp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        main_frame = tk.Frame(self, bg="light grey", height=150, width=250)
        main_frame.pack(fill="both", expand="true")
        self.geometry("300x110")
        self.resizable(0, 0)
        self.title("Registration")
        text_styles = {"font": ("Verdana", 8), "background": "light grey", "foreground": "black"}

        label_user = tk.Label(main_frame, text_styles)
        label_user.grid(row=1, column=0)
        label_user = tk.Label(main_frame, text_styles, text="New username:")
        label_user.grid(row=2, column=0, sticky="E")
        label_pw = tk.Label(main_frame, text_styles, text=" New password:")
        label_pw.grid(row=3, column=0)

        entry_user = tk.Entry(main_frame, width=25)
        entry_user.grid(row=2, column=1)
        entry_pw = tk.Entry(main_frame, width=25)
        entry_pw.grid(row=3, column=1)

        btn_create = tk.Button(main_frame, text="Create an account",  width=15, command=lambda: create())
        btn_create.place(rely=0.65, relx=0.50)

        def create():
            user = entry_user.get()
            pw = entry_pw.get()
            confirmation = confirm(user)
            if not confirmation:
                tk.messagebox.showerror("Mistake", "Such a user already exists ")
            else:
                if len(pw) > 3:
                    psw = open("psw.txt", "a")
                    psw.write(f"Name,{user},Password,{pw},\n")
                    psw.close()
                    tk.messagebox.showinfo("Information", "Your account has been saved ")
                    SignUp.destroy(self)

                else:
                    tk.messagebox.showerror("Mistake",
                                            "Password must be at least 4 characters long")

        def confirm(username):
            # Checks the text file for a username/password combination.
            try:
                with open("psw.txt", "r") as psw:
                    for line in psw:
                        line = line.split(",")
                        if line[1] == username:
                            return False
                return True
            except FileNotFoundError:
                return True


def main():
    root = tk.Tk()
    app = FirstWin(root)
    root.mainloop()


if __name__ == "__main__":
    main()
