from bs4 import BeautifulSoup
import lxml

def parseHtml(pageSource):
    return BeautifulSoup(pageSource, 'lxml')

def get_img_tags(pageSource):
    parsedHtml = parseHtml(pageSource)
    imgTags = parsedHtml.find_all('img')
    return imgTags