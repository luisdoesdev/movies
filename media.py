import webbrowser

# create a class movie to organize the properties of an object


# class
class Movie():
    """ function to "init"iate  the class """
    def __init__(self, title, movie_desc, poster_image_url,
                 trailer_youtube_url, movie_rating):

            self.title = title
            self.movie_desc = movie_desc
            self.poster_image_url = poster_image_url
            self.trailer_youtube_url = trailer_youtube_url
            self.movie_rating = movie_rating

# fuction to call YouTube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
