import fresh_tomatoes
import media

#mutiple instances created
spiderman = media.Movie("Spiderman: Homecoming",
                        "Young Peter Parker (Tom Holland) navigates his way through high school while fighting crime as Spider-Man.",
                        "http://pre02.deviantart.net/adb5/th/pre/i/2016/106/a/f/poster_spiderman__homecoming_by_batcrazyman-d9z63fn.jpg",
                        "https://youtu.be/n9DwoQ7HWvI",
                        "PG-13")


transformers = media.Movie("Transformers: The Last Knight",
                        "Age of Extinction left off, with Optimus Prime heading out into space with the....",
                        "http://media.comicbook.com/2016/12/transformers-5-last-knight-poster-1-by-burakrall-da77k79-215279.jpg",
                        "https://www.youtube.com/watch?v=qLA6cpLwr6A",
                           "PG-13")


guardians = media.Movie("Guardians of the Galaxy 2",
                        "Star-Lord (Chris Pratt) tries to find his true father.",
                        "http://pre15.deviantart.net/1f5c/th/pre/i/2015/228/d/5/guardians_of_the_galaxy_vol_2_by_batcrazyman-d95z0yz.jpg",
                        "https://youtu.be/dW1BIid8Osg",
                        "PG-13")


assassins_creed = media.Movie("Assassins Creed",
                        "Callum Lynch discovers he is a descendant of the secret Assassins society through unlocked genetic memories that allow him to relive the adventures of his ancestor, Aguilar, in 15th century Spain. After gaining incredible knowledge and skills he's poised to take on the oppressive Knights Templar in the present day.",
                        "http://vignette4.wikia.nocookie.net/assassinscreed/images/0/06/Assassin%27s_Creed_poster.jpg",
                        "https://youtu.be/zDQz0uUY14E",
                        "PG-13")


justice_league = media.Movie("Justice League",
                        "Batman, Superman, Wonder Woman, the Flash, Aquaman and Cyborg unite to battle the evil Steppenwolf.",
                        "http://pre10.deviantart.net/a275/th/pre/f/2016/206/2/c/justice_league__2017____poster___1_by_camw1n-dab9vpk.png",
                        "https://youtu.be/fIHH5-HVS9o",
                        "PG-13")


wonder_woman = media.Movie("Wonder Woman",
                        "After leaving her all-female island, Wonder Woman discovers her full powers and true destiny while fighting alongside soldiers during World War I.",
                        "http://s3.birthmoviesdeath.com/images/made/Wonder-Woman-Poster_1200_1778_81_s.jpg",
                        "https://youtu.be/Tgk_63b-Mrw",
                        "PG-13")


#list or array of instances created
movies = [spiderman, transformers, guardians, assassins_creed, justice_league, wonder_woman]

fresh_tomatoes.open_movies_page(movies)
