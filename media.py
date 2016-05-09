import webbrowser

class Movie():
	def __init__(self, title_in, story_in, poster_in, trailer_in):
		self.title = title_in
		self.storyline = story_in
		self.poster_image_url = poster_in
		self.trailer_youtube_url = trailer_in

	def show_trailer(self):
		webbrowser.open(self.trailer)