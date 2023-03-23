class ForceUser:

    def __str__(self):
        return f'I am {self.name}, my mantra is {self.get_code()}'

    def __repr__(self):
        return 'JediMaster("name")'

    def attacking(self):
        return f'{self.name} is Force attacking!'

    def getting_hit(self):
        return f'{self.name} is being attacked!'

    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count


class JediMaster(ForceUser):

    count = 0

    def __init__(self, name='Random Master'):
        self.name = name
        self.alignment = "good"
        JediMaster.count += 1

    @staticmethod
    def get_code():
        return 'There is no emotion, there is only PEACE.'

    @classmethod
    def get_count(cls):
        return cls.count


class SithLord(ForceUser):

    count = 0

    def __init__(self, name='Random Master'):
        self.name = name
        self.alignment = "bad"
        SithLord.count += 1

    @staticmethod
    def get_code():
        return 'Peace is a lie, there is only PASSION!'

    @classmethod
    def get_count(cls):
        return cls.count


if __name__ == '__main__':
    random = JediMaster()
    yoda = JediMaster('Yoda')
    vader = SithLord('Vader')
    print(yoda)
    print(vader)
    # print(random.name)
    # print(yoda.get_code())
    # print(vader.get_code())
    # print(JediMaster.count)
    # print(SithLord.count)
    # print(ForceUser.get_count())
    # print(random.get_count())
    # print(yoda.get_count())
    print(yoda.__repr__())
