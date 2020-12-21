from selenium import webdriver

class CardList:

    list = [];
    def card_list_parsing(driver: webdriver):
        results = driver.find_elements_by_xpath('//div[@class="catalog-item"]')

        print(len(results))

        for result in results:
            name_block = result.find_element_by_class_name("product-info__title")
            sub_name_block = name_block.find_element_by_class_name("product-info__title-link")

            price = result.find_element_by_class_name("product-min-price__current")
            print(f'{sub_name_block.text} | {price.text}')
