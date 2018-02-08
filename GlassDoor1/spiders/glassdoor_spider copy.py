from scrapy import Spider
from scrapy.selector import Selector
from GlassDoor1.items import Glassdoor1Item
import re


class GlassdoorSpider(Spider):
    #Find links from top100 page 
    #overviews = response.xpath('//div[@class="employer-logo"]/a/@href').extract()
    reviewUrls = ['https://www.glassdoor.com/Reviews/Facebook-Reviews-E40772.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Google-EI_IE9079.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-lululemon-EI_IE42589.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-HubSpot-EI_IE227605.11,18.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Ultimate-Software-EI_IE7900.11,28.htm',
 'https://www.glassdoor.com/Reviews/SAP-Reviews-E10471.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Salesforce-EI_IE11159.11,21.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Delta-Air-Lines-EI_IE197.11,26.htm',
 'https://www.glassdoor.com/Reviews/Working-at-LinkedIn-EI_IE34865.11,19.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Southwest-Airlines-EI_IE611.11,29.htm',
 'https://www.glassdoor.com/Reviews/Working-at-NVIDIA-EI_IE7633.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-AvalonBay-Communities-EI_IE2616.11,32.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Paylocity-EI_IE29987.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Intuit-EI_IE2293.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Adobe-EI_IE1090.11,16.htm',
 'https://www.glassdoor.com/Reviews/Working-at-VMware-EI_IE12830.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-SAP-Concur-EI_IE8763.11,21.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Forrester-EI_IE6443.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Johnson-and-Johnson-EI_IE364.11,30.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Microsoft-EI_IE1651.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Ellie-Mae-EI_IE260441.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Hilton-EI_IE330.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Protiviti-EI_IE30849.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Oshkosh-Corporation-EI_IE1740.11,30.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Eli-Lilly-and-Company-EI_IE223.11,32.htm',
 'https://www.glassdoor.com/Reviews/Working-at-NIKE-EI_IE1699.11,15.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Monsanto-Company-EI_IE11986.11,27.htm',
 'https://www.glassdoor.com/Reviews/Working-at-United-Airlines-EI_IE683.11,26.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Electronic-Arts-EI_IE1628.11,26.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Zillow-EI_IE40802.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Roche-EI_IE3480.11,16.htm',
 'https://www.glassdoor.com/Reviews/Working-at-3M-EI_IE446.11,13.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Procter-and-Gamble-EI_IE544.11,29.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Guidewire-EI_IE122537.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Capital-One-EI_IE3736.11,22.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Hyatt-EI_IE2839.11,16.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Stryker-EI_IE1918.11,18.htm',
 'https://www.glassdoor.com/Reviews/Working-at-T-Mobile-EI_IE9302.11,19.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Travelers-EI_IE1904.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-CDW-EI_IE2347.11,14.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Accenture-EI_IE4138.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Apple-EI_IE1138.11,16.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Darden-EI_IE4160.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Taylor-Morrison-EI_IE37887.11,26.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Insperity-EI_IE3608.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Cisco-Systems-EI_IE1425.11,24.htm',
 'https://www.glassdoor.com/Reviews/Working-at-adidas-EI_IE10692.11,17.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Shell-EI_IE5833.11,16.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Starbucks-EI_IE2202.11,20.htm',
 'https://www.glassdoor.com/Reviews/Working-at-Walt-Disney-Company-EI_IE717.11,30.htm']

#Split links to get suffix:
#endUrls = list(map(lambda x: x.split('Reviews/')[1],reviewUrls))

endUrls = ['Facebook-Reviews-E40772.htm',
 'Working-at-Google-EI_IE9079.11,17.htm',
 'Working-at-lululemon-EI_IE42589.11,20.htm',
 'Working-at-HubSpot-EI_IE227605.11,18.htm',
 'Working-at-Ultimate-Software-EI_IE7900.11,28.htm',
 'SAP-Reviews-E10471.htm',
 'Working-at-Salesforce-EI_IE11159.11,21.htm',
 'Working-at-Delta-Air-Lines-EI_IE197.11,26.htm',
 'Working-at-LinkedIn-EI_IE34865.11,19.htm',
 'Working-at-Southwest-Airlines-EI_IE611.11,29.htm',
 'Working-at-NVIDIA-EI_IE7633.11,17.htm',
 'Working-at-AvalonBay-Communities-EI_IE2616.11,32.htm',
 'Working-at-Paylocity-EI_IE29987.11,20.htm',
 'Working-at-Intuit-EI_IE2293.11,17.htm',
 'Working-at-Adobe-EI_IE1090.11,16.htm',
 'Working-at-VMware-EI_IE12830.11,17.htm',
 'Working-at-SAP-Concur-EI_IE8763.11,21.htm',
 'Working-at-Forrester-EI_IE6443.11,20.htm',
 'Working-at-Johnson-and-Johnson-EI_IE364.11,30.htm',
 'Working-at-Microsoft-EI_IE1651.11,20.htm',
 'Working-at-Ellie-Mae-EI_IE260441.11,20.htm',
 'Working-at-Hilton-EI_IE330.11,17.htm',
 'Working-at-Protiviti-EI_IE30849.11,20.htm',
 'Working-at-Oshkosh-Corporation-EI_IE1740.11,30.htm',
 'Working-at-Eli-Lilly-and-Company-EI_IE223.11,32.htm',
 'Working-at-NIKE-EI_IE1699.11,15.htm',
 'Working-at-Monsanto-Company-EI_IE11986.11,27.htm',
 'Working-at-United-Airlines-EI_IE683.11,26.htm',
 'Working-at-Electronic-Arts-EI_IE1628.11,26.htm',
 'Working-at-Zillow-EI_IE40802.11,17.htm',
 'Working-at-Roche-EI_IE3480.11,16.htm',
 'Working-at-3M-EI_IE446.11,13.htm',
 'Working-at-Procter-and-Gamble-EI_IE544.11,29.htm',
 'Working-at-Guidewire-EI_IE122537.11,20.htm',
 'Working-at-Capital-One-EI_IE3736.11,22.htm',
 'Working-at-Hyatt-EI_IE2839.11,16.htm',
 'Working-at-Stryker-EI_IE1918.11,18.htm',
 'Working-at-T-Mobile-EI_IE9302.11,19.htm',
 'Working-at-Travelers-EI_IE1904.11,20.htm',
 'Working-at-CDW-EI_IE2347.11,14.htm',
 'Working-at-Accenture-EI_IE4138.11,20.htm',
 'Working-at-Apple-EI_IE1138.11,16.htm',
 'Working-at-Darden-EI_IE4160.11,17.htm',
 'Working-at-Taylor-Morrison-EI_IE37887.11,26.htm',
 'Working-at-Insperity-EI_IE3608.11,20.htm',
 'Working-at-Cisco-Systems-EI_IE1425.11,24.htm',
 'Working-at-adidas-EI_IE10692.11,17.htm',
 'Working-at-Shell-EI_IE5833.11,16.htm',
 'Working-at-Starbucks-EI_IE2202.11,20.htm',
 'Working-at-Walt-Disney-Company-EI_IE717.11,30.htm']


    #reviewUrls =  list(map(lambda x: x.replace("Overview","Reviews"),overviewUrls))

    name = "glassdoor_spider2"
    allowed_urls = ['https://www.glassdoor.com/']
    start_urls = 'https://www.glassdoor.com/Reviews/Facebook-Reviews-E40772.htm' #remove slicing once ready to go

    def verify(self, content):
        if isinstance(content, list):
            if len(content) > 0:
                return content[0]
            else:
                return ""
        else:
            return content


    def parse(self, response):

        ends = ['Facebook-Reviews-E40772.htm',
 'Working-at-Google-EI_IE9079.11,17.htm',
 'Working-at-lululemon-EI_IE42589.11,20.htm',
 'Working-at-HubSpot-EI_IE227605.11,18.htm',
 'Working-at-Ultimate-Software-EI_IE7900.11,28.htm',
 'SAP-Reviews-E10471.htm',
 'Working-at-Salesforce-EI_IE11159.11,21.htm',
 'Working-at-Delta-Air-Lines-EI_IE197.11,26.htm',
 'Working-at-LinkedIn-EI_IE34865.11,19.htm',
 'Working-at-Southwest-Airlines-EI_IE611.11,29.htm',
 'Working-at-NVIDIA-EI_IE7633.11,17.htm',
 'Working-at-AvalonBay-Communities-EI_IE2616.11,32.htm',
 'Working-at-Paylocity-EI_IE29987.11,20.htm',
 'Working-at-Intuit-EI_IE2293.11,17.htm',
 'Working-at-Adobe-EI_IE1090.11,16.htm',
 'Working-at-VMware-EI_IE12830.11,17.htm',
 'Working-at-SAP-Concur-EI_IE8763.11,21.htm',
 'Working-at-Forrester-EI_IE6443.11,20.htm',
 'Working-at-Johnson-and-Johnson-EI_IE364.11,30.htm',
 'Working-at-Microsoft-EI_IE1651.11,20.htm',
 'Working-at-Ellie-Mae-EI_IE260441.11,20.htm',
 'Working-at-Hilton-EI_IE330.11,17.htm',
 'Working-at-Protiviti-EI_IE30849.11,20.htm',
 'Working-at-Oshkosh-Corporation-EI_IE1740.11,30.htm',
 'Working-at-Eli-Lilly-and-Company-EI_IE223.11,32.htm',
 'Working-at-NIKE-EI_IE1699.11,15.htm',
 'Working-at-Monsanto-Company-EI_IE11986.11,27.htm',
 'Working-at-United-Airlines-EI_IE683.11,26.htm',
 'Working-at-Electronic-Arts-EI_IE1628.11,26.htm',
 'Working-at-Zillow-EI_IE40802.11,17.htm',
 'Working-at-Roche-EI_IE3480.11,16.htm',
 'Working-at-3M-EI_IE446.11,13.htm',
 'Working-at-Procter-and-Gamble-EI_IE544.11,29.htm',
 'Working-at-Guidewire-EI_IE122537.11,20.htm',
 'Working-at-Capital-One-EI_IE3736.11,22.htm',
 'Working-at-Hyatt-EI_IE2839.11,16.htm',
 'Working-at-Stryker-EI_IE1918.11,18.htm',
 'Working-at-T-Mobile-EI_IE9302.11,19.htm',
 'Working-at-Travelers-EI_IE1904.11,20.htm',
 'Working-at-CDW-EI_IE2347.11,14.htm',
 'Working-at-Accenture-EI_IE4138.11,20.htm',
 'Working-at-Apple-EI_IE1138.11,16.htm',
 'Working-at-Darden-EI_IE4160.11,17.htm',
 'Working-at-Taylor-Morrison-EI_IE37887.11,26.htm',
 'Working-at-Insperity-EI_IE3608.11,20.htm',
 'Working-at-Cisco-Systems-EI_IE1425.11,24.htm',
 'Working-at-adidas-EI_IE10692.11,17.htm',
 'Working-at-Shell-EI_IE5833.11,16.htm',
 'Working-at-Starbucks-EI_IE2202.11,20.htm',
 'Working-at-Walt-Disney-Company-EI_IE717.11,30.htm']

        revfilter = '?sort.sortType=RD&sort.ascending=false&filter.defaultEmploymentStatuses=false&filter.defaultLocation=false&filter.employmentStatus=REGULAR'
        #Append the url filter string to all base review pages
        endUrlsFilter = list(map(lambda x: x+revfilter,ends))

        for index, name in enumerate(ends):
            url = 'https://www.glassdoor.com/Reviews/{}.htm?sort.sortType=RD&sort.ascending=false&filter.defaultEmploymentStatuses=false&filter.defaultLocation=false&filter.employmentStatus=REGULAR'.format(name)

            i = 2
            names_url = 'https://www.glassdoor.com/Reviews/' + name + '_P' + str(i) + '.htm?sort.sortType=RD&sort.ascending=false&filter.defaultEmploymentStatuses=false&filter.defaultLocation=false&filter.employmentStatus=REGULAR'

            yield Request(url, callback = self.parse_review, meta={'name': name})
            yield Request(names_url, callback= self.parse_company, meta={'name': name})


        #extract Selectors for the 10 review sections
        #pageReviews = response.xpath('//li[@class=" empReview cf "]')

    def parse_company(self, response):
        
        i = 2
        # determine how many pages per company to scrape
        reviewcount = response.xpath('//div[@class="padTopSm margRtSm margBot minor"]/text()').extract_first()
        reviewcount = int(''.join(re.findall(r'\d+',str(reviewcount))))
        if (reviewcount != []):
            pagesToScrape = reviewcount//10
        else:
            pagesToScrape = 50


        while(i< pagesToScrape):
        # while(i < 5):
            names_url = 'https://www.glassdoor.com/Reviews/' + response.meta['name'] + '_P' + str(i) + '.htm?sort.sortType=RD&sort.ascending=false&filter.defaultEmploymentStatuses=false&filter.defaultLocation=false&filter.employmentStatus=REGULAR'
            # print(names_url,'!' * 50)
            # if i > pagesToScrape:
                # break
            # else:

            yield Request(names_url, callback = self.parse_review)

            i += 1
#=====================================================


        #get the total review count for the company, from each url, post-filter
        reviewcount = response.xpath('//div[@class="padTopSm margRtSm margBot minor"]/text()').extract_first()
        reviewcount = int(''.join(re.findall(r'\d+',str(reviewcount))))
        if (reviewcount != []):
            pagesToScrape = reviewcount//10
        else:
            pagesToScrape = 50


        for page in pagesToScrape: #Extract reviews one page at time
            

            JobTitle = response.xpath('//span[@class="authorJobTitle reviewer"]/text()').extract()
            ReviewDate = response.xpath('//time[@class="date subtle small"]/text()').extract()
            # fix extra results in Recommends, Outlook, CEO
            Recommends = response.xpath('//span[@class="middle"]/text()').extract()
            Outlook = 
            CEO = 

            MainText = response.xpath('//div[@class="infoEntity"]/span/text()').extract()[3]
            #newline issues causing multiple results, no results e.g. in advice
            Pros = response.xpath('//p[@class=" pros mainText truncateThis wrapToggleStr"]/text()').extract()
            Cons = response.xpath('//p[@class=" cons mainText truncateThis wrapToggleStr"]/text()').extract()
            Advice = response.xpath('//p[@class=" adviceMgmt mainText truncateThis wrapToggleStr"]/text()').extract()
            
            #Star rating still grabs first overall rating
            StarRating = response.xpath('//span[@class="value-title"]').extract()

            #These go together, still needs work
            WorkLifeBalance = response.xpath('//span[@class="gdBars gdRatings med "]/text()').extract()
            CultureValues = 
            CareerOpps = 
            CompBenefits = 
            SeniorMgmt = 


            item = Glassdoor2Item()
            item['Name'] = Name
            item['JobTitle'] = JobTitle
            item['ReviewDate'] = ReviewDate
            item['Recommends'] = Recommends
            item['Outlook'] = Outlook
            item['CEO'] = CEO
            item['MainText'] = MainText
            item['Pros'] = Pros
            item['Cons'] = Cons
            item['Advice'] = Advice
            item['StarRating'] = StarRating
            item['WorkLifeBalance'] = WorkLifeBalance
            item['CultureValues'] = CultureValues
            item['CareerOpps'] = CareerOpps
            item['CompBenefits'] = CompBenefits
            item['SeniorMgmt'] = SeniorMgmt

            yield item






          
