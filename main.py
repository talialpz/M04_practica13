#En aquest main importarem les classes, li donarem valor a les instancies i les trucarem

#Importem la class del document
from book import book
#Li donem el valor a la instancia i la truquem
book1 = book("Tirant lo blanc", "Català", "Joanot Martorell", "271", "1490", "Novel·la")
book1.info()
#Fem el set de name per modificar la instancia anterior
book1.setName("Don Quijote")
book1.info()

book2 = book("Don Quijote", "Castellà", "Miguel de Cervantes", "1345", "1605", "Novel·la")
book2.info()
book2.setName("Tirant lo blanc")
book2.info()


from user import user

user1 = user("Ramon", "Font", "661346808", "rfont22@jaumebalmes.net", "19", "home")
user1.salutacio()
user1.setName("Talia")
user1.salutacio()

user2 = user("Talia", "Lopez", "658449811", "tlopez22@jaumebalmes.net", "25", "indefinit")
user2.salutacio()
user2.setName("Ramon")
user2.salutacio()

from university import university

university1 = university("UAB", "Matins i tardes", "Vicent Villar", "pública", "1968", "barcelona")
university1.info()
university1.setName("UB")
university1.info()

university2 = university("UA", "Matins i tardes", "Alfons el magnanim", "pública", "1824", "barcelona")
university2.info()
university2.setName("UAB")
university2.info()