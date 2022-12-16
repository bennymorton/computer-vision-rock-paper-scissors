import cv2
import time
import random
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

user_wins = 0
computer_wins = 0

def get_prediction():
    start_time = round(time.time())

    def close_camera():
        cap.release()
        cv2.destroyAllWindows()

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        if round(time.time()) == start_time + 5:
            user_choice = np.argmax(prediction)
            if user_choice == 0:
                close_camera()
                return "Rock"
            if user_choice == 1:
                close_camera()
                return "Paper"
            if user_choice == 2:
                close_camera()
                return "Scissors"
        
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object and
    # Destroy all the windows
    close_camera()

def get_winner(computer_choice, user_choice):
    def user_win():
        print("You won!")
        user_wins += 1

    def computer_win():
        print('You lose!')
        computer_wins += 1

    # user winning outcomes
    if computer_choice == "Rock" and user_choice == "Paper":
        user_win()
    elif computer_choice == "Scissors" and user_choice == "Rock":
        user_win()
    elif computer_choice == "Paper" and user_choice == "Scissors":
        user_win()
    # computer winning scenarios
    elif computer_choice == "Rock" and user_choice == "Scissors":
        computer_win()
    elif computer_choice == "Scissors" and user_choice == "Paper":
        computer_win()
    elif computer_choice == "Paper" and user_choice == "Rock":
        computer_win()
    # tieing scenarios
    else:
        print("It is a tie!")

def get_computer_choice():
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)

def play():
    computer_choice = get_computer_choice()
    user_choice = get_prediction()
    get_winner(computer_choice, user_choice)

while computer_wins <= 3 and user_wins <= 3:
    play()