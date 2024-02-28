#| Implement a URL shortener with the following methods:
#| shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
#| restore(short), which expands the shortened string into the original url.
#| If no such shortened string exists, return null.

#-----------------#
# Define Function #
#-----------------#

import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_short = {}
        self.short_to_url = {}
        self.base_url = "http://short.url/"
        self.alphabet = string.ascii_letters + string.digits  # Alphanumeric characters
        self.short_length = 6

    def generate_short_key(self):
        """Generates a unique six-character key."""
        key = ''.join(random.choices(self.alphabet, k=self.short_length))
        while key in self.short_to_url:
            key = ''.join(random.choices(self.alphabet, k=self.short_length))
        return key

    def shorten(self, url):
        """Shortens the url into a six-character alphanumeric string."""
        #| Check if the URL has already been shortened
        if url in self.url_to_short:
            return self.base_url + self.url_to_short[url]
        
        #| Generate a unique short key
        short_key = self.generate_short_key()
        
        #| Map the URL to the new short key and vice versa
        self.url_to_short[url] = short_key
        self.short_to_url[short_key] = url
        
        return self.base_url + short_key

    def restore(self, short):
        """Expands the shortened string into the original url."""
        #| Extract the key from the shortened URL
        short_key = short.replace(self.base_url, "")
        
        #| Return the original URL if it exists
        if short_key in self.short_to_url:
            return self.short_to_url[short_key]
        
        #| Return None if the shortened URL does not exist
        return None

#------------------#
# Test Application #
#------------------#

shortener = URLShortener()
short_url = shortener.shorten("https://www.example.com")
print("Shortened URL:", short_url)

original_url = shortener.restore(short_url)
print("Original URL:", original_url)
