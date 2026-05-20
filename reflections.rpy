# ==============================================================================
#      _____  ______  ______ _      ______ _____ _______ _____ ____  _   _  _____ 
#     |  __ \|  ____|  ____| |    |  ____/ ____|__   __|_  _/ __ \| \ | |/ ____|
#     | |__) | |__  | |__  | |    | |__ | |       | |    | || |  | |  \| | (___  
#     |  _  /|  __| |  __| | |    |  __|| |       | |    | || |  | | . ` |\___ \ 
#     | | \ \| |____| |    | |____| |___| |____   | |   _| || |__| | |\  |____) |
#     |_|  \_\______|_|    |______|______\_____|  |_|  |_____\____/|_| \_|_____/ 
#                                                                                
# ==============================================================================

# --- REN'PY CONFIGURATION OVERRIDES ---
init -1 python:
    # We turn off standard main menu music so our script loop can handle audio natively
    config.main_menu_music = None

# ------------------------------------------------------------------------------
# CORE PYTHON INITIALIZATION & ENVIRONMENTAL METADATA SCANNER
# ------------------------------------------------------------------------------
init python:
    import random
    import os
    import sys
    import ctypes
    import time
    import math
    from datetime import datetime

    # --- BASE TEXT POOL ---
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
        "let him cook.",
        "press escape for free robux and limiteds",
        "what the fuck",
        "bro really compiled an entire game just to do nothing.",
        "it's just a prank, bro. look at the camera.",
        "@everyone nudes",
        "he's pulling his cock out!",
        "istg ur gay",
        "birds aren't real. neither is this game.",
        "this is what unlimited access to the internet at age 7 does to a person.",
        "bye",
        "yo pi'erre, you wanna come out here?",
        "yes. it is supposed to crash when you press the x. dont try it tho. im loneley",
        "foiddestroyer678 is typing...",
        "the end is never the end is never the end is never...",
        "just monika.",
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
        "but nobody came.",
        "disconnected from server: timed out.",
        "get a job loser",
        "steam release: after gta 6",
        "wake up",
        "its all a dream.",
        "just wish i was normal.. :/",
        "no...",
        "GET OUT OF MY HEADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
        "fart",
        "こんにちは、あなたはとてもかわいいです",
        "ебать",
        "calculating the exact amount of time you've wasted...",
        "i can see you.",
        "smile for the camera.",
        "error: terminal breach initiated.",
        "your pc ran into a problem and needs to restart :(",
        "play something else",
        "doki doki literal torture :3"
    ]

    # --- LOCAL FILESYSTEM SCANNER ---
    def run_filesystem_scan():
        scan_quotes = []
        try:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            desktop_files = [f.lower() for f in os.listdir(desktop_path)] if os.path.exists(desktop_path) else []
            
            if any("valorant" in f for f in desktop_files):
                scan_quotes.append("close valorant. your hardstuck rank isn't going anywhere.")
            if any("league" in f or "lol" in f for f in desktop_files):
                scan_quotes.append("uninstalled league of legends yet? today is a good day to touch grass.")
            if any("osu" in f for f in desktop_files):
                scan_quotes.append("job application.")
            if any("steam" in f for f in desktop_files):
                scan_quotes.append("you have steam installed, yet you are running an unevaluated script.")
            if any("discord" in f or "vesktop" in f for f in desktop_files):
                scan_quotes.append("your discord status says 'nothing'. but they know you're staring at me.")
            if any("spotify" in f for f in desktop_files):
                scan_quotes.append("turn off spotify. song.mp3 is the only track you need right now.")
            if any("roblox" in f for f in desktop_files):
                scan_quotes.append("robloz")
            if any("ddlc" in f or "doki" in f for f in desktop_files):
                scan_quotes.append("you have ddlc on your desktop. ily twin")
            if any("fl studio" in f or "flstudio" in f for f in desktop_files):
                scan_quotes.append("ur music is fucking horrible. uninstall fl rn bro")
            if any("chrome" in f or "opera" in f or "firefox" in f or "edge" in f for f in desktop_files):
                scan_quotes.append("clear your browser history. the void knows.")
            if any("homework" in f or "school" in f or "essay" in f for f in desktop_files):
                scan_quotes.append("a homework folder aint hiding shit bucko")
            if any("vscode" in f or "code" in f for f in desktop_files):
                scan_quotes.append("i see visual studio code on your desktop. did you look at my source code?")
            if len(desktop_files) > 30:
                scan_quotes.append(f"you have {len(desktop_files)} items cluttering your desktop. are you larping as speed bro.")
            if len(desktop_files) == 0:
                scan_quotes.append("empty ass desktop")
        except Exception:
            pass
        return scan_quotes

    # --- CLOCK WATCHER METRICS ---
    def get_time_based_reflections():
        now = datetime.now()
        current_hour = now.hour
        current_day = now.weekday()
        timed_quotes = []
        
        if 20 <= current_hour or current_hour < 5:
            timed_quotes.extend([
                f"it is currently {now.strftime('%I:%M %p')}. go to sleep.",
                "nothing good happens after 2 am. especially not in this void.",
                "staring at digital snow at 4 am. peak lifestyle choices.",
                "your sleep schedule is more corrupted than yuri.chr.",
                "tomorrow is going to hurt if you don't close this app right now."
            ])
        if current_day in [4, 5]:
            timed_quotes.extend(["it's the weekend. shouldn't you be out doing... literally anything else?", "imagine having weekend plans. couldn't be us, chat."])
        elif current_day == 6:
            timed_quotes.extend(["the weekend is practically over. wake up.", "per my last reflection, monday is coming for you."])
        elif 9 <= current_hour <= 17:
            timed_quotes.extend(["shouldn't you be working or paying attention to class right now?"])
            
        return timed_quotes

    # Run baseline operations
    cached_filesystem_quotes = run_filesystem_scan()
    start_time = int(time.time())
    last_text = ""

# ------------------------------------------------------------------------------
# RENDERING SURFACES & SCREEN UI DESIGN
# ------------------------------------------------------------------------------
init python:
    class SnowParticleMatrix(renpy.Displayable):
        def __init__(self):
            super(SnowParticleMatrix, self).__init__()
            self.particles = []
            for _ in range(100):
                self.particles.append([random.uniform(0, 1280), random.uniform(0, 720), random.uniform(1.0, 3.5), random.uniform(0.5, 2.0)])
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            canvas = render.canvas()
            for p in self.particles:
                p[1] += p[3]
                p[0] += math.sin(st + p[2]) * 0.5
                if p[1] > 720:
                    p[1] = random.uniform(-20, -5)
                    p[0] = random.uniform(0, 1280)
                canvas.circle((245, 245, 250), (int(p[0]), int(p[1])), int(p[2]))
            renpy.redraw(self, 0)
            return render

screen digital_snow():
    add SnowParticleMatrix()

# --- THE CUSTOM MINIMALIST MAIN MENU ---
screen main_menu():
    tag menu
    style_prefix "main_menu"

    # Background canvas elements
    add "#000000"
    show screen digital_snow

    # Menu Panel UI Structure
    vbox:
        align (0.5, 0.45)
        spacing 15

        text "reflections." font "gui/font/Cambria.ttf" size 52 color "#ffffff" xalign 0.5 at menu_fade_in

        null height 20

        textbutton "enter the void":
            xalign 0.5
            text_font "gui/font/Cambria.ttf" text_size 22
            text_idle_color "#8c8c91" text_hover_color "#ffffff"
            action Start()
            at menu_fade_in

        textbutton "close app":
            xalign 0.5
            text_font "gui/font/Cambria.ttf" text_size 22
            text_idle_color "#8c8c91" text_hover_color "#ffffff"
            action Quit(confirm=False)
            at menu_fade_in

# Simple fade-in effect layout for the custom menu typography
transform menu_fade_in:
    alpha 0.0
    linear 1.5 alpha 1.0

# --- GLITCH ANOMALY SURFACES ---
screen fake_bsod_anomaly():
    add "#0078d7"
    vbox:
        xpos 100 ypos 150 spacing 40
        text ":(" font "gui/font/Segoe-UI.ttf" size 90 color "#fff"
        vbox:
            spacing 10
            text "your pc ran into a problem and needs to restart. we're just" font "gui/font/Segoe-UI.ttf" size 24 color "#fff"
            text "collecting some error info, and then we'll restart for you." font "gui/font/Segoe-UI.ttf" size 24 color "#fff"
        text "stop code: reflections_is_in_ur_pc_bozo" font "gui/font/Segoe-UI.ttf" size 16 color "#fff"

screen void_popup_anomaly(lines):
    modal True
    add "#000000e6"
    frame:
        background "#050505" border_color "#8c8c91" border_width 1
        xsize 460 ysize 180 align (0.5, 0.5) padding (30, 25)
        vbox:
            spacing 12
            for line in lines:
                text line font "gui/font/Cambria.ttf" size 18 color "#bcbfc8"
        frame:
            background "#050505" border_color "#8c8c91" border_width 1
            xsize 70 ysize 28 align (0.95, 0.9)
            textbutton "yes":
                text_font "gui/font/Cambria.ttf" text_size 15 text_bold True
                text_idle_color "#d2d7dc" text_hover_color "#ffffff"
                action Return()

# ------------------------------------------------------------------------------
# CORE APPLICATION LAUNCH HOOKS (RUNS AFTER "ENTER THE VOID" CLICKED)
# ------------------------------------------------------------------------------
label start:
    $ quick_menu = False
    scene black
    show screen digital_snow
    
    if renpy.loadable("song.mp3"):
        play music "song.mp3" loop
        
    "reflections."
    jump void_matrix_loop

label void_matrix_loop:
    python:
        if not os.path.exists(os.path.join(config.gamedir, "characters/yuri.chr")):
            if "error: file 'characters/yuri.chr' not found." not in text_pool:
                text_pool.append("you actually deleted her file. the commitment is terrifying.")

    $ elapsed = int(time.time() - start_time)
    $ renpy.call_in_new_context("check_achievements_silent", elapsed=elapsed)

    python:
        active_pool = text_pool.copy()
        active_pool.extend(get_time_based_reflections())
        active_pool.extend(cached_filesystem_quotes)
        
        chosen_text = random.choice(active_pool)
        while chosen_text == last_text:
            chosen_text = random.choice(active_pool)
        last_text = chosen_text
        
        glitch_roll = random.random()
        
    if glitch_roll < 0.00015:
        jump trigger_engine_glitch
        
    show text "[chosen_text]" font "gui/font/Cambria.ttf" size 26 color "#d2d7dc" at truecenter with Dissolve(2.0)
    $ renpy.pause(random.uniform(3.0, 7.0))
    hide text with Dissolve(1.5)
    $ renpy.pause(1.0)
    jump void_matrix_loop

# ------------------------------------------------------------------------------
# SYSTEM BREACH MATRIX
# ------------------------------------------------------------------------------
label trigger_engine_glitch:
    python:
        glitch_pool = ["calculator", "camera", "notepad", "paint", "taskmanager", "go_play_something_else", "ddlc_name_call", "fake_bsod", "fake_uac", "void_popup"]
        glitch_type = random.choice(glitch_pool)
        
        try:
            if glitch_type == "calculator":
                os.system("start calc.exe")
                chosen_text = "calculating the exact amount of time you've wasted..."
            elif glitch_type == "camera":
                os.system("start microsoft.windows.camera:")
                chosen_text = "smile for the camera."
            elif glitch_type == "notepad":
                os.system("start notepad.exe")
                chosen_text = "take some notes."
            elif glitch_type == "paint":
                os.system("start mspaint.exe")
                chosen_text = "make a drawing."
            elif glitch_type == "taskmanager":
                os.system("start taskmgr.exe")
                chosen_text = "oops."
            elif glitch_type == "go_play_something_else":
                os.system("start steam://open/main")
                chosen_text = "go play something else."
            elif glitch_type == "ddlc_name_call":
                chosen_text = f"i am looking right at you, {os.getlogin().lower()}."
        except Exception:
            pass

    if glitch_type in ["calculator", "camera", "notepad", "paint", "taskmanager", "go_play_something_else", "ddlc_name_call"]:
        show text "[chosen_text]" font "gui/font/Cambria.ttf" size 26 color "#d2d7dc" at truecenter with Dissolve(1.0)
        $ renpy.pause(5.0)
        hide text with Dissolve(1.5)
        jump void_matrix_loop

    elif glitch_type == "fake_bsod":
        $ renpy.music.pause()
        show screen fake_bsod_anomaly
        $ renpy.pause(6.0)
        hide screen fake_bsod_anomaly
        $ renpy.music.unpause()
        jump void_matrix_loop

    elif glitch_type == "fake_uac":
        $ renpy.music.pause()
        python:
            try:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, None, None, 1)
            except Exception:
                pass
        $ renpy.music.unpause()
        show text "did that scare u?" font "gui/font/Cambria.ttf" size 26 color "#d2d7dc" at truecenter with Dissolve(1.0)
        $ renpy.pause(4.0)
        hide text with Dissolve(1.5)
        jump void_matrix_loop

    elif glitch_type == "void_popup":
        $ renpy.music.pause()
        python:
            thoughts = [
                ["an anomaly has occurred.", "the system is running out of thoughts.", "do you wish to stay here?"],
                ["no", "no", "no"]
            ]
            chosen_lines = random.choice(thoughts)
        call screen void_popup_anomaly(lines=chosen_lines)
        $ renpy.music.unpause()
        jump void_matrix_loop
