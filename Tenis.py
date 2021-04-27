#Programa de simulación de tienda virtual de ropa orientado a objetos
#Elaborado por Isaac Valverde
#24/04/2021
class tenis:
	#-------Se definen los atributos-------
	#Invetario del producto (número de ejemplares que hay del producto)
	#inventario=0
	#Nombre del producto (Cadena de texto)
	#modelo="unknown"
	#Precio del producto
	#precio=0
	#Ganancias que ha generado el producto
	ganancias=0
	#Numero de articulos vendidos
	ventas=0

	#-------Se definen los metodos-------
	#inicialización del objeto
	def __init__ (self, model, invent, price):
		self.modelo=model
		self.inventario=invent
		self.precio=price

	#Vender (Se resta el número de tenis que se venden al inventario)
	def venta (self, vendidos):
		#Se revisa si hay suficientes productos en el inventario para cubrir el pedido
		if (vendidos>self.inventario):
			#Se notifica que no hay suficientes productos para cubrir el pedido
			return ("No hay productos suficientes para cubrir el pedido")
		else:
			#Se resta el numero de productos vendidos al invetario
			self.inventario-=vendidos #Esto es equivalente a: self.inventario=self.inventario-vendidos
			#Se registra el monto de la venta
			tenis.ganancias+=self.precio*vendidos
			#Se registra la cantidad de articulos que se vendió
			tenis.ventas+=vendidos

	#Surtir (Se suma el número de tenis que llegan al inventario)
	def surtir (self, surtidos):
		#Se añade al inventario el numero de productos que llegan
		self.inventario+=surtidos #Esto es equivalente a: self.inventario=self.inventario+surtidos

	#Ventas (Devuelve la cantidad de articulos que se han vendido y su valor economico)
	def historial (self):
		return (tenis.ventas,tenis.ganancias)

