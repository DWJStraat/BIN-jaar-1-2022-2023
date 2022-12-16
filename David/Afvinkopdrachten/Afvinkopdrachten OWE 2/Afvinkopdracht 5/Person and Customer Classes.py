class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone


class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        super().__init__(name, address, phone)
        self.customer_number = str(customer_number)
        self.mailing_list = bool(mailing_list)


def main():
    Me = Customer('David', 'London SW1A 1AA, United Kingdom', '+44 303 123 7300', '0000', True)
    print(Me.name)
    print(Me.address)
    print(Me.phone)
    print(Me.customer_number)
    print(Me.mailing_list)

main()