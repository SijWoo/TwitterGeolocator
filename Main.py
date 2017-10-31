from twitterBot import TweetCollector
from visualBar import graphCityStats
class cityLocal:
    def __init__(self, longitude= 30.275579, latitude= -97.743871, radius= 6, name= "austin"):
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
        self.name = name

if __name__ == "__main__":
    searchCount = int(input("Enter how many searches you want to do: "))
    searchArray = []
    tweetArray = []
    for i in range (0, searchCount):
        longitude = float(input("Enter a longitude to search: "))
        latitude = float(input("Enter a latitude to search: "))
        radius = float(input("Enter a search radius: "))
        name = input("Enter the name of the city: ")
        searchArray.append(cityLocal(longitude, latitude, radius, name))

    for i in range (0, searchCount):
        print(searchArray[i].name, ",", searchArray[i].longitude, "," , searchArray[i].latitude, "," , searchArray[i].radius)

    tweetBot = TweetCollector()
    tweetsPerCity = []
    for i in range(0,searchCount):
        tweetsPerCity.append(tweetBot.getTweets("help", searchArray[i]))
    
    polarity = []
    subjectivity = []
    for setOfTweets in tweetsPerCity:
        polarity.append(TweetCollector.getAveragePolarity(setOfTweets))
        subjectivity.append(TweetCollector.getAverageSubjectivity(setOfTweets))

    names = [city.name for city in searchArray]
    graphCityStats(names, polarity, subjectivity)
