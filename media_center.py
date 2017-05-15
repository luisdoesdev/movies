import webbrowser

#create a class movie to organize the properties of an object


#class
class Movie():
#function to "init"iate  the class    
    def __init__(self, movie_title, 
                movie_story, movie_poster, 
                trailer_youtube):

        self.title = movie_title
        self.story = movie_story
        self.poster = movie_poster
        self.trailer = trailer_youtube

#fuction to call YouTube trailer 
    def show_trailer():
        webbrowser.open(self.trailer_youtube)

"""=====
test to see if code is working

Declare the object 
movie = Movie("Toy Story",
                "",'',
              'https://www.youtube.com/watch?v=lKV_-ABu39M')

Call the object
webbrowser.open(movie.trailer)

=======
"""

          