# Code was written by clotpoledollophead

import tkinter as tk
# the messagebox module is not automatically imported with tkinter
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
import random
import pygame
import time

timer_running = False  # Flag to indicate if the timer is running
start_time = 0  # Variable to store the start time
elapsed_time = 0  # Variable to store the elapsed time

# Initializes the Pygame modules and prepares the library for use in program
pygame.init()

# Define the quiz title
quiz_title = "Hogwarts House Quiz" # Title in the middle of the screen

# List of sound effects used
sound_effects = [
                 "music\\Gryffindor.mp3", #0
                 "music\\Hufflepuff.mp3", #1
                 "music\\Ravenclaw.mp3", #2
                 "music\\Slytherin.mp3", #3
                 "music\\Soaring over Hogwarts.mp3", #4
                 "music\\Azkaban.mp3",  #5
                 "music\\hat_Gryffindor.mp3",  #6
                 "music\\hat_Hufflepuff.mp3",  #7
                 "music\\hat_Ravenclaw.mp3",  #8
                 "music\\hat_Slytherin.mp3",  #9
                 "music\\hat_Azkaban.mp3" #10
                 ]

# Define the quiz questions
questions = [
    "Are you ready to start the quiz?", 
    "Q1. Do you like to interact with others?",
    "Q2. What do you think are the most important qualities of an individual?",
    "Q3. If you could travel through time, what would you do?",
    "Q4. Which mythical creature would you choose to be?",
    "Q5. When learning new knowledge, what methods do you prefer??", 
    "Q6. If you are lost, what would you do?", 
    "Q7. Where would you sit if you could sit anywhere in the Great Hall at Hogwarts?", 
    "Q8. How would you decorate your Hogwarts dorm room?", 
    "Q9. What is your favorite spell?", 
    "Q10. If you were a wizard, what kind of magic would you most likely use?", 
    "Q11. Choose your favorite Wizarding World location: ", 
    "Q12. Choose your favorite celebration of the year: ", 
    "Q13. Choose your favorite Hogwarts architecture: ", 
    "Q14. What's your favorite magical activity?", 
    "Q15. Choose your favorite Hogwarts student club?", 
    "Q16. Choose your favorite magical game: ",
    "Q17. Choose your favorite magical item: ", 
    "Q18. What social activity do you enjoy participating in?", 
    "Q19. In teamwork, what is your usual role?", 
    "Q20. What is your preferred movie genre?", 
    "Q21. In team discussions, you usually:"
]

# Define the choices for each question: always in the order GRYFFINDOR, HUFFLEPUFF, RAVENCLAW, SLYTHERIN
choices = [
    [["Ready to face the challenges and unravel my true nature!", ""], #q0
     ["Ready to put my dedication to the test and embrace who I truly am.", ""],
     ["Ready to unravel the mysteries of my own personality through this quiz.", ""],
     ["Ready to seize every opportunity for self-discovery and personal growth.", ""]],
    [["Yes, I love to interact with others", ""], #q1
     ["I like to interact with a small amount of people", ""],
     ["Depends, sometimes I like to be alone", ""],
     ["No, I don’t like to interact with others", ""]],
    [["Courage and adventurous spirit", ""], #q2
     ["Honesty and loyalty", ""],
     ["Intelligence and creativity", ""],
     ["Ambition and desire", ""]],
    [["Go back in time to fix your mistakes", ""], #q3
     ["Go to the future to look at your fate", ""],
     ["Go back in time to study history and culture", ""],
     ["Go to the future to see how the world develops", ""]],
    [["Phoenix", "img:pics\\phoenix.png"], #q4
     ["Thunderbird", "img:pics\\thunderbird.png"],
     ["Dragon", "img:pics\\dragon.png"],
     ["Werewolf", "img:pics\\werewolf.png"]],
    [["Learning from teachers and experts", ""], #q5
     ["Learning from books", ""],
     ["Learning by doing and experimenting", ""],
     ["Learning from experience", ""]],
    [["Listen to your instincts", ""], # q6
     ["Try to find help", ""],
     ["Find a place to stop and think about what to do next", ""],
     ["Try to find a map or other guides", ""]],
    [["The high table", ""], #q7
     ["The last row", ""],
     ["The left of the hall", ""],
     ["The right of the hall", ""]],
    [["Candles and fireplace", "img:pics\\8-G.webp"], #q8
     ["Crystal clear glass and brass utensils", "img:pics\\8-H.jpg"],
     ["Bronze decorations and dark red candlesticks", "img:pics\\8-R.jpg"],
     ["Dark red curtains and wallpaper", "img:pics\\8-S.jpeg"]],
    [["Expelliarmus", "img:pics\\9-G.jpg"], #q9
     ["Expecto Patronum", "img:pics\\9-H.jpg"],
     ["Wingardium Leviosa", "img:pics\\9-R.jpg"],
     ["Sectumsempra", "img:pics\\9-S.jpg"]],
    [["Charms magic", ""], #q10
     ["Summoning magic", ""],
     ["Transfiguration magic", ""],
     ["Potions", ""]], 
    [["Forbidden Forest", "img:pics\\11-G.jpeg"], #q11
     ["Lakeside", "img:pics\\11-H.jpg"], 
     ["Library", "img:pics\\11-R.webp"], 
     ["Fountain Square", "img:pics\\11-S.webp"]], 
    [["Halloween", ""], #q12
     ["Christmas", ""], 
     ["Summer Solstice", ""], 
     ["Spring Equinox", ""]], 
    [["Tower", "img:pics\\13-G.jpeg"], #q13
     ["Greenhouse", "img:pics\\13-H.jpg"], 
     ["Library", "img:pics\\13-R.jpeg"], 
     ["Dungeon", "img:pics\\13-S.webp"]], 
    [["Quidditch", "img:pics\\14-G.jpeg"], #q14
     ["Yule Ball", "img:pics\\14-H.webp"], 
     ["Wizard's Duel", "img:pics\\14-R(duel).jpg"], 
     ["Summoner's Court", "img:pics\\14-S(Summoner's Court).webp"]], 
    [["Duelling Club", "img:pics\\15-G(duelling club).webp"], #q15
     ["Slug Club", "img:pics\\15-H(slug club dinner).jpeg"], 
     ["Gobstones Club", "img:pics\\15-R(Gobstones).webp"], 
     ["Inquistorial Squad", "img:pics\\15-S(InquisitorialSquad).webp"]], 
    [["Quidditch", "img:pics\\16-G(quidditch).jpg"], #q16
     ["Gobstones", "img:pics\\16-H(gobstones).jpg"], 
     ["Wizard Skittles", "img:pics\\16-R(Wizard_Skittles).webp"], 
     ["Exploding Snap", "img:pics\\16-S(Exploding snap).webp"]], 
    [["Mirror of Erised", "img:pics\\17-G(Mirror of Erised).jpeg"], #q17
     ["Time-Turner", "img:pics\\17-H (Time Turner).webp"], 
     ["Invisibility Cloak", "img:pics\\17-R(invisibility cloak).jpeg"], 
     ["Pensieve", "img:pics\\17-S(pensieve).jpeg"]], 
    [["Sports competitions or games", ""], #q18
     ["Parties or gatherings", ""], 
     ["Academic conferences or workshops", ""], 
     ["Book clubs or cultured events", ""]], 
    [["Leader or competitor", ""], #q19
     ["Team connector or meditator", ""], 
     ["Problem solver or explorer", ""], 
     ["Analyst or strategist", ""]], 
    [["Action and adventure", ""], #q20
     ["Romantic comedy", ""], 
     ["Science fiction and fantasy", ""], 
     ["Documentary", ""]], 
    [["Express your opinions and provide clear suggestions", ""], #q21
     ["Listen to others' opinions and help resolve conflicts", ""], 
     ["Offer new perspectives and explore different options", ""], 
     ["Analyze the discussion content and provide logical insights", ""]]
]

# Define the house descriptions
house_descriptions = {
    "Gryffindor": "\nYou belong in Gryffindor,\nWhere dwell the brave at heart,\nTheir daring, nerve, and chivalry\nSet Gryffindors apart.",
    "Hufflepuff": "\nYou belong in Hufflepuff,\nWhere they are just and loyal,\nThose patient Hufflepuffs are true\nAnd unafraid of toil.",
    "Ravenclaw": "\nYou're a wise old Ravenclaw,\nif you've a ready mind,\nWhere those of wit and learning,\nWill always find their kind.",
    "Slytherin": "\nIn Slytherin you belong\nYou'll make your real friends,\nThose cunning folks use any means\nTo achieve their ends."
}

# Define the list to store the user's answers
answers = []

def start_timer():
    global timer_running, start_time
    if not timer_running:
        timer_running = True
        start_time = time.time()

def stop_timer():
    global timer_running, elapsed_time
    if timer_running:
        timer_running = False
        elapsed_time = time.time() - start_time

# Function to stop playing background music
def stop_music():
    pygame.mixer.music.stop()

# Function to play background music + sound effects
def play_music(track_number):
    pygame.mixer.music.load(sound_effects[track_number])  # Set path to music file
    if track_number >= 6:
        pygame.mixer.music.play(0)  # Set 0 to play the music once; to NOT loop
        time.sleep(4) # Delay to play the mp3 file
    else:
        pygame.mixer.music.play(-1)  # Set -1 to loop the music indefinitely

# Function to update the progress bar
def update_progress(current_question):
    progress = int((current_question / (len(questions))) * 100)  # Calculate progress percentage
    progress_bar["value"] = progress

# Function to handle submitting the quiz
def submit_quiz():
    
    # Create the result label
    result_label = tk.Label(canvas, text="", bg="white")
    result_label.pack()
    
    calculate_house(house_counts)
    result = get_max_house(house_counts)
    name = name_entry.get()  # Get the value entered in the name entry field
    
    stop_timer()
    if elapsed_time <= 16:
        house_descriptions[result] = "\nWelcome to Azkaban,\nA place of darkness and despair,\nWhere hope is but a flickering flame,\nAnd souls are left in disrepair;\n"
    
    result_label.config(text=f"{name}, {house_descriptions[result]}", font=("High Tower Text", 20, "bold"), pady=20)
    
    stop_music()
    
    # House colors for results
    house_colors = ["#ac0001", "#f0c75c", "#222f5b", "#2a623d", "#2B2C3B"]
    
    # House crests
    house_image_paths = ["pics\\House-Gryffindor.webp",
                   "pics\\House-Hufflepuff.webp",
                   "pics\\House-Ravenclaw.webp",
                   "pics\\House-Slytherin.webp", 
                   "pics\\Azkaban.webp"
                   ]
    
    if elapsed_time <= 16:
        result_house_color = house_colors[4]
        result_image_path = house_image_paths[4]
        play_music(10)
        play_music(5)
    else:
        if result == "Gryffindor":
            result_house_color = house_colors[0]
            result_image_path = house_image_paths[0]
            play_music(6)
            play_music(0)
        elif result == "Hufflepuff":
            result_house_color = house_colors[1]
            result_image_path = house_image_paths[1]
            play_music(7)
            play_music(1)
        elif result == "Ravenclaw":
            result_house_color = house_colors[2]
            result_image_path = house_image_paths[2]
            play_music(8)
            play_music(2)
        elif result == "Slytherin":
            result_house_color = house_colors[3]
            result_image_path = house_image_paths[3]
            play_music(9)
            play_music(3)
        
    result_label.config(bg=result_house_color)
    
    result_image = Image.open(result_image_path)
    result_image = result_image.resize((200, 200), Image.Resampling.LANCZOS)
    result_image = ImageTk.PhotoImage(result_image)
    result_image_label = tk.Label(canvas, image=result_image)
    result_image_label.image = result_image
    result_image_label.pack()
    
    question_label.pack_forget()


# Initialize the house_counts dictionary
house_counts = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

# Function to calculate the Hogwarts House based on answers
def calculate_house(house_counts):
    # Loop over each question and see if there are equivalent answers
    for i in range(len(answers)):
        answer = answers[i]
        question_choices = choices[i]
        
        for j in range(len(question_choices)):
            if answer == question_choices[j][0]:
                # converts the keys into a list, and gets the key at index j in the list
                house_name = list(house_counts.keys())[j]
                house_counts[house_name] += 1
                break

def get_max_house(house_counts):

    # Determine the house with the highest count
    max_count = max(house_counts.values())
    max_houses = []
    for house, count in house_counts.items():
        if count == max_count:
            max_houses.append(house)

    # If there's a tie, choose randomly. Otherwise, return the house with the highest count.
    if len(max_houses) > 1:
        return random.choice(max_houses)
    else:
        return max_houses[0]

# Function to handle selecting a choice
def select_choice(question_index, choice_index):
    answer_description = choices[question_index][choice_index][0]
    answers.append(answer_description)

    # Clear the current question
    question_label.config(text="")
    for i in range(len(choice_buttons)):
        choice_buttons[i].destroy()

    # Move to the next question or finish the quiz
    if question_index + 1 < len(questions):
        ask_question(question_index + 1)
    else:
        submit_quiz()

# Function to ask a question
def ask_question(question_index):
    
    # Display the name label and entry field only on the first question
    if question_index == 0:
        name_label.pack()
        name_entry.pack()

    if question_index == 1:
        name_label.pack_forget()
        name_entry.pack_forget()
    
    # Display the question
    question_label.config(text=questions[question_index], font=("High Tower Text", 30))
    question_label.pack(pady=20)

    # Display the choices
    for i in range(len(choices[question_index])):        
        choice = choices[question_index][i]
        description = choice[0]
        image_path = choice[1]

        # Update the progress bar based on the current index
        update_progress(question_index)  # Update progress
        
        choice_button = tk.Button(canvas, text=description, font=("High Tower Text", 16),
                                  command=lambda i=i: select_choice(question_index, i), width=400)
        # The command parameter expects a function or method that should be executed when the button is clicked.
        # In this case, a lambda function is used as the command.
        
        # This is the argument passed to the lambda function.
        # It assigns the current value of i to the lambda function's i parameter.
        # This helps in capturing the current value of i at the time of creating the button,
        # ensuring that each button has a unique value for i. 
        
        # Tkinter handles the detection of the button click event,
        # and the lambda function serves as a convenient way to specify the command or code
        # that should be executed when the button is clicked.

        if image_path.startswith("img:") and len(image_path) > 4:
            image = Image.open(image_path[4:])
            # Resize the image with Resampling.LANCZOS
            # LANCZOS is a type of resampling filter that is commonly used for image resizing.
            # It uses a windowed sinc function to interpolate the pixel values when resizing the image. 
            image = image.resize((75, 75), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            choice_button.config(image=photo, compound=tk.TOP)
            choice_button.image = photo

        choice_button.pack(pady=10, padx=20)
        choice_buttons.append(choice_button)

# Quit the quiz
def quit_quiz():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit the quiz?"):
        root.destroy()

# Create the main Tkinter window
root = tk.Tk()
root.title("Hogwarts House Quiz") # Title that sppears on the left upper side of the window
root.geometry("1920x1080")

# Load the background image
background_image = Image.open("Hogwarts Legacy   2_13_2023 10_01_58 PM.png")

# Create a copy of the image with transparency
background_with_transparency = background_image.copy()

# Adjust the alpha channel to make the image more transparent
alpha_value = 128  # 0 (fully transparent) to 255 (fully opaque)
background_with_transparency.putalpha(alpha_value)

# Create a Tkinter-compatible photo image from the image with transparency
background_photo = ImageTk.PhotoImage(background_with_transparency)

# Create a Canvas widget to display the background image
canvas = tk.Canvas(root, width=background_with_transparency.width, height=background_with_transparency.height)
canvas.pack(fill=tk.BOTH, expand=True)

# Display the background image on the Canvas
canvas.create_image(0, 0, image=background_photo, anchor=tk.NW)

# Create the quiz title label (in the middle of the screen)
title_label = tk.Label(canvas, text=quiz_title, font=("Felix Titling", 50, "bold"), bg="white")
title_label.pack()

# Create and display progressbar
progress_bar = Progressbar(canvas, length=750, mode="determinate")
progress_bar.pack()

# Create the question label
question_label = tk.Label(canvas, text="", bg="white")
question_label.pack()

# Create a label and entry field for the user's name
name_label = tk.Label(canvas, text="Enter your name:", bg="white", font=("High Tower Text", 15))
name_label.pack()
name_entry = tk.Entry(canvas, font=("High Tower Text", 20))
name_entry.pack()

# Create a list to store the choice buttons
choice_buttons = []

# Start playing background music
play_music(4)

# Start the timer
start_timer()

# Start the quiz
ask_question(0)

# Create a quit button
quit_button = tk.Button(canvas, text="Quit", command=quit_quiz)
quit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
