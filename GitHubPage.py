from selenium.webdriver.common.keys import Keys
import time

class GitHubPage:
    def __init__(self, driver):
        self.driver = driver

    def clickLink(self, driver, xpath, index):
        links = driver.find_elements_by_xpath(xpath)
        currentLink = links[index]
        currentLink.click()
        errorMessahe = driver.find_elements_by_id("parallax_error_text")
        return len(errorMessahe) == 0

    def goBackToSearchPage(self, driver):
        driver.back()

    def navigateToSite(self, driver, site):
        driver.get(site)

    def searchInGithub(self, driver, xpath, keyword):
        searchBox = driver.find_element_by_xpath(xpath)
        searchBox.send_keys(keyword)
        searchBox.send_keys(Keys.ENTER)

    def makeJson(self, title, description, tags, time, language, stars):
        jsonDictionary = {'title': '', 'description': '', 'tags': '', 'time': '', 'language': '', 'stars': ''}
        jsonDictionary['title'] = title
        jsonDictionary['description'] = description
        jsonDictionary['tags'] = tags
        jsonDictionary['time'] = time
        jsonDictionary['language'] = language
        jsonDictionary['stars'] = stars
        return jsonDictionary

    def getLanuguages(self, driver):
        languagesBar = driver.find_element_by_xpath("//div[@title='Click for language details']")
        languagesBar.click()
        time.sleep(1)
        languages = driver.find_elements_by_xpath("//a[@data-ga-click='Repository, language stats search click, location:repo overview']/span")
        languagesString = "";
        length = len(languages)
        #for i in languages:
            #languagesString += i.text + ' '
        for i in range(0,length):
            if languages[i].text != "":
                languagesString += languages[i].text + ' '
        return languagesString

    def storeDataFromPage(self, driver):
        title = driver.find_element_by_xpath("//span[@class='author']/a").text
        titlePrefix = driver.find_element_by_xpath("//strong[@itemprop='name']/a").text
        title = title  + '/' + titlePrefix
        description = driver.find_element_by_xpath("//span[@itemprop='about']").text
        # tags are plural elements
        tags = driver.find_elements_by_xpath("//div[@class='list-topics-container f6 mt-1']/a")
        tagsListString = '';
        for i in tags:
            if i.text != "":
                tagsListString += i.text + '. '
        time = driver.find_element_by_xpath("//span[@itemprop='dateModified']/relative-time").text
        language = self.getLanuguages(driver)
        stars = driver.find_element_by_xpath("//li/a[@class='social-count js-social-count']").text
        jsonToStore = self.makeJson(title, description, tagsListString, time, language, stars)
        return jsonToStore
