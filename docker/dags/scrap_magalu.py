import scrapy

base_url = 'https://www.magazineluiza.com.br/busca/garrafa+stanley+aerolight+fast+flow/?page=1'

class Magalu(scrapy.Spider):
    name='m'
    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    def start_requests(self):
        yield scrapy.Request(f'{base_url}')

    def parse(self, response):
        total = response.xpath('//button[@type="next"]//ancestor::ul//li[position() = last() - 1]//text()').get()
        print('*'*50)
        print(total)
        print('*'*50)
        for i in range(1, int(total)+1):
            yield scrapy.Request(f'{base_url}?page={i}',callback=self.parse2)


    def parse2(self, response):
        print(response.url)
        # print(response.text)
        blocos = response.xpath('//div[@data-testid="product-list"]//li')
        print('blocos')
        print(blocos)

        for bloco in blocos:
            title = bloco.xpath('.//h2[@data-testid="product-title"]//text()').get()
            print(title)
            # .xpath(u"normalize-space(.//strong[. = 'Address:']/following-sibling::text())").extract()
            price = bloco.xpath('normalize-space(.//p[@data-testid="price-value"]//following-sibling::text())').get()
            print('[' + price + ']')
            
            review = bloco.xpath('.//span[@format="score-count"]//text()').get()
            print(review)

            yield {
                'title' : title,
                'price' : price,
                'review': review,
                'store':'Magazine Luiza'
            }

        # if response.xpath('//button[@type="next"]').get():
        #     yield scrapy.Request(f'{base_url}?page={self.page}',callback=self.parse)