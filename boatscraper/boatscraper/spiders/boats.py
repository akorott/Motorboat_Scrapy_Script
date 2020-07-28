import scrapy

class BoatsSpider(scrapy.Spider):
    name = 'boats'
    page_num = 48
    allowed_domains = ['boat24.com']
    start_urls = ['https://www.boat24.com/en/powerboats/?page=48&sort=chfasc']

    def parse(self, response):

        boats_on_page = response.xpath("//div[@class='inner']")

        for boat in boats_on_page:
            boat_url = boat.xpath(".//a/@href").extract_first()

            yield scrapy.Request(boat_url, callback=self.parse_boats)

        next_page_url = 'https://www.boat24.com/en/powerboats/?page=' + str(BoatsSpider.page_num) + '&sort=chfasc'


        if BoatsSpider.page_num <= 10368:
            BoatsSpider.page_num += 48
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_boats(self, response):
        price = response.xpath("//span[@itemprop='price']/text()").extract()

        category = response.xpath("//label[. = 'Category']/following-sibling::a/text()").extract()
        boat_type = response.xpath("//label[. = 'Boat Type']/following-sibling::a/text()").extract()
        manufacturer = response.xpath("//label[. = 'Manufacturer']/following-sibling::a/text()").extract()
        model = response.xpath("//label[. = 'Model']/following-sibling::a/text()").extract()
        if len(model) == 0:
            model = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Model')]/following-sibling::text()").extract()

        boat_name = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Boat Name')]/following-sibling::text()").extract()
        type = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Type')]/following-sibling::text()").extract()
        year = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Year Built')]/following-sibling::text()").extract()
        condition = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Condition')]/following-sibling::text()").extract()
        length = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Length')]/following-sibling::text()").extract()
        width = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Width')]/following-sibling::text()").extract()
        depth = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Depth')]/following-sibling::text()").extract()
        displacement = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Displacement')]/following-sibling::text()").extract()
        ce_design_category = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'CE Design Category')]/following-sibling::text()").extract()
        nr_people = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Certified Nr. Of Persons')]/following-sibling::text()").extract()
        nr_cabins = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'No. Of Cabins')]/following-sibling::text()").extract()
        nr_beds = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'No. Of Beds')]/following-sibling::text()").extract()
        nr_toilets = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Toilets')]/following-sibling::text()").extract()
        nr_bathrooms = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'No. Of Bathrooms')]/following-sibling::text()").extract()
        nr_showers = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Showers')]/following-sibling::text()").extract()
        hull_color = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Hull Color')]/following-sibling::text()").extract()
        material = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Material')]/following-sibling::text()").extract()
        fresh_water_cap = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Fresh Water Capacity')]/following-sibling::text()").extract()
        holding_tank = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Holding Tank')]/following-sibling::text()").extract()
        propulsion = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Propulsion')]/following-sibling::text()").extract()
        engine = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Engine')]/following-sibling::text()").extract_first()
        engine_performance = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Engine Performance')]/following-sibling::text()").extract()
        fuel_cap = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Fuel Capacity')]/following-sibling::text()").extract_first()
        fuel_type = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Fuel Type')]/following-sibling::text()").extract()
        engine_hours = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Engine Hours')]/following-sibling::text()").extract_first()
        max_speed = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Max Speed')]/following-sibling::text()").extract()
        cruising_speed = response.xpath("//ul[@class='detailListHorizontal']/li/label[contains(text(),'Cruising Speed')]/following-sibling::text()").extract()

        location = response.xpath("//div[@class='detailStandort']/p/text()").extract()

        ad_date = response.xpath("//div[@class='detailIdInfo detailInfoCom']/p[contains(.,'Ad date: ')]/strong/text()").extract()
        number_of_views_last_7_days = response.xpath("//div[@class='detailIdInfo detailInfoCom']/p[contains(.,'Number of views last 7 days: ')]/strong/text()").extract()

        comments = response.xpath("//section[@itemprop='description']/text()").extract()
        comments = [x.strip() for x in comments]
        comments2 = response.xpath("//section[@itemprop='description']/p/text()").extract()
        comments2 = [x.strip() for x in comments2]

        equipment = response.xpath("//div[@class='detailAusstattung']/ul/li/text()").extract()

        yield {
            'Price': price,
            'Category': category,
            'Boat Type': boat_type,
            'Manufacturer': manufacturer,
            'Model': model,
            'Boat name': boat_name,
            'Type': type,
            'Year Built': year,
            'Condition': condition,
            'Length': length,
            'Width': width,
            'Depth': depth,
            'Displacement': displacement,
            'CE Design Category': ce_design_category,
            'Cert Number of People': nr_people,
            'Number of Cabins': nr_cabins,
            'Number of beds': nr_beds,
            'Hull Color': hull_color,
            'Number of Toilets': nr_toilets,
            'Number of Bathrooms': nr_bathrooms,
            'Number of Showers': nr_showers,
            'Material': material,
            'Fresh Water Cap': fresh_water_cap,
            'Holding Tank': holding_tank,
            'Propulsion': propulsion,
            'Engine': engine,
            'Engine Performance': engine_performance,
            'Fuel Capacity': fuel_cap,
            'Fuel Type': fuel_type,
            'Engine Hours': engine_hours,
            'Max Speed': max_speed,
            'Cruising Speed': cruising_speed,
            'Location': location,
            'Advertisement Date': ad_date,
            'Number of views last 7 days': number_of_views_last_7_days,
            'Comments': comments,
            'Additional Comments': comments2,
            'Equipment': equipment,

            }