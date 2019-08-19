from decimal import Decimal


class CommissionEmployee:
    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, value):
        if value < Decimal("0.0"):
            raise ValueError("gross_sales should be >= 0")

        self._gross_sales = value

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        if not (Decimal("0.0") <= value <= Decimal("1.0")):
            raise ValueError("commission_rate should be between 0 and 1")

        self._commission_rate = value

    @property
    def earnings(self):
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first_name}, {self.last_name}, {self.ssn}, {self.gross_sales}, {self.commission_rate})"


class SalariedCommissionEmployee(CommissionEmployee):
    def __init__(
        self, first_name, last_name, ssn, gross_sales, commission_rate, base_salary
    ):
        super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)
        self.base_salary = base_salary

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        if value < Decimal("0.0"):
            raise ValueError("base_salary should be >= 0")

        self._base_salary = value

    @property
    def earnings(self):
        return self.base_salary + super().earnings

    def __repr__(self):
        return f"Salaried - {super().__repr__()}. Base salary = {self.base_salary:,.2f}"


if __name__ == "__main__":
    c = CommissionEmployee(
        "Sue", "Jones", "333-33-3333", Decimal("10000.00"), Decimal("0.06")
    )
    print(repr(c))
    print(f"{c.earnings:.2f}")

    c.gross_sales = Decimal("20_000.00")
    c.commission_rate = Decimal("0.1")
    print(f"{c.earnings:,.2f}")

    print(f"{'*' * 40} - SalariedCommissionEmployee - {'*' * 40}")

    s = SalariedCommissionEmployee(
        "Bob",
        "Lewis",
        "444-44-4444",
        Decimal("5000.00"),
        Decimal("0.04"),
        Decimal("300.00"),
    )
    print(
        s.first_name,
        s.last_name,
        s.ssn,
        s.gross_sales,
        s.commission_rate,
        s.base_salary,
    )
    print(s.earnings)
    print(repr(s))

