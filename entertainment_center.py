import media
import fresh_tomatoes

bambi = media.Movie("Bambi", 
						"Only you can prevent forest fires", 
						"https://upload.wikimedia.org/wikipedia/en/thumb/8/88/Walt_Disney%27s_Bambi_poster.jpg/220px-Walt_Disney%27s_Bambi_poster.jpg",
						"https://www.youtube.com/watch?v=uFJz2IMUeDE")

eraserhead = media.Movie("Eraserhead",
						"A man with strange hair has a deformed mutant child",
						"https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Eraserhead.jpg/220px-Eraserhead.jpg",
						"https://www.youtube.com/watch?v=dU7OqGCIcak")

the_thing = media.Movie("The Thing",
						"An alien being that can assume the form of those it kills terrorizes Kurt Russell",
						"https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/ThingPoster.jpg/220px-ThingPoster.jpg",
						"https://www.youtube.com/watch?v=F7t-919Ec9U")

# movie list used to dynamically generate page
movies = [bambi, eraserhead, the_thing]

fresh_tomatoes.create_movie_tiles_content(movies)

fresh_tomatoes.open_movies_page(movies)