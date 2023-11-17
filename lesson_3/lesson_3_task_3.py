from address import Address
from mailing import Mailing


mailing = Mailing()
mailing.to_address.post_index = "123 456"
mailing.to_address.city = "City 1"
mailing.to_address.street = "Street 1"
mailing.to_address.house = 1
mailing.to_address.flat = 11

mailing.from_address.post_index = "654 321"
mailing.from_address.city = "City 2"
mailing.from_address.street = "Street 2"
mailing.from_address.house = 2
mailing.from_address.flat = 22

mailing.cost = 1000
mailing.track = 'track_111'

to_address = f' из {mailing.to_address.post_index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}'
from_address = f' в {mailing.from_address.post_index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat}'
print(f'Отправление {mailing.track}' + to_address + from_address + f'. Стоимость {mailing.cost} рублей.')
