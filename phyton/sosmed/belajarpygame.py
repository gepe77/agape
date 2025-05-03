import pygame
import socket
import json

pygame.init()

# Server settings
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 52028
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

# Screen settings
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Social Media")

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GRAY = (180, 180, 180)

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# User system
current_user = ""
posts = []

def send_request(data):
    client.send(json.dumps(data).encode())
    response = json.loads(client.recv(4096).decode())
    return response

def sign_up(username):
    global current_user
    response = send_request({"action": "signup", "username": username})
    if "message" in response:
        current_user = username

def post_message(text):
    if current_user:
        send_request({"action": "post", "username": current_user, "text": text})
        get_posts()

def like_post(index):
    send_request({"action": "like", "post_index": index})
    get_posts()

def get_posts():
    global posts
    posts = send_request({"action": "get_posts"})

def draw_posts():
    y_offset = 120
    for i, post in enumerate(posts):
        pygame.draw.rect(screen, GRAY, (50, y_offset, 400, 90), border_radius=10)
        draw_text(post["username"], 22, BLUE, 60, y_offset + 10)
        draw_text(post["text"], 20, BLACK, 60, y_offset + 30)
        draw_text(f"❤ {post['likes']}", 18, RED, 380, y_offset + 60)
        y_offset += 110

def draw_input_box():
    pygame.draw.rect(screen, LIGHT_GRAY, (50, HEIGHT - 60, 400, 40), border_radius=10)
    draw_text(input_text, 24, BLACK, 60, HEIGHT - 50)

input_active = False
input_text = ""
signing_up = True
username_input = ""

running = True

while running:
    screen.fill(WHITE)
    
    if signing_up:
        draw_text("Sign Up - Enter Username", 28, BLUE, 100, 300)
        draw_text(username_input, 28, BLACK, 100, 350)
    else:
        draw_text(f"Logged in as {current_user}", 20, BLUE, 50, 50)
        draw_text("Pygame Social Media", 32, BLUE, 120, 20)
        draw_posts()
        if input_active:
            draw_input_box()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif signing_up:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sign_up(username_input)
                    signing_up = False
                    get_posts()
                elif event.key == pygame.K_BACKSPACE:
                    username_input = username_input[:-1]
                else:
                    username_input += event.unicode
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                y_offset = 120
                for i in range(len(posts)):
                    if 50 <= x <= 450 and y_offset <= y <= y_offset + 90:
                        like_post(i)
                    y_offset += 110
                if 50 <= x <= 450 and HEIGHT - 60 <= y <= HEIGHT - 20:
                    input_active = True
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    if input_text:
                        post_message(input_text)
                    input_text = ""
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
    
    pygame.display.flip()

client.close()
pygame.quit()