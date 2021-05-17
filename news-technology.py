import requests as req
import pymsteams

request = req.get("http://newsapi.org/v2/top-headlines",
                  headers={'X-Api-Key': '<YOUR API KEY>'},
                  params={'country': 'in', 'category': 'technology'},
                  )
response = request.json()

webhookConnection = pymsteams.connectorcard("<YOUR WEBHOOK URL>")


def get_News():
    articles = response['articles']
    i =0
    while i < len(articles):
        News = articles[i]
        title = News['title']
        description = News['description']
        publishedAt = News['publishedAt']
        content = News['content']
        url = News['url']
        image = News['urlToImage']
        i = i + 1
        message = create_Message(title, image, description, url,content,publishedAt)
        send_Message(message)
    webhookConnection.send()


def create_Message(title, image, description, url,content,publishedAt):
    messageCard = pymsteams.cardsection()
    messageCard.activityTitle(title)
    messageCard.addImage(image)
    messageCard.activitySubtitle(description)
    messageCard.text(content)
    messageCard.activityText(publishedAt)
    messageCard.linkButton('more info', url)
    messageCard.text(" ")
    return messageCard


def send_Message(messageCard):
    webhookConnection.addSection(messageCard)
    webhookConnection.summary(" ")


if __name__ == '__main__': get_News()
