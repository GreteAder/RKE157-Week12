import sqlite3

def get_allgaames():

   with sqlite3.connect("db/TopGamesDB (1).db") as connection:
      cursor = connection.cursor()
     
      cursor.execute("""
      SELECT id, name , releaseYear
      From Game
      ORDER by id;
      """)

      return cursor.fetchall()

def get_games_with_genres():

   with sqlite3.connect("db/TopGamesDB (1).db") as connection:
      cursor = connection.cursor()
     
      cursor.execute("""
     SELECT Game.name, Genre.name
     FROM Game
     JOIN GenreInGame ON Game.id = GenreInGame.gameId
     JOIN Genre ON Genre.id = GenreInGame.genreId
     ORDER BY Game.name, Genre.name;
      """)

      return cursor.fetchall()

games = get_games_with_genres()

def search_games(keyword):

    with sqlite3.connect("db/TopGamesDB (1).db") as connection:
        cursor = connection.cursor()

        keyword_lower = keyword.lower()

        cursor.execute("""
            SELECT id, name, releaseYear
            FROM Game
            WHERE LOWER(name) LIKE ?
            ORDER BY name;
        """, (f"%{keyword_lower}%",))

    return cursor.fetchall()


games = search_games("witcher")

for game in games:
    print(game)