import scrapy


class InvestingSpider(scrapy.Spider):
    name = 'investing'
    start_urls = [
        "https://in.investing.com/indices/s-p-cnx-nifty-historical-data?end_date=1638383400&interval_sec=weekly&st_date=946665000&interval_sec=daily"
    ]

    def parse(self, response):
        rows = response.css("table.common-table tr.common-table-item")
        for row in rows:
            yield{
                "date": row.css("td")[0].css('span.text::text').get(),
                "price": row.css("td")[1].css('span.text::text').get(),
                "open": row.css("td")[2].css('span.text::text').get(),
                "high": row.css("td")[3].css('span.text::text').get(),
                "low": row.css("td")[4].css('span.text::text').get(),
                "volume": row.css("td")[5].css('span.text::text').get(),
                "percent_change": row.css("td")[6].css('span.text::text').get()
            }