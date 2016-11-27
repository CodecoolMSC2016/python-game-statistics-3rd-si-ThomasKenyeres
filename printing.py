from reports import *

# Printing functions
print("There are " + str(count_games("game_stat.txt")) + " in the file")
print("It's " + str(decide("game_stat.txt", 1989)) + " that there's at least one game of the given year")
print("The game from the latest year is " + str(get_latest("game_stat.txt")))
print("There are " + str(count_by_genre("game_stat.txt", "First-person shooter")) + " of the given genre")
print("The line number of the given name is: " + str(get_line_number_by_title("game_stat.txt", "Minecraft")))
print("\nGames in alphabetical order: " + str(sort_abc("game_stat.txt")))
print("\nGenres: " + str(get_genres("game_stat.txt")))
print("Release date of top sold fps: " + str(when_was_top_sold_fps("game_stat.txt")))
