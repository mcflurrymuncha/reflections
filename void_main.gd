extends Control

# UI Elements
@onready var reflection_text = $ReflectionText
@onready var matrix_timer = $MatrixTimer

# Tracking variables
var start_time: int = 0
var last_text: String = ""
var cached_filesystem_quotes: Array = []
var unlocked_achievements: Array = []

# Core Text Pool (Kept completely lowercase)
var text_pool: Array = [
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

# Achievements definitions
var ach_manifest = {
	"the_beginning": {"title": "achievement unlocked: the beginning", "desc": "welcome to the void.", "req": 1},
	"patience": {"title": "achievement unlocked: patience", "desc": "successfully stood still for 5 minutes.", "req": 300},
	"crazy_commitment": {"title": "achievement unlocked: the commitment is crazy", "desc": "1 hour of absolute nothingness.", "req": 3600}
}

func _ready():
	DisplayServer.window_set_title("reflections.")
	start_time = Time.get_unix_time_from_system()
	
	# run file scan on startup
	cached_filesystem_quotes = run_filesystem_scan()
	
	# setup background music if song.mp3 exists in the project root
	if FileAccess.file_exists("res://song.mp3"):
		var audio_player = AudioStreamPlayer.new()
		add_child(audio_player)
		audio_player.stream = load("res://song.mp3")
		audio_player.play()
		
	# start the void processing loop
	void_matrix_loop()

func void_matrix_loop():
	# achievement tracking checks
	var elapsed = int(Time.get_unix_time_from_system() - start_time)
	for key in ach_manifest.keys():
		if not unlocked_achievements.has(key) and elapsed >= ach_manifest[key]["req"]:
			unlocked_achievements.append(key)
			print(ach_manifest[key]["title"] + " - " + ach_manifest[key]["desc"]) # custom popup notice can be added here
			
	# bundle pool options together
	var active_pool = text_pool.duplicate() + get_time_based_reflections() + cached_filesystem_quotes
	
	# choose text cleanly without duplicates
	var chosen_text = active_pool.pick_random()
	while chosen_text == last_text:
		chosen_text = active_pool.pick_random()
	last_text = chosen_text
	
	# ultra-rare environmental glitch execution roll
	if randf() < 0.005:
		trigger_engine_glitch()
		return
		
	# update text display with a subtle fade in/out script sequence
	reflection_text.text = chosen_text
	var tween = create_tween()
	reflection_text.modulate.a = 0.0
	tween.tween_property(reflection_text, "modulate:a", 1.0, 2.0)
	
	# random display hold duration before resetting loop
	matrix_timer.wait_time = randf_range(4.0, 8.0)
	matrix_timer.one_shot = true
	matrix_timer.start()
	await matrix_timer.timeout
	
	var fade_out = create_tween()
	fade_out.tween_property(reflection_text, "modulate:a", 0.0, 1.5)
	await fade_out.finished
	
	void_matrix_loop()

func run_filesystem_scan() -> Array:
	var scan_quotes = []
	var user_profile = OS.get_environment("USERPROFILE")
	if user_profile == "":
		return scan_quotes # not on windows or environment missing
		
	var desktop_path = user_profile + "/Desktop/"
	var dir = DirAccess.open(desktop_path)
	
	if dir:
		dir.list_dir_begin()
		var file_name = dir.get_next()
		var count = 0
		while file_name != "":
			count += 1
			var f_low = file_name.to_lower()
			if "valorant" in f_low: scan_quotes.append("close valorant. your hardstuck rank isn't going anywhere.")
			if "league" in f_low or "lol" in f_low: scan_quotes.append("uninstalled league of legends yet? today is a good day to touch grass.")
			if "osu" in f_low: scan_quotes.append("job application.")
			if "steam" in f_low: scan_quotes.append("you have steam installed, yet you are running an unevaluated script.")
			if "discord" in f_low or "vesktop" in f_low: scan_quotes.append("your discord status says 'nothing'. but they know you're staring at me.")
			if "spotify" in f_low: scan_quotes.append("turn off spotify. song.mp3 is the only track you need right now.")
			if "fl studio" in f_low or "flstudio" in f_low: scan_quotes.append("ur music is fucking horrible. uninstall fl rn bro")
			if "vscode" in f_low: scan_quotes.append("i see visual studio code on your desktop. did you look at my source code?")
			file_name = dir.get_next()
			
		if count > 30: scan_quotes.append("you have " + str(count) + " items cluttering your desktop. are you larping as speed bro.")
		if count == 0: scan_quotes.append("empty ass desktop")
	return scan_quotes

func get_time_based_reflections() -> Array:
	var time_dict = Time.get_time_dict_from_system()
	var datetime_dict = Time.get_datetime_dict_from_system()
	var hour = time_dict["hour"]
	var weekday = datetime_dict["weekday"] # 0 = sunday, 6 = saturday
	var timed_quotes = []
	
	if hour >= 20 or hour < 5:
		timed_quotes.append("nothing good happens after 2 am. especially not in this void.")
		timed_quotes.append("staring at digital snow at 4 am. peak lifestyle choices.")
		timed_quotes.append("your sleep schedule is more corrupted than yuri.chr.")
	if weekday == 0 or weekday == 6:
		timed_quotes.append("it's the weekend. shouldn't you be out doing... literally anything else?")
	elif hour >= 9 and hour <= 17:
		timed_quotes.append("shouldn't you be working or paying attention to class right now?")
	return timed_quotes

func trigger_engine_glitch():
	var glitch_pool = ["calc", "notepad", "paint", "taskmgr"]
	var choice = glitch_pool.pick_random()
	
	# Godot's safe OS execute interface to seamlessly drop external system commands
	if choice == "calc": 
		OS.execute("calc.exe", [])
		reflection_text.text = "calculating the exact amount of time you've wasted..."
	elif choice == "notepad": 
		OS.execute("notepad.exe", [])
		reflection_text.text = "take some notes."
	elif choice == "paint": 
		OS.execute("mspaint.exe", [])
		reflection_text.text = "make a drawing."
	elif choice == "taskmgr": 
		OS.execute("taskmgr.exe", [])
		reflection_text.text = "oops."
		
	matrix_timer.wait_time = 5.0
	matrix_timer.start()
	await matrix_timer.timeout
	void_matrix_loop()
