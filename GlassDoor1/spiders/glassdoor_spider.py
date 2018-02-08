from scrapy import Spider
from scrapy.selector import Selector
from GlassDoor1.items import Glassdoor1Item


class GlassdoorSpider(Spider):
    #Find links from top100 page 
    #overviews = response.xpath('//div[@class="employer-logo"]/a/@href').extract()
    overviews = ['/facebook',
 '/Overview/Working-at-Bain-and-Company-EI_IE3752.11,27.htm',
 '/Overview/Working-at-Boston-Consulting-Group-EI_IE3879.11,34.htm',
 '/Overview/Working-at-In-N-Out-Burger-EI_IE14276.11,26.htm',
 '/Overview/Working-at-Google-EI_IE9079.11,17.htm',
 '/Overview/Working-at-lululemon-EI_IE42589.11,20.htm',
 '/Overview/Working-at-HubSpot-EI_IE227605.11,18.htm',
 '/Overview/Working-at-World-Wide-Technology-EI_IE9553.11,32.htm',
 '/Overview/Working-at-St-Jude-Children-s-Research-Hospital-EI_IE28315.11,47.htm',
 '/Overview/Working-at-Ultimate-Software-EI_IE7900.11,28.htm',
 '/sap',
 '/Overview/Working-at-McKinsey-and-Company-EI_IE2893.11,31.htm',
 '/Overview/Working-at-Keller-Williams-EI_IE114145.11,26.htm',
 '/Overview/Working-at-E-and-J-Gallo-Winery-EI_IE2778.11,31.htm',
 '/Overview/Working-at-Salesforce-EI_IE11159.11,21.htm',
 '/Overview/Working-at-Power-Home-Remodeling-EI_IE405781.11,32.htm',
 '/Overview/Working-at-Delta-Air-Lines-EI_IE197.11,26.htm',
 '/Overview/Working-at-Academy-Mortgage-EI_IE336856.11,27.htm',
 '/Overview/Working-at-The-Church-of-Jesus-Christ-of-Latter-day-Saints-EI_IE122747.11,58.htm',
 '/Overview/Working-at-H-E-B-EI_IE2824.11,16.htm',
 '/Overview/Working-at-LinkedIn-EI_IE34865.11,19.htm',
 '/Overview/Working-at-DocuSign-EI_IE307604.11,19.htm',
 '/Overview/Working-at-Southwest-Airlines-EI_IE611.11,29.htm',
 '/Overview/Working-at-NVIDIA-EI_IE7633.11,17.htm',
 '/Overview/Working-at-Fast-Enterprises-EI_IE241404.11,27.htm',
 '/Overview/Working-at-AvalonBay-Communities-EI_IE2616.11,32.htm',
 '/Overview/Working-at-Nestlé-Purina-EI_IE14081.11,24.htm',
 '/Overview/Working-at-Blizzard-Entertainment-EI_IE24858.11,33.htm',
 '/Overview/Working-at-Paylocity-EI_IE29987.11,20.htm',
 '/Overview/Working-at-Intuit-EI_IE2293.11,17.htm',
 '/Overview/Working-at-Adobe-EI_IE1090.11,16.htm',
 '/Overview/Working-at-NewYork-Presbyterian-Hospital-EI_IE121522.11,40.htm',
 '/Overview/Working-at-VMware-EI_IE12830.11,17.htm',
 '/Overview/Working-at-SAP-Concur-EI_IE8763.11,21.htm',
 '/Overview/Working-at-Boston-Scientific-EI_IE2187.11,28.htm',
 '/Overview/Working-at-Forrester-EI_IE6443.11,20.htm',
 '/Overview/Working-at-Kimpton-Hotels-and-Restaurants-EI_IE9955.11,41.htm',
 '/Overview/Working-at-Johnson-and-Johnson-EI_IE364.11,30.htm',
 '/Overview/Working-at-Microsoft-EI_IE1651.11,20.htm',
 '/Overview/Working-at-Ellie-Mae-EI_IE260441.11,20.htm',
 '/Overview/Working-at-Hilton-EI_IE330.11,17.htm',
 '/Overview/Working-at-Yardi-Systems-EI_IE31057.11,24.htm',
 '/Overview/Working-at-Smile-Brands-EI_IE321628.11,23.htm',
 '/Overview/Working-at-Progressive-Leasing-EI_IE665607.11,30.htm',
 '/Overview/Working-at-Memorial-Sloan-Kettering-EI_IE4711.11,35.htm',
 '/Overview/Working-at-Texas-Health-Resources-EI_IE7647.11,33.htm',
 '/Overview/Working-at-Protiviti-EI_IE30849.11,20.htm',
 '/Overview/Working-at-Oshkosh-Corporation-EI_IE1740.11,30.htm',
 '/Overview/Working-at-Wegmans-Food-Markets-EI_IE3042.11,31.htm',
 '/Overview/Working-at-SpaceX-EI_IE40371.11,17.htm',
 '/Overview/Working-at-Discount-Tire-EI_IE6632.11,24.htm',
 '/Overview/Working-at-Eli-Lilly-and-Company-EI_IE223.11,32.htm',
 '/Overview/Working-at-NIKE-EI_IE1699.11,15.htm',
 '/Overview/Working-at-Monsanto-Company-EI_IE11986.11,27.htm',
 '/Overview/Working-at-United-Airlines-EI_IE683.11,26.htm',
 '/Overview/Working-at-Electronic-Arts-EI_IE1628.11,26.htm',
 '/Overview/Working-at-Zillow-EI_IE40802.11,17.htm',
 '/Overview/Working-at-Capital-Group-EI_IE9441.11,24.htm',
 '/Overview/Working-at-Roche-EI_IE3480.11,16.htm',
 '/Overview/Working-at-3M-EI_IE446.11,13.htm',
 '/Overview/Working-at-REI-EI_IE7319.11,14.htm',
 '/Overview/Working-at-Procter-and-Gamble-EI_IE544.11,29.htm',
 '/Overview/Working-at-Kronos-Incorporated-EI_IE2196.11,30.htm',
 '/Overview/Working-at-Kwik-Trip-EI_IE18377.11,20.htm',
 '/Overview/Working-at-Yahoo-EI_IE5807.11,16.htm',
 '/arm',
 '/Overview/Working-at-Northwestern-Mutual-EI_IE2919.11,30.htm',
 '/Overview/Working-at-Guidewire-EI_IE122537.11,20.htm',
 '/Overview/Working-at-Capital-One-EI_IE3736.11,22.htm',
 '/Overview/Working-at-Trader-Joe-s-EI_IE5631.11,23.htm',
 '/Overview/Working-at-Hyatt-EI_IE2839.11,16.htm',
 '/Overview/Working-at-Chick-fil-A-EI_IE5873.11,22.htm',
 '/Overview/Working-at-Extra-Space-EI_IE35227.11,22.htm',
 '/Overview/Working-at-Slalom-EI_IE31102.11,17.htm',
 '/Overview/Working-at-J-Crew-EI_IE2848.11,17.htm',
 '/Overview/Working-at-Stryker-EI_IE1918.11,18.htm',
 '/Overview/Working-at-Deloitte-EI_IE2763.11,19.htm',
 '/Overview/Working-at-Toyota-North-America-EI_IE3544.11,31.htm',
 '/Overview/Working-at-T-Mobile-EI_IE9302.11,19.htm',
 '/Overview/Working-at-Travelers-EI_IE1904.11,20.htm',
 '/Overview/Working-at-CDW-EI_IE2347.11,14.htm',
 '/Overview/Working-at-Aurora-Health-Care-EI_IE121528.11,29.htm',
 '/Overview/Working-at-Accenture-EI_IE4138.11,20.htm',
 '/Overview/Working-at-Apple-EI_IE1138.11,16.htm',
 '/Overview/Working-at-Darden-EI_IE4160.11,17.htm',
 '/Overview/Working-at-QuikTrip-EI_IE2947.11,19.htm',
 '/Overview/Working-at-Taylor-Morrison-EI_IE37887.11,26.htm',
 '/Overview/Working-at-Insperity-EI_IE3608.11,20.htm',
 '/Overview/Working-at-Cisco-Systems-EI_IE1425.11,24.htm',
 '/Overview/Working-at-Massachusetts-General-Hospital-EI_IE20189.11,41.htm',
 '/Overview/Working-at-Kaiser-Permanente-EI_IE19466.11,28.htm',
 '/Overview/Working-at-Ceridian-EI_IE179.11,19.htm',
 '/Overview/Working-at-adidas-EI_IE10692.11,17.htm',
 '/Overview/Working-at-Morrison-Healthcare-EI_IE5949.11,30.htm',
 '/Overview/Working-at-Shell-EI_IE5833.11,16.htm',
 '/Overview/Working-at-Starbucks-EI_IE2202.11,20.htm',
 '/Overview/Working-at-Liberty-National-Life-EI_IE19017.11,32.htm',
 '/Overview/Working-at-Walt-Disney-Company-EI_IE717.11,30.htm',
 '/Overview/Working-at-KPMG-EI_IE2867.11,15.htm',
 '/Overview/Working-at-BAYADA-Home-Health-Care-EI_IE153924.11,34.htm']

    #Find company names only from top 100 page
    #names = response.xpath('//span[@class="employer-name"]/text()').extract()

    names = ['Facebook',
 'Bain & Company',
 'Boston Consulting Group',
 'In-N-Out Burger',
 'Google',
 'lululemon',
 'HubSpot',
 'World Wide Technology',
 "St. Jude Children's Research Hospital",
 'Ultimate Software',
 'SAP',
 'McKinsey & Company',
 'Keller Williams',
 'E. & J. Gallo Winery',
 'Salesforce',
 'Power Home Remodeling',
 'Delta Air Lines',
 'Academy Mortgage',
 'The Church of Jesus Christ of Latter-day Saints',
 'H E B',
 'LinkedIn',
 'DocuSign',
 'Southwest Airlines',
 'NVIDIA',
 'Fast Enterprises',
 'AvalonBay Communities',
 'Nestlé Purina',
 'Blizzard Entertainment',
 'Paylocity',
 'Intuit',
 'Adobe',
 'NewYork-Presbyterian Hospital',
 'VMware',
 'SAP Concur',
 'Boston Scientific',
 'Forrester',
 'Kimpton Hotels & Restaurants',
 'Johnson & Johnson',
 'Microsoft',
 'Ellie Mae',
 'Hilton',
 'Yardi Systems',
 'Smile Brands',
 'Progressive Leasing',
 'Memorial Sloan Kettering',
 'Texas Health Resources',
 'Protiviti',
 'Oshkosh Corporation',
 'Wegmans Food Markets',
 'SpaceX',
 'Discount Tire',
 'Eli Lilly and Company',
 'NIKE',
 'Monsanto Company',
 'United Airlines',
 'Electronic Arts',
 'Zillow',
 'Capital Group',
 'Roche',
 '3M',
 'REI',
 'Procter & Gamble',
 'Kronos Incorporated',
 'Kwik Trip',
 'Yahoo',
 'Arm',
 'Northwestern Mutual',
 'Guidewire',
 'Capital One',
 "Trader Joe's",
 'Hyatt',
 'Chick-fil-A',
 'Extra Space',
 'Slalom',
 'J. Crew',
 'Stryker',
 'Deloitte',
 'Toyota North America',
 'T-Mobile',
 'Travelers',
 'CDW',
 'Aurora Health Care',
 'Accenture',
 'Apple',
 'Darden',
 'QuikTrip',
 'Taylor Morrison',
 'Insperity',
 'Cisco Systems',
 'Massachusetts General Hospital',
 'Kaiser Permanente',
 'Ceridian',
 'adidas',
 'Morrison Healthcare',
 'Shell',
 'Starbucks',
 'Liberty National Life',
 'Walt Disney Company',
 'KPMG',
 'BAYADA Home Health Care']

    #Join to create valid URLs
    overviewUrls = ['https://www.glassdoor.com' + str(x) for x in overviews]
    #Obtain the review page URLs
    reviewUrls =  list(map(lambda x: x.replace("Overview","Reviews"),overviewUrls))

    name = "glassdoor_spider"
    allowed_urls = ['https://www.glassdoor.com/']
    start_urls = overviewUrls #remove slicing once ready to go

    def parse(self, response):

        labels = response.xpath('//div[@class="infoEntity"]/label/text()').extract()
        #Extract all the company overview meta-data FOR EACH company overview
        #testCompanyInfo = response.xpath('//div[@class="infoEntity"]/span/text()').extract()

        item = Glassdoor1Item()

        if ('Headquarters' in labels):
            CompanyHQlookup = labels.index('Headquarters')-1
            item['CompanyHQ'] = response.xpath('//div[@class="infoEntity"]/span/text()').extract()[CompanyHQlookup]
        else:
            item['CompanyHQ'] = ""

        if ('Size' in labels):
            Sizelookup = labels.index('Size')-1
            item['Size'] = response.xpath('//div[@class="infoEntity"]/span/text()').extract()[Sizelookup]
        else:
            item['Size'] = ""

        if ('Type' in labels):
            CompanyTypelookup = labels.index('Type')-1
            item['Type'] = response.xpath('//div[@class="infoEntity"]/span/text()').extract()[CompanyTypelookup]
        else:
            item['Type'] = ""

        if ('Industry' in labels):
            Industylookup = labels.index('Industry')-1
            item['Industry'] = response.xpath('//div[@class="infoEntity"]/span/text()').extract()[Industylookup]
        else:
            item['Industry'] = ""

        if ('Revenue' in labels):
            Revenuelookup = labels.index('Revenue')-1
            item['Revenue'] = response.xpath('//div[@class="infoEntity"]/span/text()').extract()[Revenuelookup]
        else:
            item['Revenue'] = ""

        item['Name'] =  response.xpath('//h1[@class=" strong tightAll"]/text()').extract()

        print('='*50)

        yield item

###################################################### STAGE 2 get review details

        # revfilter = '?sort.sortType=RD&sort.ascending=false&filter.defaultEmploymentStatuses=false&filter.defaultLocation=false&filter.employmentStatus=REGULAR'
        # #Append the url filter string to all base review pages
        # reviewUrls = list(map(lambda x: x+revfilter,reviewUrls))

        # #pageReviews returns 10 results from the response.xpath below, need to extract sub-info
        # #extract Selectors for the 10 review sections
        # pageReviews = response.xpath('//li[@class=" empReview cf "]')

        # #get the total review count for the company, from each url, post-filter
        # reviewcount = response.xpath('//div[@class="padTopSm margRtSm margBot minor"]/text()').extract()
        # reviewcount = int(''.join(re.findall(r'\d+',str(reviewcount))))

        # for i in pageReviews: #Extract reviews one page at time
            
        #     JobTitle = response.xpath('//span[@class="authorJobTitle reviewer"]/text()').extract()
        #     ReviewDate = response.xpath('//time[@class="date subtle small"]/text()').extract()
        #     # fix extra results in Recommends, Outlook, CEO
        #     Recommends = response.xpath('//span[@class="middle"]/text()').extract()
        #     Outlook = 
        #     CEO = 

        #     MainText = response.xpath('//div[@class="infoEntity"]/span/text()').extract()[3]
        #     #newline issues causing multiple results, no results e.g. in advice
        #     Pros = response.xpath('//p[@class=" pros mainText truncateThis wrapToggleStr"]/text()').extract()
        #     Cons = response.xpath('//p[@class=" cons mainText truncateThis wrapToggleStr"]/text()').extract()
        #     Advice = response.xpath('//p[@class=" adviceMgmt mainText truncateThis wrapToggleStr"]/text()').extract()
            
        #     #Star rating still grabs first overall rating
        #     StarRating = response.xpath('//span[@class="value-title"]').extract()

        #     #These go together, still needs work
        #     WorkLifeBalance = response.xpath('//span[@class="gdBars gdRatings med "]/text()').extract()
        #     CultureValues = 
        #     CareerOpps = 
        #     CompBenefits = 
        #     SeniorMgmt = 


        #     item = Glassdoor1Item()
        #     item['JobTitle'] = JobTitle
        #     item['ReviewDate'] = ReviewDate
        #     item['Recommends'] = Recommends
        #     item['Outlook'] = Outlook
        #     item['CEO'] = CEO
        #     item['MainText'] = MainText
        #     item['Pros'] = Pros
        #     item['Cons'] = Cons
        #     item['Advice'] = Advice
        #     item['StarRating'] = StarRating
        #     item['WorkLifeBalance'] = WorkLifeBalance
        #     item['CultureValues'] = CultureValues
        #     item['CareerOpps'] = CareerOpps
        #     item['CompBenefits'] = CompBenefits
        #     item['SeniorMgmt'] = SeniorMgmt

        #     yield item






          
