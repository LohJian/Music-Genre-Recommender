import time 
import random

#Music Genre Recommender Program

#welcome message first
print("🎶 Welcome to Music Genre Recommender 🎶")
time.sleep(0.5)
print("We will suggest a music genre based on your mood!👨🏻‍🎤")
time.sleep(2)

# Music Database
music_db = {
    "happy": [
        "Pop - Taylor Swift: Love Story",
        "Dance - BTS: Dynamite",
        "K-Pop - BLACKPINK: How You Like That",
        "Pop - Ed Sheeran: Shape of You",
        "Dance - Dua Lipa: Levitating",
        "K-pop - YENA, Feat. BIBI: SMILEY"
    ],
    "sad": [
        "Blues - B.B. King: The Thrill Is Gone",
        "Lo-Fi - Chillhop: Late Night Vibes",
        "Jazz - Miles Davis: Blue in Green",
        "Pop - Adele: Someone Like You",
        "Acoustic - Sam Smith: Stay With Me",
        "K-Pop - TAEYANG: Eyes, Nose, Lips",
        "K-Pop - TWICE: Cry For Me"
    ],
    "energetic": [
        "Rock - Linkin Park: Numb",
        "EDM - Martin Garrix: Animals",
        "Hip-Hop - Eminem: Lose Yourself",
        "Rock - Queen: We Will Rock You",
        "K-Pop - Hearts2Hearts: Style",
        "K-Pop - IVE: Rebel Heart"
    ],
    "relaxed": [
        "Classical - Mozart: Eine kleine Nachtmusik",
        "Chillhop - Lofi Beats: Study Session",
        "Acoustic - Ed Sheeran: Perfect",
        "Jazz - Norah Jones: Don’t Know Why",
        "Classical - Beethoven: Symphony No.9",
        "K-Pop - Girls' Generation: Lion Heart"
    ],
    "romantic": [
        "Pop - Bruno Mars: Just the Way You Are",
        "Pop - Ed Sheeran: Thinking Out Loud",
        "Acoustic - John Legend: All of Me",
        "Jazz - Frank Sinatra: Fly Me to the Moon",
        "Pop - Shania Twain: You're Still the One",
        "K-Pop - TWICE: What is Love?"
    ],
    "angry": [
        "Rock - Nirvana: Smells Like Teen Spirit",
        "Metal - Metallica: Enter Sandman",
        "Rock - Rage Against the Machine: Killing in the Name",
        "Punk - Green Day: American Idiot",
        "Hip-Hop - DMX: X Gon’ Give It to Ya",
        "K-Pop - Red Velvet: Psycho",
        "K-Pop - IVE: Accendio"
    ],
    "motivated": [
        "Hip-Hop - Kanye West: Stronger",
        "Rock - Survivor: Eye of the Tiger",
        "Pop - Katy Perry: Roar",
        "Hip-Hop - Drake: Started From the Bottom",
        "EDM - Avicii: Wake Me Up",
        "K-Pop - aespa: Live My Life"
    ],
    "sleepy": [
        "Lo-Fi - Lofi Girl: Sleepy Beats",
        "Classical - Debussy: Clair de Lune",
        "Acoustic - Jack Johnson: Banana Pancakes",
        "Ambient - Brian Eno: Ambient 1",
        "Jazz - Bill Evans: Peace Piece",
        "K-Pop - TAEYEON: 11:11",
        "Indie - Penny: Lighter 打火机"
    ],
    "party": [
        "EDM - Calvin Harris: Summer",
        "Pop - Pitbull ft. Kesha: Timber",
        "Dance - Lady Gaga: Just Dance",
        "Hip-Hop - Nicki Minaj: Starships",
        "EDM - The Chainsmokers: Closer",
        "K-Pop - i-dle: Queencard",
        "K-Pop - BIGBANG: BANG BANG BANG"
    ]
}

while True:
    mood = input("\nHow do you feel today? (Type 'quit' to stop / happy, sad, energetic, relaxed, romantic, angry, motivated, sleepy, party): ")
    mood = mood.lower().strip()

    if mood == 'quit':
        print("Thank you for using the Music Genre Recommender! 🎵")
        break

    if mood in music_db:
        time.sleep(1)
        print(f"Got it! You are feeling {mood}.")
        suggestion = random.choice(music_db[mood])
        print(f"\nBased on your mood, we recommend: {suggestion} 🎧")
        
        time.sleep(1)
        again = input("\nWould you like another recommendation? (yes/no): ").lower().strip()
        if again != 'yes':
            print("\nThanks for using the Music Genre Recommender! 🎵")
            break

    else:
        print(f"'{mood}' is not a valid option. Please try again.")
        print("Please try again with: happy, sad, energetic, relaxed, romantic, angry, motivated, sleepy, party.")
