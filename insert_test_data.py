import os
import django

# Asegurarse de que el script pueda acceder a los modelos de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.menu.models import CategoriaProducto, Producto, Ingrediente

def run():
    print("Limpiando base de datos...")
    Producto.objects.all().delete()
    CategoriaProducto.objects.all().delete()
    Ingrediente.objects.all().delete()

    print("Creando ingredientes...")
    ing_camaron = Ingrediente.objects.create(nombre="Camarón")
    ing_pulpo = Ingrediente.objects.create(nombre="Pulpo")
    ing_cebolla = Ingrediente.objects.create(nombre="Cebolla")
    ing_ajo = Ingrediente.objects.create(nombre="Ajo")

    print("Creando categorías...")
    cat_especialidades = CategoriaProducto.objects.create(nombre="Especialidades del Mar")
    cat_caldos = CategoriaProducto.objects.create(nombre="Caldos y Sopas")
    cat_bebidas = CategoriaProducto.objects.create(nombre="Bebidas")

    print("Creando productos...")
    
    # Especialidades
    p1 = Producto.objects.create(
        nombre="Cocteles",
        descripcion="Camarón, caracol, pulpo...",
        precio=70.00,
        categoria=cat_especialidades
    )
    p1.ingredientes.add(ing_camaron, ing_pulpo, ing_cebolla)

    p2 = Producto.objects.create(
        nombre="Mariscada TAWA",
        descripcion="Pulpos encebollados, camarones...",
        precio=250.00,
        categoria=cat_especialidades
    )
    p2.ingredientes.add(ing_camaron, ing_pulpo, ing_cebolla)

    p3 = Producto.objects.create(
        nombre="Pulpos a la Gallega",
        descripcion="Delicioso pulpo cocido con pimentón, aceite de oliva y sal.",
        precio=145.00,
        categoria=cat_especialidades
    )
    p3.ingredientes.add(ing_pulpo)

    p4 = Producto.objects.create(
        nombre="Camarones Empanizados",
        descripcion="Crujientes camarones rebosados acompañados de ensalada.",
        precio=180.00,
        categoria=cat_especialidades
    )
    p4.ingredientes.add(ing_camaron)

    p5 = Producto.objects.create(
        nombre="Tawinas",
        descripcion="Pulpa de cangrejo con aceite, limón, vino, picante, caldo.",
        precio=145.00,
        categoria=cat_especialidades
    )

    p6 = Producto.objects.create(
        nombre="Mojarras",
        descripcion="Frita al mojo de ajo o a la diabla. Precio según peso.",
        precio=150.00, # Precio base
        categoria=cat_especialidades
    )
    p6.ingredientes.add(ing_ajo)

    # Caldos y Sopas
    p7 = Producto.objects.create(
        nombre="Caldo de Camarón",
        descripcion="Tradicional caldo rojo con camarón fresco.",
        precio=170.00,
        categoria=cat_caldos
    )
    p7.ingredientes.add(ing_camaron)

    p8 = Producto.objects.create(
        nombre="Sopa de Mariscos",
        descripcion="La mejor selección de frutos del mar en un caldo sazonado.",
        precio=170.00,
        categoria=cat_caldos
    )
    p8.ingredientes.add(ing_camaron, ing_pulpo)

    # Bebidas
    Producto.objects.create(nombre="Coca Cola", precio=25.00, categoria=cat_bebidas)
    Producto.objects.create(nombre="Cerveza Corona", precio=35.00, categoria=cat_bebidas)
    Producto.objects.create(nombre="Clamato", precio=60.00, categoria=cat_bebidas)
    Producto.objects.create(nombre="Jumex", precio=25.00, categoria=cat_bebidas)
    Producto.objects.create(nombre="Agua Embotellada", precio=25.00, categoria=cat_bebidas)

    print("¡Datos de prueba insertados con éxito!")

if __name__ == '__main__':
    run()
