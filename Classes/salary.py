from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, work_hour = 0):
        super().__init__(name)
        self._work_hour = work_hour

    def get_salary(self):
        return 200.0 * self._work_hour


class Saleman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    def get_salary(self):
        return 1800.0 + self._sales * 0.05


class EmployeeFactory():
    """创建员工的工厂（工厂模式-通过工厂实现对象使用者和对象之间的解耦合"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        if emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Saleman(*args, **kwargs)
        return emp


def main():
    emp_inf= [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('p', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000)
    ]
    for emp in emp_inf:
        print(f'{emp._name}: {emp.get_salary()}')


if __name__ == '__main__':
    main()