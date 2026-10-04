import sqlite3

import sqlite3


def get_games_by_publisher(publisher_name):

    with sqlite3.connect("db/TopGamesDB (1).db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Game.releaseYear, Publisher.name
            FROM Game
            JOIN GamePublisher ON Game.id = GamePublisher.gameId
            JOIN Publisher ON Publisher.id = GamePublisher.publisherId
            WHERE LOWER(Publisher.name) = LOWER(?)
            ORDER BY Game.name;
        """, (publisher_name,))

        return cursor.fetchall()


games = get_games_by_publisher("Nintendo")


for game in games:
    print(f"Game: {game[0]}, {game[1]}, {game[2]}")
    