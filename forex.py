from random import choice
import string

class list_of_conversions():

    def __init__(self):

        self.valid_conversions = self.read_dict("conversions.txt")

    def read_dict(self, dict_path):
        """Read and return all words in dictionary."""

        dict_file = open(dict_path)
        valid_conversions = [w.strip() for w in dict_file]
        dict_file.close()
        return valid_conversions

    def check_valid_(self, word ):
        """Check if a word is a valid word in the conversion list"""

        conversion_exists = word in self.valid_conversions
    

        
        print("break")
        print(conversion_exists)

        if conversion_exists:
            result = "ok"

        else:
            result = "invalid-conversion"
        return result

