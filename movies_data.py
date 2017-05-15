import requests
import json





#call the request
def get(mov):
    url = "http://www.omdbapi.com/?t="
    response = requests.get(url+mov)
    #return JSON data
    jData = json.loads( response.content)
    return jData

#movies
toy_story = "toy+story" 
seven_samurai = "seven_samurai"









