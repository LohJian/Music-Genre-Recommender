# Simple Music Genre Recommender
def main():
    print("Welcome to the Music Genre Recommender!")
    
    # Get user input
    genre = input("Enter your favourite genre (Pop/Rock/HipHop): ").strip().capitalize()
    
    # Simple if/else logic to provide a recommendation
    if genre == "Pop":
        print("Recommendation: Taylor Swift")
    elif genre == "Rock":
        print("Recommendation: Queen")
    elif genre == "Hiphop":
        print("Recommendation: Kendrick Lamar")
    else:
        print(f"Recommendation: Check out the top artists in {genre}!")

# This line makes the program run
if __name__ == "__main__":
    main()