# ==============================================================================
#      _____  ______  ______ _      ______ _____ _______ _____ ____  _   _  _____ 
#     |  __ \|  ____|  ____| |    |  ____/ ____|__   __|_   _/ __ \| \ | |/ ____|
#     | |__) | |__  | |__  | |    | |__ | |       | |    | || |  | |  \| | (___  
#     |  _  /|  __| |  __| | |    |  __|| |       | |    | || |  | | . ` |\___ \ 
#     | | \ \| |____| |    | |____| |___| |____   | |   _| || |__| | |\  |____) |
#     |_|  \_\______|_|    |______|______\_____|  |_|  |_____\____/|_| \_|_____/ 
#                                                                                 
#                      -- a minimalist ambient anti-game --
# ==============================================================================

import pygame
import sys
import random
import time
import math
from pypresence import Presence

# ------------------------------------------------------------------------------
# discord integration
# ------------------------------------------------------------------------------
client_id = "YOUR_CLIENT_ID_HERE" 

try:
    rpc = Presence(client_id)
    rpc.connect()
    print("[system] synchronized with the void (discord rpc connected).")
except Exception:
    print("[system] discord client untraced. proceeding in isolation.")
    rpc = None


# ------------------------------------------------------------------------------
# core application setup
# ------------------------------------------------------------------------------
pygame.init()
pygame.mixer.init()

width, height = 1280, 720
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("reflections")
clock = pygame.time.Clock()


# ------------------------------------------------------------------------------
# soundtrack initialization
# ------------------------------------------------------------------------------
try:
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=-1) 
    print("[audio] 'song.mp3' successfully bound to eternity.")
except pygame.error as e:
    print(f"[audio] the silence remains unbroken. (could not load 'song.mp3'): {e}")


# ------------------------------------------------------------------------------
# simulation objects: the drifting frost
# ------------------------------------------------------------------------------
snowflakes = []

def breathe_life_into_flake(initial_scatter=False):
    return {
        "x": random.uniform(0, width),
        "y": random.uniform(0, height) if initial_scatter else random.uniform(-20, -5),
        "radius": random.uniform(1.2, 3.8),
        "speed_y": random.uniform(0.6, 1.8),
        "sway_amplitude": random.uniform(0.3, 1.2),
        "sway_speed": random.uniform(1.2, 2.8),
        "phase": random.uniform(0, 100)
    }

for _ in range(140):
    snowflakes.append(breathe_life_into_flake(initial_scatter=True))


# ------------------------------------------------------------------------------
# dynamic pool of reflections (easter eggs & glitches)
# ------------------------------------------------------------------------------
text_pool = [
    "there is nothing to do here.",
    "in the quiet space between actions, we find ourselves.",
    "when stanley came to a set of two open doors, he entered the door on his left.",
    "f i n d   m e .",
    "where we dropping?",
    "just monika.",
    "the end is never the end is never the end is never...",
    "why are you still looking at the screen?",
    "error: file 'characters/yuri.chr' not found.",
    "it is dangerous to go alone! take nothing.",
    "would you kindly do absolutely nothing?",
    "the cake was a lie, but this void is real.",
    "did you think there was an ending? this isnt ddlc, no matter how many references there are.",
    "my head hurts",
    "100% empty!",
    "help",
    "how are u today",
    "GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD",
    "if you are reading this. you are able to read.",
    "btw u can customize the song",
    "every day i imagine a future where i can be with you",
    "boo",
    "this was made because of a boy. a boy who broke a girls heart."
]


# ------------------------------------------------------------------------------
# text state engine (fading & cycling)
# ------------------------------------------------------------------------------
text_state = {
    "current_text": random.choice(text_pool),
    "alpha": 0.0,            # current visibility (0 to 255)
    "mode": "FADE_IN",       # FADE_IN, HOLD, FADE_OUT
    "timer": time.time(),    # keeps track of milestones
    "hold_duration": 4.0     # how many seconds a line stays readable
}

def process_text_lifecycle(current_time):
    fade_speed = 3.5  # controls how quickly lines phase into existence

    if text_state["mode"] == "FADE_IN":
        text_state["alpha"] += fade_speed
        if text_state["alpha"] >= 160:  # maximum text brightness cap
            text_state["alpha"] = 160
            text_state["mode"] = "HOLD"
            text_state["timer"] = current_time

    elif text_state["mode"] == "HOLD":
        if current_time - text_state["timer"] >= text_state["hold_duration"]:
            text_state["mode"] = "FADE_OUT"

    elif text_state["mode"] == "FADE_OUT":
        text_state["alpha"] -= fade_speed
        if text_state["alpha"] <= 0:
            text_state["alpha"] = 0
            
            next_text = random.choice(text_pool)
            while next_text == text_state["current_text"]:
                next_text = random.choice(text_pool)
                
            text_state["current_text"] = next_text
            text_state["mode"] = "FADE_IN"
            text_state["hold_duration"] = random.uniform(3.0, 7.0)


# ------------------------------------------------------------------------------
# temporal tracking & discord telemetry
# ------------------------------------------------------------------------------
start_time = int(time.time())
last_rpc_update = time.time()

def mirror_state_to_discord(seconds_idle):
    if not rpc:
        return
    
    minutes = seconds_idle // 60
    status_text = "just started doing nothing" if minutes == 0 else f"successfully idle for {minutes}m"

    try:
        rpc.update(
            state=status_text,
            details="contemplating existence...",
            start=start_time,
            large_image="void", 
            large_text="reflections"
        )
    except Exception:
        pass

mirror_state_to_discord(0)


# ------------------------------------------------------------------------------
# the infinite loop
# ------------------------------------------------------------------------------
is_present = True

while is_present:
    current_time = time.time()
    elapsed_seconds = int(current_time - start_time)

    # --- a. translating interaction ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_present = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_present = False

    # --- b. clearing the canvas ---
    screen.fill((0, 0, 0))

    # --- c. persisting the drift ---
    for flake in snowflakes[:]:
        flake["y"] += flake["speed_y"]
        flake["x"] += math.sin(current_time * flake["sway_speed"] + flake["phase"]) * flake["sway_amplitude"]

        if flake["y"] > height + 10:
            snowflakes.remove(flake)
            snowflakes.append(breathe_life_into_flake(initial_scatter=False))
            continue

        pygame.draw.circle(
            screen, 
            (245, 245, 250), 
            (int(flake["x"]), int(flake["y"])), 
            int(flake["radius"])
        )

    # --- d. processing & rendering the text ---
    process_text_lifecycle(current_time)
    
    font = pygame.font.SysFont("cambria", 26)
    text_surface = font.render(text_state["current_text"], True, (210, 215, 220))
    text_surface.set_alpha(int(text_state["alpha"]))
    
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

    # --- e. rate-limiting digital speech ---
    if current_time - last_rpc_update >= 15:
        mirror_state_to_discord(elapsed_seconds)
        last_rpc_update = current_time

    clock.tick(fps)


# ------------------------------------------------------------------------------
# absolution: disconnecting the script
# ------------------------------------------------------------------------------
print("[system] goodbye.")
if rpc:
    try:
        rpc.close()
    except Exception:
        pass

pygame.quit()
sys.exit()
