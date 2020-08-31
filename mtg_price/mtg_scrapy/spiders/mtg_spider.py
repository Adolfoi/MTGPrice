# -*- coding: utf-8 -*-
import scrapy
import re

class MtgSpiderSpider(scrapy.Spider):
    name = 'mtg_spider'
    allowed_domains = ['hareruyamtg.com']
    start_urls = ['https://www.hareruyamtg.com/ja/products/search?sort=&order=&cardId=&product=&category=&cardset=6&colorsType=0&rarity%5B%5D=3&cardtypes%5B%5D=7&cardtypesType=0&format=&illustrator=&foilFlg%5B%5D=0&stock=0']

    
    def parse(self, response):
        """
        レスポンスに対するパース処理
        """
        
        item = {}
        
        print(response.css('#category_item > div.autopagerize_page_element > ul').extract_first())
        
                    #print("★response.css('#category_item > div.autopagerize_page_element > ul > li:nth-child(1) > a.itemName ::text')")
            #print(response.css('#category_item > div.autopagerize_page_element > ul > li:nth-child(1) > a.itemName ::text').extract_first)
 
        # 仮に40点取得
        for i in range(1,41):
            
            card_name = response.css('#category_item > div.autopagerize_page_element > ul > li:nth-child(' + str(i)  +  ') > a.itemName ::text').extract_first()
            card_name = card_name
            
            print("card_name:")
            print(card_name)
            
            for j in range(2,6):
                card_condition = response.css('#category_item > div.autopagerize_page_element > ul > li:nth-child(' + str(i)  +  ') > div.tableHere.product > div:nth-child(' + str(j) +  ') > div.col-xs-1.ng-star-inserted ::text').extract()[1]
                
                card_condition = card_condition.replace(" ","").replace("\n","")
                
                card_price = response.css('#category_item > div.autopagerize_page_element > ul > li:nth-child(' + str(i)  +  ') > div.tableHere.product > div:nth-child(' + str(j) +  ') > div.col-xs-4.ng-star-inserted ::text').extract()[0].replace(" ","").replace(",","").replace("¥","")
            
                card_stock = response.css('#category_item > div.autopagerize_page_element > ul > li:nth-child(' + str(i) + ') > div.tableHere.product > div:nth-child(' + str(j) +  ') > div:nth-child(3) ::text').extract()[0]
                item['card_name'] = card_name
                item['card_condition'] = card_condition
                item['card_price'] = card_price
                item['card_stock'] = card_stock
                
                yield item
            
            """
            
            # response.css で scrapy デフォルトの css セレクタを利用できる
            for post in response.css('ul.itemListLine itemListLine--searched'):
                # items に定義した Post のオブジェクトを生成して次の処理へ渡す
                
                yield Post(
                    url=post.css('div.post-header a::attr(href)').extract_first().strip(),
                    title=post.css('div.post-header a::text').extract_first().strip(),
                    date=post.css('div.post-header span.date a::text').extract_first().strip(),
                )
                

                # 再帰的にページングを辿るための処理
                older_post_link = post.css('#category_item > div.autopagerize_page_element > ul > li:nth-child(1) > a:nth-child(1)::attr(href)').extract_first()
                print("older_post_link:")
                print(older_post_link)
                
                if older_post_link is None:
                    # リンクが取得できなかった場合は最後のページなので処理を終了
                    return

                # URLが相対パスだった場合に絶対パスに変換する
                older_post_link = response.urljoin(older_post_link)
                print(older_post_link)
                
                # 次のページをのリクエストを実行する
                # yield scrapy.Request(older_post_link, callback=self.parse)
            """
