class Contact:
    def __init__(self, fn, ln, ph, addr, city, zip):
        self.first_name = fn
        self.last_name = ln
        self.phone_number = ph
        self.address = addr
        self.city = city
        self.zip = zip

    def __lt__(self, other):
        if self.last_name == other.last_name:
            if self.first_name == other.first_name:
                return True
            else:
                return False


    def __str__(self):
        return self.first_name + ' ' + self.last_name + '\n ' + self.phone_number + '\n ' + self.address + '\n ' + self.city+ " " + self.zip
    def __repr__(self):
        return f"{self.first_name},{self.last_name},{self.phone_number},{self.address},{self.city},{self.zip}"