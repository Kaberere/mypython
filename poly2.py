class ElectricOutlet:
    pass


class UKOutlet(ElectricOutlet):
    pass


class USOutlet(ElectricOutlet):
    pass
andrew_outlet = USOutlet()
edem_outlet = UKOutlet()
print(isinstance(andrew_outlet, ElectricOutlet))
print(isinstance(edem_outlet, ElectricOutlet))
