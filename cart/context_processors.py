from .cart import Cart

# create context processor to work on all pages
def cart(request):
	# return
	return {'cart': Cart(request)}