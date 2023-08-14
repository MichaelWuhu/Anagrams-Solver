import tkinter as tk
from tkinter.messagebox import showerror

# used to validate user input (6 letters returns true, anything else returns popup box)
def valid_entry(input_letters):
    only_alpha = []
    
    for i in input_letters:
        if i.isalpha():
            only_alpha.append(i)
    
    if len(only_alpha) == 6:
        return True

    showerror("Error", "Please enter 6 letters")
    return False

# solve function used to solve
def solve(input_letters):
    if not (len(input_letters) == 6):
        return 
    
    # with open('TempWords.txt', 'r') as f: # opening the text file of words
    with open('Words.txt', 'r') as f:
        content = f.read() # reads all the words and puts them into variable 'words'
        words = content.split('\n')
        # print(words)
        
    letters = [char.upper() for char in input_letters] # takes in input of array of letters and makes them all capitalized
    solved_words = []
        
        
    for word in words: # loops through all of the words in the file 'Words.txt'
        duplicate_letters = letters[:] # create a duplicate of the inputted array of letters to remove values that have been found in the word already
        isValid = True # keeps track of if the word is valid... if not then skips to next word
        # print(word)
        for letter in word: # loops through the letters
            if not (letter in letters):
                isValid = False
                break # breaks out of the loop since if one letter doesn't match, the rest don't need to be checkedd
            
        if isValid:
            for letter in word:
                if letter in duplicate_letters:
                    duplicate_letters.remove(letter) # remove the letter from the duplicate_letters array to make sure that letters won't be repeated
                    # print('duplicate_letters:', duplicate_letters)
                    # print('solved words:', solved_words)
                else:
                    isValid = False # toggles isValid to False if the word isn't an answer
       
        if isValid: # only appends the answer if it is valid
            solved_words.append(word)
    
    filtered_solved_words = solved_words[:]
    for word in solved_words: # used to remove 2 letter words 
        if len(word) <= 2:
            filtered_solved_words.remove(word)   

    return filtered_solved_words
    

def onClick():
    input_text = user_input.get()
    if valid_entry(input_text):
        answer = solve(input_text)
        answer = ', '.join(answer)
        # print(answer)    
        canvas.delete("all")  # Clear previous text on canvas
        canvas.create_text(300, 100, text=answer, fill="black", font=('Helvetica 10 bold'), width=550, anchor="center")
        # user_input.delete(0, tk.END)  # Clear the input textbox

# THESE ARE FOR TESTING 'SOLVE' FUNCTION
# letters = ['a','b','c','d','e','f']
# print(solve(letters))

root = tk.Tk()
root.title("Anagrams Solver")
root.geometry("700x600")  # Increase the window size

form_frame = tk.Frame(root)
form_frame.pack(padx=20, pady=20)

title_label = tk.Label(form_frame, text="Anagrams Solver", font=("Helvetica", 48, "bold", "underline"))  # Increase font size
title_label.grid(row=0, column=0, sticky="w", columnspan=2)

user_input_label = tk.Label(form_frame, text="Enter 6 letters:", font=("Helvetica", 24))  # Increase font size
user_input_label.grid(row=1, column=0, sticky="w")  

user_input = tk.Entry(form_frame, highlightthickness=2, highlightbackground="black", font=("Helvetica", 24))  # Increase font size and highlight thickness
user_input.grid(row=1, column=1, padx=(20, 0), pady=20)

solve_button = tk.Button(form_frame, text="Solve!", width=20, font=("Helvetica", 24), highlightthickness=2, highlightbackground="black", command=onClick)  # Increase font size and highlight thickness
solve_button.grid(row=2, column=0, columnspan=2)

canvas = tk.Canvas(form_frame, bd=5, bg="lightgray", width=600, height=200)  # Increase canvas size
canvas.grid(row=3, column=0, columnspan=2, pady=(50, 0))

canvas.create_text(300, 80, text='', fill="black", font=('Helvetica 10 bold'))

root.mainloop()
