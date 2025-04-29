from flask import Flask, render_template

app = Flask(__name__)

boss_locations = {
    "Lorencia": [
        {"name": "Golden Budge Dragon", "place": "Lorencia 1", "boxes": []},
        {"name": "Golden Goblin", "place": "Lorencia 2", "boxes": []},
        {"name": "Golden Rabbit", "place": "Lorencia 3", "boxes": []},
    ],
    "Noria": [
        {"name": "Golden Titan", "place": "Noria 1", "boxes": []},
        {"name": "Golden Goblin", "place": "Noria 2", "boxes": []},
    ],
    "Devias": [
        {"name": "Golden Soldier", "place": "Devias 1", "boxes": []},
        {"name": "Golden Goblin", "place": "Devias 2", "boxes": []},
    ],
    "Dungeon": [
        {"name": "Golden Derkon", "place": "Dungeon 1", "boxes": []},
    ],
    "Lost Tower": [
        {"name": "Golden Wheel", "place": "Lost Tower 1", "boxes": []},
        {"name": "Golden Dark Knight", "place": "Lost Tower 2", "boxes": []},
        {"name": "Golden Devil", "place": "Lost Tower 3", "boxes": []},
    ],
    "Atlans": [
        {"name": "Golden Lizard King", "place": "Atlans 1", "boxes": []},
        {"name": "Golden Vepar", "place": "Atlans 2", "boxes": []},
    ],
    "Tarkan": [
        {"name": "Golden Tantalos", "place": "Tarkan 1", "boxes": []},
        {"name": "Golden Stone Golem", "place": "Tarkan 2", "boxes": []},
        {"name": "Great Golden Dragon", "place": "Tarkan 1 or 2", "boxes": []},
    ],
    "Icarus": [
        {"name": "Golden Crust", "place": "Icarus 1", "boxes": []},
    ],
    "Aida": [
        {"name": "Golden Iron Knight", "place": "Aida 1", "boxes": []},
    ],
    "Kanturu": [
        {"name": "Golden Satyros", "place": "Kanturu 1", "boxes": []},
        {"name": "Golden Twin Tail", "place": "Kanturu 2", "boxes": []},
        {"name": "Golden Napin", "place": "Kanturu 3", "boxes": []},
    ],
}

@app.route("/")
def index():
    return render_template("index.html", boss_locations=boss_locations)

if __name__ == "__main__":
    app.run(debug=True)
