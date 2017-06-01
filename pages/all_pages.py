

from pages.my_asset_details_page import MyAssetDetailsPage

class AllPage(object):
    '''
    classdocs
    '''


    def __init__(self,driver):
        '''
        Constructor
        '''
        
        self.driver=driver
    
    
    def openpage_myassetDetailsPage(self,pagename):
        
            
        
        return  pagename.openpage(self.driver)
    
    
        