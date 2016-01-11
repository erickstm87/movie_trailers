#!/usr/bin/python
import fresh_tomatoes
import media

Dial_M = media.Movie("Dial M for Murder", "To pull off the perfect murder", "http://www.homevideos.com/movies-covers/dialm.jpg", "https://www.youtube.com/watch?v=JWP_hrNHSN4")
Fight_Club = media.Movie("Fight Club", "Please Don't Discuss It!",'http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_UY1200_CR88,0,630,1200_AL_.jpg','https://www.youtube.com/watch?v=SUXWAEX2jlg')
Zombieland = media.Movie("Zombieland", "A riveting tale of zombies and his struggle with women","http://www.sonypictures.com/movies/zombieland/assets/images/onesheet.jpg","https://www.youtube.com/watch?v=8m9EVP8X7N8")
O_Brother = media.Movie('O Brother Where Art Thou', 'A mans return to his home', 'https://upload.wikimedia.org/wikipedia/en/5/5b/O_brother_where_art_thou_ver1.jpg', 'https://www.youtube.com/watch?v=eW9Xo2HtlJI')
Midnight_Paris = media.Movie('Midnight in Paris', 'The Lost Generation comes to life', 'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg', 'https://www.youtube.com/watch?v=FAfR8omt-CY')
No_Country = media.Movie('No Country for Old Men','Brutality','http://baldmove.com/wp-content/uploads/2015/09/no-country-for-old-men.jpg','https://www.youtube.com/watch?v=38A__WT3-o0')
#print (Zombieland.trailer_youtube_url)
#O_Brother.show_trailer()
movies = [Dial_M, Fight_Club, Zombieland, O_Brother, Midnight_Paris, No_Country]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.__doc__)
