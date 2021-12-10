import scrapy
import urllib
import json

class MobilesSpider(scrapy.Spider):
    name = 'mobiles'
    #allowed_domains = ['https://www.elgiganten.dk/mobil-tablet-smartwatch/mobiltelefon/page-1']
    base_url = 'https://elkjop-prod.fact-finder.de/fact-finder/rest/v4/navigation/commerce_b2c_OCDKELG'

    headers = {
        "authority": "elkjop-prod.fact-finder.de",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "_ffo": "aHR0cHM6Ly93d3cuZWxnaWdhbnRlbi5kaw==",
        "636f5670575166375a4e": "0.7326219695934164",
        "_fft": "291639150802643",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "66785952493077423533": "g54bo8bBuW8C24Cdal24CdallmiXSFnvMudnnvMudng54bo8rxctOM",
        "accept": "application/json",
        "sec-ch-ua-mobile": "?0",
        "7835596b63657a6f3331": "vcF4jaEbdFi5g6Dk3fUmHlSBVEIGmLkfPJGjxY0XODVrLst1Z39ctUJYwer5Wj, lQ2ber3gn5mN4Bhxd5vUiSCuRcm4MJXYdWTttbu8SLa8DO3odYFclCpMp8nkQs",
        "sec-ch-ua-platform": '"Windows"'   ,
        "origin": "https://www.elgiganten.dk",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.elgiganten.dk/",
        "accept-language": "en-US,en;q=0.9,ar;q=0.8,en-AU;q=0.7,en-GB;q=0.6,it;q=0.5"
    }
    page_count = 1



    params = {"page":"1",
    "filter":"ArticleAssignments.AssignmentSystem.Product_Taxonomy:Mobil, Tablet & Smartwatch/Mobiltelefon",
    "navigation":"true","sid":"coVpWQf7ZNx5Ykcezo31fxYRI0wB53","log":"cms","format":"json"}

    def start_requests(self):
        url = self.base_url + "?" + urllib.parse.urlencode(self.params)
        #url = 'https://www.elgiganten.dk/cxorchestrator/dk/api?appMode=b2c&user=anonymous&operationName=getPageContent&variables=%7B%22uri%22%3A%22mobil-tablet-smartwatch%2Fmobiltelefon%22%2C%22appMode%22%3A%22b2c%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22bce660af19041cd34dc28411eafb9db249d06d0bfd74050efcee65644b7c7b1d%22%7D%7D'
        print(url)
        yield scrapy.Request(url=url,
                            headers=self.headers,
                            callback=self.parse)

    def parse(self, response):
        json_response = json.loads(response.text)
       # with open('first_page.json', 'w', encoding='utf-8') as f:
        #    json.dump(json.loads(response.text), f, indent=2)

        page_headers = {
            "cookie": "bm_sz=8D442ACD73D788088E73EF4D25A70654~YAAQPv8SAqeD5Z19AQAAaxWipA5Y9/hwDV0FqE0SfyVH6KR4UTDWX16YmDZ49QT34Z8xx8/qN1BKYqj+LEN2PXfu/hHmrrE7eeOaSZwz5icDyYMSUp4BpV9Jl9eWpPX6l/XcxHGcR6L/vewIPqiENf1nYCUN5ApgvZCFyT7ZAEWoCBy9ICsNTPqaJM3B8k8zACB/o4yyFWkG7Gjsk3+uEsMSXfqAmZaLBVj1+WuBu7aXxH23ly2yMo/SEEWGNTgjFl5TwfZjPKF7hdHGavpL4Pe4pcC17c0l07L+IT6TEoSCBoxBMJw=~3228466~4473651; CookieInformationConsent=%7B%22website_uuid%22%3A%2284b86b51-f2fc-40c7-b909-1ebccc8888c7%22%2C%22timestamp%22%3A%222021-12-10T13%3A57%3A13.949Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.elgiganten.dk%2F%22%2C%22consent_website%22%3A%22elgiganten.dk%22%2C%22consent_domain%22%3A%22www.elgiganten.dk%22%2C%22user_uid%22%3A%22d8f66916-0c77-4461-927c-b8edc046e666%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F96.0.4664.93%20Safari%2F537.36%22%7D; _dyid_server=7651616640419978426; _dyid=7651616640419978426; renderMode=ssr; akacd_mm=1639152176~rv=28~id=0a5676806f24c8e2d0b8270e6c81ac71; ak_bmsc=A898CD6354C30D5D237C3100AA2A40AA~000000000000000000000000000000~YAAQPv8SAhpw5p19AQAAINIQpQ7V4DszfqreWzNpgBzV8zG077jtFifYgZWZB9LCPhfR89E067luEMGnKFFoUslYXuBU899dlbyv7IqIUGeP24AdkG79MEr/pYIWVY26Ht+w2p+Kss7JICPjRPVLzP/cHkF8roN5DBMB6hjGWFBkndkAjK0L73hpIJJsIIySjItQ954ExkjR05oKNsRp349CY91nxvGKdQSg3k4aaAqWK738G/VumeSt3poM4g5GP53/OVd6K0dOV+l/h28dZgDUltU5kbVI07VAZx5U2Ji207Gv+olJ0lg90ax/kqaQjRA/p7KsKCDxpihShJMJvnuV7fS2gIISDFR+ivhhwCAhGffMOwAsPEiAbQpsAzK1vl7Dh92SDbxC3+6uqA==; _abck=0077E10C844F45CF17DB3F0F7F4FDECE~0~YAAQPv8SAnp25p19AQAABV8UpQcBOD7P41UmTYNjiyUDF6wNOf3nZGjfukLQ1+YKT+RgEftgU+VXEAZlvRkNUi7wq9xODUgxU5TbgGT57ZT05R3jTr712nsyl9oHvauphUhtyFk5uFAnKMBH5kqcyQr+IzCvhbbJxiGS9G6GEQ1M4ZhHVme0xjddfCZYFCGtsrUP2yfRPStyxqVXDMhJra/suUzUtSTUUnCZxrxHxLNoKIYuy9qT7ZzV6UBq5+O+JwC8RlPuMfNNVDlj/Mh7ap+95rLEffxGAIM9/Wy/NnPUZeB8Cex/hN8sXhkOGIcnAwUCOEinFhkTYiSuzwKGIPSUJYwNxaz9h6TZLfsae6pgucjVk+zYoRui0xFWUWAECBUIngvxW21uZGJwAh97bBq+9sLN687y7kdn~-1~-1~-1; QueueITAccepted-SDFrts345E-V3_staticdk=EventId%3Dstaticdk%26QueueId%3Dbe2cf20e-a756-4a6c-8247-db2095bf8d1b%26RedirectType%3Dsafetynet%26IssueTime%3D1639152151%26Hash%3De1be8b244a46c7fa6c3898d5fd1996b5640dab065efc7de9f8d9adb64c8a77c7; bm_mi=F5F83B9025FD77206F0A30D7F61BC5C6~ZTQDEivhpHOO5XBzlmW0XEwQLecsVjCqQIX9DyuIBw4EodRZiACLqRW8QSGVEZo/BpEwIVCb2l3Y1NlOW7rBFA1FuZGojneP/8DXKCmf8HgrHNk9uvk1fqFtu2H1a+HefIeANoUUKq6zJIo/2Xgl0bpXyaSrmCz9hqNMiILl5y2SUAI2E+bJoNsETyxkR7kD3PMjgTyJPy1laD7/rFGHU/tzJ2RJ/XBV7jg2yDjA4NEoawvqEoovyZmF73dvUheRy7jAz5V3ZLepST1sgUQHx6+lzWtmidpVnQ/CzoEkXrJJOUQGaHhE/WYYeCYwoOj1g3CiNDLvWaJ+oGKPaiTFyHcHQuN7HUlCfjbtNPXw7Og=; bm_sv=B858A07CBA6603876233C882A9F0DCAE~Qu5UIe+ZigyCFo6ZmZ6MvY7s4uW7Iaq273/s/gLwEadXb9epAlXusZmLPaWvWc9BeE66c4JQfVHCcuUxR9EE+fZr+fC2vT1UP8rKOODRDHqmayFZkVwe4V6RJSDOqsnT0anIH9UPOYaEqxFHYLr3ySjxZ9bBxv80MxLQ7JkdI18=",
            "authority": "www.elgiganten.dk",
            "x-instana-t": "31d83ef82324ffbe",
            "x-is-anonymous": "true",
            "sec-ch-ua-mobile": "?0",
            "authorization": "",
            "accept": "application/json, text/plain, */*",
            "x-app-checkout": "false",
            "x-authorization": "",
            "x-app-mode": "b2bExVat",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.elgiganten.dk/product/mobil-tablet-smartwatch/mobiltelefon/iphone-13-mini-5g-smartphone-128gb-blue/361864?context=erhverv",
            "accept-language": "en-US,en;q=0.9,ar;q=0.8,en-AU;q=0.7,en-GB;q=0.6,it;q=0.5"
        }

        page_params = {"appMode":"b2c",
        "user":"anonymous",
        "operationName":"getProductWithDetails",
        "variables":"{\"articleNumber\":\"361894\",\"isB2B\":false}",
        "extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"fa3ed3c988ffa240f42632f8ed50865860f46edd6d0edfe4e0d85150cf8b3896\"}}"}

        for hit in json_response['hits']:
            api_url = 'https://www.elgiganten.dk/cxorchestrator/dk/api'
            page_params['variables'] = "{\"articleNumber\": \"" + hit['id'] + "\", \"isB2B\":true}"
            url = api_url + '?' + urllib.parse.urlencode(page_params)
            yield scrapy.Request(url=url,
                                headers=page_headers,
                                callback=self.parse_item)

        if self.page_count < json_response['paging']["pageCount"]:
            self.page_count += 1
            self.params['page'] = self.page_count
            url = self.base_url + "?" + urllib.parse.urlencode(self.params)
            print('NUMBER OF PAGE IS ', self.page_count)
            yield scrapy.Request(url=url,
                                headers=self.headers,
                                callback=self.parse)

    def parse_item(self, response):
        data = json.loads(response.text)
        item = {
            "title": data['data']["product"]["title"],
            "brand": data['data']["product"]["brand"]["name"],
            "item_id": data['data']["product"]["_id"],
            "short_desc": data['data']["product"]['shortDescription'],
            "specs": data['data']["product"]['bulletpoints'],
            "reviews_number": data['data']["product"]['numberOfReviews'],
            "average_rating": data['data']["product"]['averageRating'],
            "page_url": data['data']["product"]['productPageUrl'],
        }
        yield item