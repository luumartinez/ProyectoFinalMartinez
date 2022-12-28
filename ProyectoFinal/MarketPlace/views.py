from django.shortcuts import render
from django.http import HttpResponse

from MarketPlace.models import Producto, Vendedor, Categoria
from django.core import serializers

from MarketPlace.forms import ProductoFormulario, VendedorFormulario, CategoriaFormulario

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.

def inicio(request):
    return render(request,'MarketPlace/inicio.html')

def categorias(request):
    if request.method == "POST":
            miFormulario = CategoriaFormulario(request.POST)
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                categoria = Categoria(tipo=informacion["tipo"], estado=informacion["estado"], tamanio=informacion["tamanio"])
                categoria.save()
                return render(request, 'MarketPlace/inicio.html')
    else:
        miFormulario = CategoriaFormulario()
    
    return render(request, 'MarketPlace/categorias.html',{"miFormulario":miFormulario})

def productos(request):
    if request.method == "POST":
            miFormulario = ProductoFormulario(request.POST)
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                producto = Producto(nombre_producto=informacion["nombre_producto"], precio=informacion["precio"], stock=informacion["stock"])
                producto.save()
                return render(request, 'MarketPlace/inicio.html')
    else:
        miFormulario = ProductoFormulario()
    
    return render(request, 'MarketPlace/productos.html',{"miFormulario":miFormulario})

def vendedores(request):
    if request.method == "POST":
            miFormulario = VendedorFormulario(request.POST)
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                vendedor = Vendedor(nombre_apellido=informacion["nombre_apellido"], mail=informacion["mail"], codigo_interno=informacion["codigo_interno"])
                vendedor.save()
                return render(request, 'MarketPlace/inicio.html')
    else:
        miFormulario = VendedorFormulario()
    
    return render(request, 'MarketPlace/vendedores.html',{"miFormulario":miFormulario})

def productosapi(request):
    productos_todos = Producto.objects.all()
    return HttpResponse(serializers.serialize('json', productos_todos))

def vendedoresapi(request):
    vendedores_todos = Vendedor.objects.all()
    return HttpResponse(serializers.serialize('json', vendedores_todos))

def categoriasapi(request):
    categorias_todas = Categoria.objects.all()
    return HttpResponse(serializers.serialize('json', categorias_todas))

def busquedaProducto(request):
    return render(request, 'MarketPlace/busquedaProducto.html')

def buscarp(request):
    nombre_producto_views = request.GET['nombre_producto']
    productos_todos = Producto.objects.filter(nombre_producto = nombre_producto_views)
    return render(request, 'MarketPlace/resultadoProducto.html', {'nombre_producto': nombre_producto_views, 'productos': productos_todos})

def busquedaCategoria(request):
    return render(request, 'MarketPlace/busquedaCategoria.html')

def buscarc(request):
    tipo_views = request.GET['tipo']
    categorias_todas = Categoria.objects.filter(tipo = tipo_views)
    return render(request, 'MarketPlace/resultadoCategoria.html', {'tipo': tipo_views, 'categorias': categorias_todas})

def busquedaVendedor(request):
    return render(request, 'MarketPlace/busquedaVendedor.html')

def buscarv(request):
    nombre_apellido_views = request.GET['nombre_apellido']
    vendedores_todos = Vendedor.objects.filter(nombre_apellido = nombre_apellido_views)
    return render(request, 'MarketPlace/resultadoVendedor.html', {'nombre_apellido': nombre_apellido_views, 'vendedores': vendedores_todos})

def leer_productos (request):
    productos_all = Producto.objects.all()
    return HttpResponse(serializers.serialize('json', productos_all))

def crear_producto (request):
    producto = Producto(nombre_producto='batidora',precio=2966,stock=True)
    producto.save()
    return HttpResponse(f'El producto {producto.nombre_producto} ha sido creado')

def editar_producto(request):
    nombre_consulta = 'batidora'
    Producto.objects.filter(nombre_producto=nombre_consulta).update(nombre_producto='NuevaBatidora')
    return HttpResponse(f'El producto {nombre_consulta} ha sido actualizado')

def eliminar_producto(request):
    nombre_nuevo='NuevaBatidora'
    producto = Producto.objects.get(nombre_producto=nombre_nuevo)
    producto.delete()
    return HttpResponse(f'El producto {nombre_nuevo} ha sido eliminado')

class ProductoList(ListView):
    model = Producto
    template = 'MarketPlace/producto_list.html'

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    success_url = '/MarketPlace/producto/list'

class ProductoEdit(UpdateView):
    model = Producto
    fields = '__all__'
    success_url = '/MarketPlace/producto/list'

class ProductoDetail(DetailView):
    model = Producto
    template = 'MarketPlace/producto_detail.html'

class ProductoDelete(DeleteView):
    model = Producto
    success_url = '/MarketPlace/producto/list'

def leer_categorias (request):
    categorias_all = Categoria.objects.all()
    return HttpResponse(serializers.serialize('json', categorias_all))

def crear_categoria (request):
    categoria = Categoria(tipo='jardin',estado= 'nuevo',tamanio= 455)
    categoria.save()
    return HttpResponse(f'La categoria {categoria.tipo} ha sido creado')

def editar_categoria(request):
    tipo_consulta = 'jardin'
    Categoria.objects.filter(tipo= tipo_consulta).update(tipo='NuevoJardin')
    return HttpResponse(f'La categoria {tipo_consulta} ha sido actualizada')

def eliminar_categoria(request):
    tipo_nuevo='NuevoJardin'
    categoria = Categoria.objects.get(tipo=tipo_nuevo)
    categoria.delete()
    return HttpResponse(f'El tipo de categoria {tipo_nuevo} ha sido eliminado')

class CategoriaList(ListView):
    model = Categoria
    template = 'MarketPlace/categoria_list.html'

class CategoriaCreate(CreateView):
    model = Categoria
    fields = '__all__'
    success_url = '/MarketPlace/categoria/list'

class CategoriaEdit(UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = '/MarketPlace/categoria/list'

class CategoriaDetail(DetailView):
    model = Categoria
    template = 'MarketPlace/categoria_detail.html'

class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = '/MarketPlace/categoria/list'


def leer_vendedores (request):
    vendedores_all = Vendedor.objects.all()
    return HttpResponse(serializers.serialize('json', vendedores_all))

def crear_vendedor (request):
    vendedor = Vendedor(nombre_apellido='Lautaro Martinez',mail='lautarito@gmail.com',codigo_interno=22)
    vendedor.save()
    return HttpResponse(f'El vendedor {vendedor.nombre_apellido} ha sido creado')

def editar_vendedor(request):
    nombre_consulta = 'Lautaro Martinez'
    Vendedor.objects.filter(nombre_apellido=nombre_consulta).update(nombre_apellido='Dibu Martinez')
    return HttpResponse(f'El vendedor {nombre_consulta} ha sido actualizado')

def eliminar_vendedor(request):
    nombre_nuevo='Dibu Martinez'
    vendedor = Vendedor.objects.get(nombre_apellido=nombre_nuevo)
    vendedor.delete()
    return HttpResponse(f'El vendedor {nombre_nuevo} ha sido eliminado')

class VendedorList(ListView):
    model = Vendedor
    template = 'MarketPlace/vendedor_list.html'

class VendedorCreate(CreateView):
    model = Vendedor
    fields = '__all__'
    success_url = '/MarketPlace/vendedor/list'

class VendedorEdit(UpdateView):
    model = Vendedor
    fields = '__all__'
    success_url = '/MarketPlace/vendedor/list'

class VendedorDetail(DetailView):
    model = Vendedor
    template = 'MarketPlace/vendedor_detail.html'

class VendedorDelete(DeleteView):
    model = Vendedor
    success_url = '/MarketPlace/vendedor/list'