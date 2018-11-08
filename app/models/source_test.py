mport unittest
from .models import source
Source = source.Source
 class SourceTest(unittest.TestCase):
    ''' test class to test behavior of Source class '''
     def setUp(self):
        ''' set up method that will run before every test '''
         self.new_source = Source("Kay", "Kay news", "Daily News plug", "https://www.kay.com", "news", "english", "ke")
     def test_instance(self):
         ''' checks if object self.new_source is an instance of Source class '''
         self.assertTrue(isinstance(self.new_source,Source))
     
if __name__ == '__main__':
    unittest.main()