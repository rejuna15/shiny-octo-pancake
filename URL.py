import math, string
import validators


class URL:
    all_chararcters = string.digits + string.ascii_letters
    base = len(all_chararcters)

    def parse_url(self, url):
        return validators.url(url)

    def encode(self, url_id):
        ret = []
        while url_id > 0:
            val = url_id % self.base # taking the last digit in id
            ret.append(self.all_chararcters[val])
            url_id = url_id // self.base
        return "".join(ret[::-1])

    def decode(self, short_url):
        int_sum = 0
        reversed_key = short_url[::-1]
        for idx, char in enumerate(reversed_key):
            int_sum += self.all_chararcters.index(char) * int(math.pow(self.base, idx))
        return int_sum
