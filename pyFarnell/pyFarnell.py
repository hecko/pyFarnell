import requests

class Farnell():
    """Setup Farnell API session

    :param apiKey: Farnells Product Search API apiKey    
    :type apiKey: str
    :param region: Region for querying information (effectively the country) (for example: 'uk.farnell.com', 'au.element14.com' or 'mexico.newark.com').
        All the regions are listed here: http://partner.element14.com/docs/Product_Search_API_REST__Description#storeinfo
    :type region: str

    """

    def __init__(self, apiKey = '', region = 'sk.farnell.com'):
        if not apiKey:
            raise Exception("Contact Farnell representative to create an accout for \'Product Search API: Standard' product for you.")
        
        self.apiKey = apiKey
        self.base_url = 'https://api.element14.com/catalog/products'

    def get_part_number(self, partNum):
        """Gets part information

        :param partNum: Farnells part order number
        :type partNum: str
        :return: product information dictionary
        :rtype: dict

        """

        params = {
                   'callInfo.responseDataFormat': 'JSON',
                   'term': 'id:' + str(partNum),
                   'storeInfo.id': 'sk.farnell.com',
                   'callInfo.apiKey': self.apiKey,
                 }
        r = requests.get(self.base_url, params = params)
        if r.status_code != 200:
            raise Exception("Developer apiKey not active - contact Farnell representative to activate account for \'Product Search API: Standard' product - API key " + str(self.apiKey))
        return r.__dict__
