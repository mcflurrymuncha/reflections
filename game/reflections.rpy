# ==============================================================================
#      _____  ______  ______ _      ______ _____ _______ _____ ____  _   _  _____ 
#     |  __ \|  ____|  ____| |    |  ____/ ____|__   __|_  _/ __ \| \ | |/ ____|
#     | |__) | |__  | |__  | |    | |__ | |       | |    | || |  | |  \| | (___  
#     |  _  /|  __| |  __| | |    |  __|| |       | |    | || |  | | . ` |\___ \ 
#     | | \ \| |____| |    | |____| |___| |____   | |   _| || |__| | |\  |____) |
#     |_|  \_\______|_|    |______|______\_____|  |_|  |_____\____/|_| \_|_____/ 
#                                                                                
# ==============================================================================

# --- METADATA, DISPLAY, & BUILD SETTINGS ---
define config.name = "reflections"
define gui.show_name = True
define config.version = "1.0.0"
define config.screen_width = 1280
define config.screen_height = 720
define config.window_title = "reflections."
define config.main_menu_music = None

init python:
    build.directory_name = "reflections-release"
    build.executable_name = "reflections"
    build.include_update = False
    
    # --- WINDOWS-ONLY PACKAGING CONFIGURATION ---
    build.package('win', 'zip', 'windows', 'windows build')
    
    # remove everything from non-windows distributions
    build.classify('**', None, 'mac')
    build.classify('**', None, 'linux')
    build.classify('**', None, 'all')
    
    # WEB-SAFE CLASSIFICATION FOR WINDOWS
    build.classify('game/**.rpy', None, 'win')
    build.classify('game/**.rpyc', 'archive', 'win')
    build.classify('game/**.mp3', 'archive', 'win')
    build.classify('game/**.MP3', 'archive', 'win')
    build.classify('game/**.ttc', 'archive', 'win')
    build.classify('game/**.TTC', 'archive', 'win')
    build.classify('game/**.ttf', 'archive', 'win')
    build.classify('game/**.TTF', 'archive', 'win')
    build.classify('game/characters/**', 'archive', 'win')

# --- CORE STRIPPED GUI RULES ---
init -1 python:
    gui.init(1280, 720)
init python:
    gui.text_font = "CAMBRIA.TTC"
    gui.name_text_font = "CAMBRIA.TTC"
    gui.interface_text_font = "CAMBRIA.TTC"
    gui.text_color = '#ffffff'
    gui.idle_color = '#8a8a8f'
    gui.hover_color = '#ffffff'

# ------------------------------------------------------------------------------
# ENVIRONMENT SCANNERS & PYTHON DATA POOLS
# ------------------------------------------------------------------------------
init python:
    import random
    import os
    import sys
    import ctypes
    import time
    import math
    from datetime import datetime

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
        "get out of my headddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
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

    def run_filesystem_scan():
        scan_quotes = []
        try:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            desktop_files = [f.lower() for f in os.listdir(desktop_path)] if os.path.exists(desktop_path) else []
            
            if any("valorant" in f for f in desktop_files): scan_quotes.append("close valorant. your hardstuck rank isn't going anywhere.")
            if any("league" in f or "lol" in f for f in desktop_files): scan_quotes.append("uninstalled league of legends yet? today is a good day to touch grass.")
            if any("osu" in f for f in desktop_files): scan_quotes.append("job application.")
            if any("steam" in f for f in desktop_files): scan_quotes.append("you have steam installed, yet you are running an unevaluated script.")
            if any("discord" in f or "vesktop" in f for f in desktop_files): scan_quotes.append("your discord status says 'nothing'. but they know you're staring at me.")
            if any("spotify" in f for f in desktop_files): scan_quotes.append("turn off spotify. song.mp3 is the only track you need right now.")
            if any("roblox" in f for f in desktop_files): scan_quotes.append("robloz")
            if any("ddlc" in f or "doki" in f for f in desktop_files): scan_quotes.append("you have ddlc on your desktop. ily twin")
            if any("fl studio" in f or "flstudio" in f for f in desktop_files): scan_quotes.append("ur music is fucking horrible. uninstall fl rn bro")
            if any("chrome" in f or "opera" in f or "firefox" in f or "edge" in f for f in desktop_files): scan_quotes.append("clear your browser history. the void knows.")
            if any("homework" in f or "school" in f or "essay" in f for f in desktop_files): scan_quotes.append("a homework folder aint hiding shit bucko")
            if any("vscode" in f or "code" in f for f in desktop_files): scan_quotes.append("i see visual studio code on your desktop. did you look at my source code?")
            if len(desktop_files) > 30: scan_quotes.append(f"you have {len(desktop_files)} items cluttering your desktop. are you larping as speed bro.")
            if len(desktop_files) == 0: scan_quotes.append("empty ass desktop")
        except Exception: pass
        return scan_quotes

    def get_time_based_reflections():
        now = datetime.now()
        current_hour, current_day = now.hour, now.weekday()
        timed_quotes = []
        if 20 <= current_hour or current_hour < 5:
            timed_quotes.extend([
                f"it is currently {now.strftime('%I:%M %p').lower()}. go to sleep.",
                "nothing good happens after 2 am. especially not in this void.",
                "staring at digital snow at 4 am. peak lifestyle choices.",
                "your sleep schedule is more corrupted than yuri.chr.",
                "tomorrow is going to hurt if you don't close this app right now."
            ])
        if current_day in [4, 5]: timed_quotes.extend(["it's the weekend. shouldn't you be out doing... literally anything else?", "imagine having weekend plans. couldn't be us, chat."])
        elif current_day == 6: timed_quotes.extend(["the weekend is practically over. wake up.", "per my last reflection, monday is coming for you."])
        elif 9 <= current_hour <= 17: timed_quotes.extend(["shouldn't you be working or paying attention to class right now?"])
        return timed_quotes

    cached_filesystem_quotes = run_filesystem_scan()
    start_time = int(time.time())
    last_text = ""

    # --- PERSISTENT TIMER ACHIEVEMENTS SETUP ---
    if persistent.unlocked_achievements is None:
        persistent.unlocked_achievements = []

    ach_manifest = {
        "the_beginning": {"title": "achievement unlocked: the beginning", "desc": "welcome to the void.", "req": 1},
        "patience": {"title": "achievement unlocked: patience", "desc": "successfully stood still for 5 minutes.", "req": 300},
        "crazy_commitment": {"title": "achievement unlocked: the commitment is crazy", "desc": "1 hour of absolute nothingness.", "req": 3600},
        "furry": {"title": "achievement unlocked owo: oooo a furry", "desc": "24 hours.", "req": 86400}
    }

# ------------------------------------------------------------------------------
# DISCORD PRESENCE PIPELINE (FALLBACK SYSTEM FOR HEADLESS COMPILING)
# ------------------------------------------------------------------------------
init python:
    discord_presence_id = "1500874965879226498"
    def dynamic_void_presence(presence=None):
        if presence:
            presence.update(
                state="staring at nothing but thoughts", details="game of the year?",
                large_image="abyss_logo", large_text="reflections. (beta)",
                buttons=[{"label": "download", "url": "https://mcflurrymuncha.github.io/reflections"}]
            )

# ------------------------------------------------------------------------------
# VISUAL DISPLAYABLES & SCREEN ENGINE
# ------------------------------------------------------------------------------
init python:
    class SnowParticleMatrix(renpy.Displayable):
        def __init__(self):
            super(SnowParticleMatrix, self).__init__()
            self.particles = [[random.uniform(0, 1280), random.uniform(0, 720), random.uniform(1.0, 3.5), random.uniform(0.5, 2.0)] for _ in range(100)]
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            canvas = render.canvas()
            for p in self.particles:
                p[1] += p[3]
                p[0] += math.sin(st + p[2]) * 0.5
                if p[1] > 720:
                    p[1], p[0] = random.uniform(-20, -5), random.uniform(0, 1280)
                canvas.circle((245, 245, 250), (int(p[0]), int(p[1])), int(p[2]))
            renpy.redraw(self, 0)
            return render

screen digital_snow():
    add SnowParticleMatrix()

screen main_menu():
    tag menu
    add "#000000"
    use digital_snow
    vbox:
        align (0.5, 0.45) spacing 15
        text "reflections." font "CAMBRIA.TTC" size 52 color "#ffffff" xalign 0.5 at menu_fade_in
        null height 20
        textbutton "enter the void":
            xalign 0.5 text_font "CAMBRIA.TTC" text_size 22 text_idle_color "#8c8c91" text_hover_color "#ffffff" action Start() at menu_fade_in
        textbutton "close app":
            xalign 0.5 text_font "CAMBRIA.TTC" text_size 22 text_idle_color "#8c8c91" text_hover_color "#ffffff" action Quit(confirm=False) at menu_fade_in

transform menu_fade_in:
    alpha 0.0
    linear 1.5 alpha 1.0

screen milestone_popup(title, desc):
    layer "overlay"
    frame:
        background Solid("#0f0f11b4")
        xsize 480 ysize 75 align (0.5, 0.85) padding (20, 12) at popup_fade_transform
        vbox:
            spacing 4
            text title font "CAMBRIA.TTC" size 18 bold True color "#e6e6eb"
            text desc font "CAMBRIA.TTC" size 15 color "#a0a0a5"

transform popup_fade_transform:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
        pause 4.0
        linear 0.5 alpha 0.0

screen fake_bsod_anomaly():
    add "#0078d7"
    vbox:
        xpos 100 ypos 150 spacing 40
        text ":(" font "SEGOEUI.TTF" size 90 color "#fff"
        vbox:
            spacing 10
            text "your pc ran into a problem and needs to restart. we're just" font "SEGOEUI.TTF" size 24 color "#fff"
            text "collecting some error info, and then we'll restart for you." font "SEGOEUI.TTF" size 24 color "#fff"
        text "stop code: reflections_is_in_ur_pc_bozo" font "SEGOEUI.TTF" size 16 color "#fff"

screen void_popup_anomaly(lines):
    modal True
    add "#000000e6"
    frame:
        background Solid("#050505")
        xsize 460 ysize 180 align (0.5, 0.5) padding (30, 25)
        vbox:
            spacing 12
            for line in lines: 
                text line font "CAMBRIA.TTC" size 18 color "#bcbfc8"
        frame:
            background Solid("#050505") xsize 70 ysize 28 align (0.95, 0.9)
            textbutton "yes":
                text_font "CAMBRIA.TTC" text_size 15 text_bold True text_idle_color "#d2d7dc" text_hover_color "#ffffff" action Return()

# ------------------------------------------------------------------------------
# LABELS & EXECUTION LOOPS
# ------------------------------------------------------------------------------
label start:
    $ quick_menu = False
    scene black
    show screen digital_snow
    if renpy.loadable("song.mp3") or renpy.loadable("SONG.MP3"):
        python:
            track = "song.mp3" if renpy.loadable("song.mp3") else "SONG.MP3"
            renpy.music.play(track, loop=True)
    "reflections."
    jump void_matrix_loop

label void_matrix_loop:
    python:
        has_yuri = False
        for ext in ["chr", "CHR"]:
            if os.path.exists(os.path.join(config.gamedir, f"characters/yuri.{ext}")):
                has_yuri = True
        if not has_yuri and "error: file 'characters/yuri.chr' not found." not in text_pool:
            text_pool.append("you actually deleted her file. the commitment is terrifying.")

    $ elapsed = int(time.time() - start_time)
    python:
        for key, data in ach_manifest.items():
            if key not in persistent.unlocked_achievements and elapsed >= data["req"]:
                persistent.unlocked_achievements.append(key)
                renpy.show_screen("milestone_popup", title=data["title"], desc=data["desc"])

    python:
        active_pool = text_pool.copy() + get_time_based_reflections() + cached_filesystem_quotes
        chosen_text = random.choice(active_pool)
        while chosen_text == last_text:
            chosen_text = random.choice(active_pool)
        last_text = chosen_text
        glitch_roll = random.random()
        
    if glitch_roll < 0.00015:
        jump trigger_engine_glitch
        
    $ formatted_text = "{font=CAMBRIA.TTC}{size=26}{color=#d2d7dc}" + chosen_text + "{/color}{/size}{/font}"
    show text "[formatted_text]" at truecenter with Dissolve(2.0)
    $ renpy.pause(random.uniform(3.0, 7.0))
    hide text with Dissolve(1.5)
    $ renpy.pause(1.0)
    jump void_matrix_loop

label trigger_engine_glitch:
    python:
        glitch_pool = ["calculator", "camera", "notepad", "paint", "taskmanager", "go_play_something_else", "ddlc_name_call", "fake_bsod", "fake_uac", "void_popup"]
        glitch_type = random.choice(glitch_pool)
        try:
            if glitch_type == "calculator": os.system("start calc.exe"); chosen_text = "calculating the exact amount of time you've wasted..."
            elif glitch_type == "camera": os.system("start microsoft.windows.camera:"); chosen_text = "smile for the camera."
            elif glitch_type == "notepad": os.system("start notepad.exe"); chosen_text = "take some notes."
            elif glitch_type == "paint": os.system("start mspaint.exe"); chosen_text = "make a drawing."
            elif glitch_type == "taskmanager": os.system("start taskmgr.exe"); chosen_text = "oops."
            elif glitch_type == "go_play_something_else": os.system("start steam://open/main"); chosen_text = "go play something else."
            elif glitch_type == "ddlc_name_call": chosen_text = f"i am looking right at you, {os.getlogin().lower()}."
        except Exception: pass

    if glitch_type in ["calculator", "camera", "notepad", "paint", "taskmanager", "go_play_something_else", "ddlc_name_call"]:
        $ formatted_text = "{font=CAMBRIA.TTC}{size=26}{color=#d2d7dc}" + chosen_text + "{/color}{/size}{/font}"
        show text "[formatted_text]" at truecenter with Dissolve(1.0)
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
            try: ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, None, None, 1)
            except Exception: pass
        $ renpy.music.unpause()
        $ formatted_text = "{font=CAMBRIA.TTC}{size=26}{color=#d2d7dc}did that scare u?{/color}{/size}{/font}"
        show text "[formatted_text]" at truecenter with Dissolve(1.0)
        $ renpy.pause(4.0)
        hide text with Dissolve(1.5)
        jump void_matrix_loop

    elif glitch_type == "void_popup":
        $ renpy.music.pause()
        python:
            thoughts = [["an anomaly has occurred.", "the system is running out of thoughts.", "do you wish to stay here?"], ["no", "no", "no"]]
            chosen_lines = random.choice(thoughts)
        call screen void_popup_anomaly(lines=chosen_lines)
        $ renpy.music.unpause()
        jump void_matrix_loop
