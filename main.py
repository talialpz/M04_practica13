#Se importa los archivos del integrante A al archivo conjunto para imprimir los resultados.

#Se crea una primera instancia de animal modificando el atributo peso
from animal import animal
#Se dota de valores a la instancia importada.
an = animal("tigre", "120", "vivípara", "carnivora", "tropical", "vertebrada")
#Se llama a la función que nos enseñara los atributos de nuestro objeto.
an.salutacio()
#Se modifica un atributo.
an.setPeso("250")
#Se vuelve a llamar a la función que nos permitira ver el atributo modificado
an.salutacio()

#Se crea una segunda instancia de animal y se modifica el atributo habitat
av = animal("avestruz", "100", "oviparo", "omnivora", "húmedo", "vertebrada")
av.salutacio()
av.setHabitat("seco")
av.salutacio()

#Se crea una primera instancia de vehicle y se modifica el atributo marca
from vehicle import vehicle
ve = vehicle("Toyota", "verso", "blanco", "7", "68mil", "2007KKG")
ve.parts()
ve.setMarca("Seat")
ve.parts()

#Se crea una segunda instancia de vehicle y se modifica el atributo color
vh = vehicle("Nissan", "qashqai", "negro", "5", "90mil", "3657LLP")
vh.parts()
vh.setColor("rojo")
vh.parts()

#Se crea una primera instancia de school y se modifica el atributo pais
from school import school
sc = school("Jaime Balmes", "España", "1942", "Bachillerato", "concertado", "850")
sc.info()
sc.setPais("Republica dominicana")
sc.info()

#Se crea una segunda instancia de school y se modifica el atributo capacidad
sh = school("Mariano Moreno 81", "Argentina", "1898", "primaria", "publico", "600")
sh.info()
sh.setCapacidad("700")
sh.info()



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