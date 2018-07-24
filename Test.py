# Unit Tests
# To run this test suite we need to have a package TextBlob installed
# Please type the following commands in the command prompt to install the package
# $ pip install -U textblob
# $ python -m textblob.download_corpora

from textblob import TextBlob
import unittest
from Index import tokenize_into_words, count_unique_words, display_top_n_words

class TestSimpleDistributerFileIndexer(unittest.TestCase):
     def test_find_top_n_words(self):
          total_count_of_words = {'rackspace': 2, 'is': 5}
          n=10
          result= display_top_n_words(total_count_of_words,n)
          expected = [('is',5),('rackspace',2)]
          self.assertEqual(expected, result)

     def test_to_check_case_insensitive(self):
          words = ['rackspace', 'racKspAce', 'RACKSPACE']
          result = count_unique_words(words)
          expected = {'rackspace': 3}
          self.assertEqual(expected, result)


     def test_to_check_if_tokenize_function_allows_TextBlob(self):
          myBlob = TextBlob("Rackspace Inc. is a managed cloud computing company based in Windcrest, Texas, USA, suburb of San Antonio, Northern Texas.")
          result = tokenize_into_words(str(myBlob))
          expected = ['Rackspace', 'Inc', 'is', 'a', 'managed', 'cloud', 'computing', 'company', 'based', 'in', 'Windcrest', 'Texas', 'USA', 'suburb', 'of', 'San', 'Antonio', 'Northern', 'Texas']
          self.assertEqual(expected, result)

     def test_to_check_if_input_is_empty_dict(self):
          expected = display_top_n_words({}, 10)
          result = []
          self.assertEqual(expected, result)

     def test_to_split_all_symbols(self):
          expected= tokenize_into_words('!*****@$%^#&*')
          result = []
          self.assertEqual(expected, result)


     # To run the unit tests

     if __name__=='__main__':
         unittest.main()
