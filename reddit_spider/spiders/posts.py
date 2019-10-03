# -*- coding: utf-8 -*-
import scrapy
import datetime 


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.reddit.com/r/ProgrammerHumor/top/?t=all']
    start_urls = ['https://www.reddit.com/r/ProgrammerHumor/top/?t=all']

    # to display top posts of all time - 'https://www.reddit.com/r/ProgrammerHumor/top/?t=all'
    # to display top posts of today - 'https://www.reddit.com/r/ProgrammerHumor/top'

   
    def parse(self, response):
    	# copy and pasting xpath from chrome works for title too
        title = response.xpath('//title/text()').extract_first()

        # prints post names
        h3 = response.xpath('//h3/text()').extract()

        currentDT = datetime.datetime.now()

        #xpaths cant be copied and pasted for loops bc they are unique to each post

        print '\n\n************************************************************\n'
        print title
        print currentDT

        #doesnt work - more zoomed out div class = rpBJOHq2PR60pnwJlUyP0
        # class right above h3 in each container - _2SdHzo12ISmrC8H86TgSCp uWdXen_41bh0iwLrgzFkc 
        # doesnt work - posts = response.xpath('//*[@class="_2SdHzo12ISmrC8H86TgSCp uWdXen_41bh0iwLrgzFkc"]')
        posts = response.xpath('.//*[@class="_eYtD2XCVieq6emjKBH3m"]')
        i = 0

        # TODO getting index out of range, tired while loop inside for and didnt work.
        #while loop can be used in place of for loop
        for post in posts:
        	#returns first post in plain text
        	#print response.xpath('//h3/text()').extract_first()
        	
        	#extracting using position number
            postTitle = response.xpath('.//h3/text()').extract()[i]
            upvotes = response.xpath('.//*[@class = "_1rZYMD_4xY3gRcSS3p8ODO"]/text()').extract()[i]
            comments = response.xpath('.//*[@class = "FHCV02u6Cp2zYL0fhQPsO"]/text()').extract()[i]
            postTime = response.xpath('.//*[@class = "_3jOxDPIQ0KaOWpzvSQo-1s"]/text()').extract()[i]
            postUser = response.xpath('.//*[@class = "_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE"]/text()').extract()[i]

            #_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE
            i += 1

            print '\n------------------------------------------------------------\n'
            print 'Post #' + str(i)
            print postTitle
            print 'Upvotes: ' + str(upvotes)
            print 'Comments: ' + str(comments)
            print 'Posted ' + str(postTime)
            print 'Posted by: ' + str(postUser)

            #doesnt work
            #yield scrapy.FormRequest('https://www.reddit.com/', method='POST')

        #didnt work to send post request
        

        print '\n\n************************************************************\n'

        #prints last one then gets some error 

        #yield data
