class Band:

    all_bands = []

    def __init__(self, name, musicians):
        self.band_name = name
        self.members = musicians
        self.__class__.all_bands.append(self)

class Musician:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Vocalist(Musician):
    def __repr__(self):
        return 'Vocalist ' +  self.name

    def __str__(self):
        return 'I am a Vocalist named ' + self.name

class Guitarist(Musician):
    pass




# A Vocalist "Is A" Musician


iggy = Vocalist('Iggy Pop')

print(str(5))


steve = Guitarist('Steve Vai')

the_stooges = Band('The Stooges',[iggy, steve])

# print('The Stooges', the_stooges.members)
assert len(the_stooges.members) == 2

the_go_gos = Band("The Go Gos", [Vocalist('Belinda Carlile')])
# print('The Go Gos', the_go_gos.members)
# assert len(the_go_gos.members) == 1

# assert len(the_stooges.members) == 2, 'Stooges should be 2 members'

# assert len(Band.all_bands) == 2

# print('success!')





















