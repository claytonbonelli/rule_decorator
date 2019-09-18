import rule


class MyRules1:

    @rule.rule
    def example1(self):
        print(1)

    @rule.rule
    def example2(self):
        print(2)

    @rule.rule
    def example3(self):
        print(3)


rule.validate(MyRules1)


class MyRules2:

    @rule.rule(3)
    def example1(self):
        print(11)

    @rule.rule(1)
    def example2(self):
        print(22)

    @rule.rule(2)
    def example3(self):
        print(33)


rule.validate(MyRules2)


class MyRules3:

    def __init__(self, *args, **kwargs):
        self.sum = kwargs['data']['sum']

    @rule.rule
    def example1(self):
        if self.sum > 10:
            print(111, "greater than 10")

    @rule.rule
    def example2(self):
        if self.sum == 10:
            print(222, "equals 10")

    @rule.rule
    def example3(self):
        if self.sum < 10:
            print(333, "less than 10")


rule.validate(MyRules3, data={'sum': 10})