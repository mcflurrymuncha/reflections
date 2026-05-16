# ==============================================================================
#      _____  ______  ______ _      ______ _____ _______ _____ ____  _   _  _____ 
#     |  __ \|  ____|  ____| |    |  ____/ ____|__   __|_   _/ __ \| \ | |/ ____|
#     | |__) | |__  | |__  | |    | |__ | |       | |    | || |  | |  \| | (___  
#     |  _  /|  __| |  __| | |    |  __|| |       | |    | || |  | | . ` |\___ \ 
#     | | \ \| |____| |    | |____| |___| |____   | |   _| || |__| | |\  |____) |
#     |_|  \_\______|_|    |______|______\_____|  |_|  |_____\____/|_| \_|_____/ 
#                                                                                 
# ==============================================================================

import pygame
import sys
import random
import time
import math
import os
import json
import subprocess
from datetime import datetime

# ------------------------------------------------------------------------------
# discord rich presence configuration
# ------------------------------------------------------------------------------
client_id = "1500874965879226498" 

try:
    from pypresence import Presence
    rpc = Presence(client_id)
    rpc.connect()
    print("discord rpc connected")
except Exception:
    print("discord rpc failed to connect, is discord open?")
    rpc = None


# ------------------------------------------------------------------------------
# core window & display instantiation
# ------------------------------------------------------------------------------
pygame.init()
pygame.mixer.init()

width, height = 1280, 720
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("reflections.")
clock = pygame.time.Clock()


# ------------------------------------------------------------------------------
# audio asset loading
# ------------------------------------------------------------------------------
try:
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=-1) 
    print("song.mp3 found and is playing")
except pygame.error as e:
    print(f"could not load song.mp3): {e}")


# ------------------------------------------------------------------------------
# particle environment: the endless winter
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
# THE ABSOLUTE GRAVEYARD OF TEXT TRANSLATIONS (ULTIMATE POOL)
# ------------------------------------------------------------------------------
text_pool = [
    "there is nothing to do here.",
    "in the quiet space between actions, we find ourselves.",
    "f i n d   m e .",
    "why are you still looking at the screen?",
    "my head hurts",
    "100% empty!",
    "help",
    "how are u today",
    "get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head",
    "if you are reading this. you are able to read.",
    "btw u can customize the song",
    "the weather today is completely overcast. just like your mind.",
    "memories that don't belong to you anymore.",
    "ambouttakam",  
    "all those moments will be lost in time, like tears in rain.", 
    "why so serious?", 
    "i see dead pixels.", 
    "h",
    "let him cook.",
    "press escape for free robux and limiteds",
    "what the fuck",
    "bro really compiled an entire exe just to do nothing.",
    "it's just a prank, bro. look at the camera.",
    "@everyone nudes",
    "he's pulling his cock out!",
    "istg ur gay",
    "birds aren't real. neither is this game.",
    "what if we kissed in the python game? jk... unless?",
    "this is what unlimited access to the internet at age 7 does to a person.",
    "have you ever had a dream that you, um, you had...",
    "bye",
    "yo pi'erre, you wanna come out here?",
    "yes. it is supposed to crash when you press the x. dont try it tho. im loneley",
    "foiddestroyer678 is typing...",
    "when stanley came to a set of two open doors, he entered the door on his left.",
    "the end is never the end is never the end is never...",
    "just monika.",
    "error: file 'characters/yuri.chr' not found.",
    "every day i imagine a future where i can be with you",
    "it is dangerous to go alone! take nothing.",
    "would you kindly do absolutely nothing?",
    "the cake was a lie, but this void is real.",
    "did you think there was an ending? this isnt ddlc.",
    "welcome to white space. you have been living here for as long as you can remember.",
    "you are the player. wake up.",
    "everything that lives is designed to end.",
    "remember our promise.",
    "despite everything, it's still you.",
    "it's a wonderful day outside. birds are singing, flowers are blooming...",
    "but nobody came.",
    "disconnected from server: timed out.",
    "this is the part where he kills you.",
    "get a job loser",
    "ARE YA GONNA PULL OVA",
    "steam release: after gta 6",
    "GUBBY",
    "dank memez",
    "sosig",
    "owo wats dis?",
    "wake up",
    "its all a dream.",
    "just wish i was normal.. :/",
    "no...",
    "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
    "GET OUT OF MY HEADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "fart",
    
    # --- glitch prompt metadata ---
    "calculating the exact amount of time you've wasted...",
    "i can see you.",
    "smile for the camera.",
    "error: terminal breach initiated.",
    "your cursor belongs to the void now.",
    "your pc ran into a problem and needs to restart :("
]


# ------------------------------------------------------------------------------
# SYSTEM FILE SCANNING ENGINE (LOCAL HACKS)
# ------------------------------------------------------------------------------
def run_filesystem_scan():
    """Scans the host computer's desktop and environment for highly personal callouts."""
    scan_quotes = []
    
    try:
        # Get path to user's real desktop folder
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        desktop_files = [f.lower() for f in os.listdir(desktop_path)] if os.path.exists(desktop_path) else []
        
        # Check for gaming installations or shortcuts
        if any("valorant" in f for f in desktop_files):
            scan_quotes.append("close valorant. your hardstuck rank isn't going anywhere.")
        if any("league" in f or "lol" in f for f in desktop_files):
            scan_quotes.append("uninstalled league of legends yet? today is a good day to touch grass.")
        if any("osu" in f for f in desktop_files):
            scan_quotes.append("job application.")
        if any("steam" in f for f in desktop_files):
            scan_quotes.append("you have steam installed, yet you are running an unevaluated python script.")
        if any("discord" in f or "equibop" in f or "vesktop" in f for f in desktop_files):
            scan_quotes.append("your discord status says 'nothing'. but they know you're staring at me.")
        if any("spotify" in f for f in desktop_files):
            scan_quotes.append("turn off spotify. song.mp3 is the only track you need right now.")
            
        # Roblox / Korone Revival specific callouts
        if any("roblox" in f for f in desktop_files):
            scan_quotes.append("weirdo.")
        if any("korone" in f or "pekora" in f for f in desktop_files):
            scan_quotes.append("ts korone")
            
        # DDLC / Visual Novel target evaluation
        if any("ddlc" in f or "doki" in f or "literature club" in f for f in desktop_files):
            scan_quotes.append("target demographic reached ig.")
            scan_quotes.append("you have ddlc on your desktop. ily twin")

        # FL Studio targeted obliteration
        if any("fl studio" in f or "flstudio" in f or "fl64" in f or ".flp" in f for f in desktop_files):
            scan_quotes.append("ur music is fucking horrible. uninstall fl rn bro")

        # Browser history / HW calls
        if any("chrome" in f or "opera" in f or "firefox" in f or "edge" in f for f in desktop_files):
            scan_quotes.append("clear your browser history. the void knows.")

        # Homework / Academic coping
        if any("homework" in f or "school" in f or "essay" in f or "pdf" in f for f in desktop_files):
            scan_quotes.append("ignore your homework. stay in the blank void. it's safer.")
            
        # Meta development environment callouts
        if any("vscode" in f or "code" in f for f in desktop_files):
            scan_quotes.append("i see visual studio code on your desktop. did you look at my source code?")
            
        # Track total clutter
        if len(desktop_files) > 30:
            scan_quotes.append(f"you have {len(desktop_files)} items cluttering your desktop. are you larping as speed bro.")

    except Exception:
        pass 
        
    return scan_quotes


# ------------------------------------------------------------------------------
# TEMPORAL CALLOUT MATRIX (CLOCK WATCHER)
# ------------------------------------------------------------------------------
def get_time_based_reflections():
    """Checks the physical real-world clock to flame the player's schedule."""
    now = datetime.now()
    current_hour = now.hour
    current_day = now.weekday() 
    
    timed_quotes = []
    
    if 20 <= current_hour < 5:
        timed_quotes.extend([
            f"it is currently {now.strftime('%I:%M %p')}. go to sleep.",
            "nothing good happens after 2 am. especially not in this void.",
            "staring at digital snow at 4 am. peak lifestyle choices.",
            "your sleep schedule is more corrupted than yuri.chr.",
            "tomorrow is going to hurt if you don't close this app right now."
        ])
        
    if current_day in [4, 5]:
        timed_quotes.extend([
            "it's the weekend. shouldn't you be out doing... literally anything else?",
            "imagine having weekend plans. couldn't be us, chat."
        ])
    elif current_day == 6:
        timed_quotes.extend([
            "the weekend is practically over. wake up.",
            "per my last reflection, monday is coming for you."
        ])
    elif 9 <= current_hour <= 17:
        timed_quotes.extend([
            "shouldn't you be working or paying attention to class right now?"
        ])

    return timed_quotes


# ------------------------------------------------------------------------------
# textual framework state management
# ------------------------------------------------------------------------------
text_state = {
    "current_text": "reflections.",
    "alpha": 0.0,
    "mode": "FADE_IN",
    "timer": time.time(),
    "hold_duration": 4.0
}

def process_text_lifecycle(current_time, active_pool):
    fade_speed = 3.5

    if text_state["mode"] == "FADE_IN":
        text_state["alpha"] += fade_speed
        if text_state["alpha"] >= 160:
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
            
            next_text = random.choice(active_pool)
            while next_text == text_state["current_text"]:
                next_text = random.choice(active_pool)
                
            text_state["current_text"] = next_text
            text_state["mode"] = "FADE_IN"
            text_state["hold_duration"] = random.uniform(3.0, 7.0)
            print(next_text)


# ------------------------------------------------------------------------------
# custom achievement configuration & save tracking
# ------------------------------------------------------------------------------
SAVE_FILE = "achievements.json"

ACHIEVEMENTS_MANIFEST = {
    "the_beginning": {"title": "achievement unlocked: the beginning", "desc": "welcome to the void.", "req_seconds": 1},
    "patience": {"title": "achievement unlocked: patience", "desc": "successfully stood still for 5 minutes.", "req_seconds": 300},
    "glitch_hunter": {"title": "achievement unlocked: terminal infection", "desc": "your system experienced its first glitch.", "req_seconds": 10},
    "insomniac": {"title": "achievement unlocked: nocturnal anomaly", "desc": "opened the void between 1 AM and 4 AM.", "req_seconds": 1},
    "crazy_commitment": {"title": "achievement unlocked: the commitment is crazy", "desc": "1 hour of absolute nothingness.", "req_seconds": 3600}
    "furry": {"title": "achievement unlocked owo: oooo a furry", "desc": "24 hours.", "req_seconds": 86400}
}

if os.path.exists(SAVE_FILE):
    try:
        with open(SAVE_FILE, "r") as f:
            unlocked_achievements = json.load(f)
    except Exception:
        unlocked_achievements = []
else:
    unlocked_achievements = []

popup_state = {
    "active": False,
    "title": "",
    "desc": "",
    "start_time": 0,
    "duration": 5.0
}

def save_achievements():
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(unlocked_achievements, f)
    except Exception:
        pass

def trigger_popup(title, desc, current_time):
    popup_state["active"] = True
    popup_state["title"] = title
    popup_state["desc"] = desc
    popup_state["start_time"] = current_time

def check_achievements(elapsed_seconds, current_time):
    for key, data in ACHIEVEMENTS_MANIFEST.items():
        if key not in unlocked_achievements:
            if key == "glitch_hunter" and not glitch_tracker["has_glitched"]:
                continue 
            if key == "insomniac" and not (1 <= datetime.now().hour <= 4):
                continue
            if elapsed_seconds >= data["req_seconds"]:
                unlocked_achievements.append(key)
                save_achievements()
                trigger_popup(data["title"], data["desc"], current_time)

def draw_achievement_popup(current_time):
    if not popup_state["active"]:
        return

    time_passed = current_time - popup_state["start_time"]
    if time_passed > popup_state["duration"]:
        popup_state["active"] = False
        return

    alpha = 180
    if time_passed < 0.5:
        alpha = int((time_passed / 0.5) * 180)
    elif time_passed > (popup_state["duration"] - 0.5):
        remaining = popup_state["duration"] - time_passed
        alpha = int((remaining / 0.5) * 180)

    box_w, box_h = 480, 75
    box_x = (width - box_w) // 2
    box_y = height - box_h - 40

    popup_surf = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
    popup_surf.fill((15, 15, 17, alpha))
    pygame.draw.rect(popup_surf, (120, 120, 125, alpha), (0, 0, box_w, box_h), 1)

    font_title = pygame.font.SysFont("cambria", 18, bold=True)
    font_desc = pygame.font.SysFont("cambria", 15)

    title_surf = font_title.render(popup_state["title"], True, (230, 230, 235))
    desc_surf = font_desc.render(popup_state["desc"], True, (160, 160, 165))

    title_surf.set_alpha(alpha)
    desc_surf.set_alpha(alpha)

    popup_surf.blit(title_surf, (20, 15))
    popup_surf.blit(desc_surf, (20, 42))
    
    screen.blit(popup_surf, (box_x, box_y))


# ------------------------------------------------------------------------------
# THE CHAOS GENERATOR ENGINE (MALFUNCTION INDUCTIONS)
# ------------------------------------------------------------------------------
glitch_tracker = {
    "has_glitched": False,
    "bsod_active": False,
    "bsod_start": 0,
    "mouse_hijack_until": 0
}

def trigger_system_glitch(current_time):
    glitch_tracker["has_glitched"] = True
    glitch_type = random.choice(["calculator", "camera", "mouse_drift", "fake_bsod", "pitch_bend", "pierre_moment", "void_popup"])
    
    try:
        if glitch_type == "calculator":
            subprocess.Popen("calc.exe")
            text_state["current_text"] = "calculating the exact amount of time you've wasted..."
            text_state["alpha"] = 160
            text_state["mode"] = "HOLD"
            text_state["timer"] = current_time

        elif glitch_type == "camera":
            subprocess.Popen("start microsoft.windows.camera:", shell=True)
            text_state["current_text"] = "smile for the camera."
            text_state["alpha"] = 160
            text_state["mode"] = "HOLD"
            text_state["timer"] = current_time

        elif glitch_type == "mouse_drift":
            glitch_tracker["mouse_hijack_until"] = current_time + random.uniform(2.0, 5.0)
            text_state["current_text"] = "your cursor belongs to the void now."
            text_state["alpha"] = 160
            text_state["mode"] = "HOLD"
            text_state["timer"] = current_time

        elif glitch_type == "fake_bsod":
            glitch_tracker["bsod_active"] = True
            glitch_tracker["bsod_start"] = current_time
            pygame.mixer.music.pause() 

        elif glitch_type == "pitch_bend":
            pygame.mixer.music.stop()
            pygame.mixer.music.play(loops=2, start=random.uniform(10.0, 50.0))
            text_state["current_text"] = "error: terminal breach initiated."
            text_state["alpha"] = 160
            text_state["mode"] = "HOLD"
            text_state["timer"] = current_time

        elif glitch_type == "pierre_moment":
            text_state["current_text"] = "yo pi'erre, you wanna come out here?"
            text_state["alpha"] = 160
            text_state["mode"] = "HOLD"
            text_state["timer"] = current_time
            pygame.mixer.music.pause()
            glitch_tracker["mouse_hijack_until"] = current_time + 1.8

        elif glitch_type == "void_popup":
            trigger_void_popup()
    except Exception:
        pass


def draw_fake_bsod():
    screen.fill((0, 120, 215)) 
    
    font_sad = pygame.font.SysFont("segoe ui", 90)
    font_main = pygame.font.SysFont("segoe ui", 22)
    font_sub = pygame.font.SysFont("segoe ui", 14)
    
    sad_face = font_sad.render(":(", True, (255, 255, 255))
    msg_1 = font_main.render("your pc ran into a problem and needs to restart. we're just", True, (255, 255, 255))
    msg_2 = font_main.render("collecting some error info, and then we'll restart for you.", True, (255, 255, 255))
    stop_code = font_sub.render("stop code: reflections_void_breach", True, (255, 255, 255))
    
    screen.blit(sad_face, (100, 150))
    screen.blit(msg_1, (100, 280))
    screen.blit(msg_2, (100, 315))
    stop_code_rect = stop_code.get_rect()
    screen.blit(stop_code, (100, 450))


def trigger_void_popup():
    """Forces a custom, stark minimalist dialogue box that pauses reality."""
    pygame.mixer.music.pause() 
    
    popup_w, popup_h = 460, 180
    popup_x = (width - popup_w) // 2
    popup_y = (height - popup_h) // 2
    
    font_mono = pygame.font.SysFont("cambria", 18)
    font_button = pygame.font.SysFont("cambria", 15, bold=True)
    
    glitch_thoughts = [
        ["an anomaly has occurred.", "the system is running out of thoughts.", "do you wish to stay here?"],
        ["no", "no", "no"],
        ["", "", ""]
    ]
    error_lines = random.choice(glitch_thoughts)
    
    in_popup = True
    while in_popup:
        screen.fill((0, 0, 0))
        for flake in snowflakes:
            pygame.draw.circle(screen, (50, 50, 55), (int(flake["x"]), int(flake["y"])), int(flake["radius"]))
            
        pygame.draw.rect(screen, (5, 5, 5), (popup_x, popup_y, popup_w, popup_h))
        pygame.draw.rect(screen, (140, 140, 145), (popup_x, popup_y, popup_w, popup_h), 1) 
        
        text_y_offset = popup_y + 30
        for line in error_lines:
            text_surf = font_mono.render(line, True, (190, 195, 200))
            screen.blit(text_surf, (popup_x + 35, text_y_offset))
            text_y_offset += 26
            
        btn_w, btn_h = 70, 28
        btn_x = popup_x + popup_w - btn_w - 35
        btn_y = popup_y + popup_h - btn_h - 25
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hovering = btn_x <= mouse_x <= btn_x + btn_w and btn_y <= mouse_y <= btn_y + btn_h
        
        btn_bg = (25, 25, 30) if is_hovering else (5, 5, 5)
        pygame.draw.rect(screen, btn_bg, (btn_x, btn_y, btn_w, btn_h))
        pygame.draw.rect(screen, (140, 140, 145), (btn_x, btn_y, btn_w, btn_h), 1)
        
        btn_text = font_button.render("yes", True, (210, 215, 220))
        screen.blit(btn_text, (btn_x + (btn_w - btn_text.get_width()) // 2, btn_y + 4))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if is_hovering:
                    in_popup = False 
                    
        pygame.display.flip()
        clock.tick(fps)
        
    try:
        pygame.mixer.music.unpause()
    except Exception:
        pass


# ------------------------------------------------------------------------------
# runtime telemetry & initial caching
# ------------------------------------------------------------------------------
start_time = int(time.time())
last_rpc_update = time.time()

def mirror_state_to_discord():
    if not rpc:
        return
    try:
        rpc.update(
            state="staring at nothing but thoughts",
            details="forza horizon 6 in 2 days",
            start=start_time,
            large_image="abyss_image", 
            large_text="reflections"
        )
    except Exception:
        pass

mirror_state_to_discord()

cached_filesystem_quotes = run_filesystem_scan()


# ------------------------------------------------------------------------------
# the execution matrix (infinite loop)
# ------------------------------------------------------------------------------
is_present = True

while is_present:
    current_time = time.time()

    # --- a. check structural adjustments (cheater file checker) ---
    if not os.path.exists("characters/yuri.chr"):
        if "error: file 'characters/yuri.chr' not found." not in text_pool:
            text_pool.append("you actually deleted her file. the commitment is terrifying.")

    # --- b. intercept execution interactions ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_present = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if glitch_tracker["bsod_active"]:
                    glitch_tracker["bsod_active"] = False
                    pygame.mixer.music.unpause()
                else:
                    is_present = False

    # --- c. mouse cursor anchoring anomalies ---
    if current_time < glitch_tracker["mouse_hijack_until"]:
        pygame.mouse.set_pos((width // 2, height // 2))

    # --- d. dynamic rendering logic blocks ---
    if glitch_tracker["bsod_active"]:
        draw_fake_bsod()
        if current_time - glitch_tracker["bsod_start"] >= 6.0:
            glitch_tracker["bsod_active"] = False
            try:
                pygame.mixer.music.unpause()
            except Exception:
                pass
    else:
        screen.fill((0, 0, 0))

        # particle dynamic translations
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

        # Build dynamic composite text array
        active_pool = text_pool.copy()
        active_pool.extend(get_time_based_reflections())
        active_pool.extend(cached_filesystem_quotes)

        # cycle display output fonts
        process_text_lifecycle(current_time, active_pool)
        font = pygame.font.SysFont("cambria", 26)
        text_surface = font.render(text_state["current_text"], True, (210, 215, 220))
        text_surface.set_alpha(int(text_state["alpha"]))
        
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)

    # --- e. milestones & structural breakdown checks ---
    elapsed_seconds = int(current_time - start_time)
    check_achievements(elapsed_seconds, current_time)
    draw_achievement_popup(current_time)

    # Anomaly activation logic
    if not glitch_tracker["bsod_active"] and random.random() < 0.00015:
        trigger_system_glitch(current_time)

    pygame.display.flip()

    # --- f. telemetry clock balancing ---
    if current_time - last_rpc_update >= 15:
        mirror_state_to_discord()
        last_rpc_update = current_time

    clock.tick(fps)


# ------------------------------------------------------------------------------
# terminate process links safely
# ------------------------------------------------------------------------------
print("[system] returning to reality. goodbye.")
if rpc:
    try:
        rpc.close()
    except Exception:
        pass

pygame.quit()
sys.exit()
