import cv2
import time
import random
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Game():
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
    # function to get user choice using camera and trained models 
    def get_prediction(self):
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
            # using the highest probability model from image at 5 seconds since function call, 
            # return either rock, paper or scissors
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

    def get_computer_choice(self):
        options = ['Rock', 'Paper', 'Scissors']
        return random.choice(options)

    def get_winner(self, computer_choice, user_choice):
        self.user_wins = 0
        self.computer_wins = 0
        self.computer_choice = computer_choice
        self.user_choice = user_choice

        def user_win():
            print("You won!")
            self.user_wins = self.user_wins + 1

        def computer_win():
            print('You lose!')
            self.computer_wins = self.computer_wins + 1

        # user winning outcomes
        if self.computer_choice == "Rock" and self.user_choice == "Paper":
            user_win()
        elif self.computer_choice == "Scissors" and self.user_choice == "Rock":
            user_win()
        elif self.computer_choice == "Paper" and self.user_choice == "Scissors":
            user_win()
        # computer winning scenarios
        elif self.computer_choice == "Rock" and self.user_choice == "Scissors":
            computer_win()
        elif self.computer_choice == "Scissors" and self.user_choice == "Paper":
            computer_win()
        elif self.computer_choice == "Paper" and self.user_choice == "Rock":
            computer_win()
        # tieing scenarios
        else:
            print("It is a tie!")
        
        def play(self):
            computer_choice = self.get_computer_choice()
            user_choice = self.get_prediction()
            self.get_winner(computer_choice, user_choice)

instance = Game()

while instance.computer_wins < 3 and instance.user_wins < 3:
    instance.play()
