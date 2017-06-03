# Luis's Favorite Movies

A website where all  my favorite movies live

## Getting started

To get up and running clone this repo into your machine.

### Prerequisites

Python 2.7 and its standar libraries

## Structure

Most of the websites document structure lives in "fresh_tomatoes.py"

The websites objects come from the "entertainment_center.py", if you wanted to add more movies to the sites this will be the place.

You will do so by naming your object eg "hello_kitty" and calling the class "Movie" whsich is located in media.py:

		hello_kitty = media.Movie

This class has five attributes in this attributes you will contain the following: "title", "story",poster_image_url and trailer_you_tube_url:

		hello_kitty = media.Movie(
				"Hello Kitty", "Hello Kitty story description",
				"Hello Kitt poster image url", "Hello Kitty's trailer youtube url")



Finally all the movies are stored in an array called "list"

		list = [movie1, 
			movie2, etc...]

You will add this array"list" in fresh_tomatoes.open_movies_page funtion wich will display the movies on the document.

		fresh_tomatoes.open_movies_page(list_movies)



## Running
to run the program: type "python entertainment_center.py" in terminal
