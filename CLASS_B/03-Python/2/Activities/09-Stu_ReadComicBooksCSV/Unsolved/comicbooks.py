# Modules
import os
import csv

# Prompt user for title lookup
book = input("What title are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "\09-Stu_ReadComicBooksCSV\Resources", "comic_books.csv")
#\09-Stu_ReadComicBooksCSV\Resources

print(csvpath)
# Set variable to check if we found the videojj
found = False

# * Search through the `comic_books.csv` to find the user's book.

# * If the CSV contains the user's title, then print out the title, the publisher name, and the year it was published.

#   * For example: `"Alien was published by DC Comics in 2015"`.

# * If the CSV does not contain the user's title, then print out a message telling them that their book could not be found.

#     * Set a variable to `False` to check if we found the comic book.

#     * In the `for` loop, change the variable to confirm that the comic book is found.