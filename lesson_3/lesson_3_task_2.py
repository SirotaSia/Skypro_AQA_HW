from smartphone import Smartphone

catalog = list()
phone1 = Smartphone('Samsung','Galaxy Note','+79998887766')
phone2 = Smartphone('Vivo','X100','+79998887755')
phone3 = Smartphone('Apple','iPhone 15','+79998887744')
phone4 = Smartphone('Xiaomi','13T','+79998887733')
phone5 = Smartphone('Nokia','Lumia 620','+79998887722')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.subscriber_number}')