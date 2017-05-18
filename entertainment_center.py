import media

import fresh_tomatoes

seven_samurai = media.Movie(
    "Seven Samurai", 
    "Seven Samurai help a village against bandit",
    "http://2.bp.blogspot.com/-tbI9Z7tqdmw/T0PUbMFBROI/AAAAAAAABIY/Ip28mqmZaUQ/s1600/Shichinin-no-samurai+1.jpg",
    "https://www.youtube.com/watch?v=VDUjDPt9w0w&disable_polymer=true")

sanjuro = media.Movie("Sanjuro",
    "A lonely samurai helps a family", 
    "https://s3.amazonaws.com/criterion-production/release_boxshots/1792-c9b9b35636a0769bf266c5376a1c5692/Sanjuro_wrap-1_original.jpg",
    "https://www.youtube.com/watch?v=ZHIRcbAMFHo")

casablanca = media.Movie("Casablanca",
    "Rick Blaine who owns a nightclub in Casablanca, discovers his old flame Ilsa is in town with her husband, Victor Laszlo. Laszlo is a famed rebel, and with Germans on his tail, Ilsa knows Rick can help them get out of the country.",
    "http://resizing.flixster.com/qwlwwAU7mmOZFuZfyJe6pJV5CAE=/800x1200/v1.bTsxMTE2ODEwMTtqOzE3NDEwOzIwNDg7ODAwOzEyMDA",
    "https://www.youtube.com/watch?v=PD9HDwMcfRE&disable_polymer=true"

)

toy_story = media.Movie(
    "Toy Story",
    "A story about a kid and his toys that come to life",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
    "https://www.youtube.com/watch?v=vwyZH85NQC4&disable_polymer=true"
)

akira = media.Movie(
    "Akira",
    "Shotaro Kaneda, a leader of a local biker gang who must stop his friend Tetsuo Shima from using his newly awakened superpowers to release the titular esper",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcS6hoa1ePkqSULxJOKdO3O1PriRxrl5bOYT5owZJsh7FDwCPDrW",
    "https://www.youtube.com/watch?v=7mdMtuGL7eg"
)

paprika = media.Movie(
    "Paprika",
    'Dr. Atsuko Chiba works as a scientist by day and, under the code name "Paprika" is a dream detective at night',
    "http://img.moviepostershop.com/paprika-movie-poster-2006-1020689313.jpg",
    "https://www.youtube.com/watch?v=1wOrvd_ylDY"
)

high_low = media.Movie(
    "High and Low",
    "Toshiro Mifune stars as a wealthy industrialist whose family becomes the target of a ruthless kidnapper",
    "http://www.impawards.com/1963/posters/high_and_low.jpg",
    "https://www.youtube.com/watch?v=LV3z2Ytxu90"
)

up = media.Movie(
    "UP",
    "A 78-year-old balloon salesman, is about to fulfill a lifelong dream",
    "http://static.rogerebert.com/uploads/movie/movie_poster/up-2009/large_zh9DXJhBdHVVaWiDURTipADamcK.jpg",
    "https://www.youtube.com/watch?v=BDCSncUZxvs&disable_polymer=true"

)

list_movies = [
    seven_samurai,
    sanjuro,
    casablanca,
    toy_story,
    akira,
    paprika,
    high_low,
    up
]

#call Media



fresh_tomatoes.open_movies_page(list_movies)



# __init_ gets called
    # self = toy_story
    #movie_title = "Toy Story"
    #movie_storyline = "come to life"
    #poster_image = "Poster Link"
    #trailer_youtube_url = "link"