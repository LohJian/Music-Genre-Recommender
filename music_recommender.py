import time 
import random

# 🎶 Music Genre Recommender Program

# 🎶 welcome message first
print("🎶 Welcome to Music Genre Recommender 🎶")
time.sleep(0.5)
print("We will suggest a music genre based on your mood!👨🏻‍🎤")
time.sleep(2)

mood=input("How was your feeling today?(sad, happy, relaxed or energetic, romantic, angry, motivated, sleepy, or party.):")
mood = mood.lower() 
time.sleep(0.8)
print("Got it! You are feeling",mood)

# Music Database
music_db = {
    "happy": [
        "Pop - Taylor Swift: Love Story",
        "Dance - BTS: Dynamite",
        "K-Pop - BLACKPINK: How You Like That",
        "Pop - Ed Sheeran: Shape of You",
        "Dance - Dua Lipa: Levitating"
    ],
    "sad": [
        "Blues - B.B. King: The Thrill Is Gone",
        "Lo-Fi - Chillhop: Late Night Vibes",
        "Jazz - Miles Davis: Blue in Green",
        "Pop - Adele: Someone Like You",
        "Acoustic - Sam Smith: Stay With Me"
    ],
    "energetic": [
        "Rock - Linkin Park: Numb",
        "EDM - Martin Garrix: Animals",
        "Hip-Hop - Eminem: Lose Yourself",
        "Rock - Queen: We Will Rock You",
        "K-pop - Hearts2Hearts: Style"
    ],
    "relaxed": [
        "Classical - Mozart: Eine kleine Nachtmusik",
        "Chillhop - Lofi Beats: Study Session",
        "Acoustic - Ed Sheeran: Perfect",
        "Jazz - Norah Jones: Don’t Know Why",
        "Classical - Beethoven: Symphony No.9"
    ],
    "romantic": [
        "Pop - Bruno Mars: Just the Way You Are",
        "Pop - Ed Sheeran: Thinking Out Loud",
        "Acoustic - John Legend: All of Me",
        "Jazz - Frank Sinatra: Fly Me to the Moon",
        "Pop - Shania Twain: You're Still the One"
    ],
    "angry": [
        "Rock - Nirvana: Smells Like Teen Spirit",
        "Metal - Metallica: Enter Sandman",
        "Rock - Rage Against the Machine: Killing in the Name",
        "Punk - Green Day: American Idiot",
        "Hip-Hop - DMX: X Gon’ Give It to Ya"
    ],
    "motivated": [
        "Hip-Hop - Kanye West: Stronger",
        "Rock - Survivor: Eye of the Tiger",
        "Pop - Katy Perry: Roar",
        "Hip-Hop - Drake: Started From the Bottom",
        "EDM - Avicii: Wake Me Up"
    ],
    "sleepy": [
        "Lo-Fi - Lofi Girl: Sleepy Beats",
        "Classical - Debussy: Clair de Lune",
        "Acoustic - Jack Johnson: Banana Pancakes",
        "Ambient - Brian Eno: Ambient 1",
        "Jazz - Bill Evans: Peace Piece"
    ],
    "party": [
        "EDM - Calvin Harris: Summer",
        "Pop - Pitbull ft. Kesha: Timber",
        "Dance - Lady Gaga: Just Dance",
        "Hip-Hop - Nicki Minaj: Starships",
        "EDM - The Chainsmokers: Closer"
    ]
}

# Suggestion Logic
if mood in music_db:
    suggestion = random.choice(music_db[mood])
    print(f"\n✅ Based on your mood({mood}), we recommend: {suggestion} 🎧")
else:
    print("Sorry, we don't have recommendations for that mood.")
    print("Please try again with: happy, sad, energetic, or relaxed, romantic, angry, motivated, sleepy, or party.")

print("\nThanks for using the Music Genre Recommender! 🎵")