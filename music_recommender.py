import time 
import random

# 🎶 welcome message first

print("🎶 Welcome to Music Genre Recommender 🎶")
time.sleep(0.5)
print("We will suggest a music genre based on your mood!👨🏻‍🎤")
time.sleep(2)

mood=input("How was your feeling today?(sad, happy, relaxed or energetic,etc.):")
print(mood)
time.sleep(0.8)
print("Got it! You are feeling",mood)



music_db = {
    "happy": ["Pop - Taylor Swift", "Dance - BTS", "K-Pop - BLACKPINK"],
    "sad": ["Blues - B.B. King", "Lo-Fi - Chillhop", "Jazz - Miles Davis"],
    "energetic": ["Rock - Linkin Park", "EDM - Martin Garrix", "Hip-Hop - Eminem"],
    "relaxed": ["Classical - Mozart", "Chillhop - Lofi Beats", "Acoustic - Ed Sheeran"]
}

suggestion = random.choice(music_db[mood])
print(f"\n✅ Based on your mood({mood}), we recommend: {suggestion} 🎧")
