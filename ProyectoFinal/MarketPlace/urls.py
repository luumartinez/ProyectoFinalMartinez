from django.urls import path
from MarketPlace import views

urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('categorias/', views.categorias,name='Categorias'),
    path('categoriasApi/', views.categoriasapi),
    path('productos/', views.productos,name='Productos'),
    path('productosApi/', views.productosapi),
    path('vendedores/', views.vendedores,name='Vendedores'),
    path('vendedoresApi/', views.vendedoresapi),
    path('busquedaProducto/', views.busquedaProducto,name='BusquedaProducto'),
    path('buscarp/', views.buscarp),
    path('busquedaCategoria/', views.busquedaCategoria,name='BusquedaCategoria'),
    path('buscarc/', views.buscarc),
    path('busquedaVendedor/', views.busquedaVendedor,name='BusquedaVendedor'),
    path('buscarv/', views.buscarv),
    path('crearProducto/', views.crear_producto),
    path('leerProductos/', views.leer_productos),
    path('editarProducto/', views.editar_producto),
    path('eliminarProducto/', views.eliminar_producto),
    path('producto/list/', views.ProductoList.as_view(),name='ListProduct'),
    path('producto/create/', views.ProductoCreate.as_view(),name='NewProduct'),
    path('producto/edit/<pk>', views.ProductoEdit.as_view(),name='EditProduct'),
    path('producto/detail/<pk>', views.ProductoDetail.as_view(),name='DetailProduct'),
    path('producto/delete/<pk>', views.ProductoDelete.as_view(),name='DeleteProduct'),
    path('crearCategoria/', views.crear_categoria),
    path('leerCategoria/', views.leer_categorias),
    path('editarCategoria/', views.editar_categoria),
    path('eliminarCategoria/', views.eliminar_categoria),
    path('categoria/list/', views.CategoriaList.as_view(),name='ListCategoria'),
    path('categoria/create/', views.CategoriaCreate.as_view(),name='NewCategoria'),
    path('categoria/edit/<pk>', views.CategoriaEdit.as_view(),name='EditCategoria'),
    path('categoria/detail/<pk>', views.CategoriaDetail.as_view(),name='DetailCategoria'),
    path('categoria/delete/<pk>', views.CategoriaDelete.as_view(),name='DeleteCategoria'),
    path('crearVendedor/', views.crear_vendedor),
    path('leerVendedor/', views.leer_vendedores),
    path('editarVendedor/', views.editar_vendedor),
    path('eliminarVendedor/', views.eliminar_vendedor),
    path('vendedor/list/', views.VendedorList.as_view(),name='ListVendedor'),
    path('vendedor/create/', views.VendedorCreate.as_view(),name='NewVendedor'),
    path('vendedor/edit/<pk>', views.VendedorEdit.as_view(),name='EditVendedor'),
    path('vendedor/detail/<pk>', views.VendedorDetail.as_view(),name='DetailVendedor'),
    path('vendedor/delete/<pk>', views.VendedorDelete.as_view(),name='DeleteVendedor'),
]