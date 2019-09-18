# Business rule decorator

###### By Clayton Boneli

Some applications have methods that are responsible for validating business rules, mainly related to values ​​that reach the application backend layer, as an example:

* information that cannot be empty, eg a date of birth
* a number that must be within a range
* etc

Many applications are built so that one or more rules are validated by methods. The problem arises because the developer has to explicitly call each of these validation methods, but what if he creates a new method and forgets to make the call? What if the call is spread across various parts of the application?

Another similar problem arises from the order of execution. How to call validation methods if they have to be executed in a predefined order? For example methodX must be executed before methodY. Again the programmer must include the call of the methods in the correct order, but what if the order changes? Pu if a new method that changes the order of execution is created?

To take control of the methods explicit call from the developer and the call order, a decorator has been created, where the programmer can define which will be executed and, optionally, their execution order.

As calling a single function the execution of the methods will be controlled by this function and the execution order if one has been defined.

Examples:

```python
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
´´´
