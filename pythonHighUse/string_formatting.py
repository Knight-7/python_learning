"""
字符串的格式化
"""
def fir_formatting():
    name = 'Knight'
    age = 21
    country = 'China'
    str = "Hello, I'm %s, I'm from %s years old. " \
          "I come from %s. I love my country very much."%(name, age, country)
    print(str)


def sec_formatting():
    strs = []
    information = {'name': 'Knight', 'age': 21}
    strs.append('Hello, {}. Are you {}?'.format('Knight', 21))
    strs.append('Hello, {1}. Are you {0}?'.format(21, 'Knight'))
    strs.append('Hello, {name}. Are you {age1}?'.format(name= 'Knight', age1=21))
    strs.append('Hello, {name}. Are you {age}?'.format(**information))
    for str in strs:
        print(str)


# 因为f-string是在运行时计算的，所以可以将它放在任意合法的Python表达式中
def thir_formatting():
    name = 'Knight'
    age = 21
    str = f'Hello, {name}. Are you {age}?'
    print(str)

    def getName(name):
        return name.upper()

    def agedec(age):
        return age - 1

    str2 = f'Hello, {getName(name)}. Are you {agedec(age)}?'
    print (str2)

    class Person():
        def __init__(self, name, age):
            self.age = age
            self.name = name

        def __str__(self):
            return f'{self.name.upper()} is {self.age}'

    p1 = Person(name, age)
    print(p1)

    str3 = {
        f'Hi {name}.'
        f'Are you {age}?'
    }
    print(str3)


if __name__ == '__main__':
    fir_formatting()
    sec_formatting()
    thir_formatting()