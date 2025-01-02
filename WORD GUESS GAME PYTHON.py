import tkinter as tk
import random

class WordGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Guessing Game")
        self.master.configure(bg="#add8e6")  # Set background color to light blue
        self.words = {"fruit": ["apple", "banana", "orange", "grape", "kiwi","pineapple", "strawberry", "watermelon", "blueberry", "peach","mango", "pear", "cherry", "plum", "apricot",
                                "papaya", "melon", "lemon", "lime", "coconut"],
                      "programming": ["python", "java", "javascript", "cplusplus", "html", "css", "php"],
                      "animal": ["elephant", "lion", "tiger", "giraffe", "zebra","hippopotamus", "rhinoceros", "crocodile", "kangaroo", "koala","panda", "cheetah", "wolf", "bear", "monkey",
                                 "camel",
                                 "fox", "deer", "rabbit", "penguin"]}
        self.category = random.choice(list(self.words.keys()))
        self.secret_word = random.choice(self.words[self.category])
        self.guesses_left = 3 
        self.create_widgets()

    def create_widgets(self):
        self.label_heading = tk.Label(self.master, text="** Word Guessing Game **", font=("Georgia", 32, "bold"), bg="#add8e6")  
        self.label_heading.pack(pady=10)

        self.label_word = tk.Label(self.master, text="Guess the word !!", font=("Verdana", 24), bg="#add8e6",fg="red")  
        self.label_word.pack(pady=5)

        self.entry = tk.Entry(self.master, font=("Arial", 16),width=20)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="SUBMIT", font=("Times New Roman", 14), command=self.check_guess,height=1,width=8)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text=f"You have {self.guesses_left} guesses left", font=("Verdana", 14), bg="#add8e6")  
        self.result_label.pack(pady=5)

        self.hint_button = tk.Button(self.master, text="Hint", font=("Arial", 12), command=self.show_hint,height=1,width=6)
        self.hint_button.pack(pady=5)

        self.restart_button = tk.Button(self.master, text="RESTART", font=("Times New Roman", 18), command=self.restart_game,height=2,width=8)
        self.restart_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().lower()
        if guess == self.secret_word:
            self.result_label.config(text=f"Congratulations! You guessed the word '{self.secret_word}' correctly!", fg="green")
            self.submit_button.config(state="disabled")
            self.entry.config(state="disabled")
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                self.result_label.config(text=f"Sorry, you're out of guesses. The word was '{self.secret_word}'.", fg="red")
                self.submit_button.config(state="disabled")
                self.entry.config(state="disabled")
            else:
                self.result_label.config(text=f"Sorry, that's not the word. You have {self.guesses_left} guesses left.", fg="black")

    def show_hint(self):
        hint = f"Category: {self.category.capitalize()}, Length: {len(self.secret_word)}"
        self.result_label.config(text=hint, fg="blue")

    def restart_game(self):
        self.category = random.choice(list(self.words.keys()))
        self.secret_word = random.choice(self.words[self.category])
        self.guesses_left = 3
        self.label_word.config(text=f"Guess the word", fg="black")
        self.result_label.config(text=f"You have {self.guesses_left} guesses left", fg="black")
        self.submit_button.config(state="normal")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    game = WordGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
