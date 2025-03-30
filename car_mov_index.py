import pygame
import cv2
import mediapipe as mp
import numpy as np

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Gesture Car Control")

# Load Car Image
car_img = pygame.image.load(r"D:\1 RAVI STARTS\ML\png-transparent-car-game-racing.png")  # Ensure correct path
car_img = pygame.transform.scale(car_img, (100, 60))
car_x, car_y = WIDTH // 2, HEIGHT // 2
car_angle = 0
CAR_WIDTH, CAR_HEIGHT = car_img.get_size()

# Speed Variable
speed = 4

# Initialize OpenCV and Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

def get_index_finger_direction(hand_landmarks):
    """ Determine the pointing direction of the index finger """
    index_tip = hand_landmarks.landmark[8]  # Tip of the index finger
    index_base = hand_landmarks.landmark[5]  # Base of the index finger
    
    dx = index_tip.x - index_base.x
    dy = index_tip.y - index_base.y
    
    if abs(dx) > abs(dy):  # More horizontal movement
        if dx > 0:
            return "Right"
        else:
            return "Left"
    else:  # More vertical movement
        if dy > 0:
            return "Down"
        else:
            return "Up"

running = True
while running:
    screen.fill((50, 50, 50))
    
    # Capture frame
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            direction = get_index_finger_direction(hand_landmarks)
            
            if direction == "Up" and car_y > 0:
                car_y -= speed  # Move up
                car_angle = 90
            elif direction == "Down" and car_y < HEIGHT - CAR_HEIGHT:
                car_y += speed  # Move down
                car_angle = 270
            elif direction == "Left" and car_x > 0:
                car_x -= speed  # Move left
                car_angle = 180
            elif direction == "Right" and car_x < WIDTH - CAR_WIDTH:
                car_x += speed  # Move right
                car_angle = 0
    
    # Draw Car
    rotated_car = pygame.transform.rotate(car_img, car_angle)
    rect = rotated_car.get_rect(center=(car_x, car_y))
    screen.blit(rotated_car, rect.topleft)
    
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()
