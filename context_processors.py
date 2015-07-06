from src.productsdb.productsdb.settings import PORTAL_URL

def products_proc(request):
    return {'PORTAL_URL': PORTAL_URL}