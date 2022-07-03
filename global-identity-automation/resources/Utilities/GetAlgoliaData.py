from utilities.BaseClass import BaseClass
from algoliasearch.search_client import SearchClient
import config
import re

class GetAlgoliaData(BaseClass):


    def getDataFromAlgolia(self,word):

        client = SearchClient.create("RLPEOSLXDV", "f68bcfb891edf1a8c1cbcc3fa98a2946")

        # Create a new index and add a record
        index = client.init_index("product_data")

        #Search the index and print the results
        res = index.search(word, {
            'attributesToRetrieve': [
                'title',
                'tags',
                'foundry_title'
            ],
            'hitsPerPage': 8
        })
        results = res["hits"]
        results = str(results)
        return results

    def gettags(self,word):
        result = self.getDataFromAlgolia(word)
        tags = re.findall("'tags': \['(.*?)'\], '", result)
        return tags

    def getfonts(self,word):
        result = self.getDataFromAlgolia(word)
        fonts = re.findall(", 'title': '(.*?)', '", result)
        return fonts

    def getfoundries(self,word):
        result = self.getDataFromAlgolia(word)
        foundries = re.findall("'foundry_title': '(.*?)', '", result)
        return foundries