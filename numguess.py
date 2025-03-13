import random
import tkinter as tk
from tkinter import messagebox


class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#2C3E50")

        self.label_title = tk.Label(root, text="Guess the Number!", font=("Arial", 18, "bold"), fg="white",
                                    bg="#2C3E50")
        self.label_title.pack(pady=10)

        self.label_instruction = tk.Label(root, text="Enter a number greater than 9:", font=("Arial", 12), fg="white",
                                          bg="#2C3E50")
        self.label_instruction.pack()

        self.entry_top_range = tk.Entry(root, font=("Arial", 14), justify="center", bg="#ECF0F1")
        self.entry_top_range.pack(pady=5)

        self.btn_start = tk.Button(root, text="Start Game", font=("Arial", 14, "bold"), bg="#27AE60", fg="white",
                                   command=self.start_game)
        self.btn_start.pack(pady=5)

        self.label_guess = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#2C3E50")
        self.label_guess.pack()

        self.entry_guess = tk.Entry(root, font=("Arial", 14), justify="center", bg="#ECF0F1")
        self.entry_guess.pack(pady=5)

        self.btn_guess = tk.Button(root, text="Submit Guess", font=("Arial", 14, "bold"), bg="#2980B9", fg="white",
                                   command=self.check_guess)
        self.btn_guess.pack(pady=5)

        self.random_number = None
        self.top_of_range = None

    def start_game(self):
        top_of_range = self.entry_top_range.get()
        if top_of_range.isdigit():
            top_of_range = int(top_of_range)
            if top_of_range <= 9:
                messagebox.showwarning("Invalid Input", "Please enter a number greater than 9.")
                return
            self.top_of_range = top_of_range
            self.random_number = random.randint(1, top_of_range)
            self.label_guess.config(text=f"Guess a number between 1 and {top_of_range}:")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def check_guess(self):
        guess = self.entry_guess.get()
        if guess.isdigit():
            guess = int(guess)
            if guess > self.random_number:
                messagebox.showinfo("Too High!", "Your guess is too high. Try again!")
            elif guess < self.random_number:
                messagebox.showinfo("Too Low!", "Your guess is too low. Try again!")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the correct number: {guess}")
                self.ask_play_again()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.entry_top_range.delete(0, tk.END)
            self.entry_guess.delete(0, tk.END)
            self.label_guess.config(text="")
        else:
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()