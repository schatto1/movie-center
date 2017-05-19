import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
# print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://resizing.flixster.com/5x1smnlGnkJxJ2x5iRnCn7t1Y2k=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDA5OzEyMDA7ODAwOzEyMDA",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
# print(avatar.storyline)
# avatar.show_trailer()
moana = media.Movie("Moana",
                    "An adventurous teenager sails out on a daring mission to save her people.",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
# print(moana.storyline)
# moana.show_trailer()

tangled = media.Movie("Tangled",
                      "When the kingdom's most-wanted bandit, Flynn Rider (Zachary Levi), hides in a convenient tower, he immediately becomes a captive of Rapunzel (Mandy Moore), the spire's longtime resident.",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcSukZhxL8HfXfR5r-yCxq6Ct4Er8yx6juL8P3lvuHn42XdxF7JH",
                      "https://www.youtube.com/watch?v=ip_0CFKTO9E")
# print(tangled.storyline)
# tangled.show_trailer()

kiki = media.Movie("Kiki's Delivery Service",
                   "In this anime feature, 13-year-old Kiki (Kirsten Dunst) moves to a seaside town with her talking cat, Jiji (Phil Hartman), to spend a year alone, in accordance with her village's tradition for witches in training.",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcSDSJj2zOLZWJJn33hCydMght9TVIEAj5EbU-TqB584bLriw4vD",
                   "https://www.youtube.com/watch?v=4bG17OYs-GA")
# print(kiki.storyline)
# kiki.show_trailer()

laputa = media.Movie("Laputa: The Castle in the Sky",
                   "Follow the adventures of a young boy and girl attempting to keep a magic crystal from a group of military agents, while searching for a legendary floating castle.",
                   "http://t3.gstatic.com/images?q=tbn:ANd9GcRdajvHzODMm_1oGN_76hQIpfCVaMdKkiffcyKU68rMqspsXx9B",
                   "https://youtu.be/LMZe7EDsaiU")
# print(laputa.storyline)
# laputa.show_trailer()

movies = [toy_story, avatar, moana, tangled, kiki, laputa]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
