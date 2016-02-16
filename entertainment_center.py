import media
import fresh_tomatoes
"""
Created six movie objects using class Movie from media.
"""
gone_girl = media.Movie("Gone Girl", 
	                    "Set in Southeast Missouri the story begins as a mystery that follows" 
	                    "the events surrounding Nick Dunne (Affleck), who becomes the primary suspect" 
	                    "in the sudden disappearance of his wife, Amy (Pike).",
	                    "https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
	                    "https://www.youtube.com/watch?v=1bwNPpKWBRk")


sex_and_the_city_1 = media.Movie("Sex and the City 1",
	                             " Four women's life in New York City",
	                             "https://upload.wikimedia.org/wikipedia/en/c/cb/Sex_and_the_City_The_Movie.jpg",
	                             "https://www.youtube.com/watch?v=g9Mx2OLnoGI")

sex_and_the_city_2 = media.Movie("Sex and the City 2",
	                             "Four Women's life in New York City",
	                             "https://upload.wikimedia.org/wikipedia/en/2/2d/Sex_and_the_City_2_poster.jpg",
	                             "https://www.youtube.com/watch?v=pY7sAJm8Fuk")

saving_private_ryan = media.Movie("Saving Private Ryan",
	                              "Saving Private Ryan is a 1998 American epic war drama film set "
	                              "during the Invasion of Normandy in World War II.",
	                              "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
	                              "https://www.youtube.com/watch?v=vwAxi4A2YcY")
benjamin_button = media.Movie("The Curious Case of Benjamin Button",
	                          "The storyline by Eric Roth and Robin Swicord is loosely based on the 1922 short story" 
	                          "of the same name by F. Scott Fitzgerald.",
	                          "https://upload.wikimedia.org/wikipedia/en/7/7d/Curious_case_of_benjamin_button_ver3.jpg",
	                          "https://www.youtube.com/watch?v=O6wP_LKA0DE")
cold_mountain = media.Movie("Cold Mountain",
	                        "The film tells the story of a wounded deserter from the Confederate army close the" 
	                        "end of the American Civil War, who is on his way to return to the love of his life.",
	                        "https://upload.wikimedia.org/wikipedia/en/2/2a/Cold_Mountain_Poster.jpg",
	                        "https://www.youtube.com/watch?v=uXGtunJ9Jqk")

#Created a Movie list and pass it to the function "open_movie_opage()"
movies = [gone_girl,saving_private_ryan, benjamin_button, 
          cold_mountain, sex_and_the_city_1, sex_and_the_city_2,]	                             
fresh_tomatoes.open_movies_page(movies)