import time
from GitHubPage import GitHubPage
from pymongo import MongoClient
from selenium import webdriver

# Initializations -------------------
githubHome = "https://github.com/"
keyword = 'selenium'
driver = webdriver.Chrome('C:\JavaGrid\chromedriver')

#the testScenario-----------------------------
page = GitHubPage(driver)
page.navigateToSite(driver, githubHome)
startSearchQueryTime = time.time() # Timing the search Query
searchButtonXpath = "//input[@data-unscoped-placeholder='Search GitHub']"
page.searchInGithub(driver,searchButtonXpath , keyword)
endSearchQueryTime = time.time()
totalTime = round(endSearchQueryTime - startSearchQueryTime, 3)
outputMessage = "The search query has lasted for %s milliseconds"
print(outputMessage%totalTime)
# Connent to mongo Data Base----------------------
client = MongoClient('mongodb://localhost:1111/')
db = client.test_database # getting the data base
collection = db.test_collection # Getting the collection
posts = db.posts # Inserting a Document
isValidPage = True
print("Result of run time and data that is added to Mongo DB")
for i in range(0,5):
    clickOnPageLinkTime = time.time()  # Timing from the moment you click on the link until it appears
    isValidPage &= page.clickLink(driver, "//ul[@class='repo-list']/div/div/h3/a", i)
    clickOnPageLinkEndTime = time.time()
    totalTimeOfPageLoad = round(clickOnPageLinkEndTime - clickOnPageLinkTime, 3)
    pageLoadOutputMessage = "Page #%d load has lasted for %s milliseconds"
    print(pageLoadOutputMessage % (i+1,totalTimeOfPageLoad))
    outcomeDictionary = page.storeDataFromPage(driver)
    post_id = posts.insert_one(outcomeDictionary).inserted_id
    print(outcomeDictionary)
    page.goBackToSearchPage(driver)
assert isValidPage, "One of the pages contains 404 message"



