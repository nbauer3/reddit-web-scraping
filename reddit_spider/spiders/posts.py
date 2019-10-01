# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.reddit.com/r/ProgrammerHumor/']
    start_urls = ['https://www.reddit.com/r/ProgrammerHumor/']

 # yield not working w/ ROBOTSTXT_OBEY = True OR False so idk whats going on here
   
    def parse(self, response):
    	# copy and pasting xpath from chrome works for title too
        title = response.xpath('//title/text()').extract_first()

        # prints post names
        h3 = response.xpath('//h3/text()').extract()

        #old xpath class name might be regenerated but hasnt changed yet
        #posts = response.xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]')
        #post = response.xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]/text()').extract()

        #xpaths cant be copied and pasted for loops bc they are unique to each post
        data = {
        	'Title': title,
        	'Post': h3
        }

        print '\n\n************************************************************\n'
        print title

        #more zoomed out div class = rpBJOHq2PR60pnwJlUyP0
        posts = response.xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]')
        for post in posts:
        	#returns first post in plain text
        	#print response.xpath('//h3/text()').extract_first()

        	#_first() prints first post Title many times, extract prints all many times
        	#postTitle = response.xpath('.//h3/text()').extract_first()
        	postTitle = response.xpath('//h3/text()').extract_first()

	        print '\n\n------------------------------------------------------------\n'
	        print postTitle

        print '\n\n************************************************************\n'

        #for post in posts:
        	#text = post.xpath('')

        # returns a bunch of h1 h2 and h3's
        # response.xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]')

        #yield data
