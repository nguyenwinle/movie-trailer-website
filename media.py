import webbrowser #calling for webbrowser module


class Movie(): #created a class called Movie 
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movies_rating): #constructor
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = movies_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
