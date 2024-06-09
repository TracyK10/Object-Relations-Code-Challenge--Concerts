class Band:
    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown
        self._concerts = []
        self._venues = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, hometown):
        if hasattr(self, '_hometown'):
            raise AttributeError("Hometown cannot be changed after the band is instantiated")
        if isinstance(hometown, str) and len(hometown)>0:
            self._hometown = hometown
        else:
            raise ValueError("Hometown must be a non-empty string")
    
    @property
    def concerts(self):
        return self._concerts
    
    def add_concerts(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise ValueError("Concert must be an instance of Concert class")
    
    @property
    def venues(self):
        return self._venues
    
    def add_venues(self, venue):
        if isinstance(venue, Venue):
            self._venues.append(venue)
        else:
            raise ValueError("Venues must be of type Venue")

    def play_in_venue(self, venue, date):
        """Creates and returns a new concert object for the band in that venue on that date"""
        concert = Concert(date, self, venue)
        self.add_concerts(concert)
        venue.add_concerts(concert)
        self.add_venues(venue)

    def all_introductions(self):
        if not self._concerts:
            return None
        return [concert.introduction() for concert in self._concerts]


class Concert:
    def __init__(self, date, band, venue):
        self._date = date
        self._band = band
        self._venue = venue
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date)>0:
            self._date = date
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band
        else:
            raise ValueError("Band must be an instance of Band")
        
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, venue):
        if isinstance(venue, Venue):
            self._venue = venue
        else:
            raise ValueError("Venue must be an instance of Venue")
    
    def hometown_show(self):
        """Returns True if the concert is in the band's hometown else returns False"""
        if self.venue.city == self.band.hometown:
            return True
        else:
            return False

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all_concerts = []
    
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._concerts = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city)>0:
            self._city = city
        else:
            raise ValueError("City must be a non-empty string")

    def add_concerts(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise ValueError("Concert must be an instance of Concert")

    def concerts(self):
        return self._concerts

    def concert_on(self, date):
        return [concert for concert in self._concerts if concert.date == date]

    def bands(self):
        return list(set(concert.band for concert in self._concerts))
