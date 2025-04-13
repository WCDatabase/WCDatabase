import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Tag": [
        "Comedy", "Fantasy", "Drama", "Romance", "Adventure", "Action", "Sci-Fi", "Slice of life", "Furry",
        "LGBT+", "Horror", "Gaming", "Crazy", "Real-Life", "Manga", "Parody or Satire", "Anime", "Supernatural",
        "Geeky", "BL", "Thriller", "Superheroes", "Mystery", "Heartwarming", "Historical", "Animals", 
        "Mystery or Noir", "Workplace", "Spiritual", "Short story", "Crime/Mystery", "Political", "GL",
        "Fan Fiction", "Magic", "School", "Post-apocalyptic", "Pokémon", "Monsters", "All Ages", "Gag-a-Day",
        "Informative", "Erotic", "Alien", "Color", "Demons", "Cats", "Space", "Zombies", "Inspirational", 
        "PMD", "Dragon", "Surreal", "Sports", "Ghosts", "Vampire", "Black and White", "Angels", "Superpowers",
        "Witches", "Wolves", "Dogs", "Robots", "Tragedy", "High School", "Werewolves", "Mythology", "Urban",
        "Spirits", "Elves", "Warrior Cats", "Medieval", "Graphic Novel", "Short", "Knights", "Adult", "Dark",
        "Anthology", "Psychological", "Detective", "Apocalypse", "Mental Health", "Wizards", "Foxes", "Sex",
        "Steampunk", "Fairies", "Pirates", "Time Travel", "Warriors", "Dinosaurs", "Family", "DnD", "Birds",
        "Cyberpunk", "Depression", "Rabbits", "Androids", "Drugs", "Bounty Hunters"
    ],
    "Count": [
        19683, 19534, 12591, 11994, 10317, 9730, 8103, 6441, 4425, 3720, 3511, 3124, 2814, 2349, 2270, 2173, 1994,
        1950, 1930, 1794, 1710, 1683, 1144, 949, 841, 837, 830, 816, 741, 702, 624, 545, 521, 502, 462, 444, 330,
        316, 275, 262, 238, 201, 188, 173, 171, 171, 167, 162, 156, 150, 138, 131, 117, 108, 90, 79, 79, 77, 74,
        69, 60, 60, 57, 56, 56, 54, 49, 45, 45, 44, 43, 42, 39, 39, 38, 37, 37, 37, 35, 34, 31, 31, 30, 30, 30,
        29, 29, 29, 25, 24, 23, 23, 22, 22, 21, 21, 21, 20, 20, 20
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort by count descending and pick top 15
top_tags = df.sort_values(by="Count", ascending=False).head(15)

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.barh(top_tags["Tag"][::-1], top_tags["Count"][::-1], color="#66cc5e", edgecolor="#296f21")

# Style
plt.gca().set_facecolor('#2a2a2a')
plt.gcf().patch.set_facecolor('#2a2a2a')
plt.xticks(color='white')
plt.yticks(color='white')
plt.title("Top 15 Most Used Webcomic Tags (wcdatabase.com)", color='white')
plt.xlabel("Number of Uses", color='white')

for bar in bars:
    plt.text(bar.get_width() + 300, bar.get_y() + bar.get_height()/2, f'{bar.get_width()}', va='center', color='white')

plt.tight_layout()
plt.grid(visible=False)
plt.box(False)

# Save image
plt.savefig("top_webcomic_tags_chart15.png", dpi=300, bbox_inches='tight')
plt.show()