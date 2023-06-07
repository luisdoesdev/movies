import media

import fresh_tomatoes

seven_samurai = media.Movie(
    "Seven Samurai", "Seven Samurai help a village against bandit",
    "http://2.bp.blogspot.com/-tbI9Z7tqdmw/T0PUbMFBROI/AAAAAAAABIY/Ip28mqmZaUQ/s1600/Shichinin-no-samurai+1.jpg",  # noqa
    "https://www.youtube.com/watch?v=wJ1TOratCTo&disable_polymer=true",
    "100")

sanjuro = media.Movie("Sanjuro", "A lonely samurai helps a family", "https://s3.amazonaws.com/criterion-production/release_boxshots/1792-c9b9b35636a0769bf266c5376a1c5692/Sanjuro_wrap-1_original.jpg",  # noqa
    "https://www.youtube.com/watch?v=ZHIRcbAMFHo", "100")

high_low = media.Movie(
    "High and Low",
    "Toshiro Mifune stars as a wealthy industrialist whose family becomes\
     the target of a ruthless kidnapper",
    "https://upload.wikimedia.org/wikipedia/en/6/6a/HIGH_AND_LOW_JP_.jpg",
    "https://www.youtube.com/watch?v=LV3z2Ytxu90", "94")

casablanca = media.Movie("Casablanca", "Rick Blaine who owns a nightclub in \
    Casablanca, discovers his old flame Ilsa is in town with her husband, \
    Victor Laszlo. Laszlo is a famed rebel, and with Germans on his tail,\
    Ilsa knows Rick can help them get out of the country.",
    "https://m.media-amazon.com/images/M/MV5BY2IzZGY2YmEtYzljNS00NTM5LTgwMzUtMzM1NjQ4NGI0OTk0XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=PD9HDwMcfRE&disable_polymer=true", "97")

toy_story = media.Movie(
    "Toy Story",
    "A story about a kid and his toys that come to life",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",  # noqa
    "https://youtu.be/v-PjgYDrg70&disable_polymer=true", "100"
)

akira = media.Movie(
    "Akira",
    "Shotaro Kaneda, a leader of a local biker gang who must stop\
     his friend Tetsuo Shima from using his newly awakened superpowers \
     to release the titular esper",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcS6hoa1ePkqSULxJOKdO3O1PriRxrl5bOYT5owZJsh7FDwCPDrW",  # noqa,
    "https://youtu.be/nA8KmHC2Z-g", "87")

paprika = media.Movie(
    "Paprika",
    'Dr. Atsuko Chiba works as a scientist by day and, under the code name\
     "Paprika" is a dream detective at night',
    "https://upload.wikimedia.org/wikipedia/en/1/16/Paprikaposter.jpg",
    "https://www.youtube.com/watch?v=yn7U1KIGeuQ", "84")



up = media.Movie(
    "UP",
    "A 78-year-old balloon salesman, is about to fulfill a lifelong dream",
    "http://static.rogerebert.com/uploads/movie/movie_poster/up-2009/large_zh9DXJhBdHVVaWiDURTipADamcK.jpg",  # noqa
    "https://youtu.be/ZE_V0g9q4g0&disable_polymer=true", "98")

parasite = media.Movie(
    "Parasite",
    "Greed and class discrimination threaten the newly formed symbiotic \
      relationship between the wealthy Park family and the destitute Kim clan.",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png",
    "https://youtu.be/isOGD_7hNIY", "99")


# This array holds all the movie objects
list_movies = [
    seven_samurai,
    sanjuro,
    high_low,
    casablanca,
    toy_story,
    up,
    akira,
    paprika,
    parasite
]

# call Media and the list of movies from the object
fresh_tomatoes.open_movies_page(list_movies)
