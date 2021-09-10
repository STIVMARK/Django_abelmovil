from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.


#def login(request):
#    return render(request, "registration/login.html")

def index(request):
    return render(request, "base.html")


# ******************************************************************
# CRUD de user
# ******************************************************************

def c_usuario(request):
    if request.method == "POST":
        usuarioform=UsuarioForm(request.POST)
        if usuarioform.is_valid():
            usuarioform.save()
            return redirect('r_usuario')
        else:
            usuarioform = UsuarioForm()
    else:
        usuarioform = UsuarioForm()

    return render(request,"usuario/c_usuario.html",{'usuarioform':usuarioform})


def r_usuario(request):

    usuario = Usuario.objects.all()
    return render(request,"usuario/r_usuario.html",{'usuario_ls':usuario})


def u_usuario(request,id):
    if request.method =="POST":
        usuario = get_object_or_404(Usuario, pk=id)
        usuarioForm =UsuarioForm(request.POST or None, instance=usuario)
        if usuarioForm.is_valid():
            usuarioForm.save()
            return redirect('r_usuario')
        else:
            usuarioForm = UsuarioForm(instance=usuario)
    else: #Get
        usuario = get_object_or_404(Usuario, pk=id)
        usuarioForm =UsuarioForm(request.POST or None, instance=usuario)
    return render(request,"usuario/u_usuario.html",{'usuarioForm':usuarioForm})


def d_usuario(request, id):
    if request.method =="POST":
        usuario = get_object_or_404(Usuario,pk=id)
        usuarioForm = UsuarioForm(request.POST or None, instance= usuario)
        if usuarioForm.is_valid():
            usuario.estado = 0
            usuario.save()
            return redirect('r_usuario')
    else: #get
        usuario = get_object_or_404(Usuario, pk=id)
        usuarioForm = UsuarioForm(request.POST or None, instance=usuario)

    return render(request,"usuario/d_usuario.html",{'userForm': usuarioForm})




# ******************************************************************
# CRUD de cliente
# ******************************************************************

def c_cliente(request):
    if request.method == "POST":
        clienteform=ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()
            return redirect('r_cliente')
        else:
            clienteform = ClienteForm()
    else:
        clienteform = ClienteForm()

    return render(request,"cliente/c_cliente.html",{'clienteform':clienteform})


def r_cliente(request):

    cliente = Cliente.objects.all()
    return render(request,"cliente/r_cliente.html",{'cliente_ls':cliente})


def u_cliente(request,id):
    if request.method =="POST":
        cliente = get_object_or_404(Cliente, pk=id)
        clienteform =ClienteForm(request.POST or None, instance=cliente)
        if clienteform.is_valid():
            clienteform.save()
            return redirect('r_cliente')
        else:
            clienteform = ClienteForm(instance=cliente)
    else: #Get
        cliente = get_object_or_404(Cliente, pk=id)
        clienteform =ClienteForm(request.POST or None, instance=cliente)
    return render(request,"cliente/u_cliente.html",{'clienteform':clienteform})


def d_cliente(request, id):
    if request.method =="POST":
        cliente = get_object_or_404(Cliente,pk=id)
        clienteform = ClienteForm(request.POST or None, instance= cliente)
        if clienteform.is_valid():
            cliente.estado = 0
            cliente.save()
            return redirect('r_cliente')
    else: #get
        cliente = get_object_or_404(Cliente, pk=id)
        clienteform = ClienteForm(request.POST or None, instance=cliente)

    return render(request,"cliente/d_cliente.html",{'clienteform': clienteform})





# ******************************************************************
# CRUD de Mantenimiento
# ******************************************************************

def c_mantenimiento(request):
    if request.method == "POST":
        mantenimientoform=MantenimientoForm(request.POST)
        if mantenimientoform.is_valid():
            mantenimientoform.save()
            return redirect('r_mantenimiento')
        else:
            mantenimientoform = MantenimientoForm()
    else:
        mantenimientoform = MantenimientoForm()

    return render(request,"mantenimiento/c_mantenimiento.html",{'mantenimientoform':mantenimientoform})


def r_mantenimiento(request):
    mantenimiento = Mantenimiento.objects.all()
    return render(request,"mantenimiento/r_mantenimiento.html",{'mantenimientos_ls':mantenimiento})



def u_mantenimiento(request,id):
    if request.method =="POST":
        mantenimiento = get_object_or_404(Mantenimiento, pk=id)
        mantenimientoForm =MantenimientoForm(request.POST or None, instance=mantenimiento)
        if mantenimientoForm.is_valid():
            mantenimientoForm.save()
            return redirect('r_mantenimiento')
        else:
            mantenimientoForm = MantenimientoForm(instance=mantenimiento)
    else: #Get
        mantenimiento = get_object_or_404(Mantenimiento, pk=id)
        mantenimientoForm =MantenimientoForm(request.POST or None, instance=mantenimiento)
    return render(request,"mantenimiento/u_mantenimiento.html",{'mantenimientoForm':mantenimientoForm})


def d_mantenimiento(request, id):
    if request.method =="POST":
        mantenimiento = get_object_or_404(Mantenimiento,pk=id)
        mantenimientoForm = MantenimientoForm(request.POST or None, instance= mantenimiento)
        if mantenimientoForm.is_valid():
            mantenimiento.estado = 0
            mantenimiento.save()
            return redirect('r_mantenimiento')
    else: #get
        mantenimiento = get_object_or_404(Mantenimiento, pk=id)
        mantenimientoForm = MantenimientoForm(request.POST or None, instance=mantenimiento)

    return render(request,"mantenimiento/d_mantenimiento.html",{'mantenimientoForm': mantenimientoForm})







# ******************************************************************
# CRUD de Nota Venta
# ******************************************************************

def c_nota_venta(request):
    if request.method == "POST":
        nota_ventaform= NotaVentaForm(request.POST)
        if nota_ventaform.is_valid():
            nota_ventaform.save()
            return redirect('r_nota_venta')
        else:
            nota_ventaform = NotaVentaForm()
    else:
        nota_ventaform = NotaVentaForm()

    return render(request,"nota_venta/c_nota_venta.html",{'nota_venta_form': nota_ventaform})


def r_nota_venta(request):
    nota_venta = Nota_Venta.objects.all()
    return render(request,"nota_venta/r_nota_venta.html",{'nota_venta_ls':nota_venta})


def u_nota_venta(request,id):
    if request.method =="POST":
        nota_venta = get_object_or_404(Nota_Venta, pk=id)
        nota_ventaform =NotaVentaForm(request.POST or None, instance=nota_venta)
        if nota_ventaform.is_valid():
            nota_ventaform.save()
            return redirect('r_nota_venta')
        else:
            nota_ventaform = NotaVentaForm(instance=nota_venta)
    else: #Get
        nota_venta = get_object_or_404(Nota_Venta, pk=id)
        nota_ventaform =NotaVentaForm(request.POST or None, instance=nota_venta)
    return render(request,"nota_venta/u_nota_venta.html",{'nota_ventaform':nota_ventaform})


def d_nota_venta(request, id):
    if request.method =="POST":
        nota_venta = get_object_or_404(Nota_Venta,pk=id)
        nota_ventaform = NotaVentaForm(request.POST or None, instance= nota_venta)
        if nota_ventaform.is_valid():
            nota_venta.estado = 0
            nota_venta.save()
            return redirect('r_nota_venta')
    else: #get
        nota_venta = get_object_or_404(Nota_Venta, pk=id)
        nota_ventaform = NotaVentaForm(request.POST or None, instance=nota_venta)

    return render(request,"nota_venta/d_nota_venta.html",{'nota_ventaform': nota_ventaform})



# ******************************************************************
# CRUD de Detalle Venta
# ******************************************************************

def c_detalle_nota_venta(request):
    if request.method == "POST":
        detalle_ventaform=DetalleVentaForm(request.POST)
        if detalle_ventaform.is_valid():
            detalle_ventaform.save()
            return redirect('r_detalle_nota_venta')
        else:
            detalle_ventaform = DetalleVentaForm()
    else:
        detalle_ventaform = DetalleVentaForm()

    return render(request,"detalle_venta/c_detalle_venta.html",{'detalle_ventaform':detalle_ventaform})


def r_detalle_nota_venta(request):

    detalle_venta = Detalle_Nota_Venta.objects.all()
    return render(request,"detalle_venta/r_detalle_venta.html",{'detalle_venta_ls':detalle_venta})


def u_detalle_nota_venta(request,id):
    if request.method =="POST":
        detalle_venta = get_object_or_404(Detalle_Nota_Venta, pk=id)
        detalle_ventaForm =DetalleVentaForm(request.POST or None, instance=detalle_venta)
        if detalle_ventaForm.is_valid():
            detalle_ventaForm.save()
            return redirect('r_detalle_nota_venta')
        else:
            detalle_ventaForm = DetalleVentaForm(instance=detalle_venta)
    else: #Get
        detalle_venta = get_object_or_404(Detalle_Nota_Venta, pk=id)
        detalle_ventaForm =DetalleVentaForm(request.POST or None, instance=detalle_venta)
    return render(request,"detalle_venta/u_detalle_venta.html",{'detalle_ventaForm':detalle_ventaForm})


def d_detalle_nota_venta(request, id):
    if request.method =="POST":
        detalle_venta = get_object_or_404(Detalle_Nota_Venta,pk=id)
        detalle_ventaForm = DetalleVentaForm(request.POST or None, instance= detalle_venta)
        if detalle_ventaForm.is_valid():
            detalle_venta.estado = 0
            detalle_venta.save()
            return redirect('r_detalle_nota_venta')
    else: #get
        detalle_venta = get_object_or_404(Detalle_Nota_Venta, pk=id)
        detalle_ventaForm = DetalleVentaForm(request.POST or None, instance=detalle_venta)

    return render(request,"detalle_venta/d_detalle_venta.html",{'detalle_ventaForm': detalle_ventaForm})


# ******************************************************************
# CRUD de factura
# ******************************************************************

def c_factura(request):
    if request.method == "POST":
        facturaform=FacturaForm(request.POST)
        if facturaform.is_valid():
            facturaform.save()
            return redirect('r_factura')
        else:
            facturaform = FacturaForm()
    else:
        facturaform = FacturaForm()

    return render(request,"factura/c_factura.html",{'facturaform':facturaform})


def r_factura(request):

    factura = Factura.objects.all()
    return render(request,"factura/r_factura.html",{'factura_ls':factura})


def u_factura(request,id):
    if request.method =="POST":
        factura = get_object_or_404(Factura, pk=id)
        facturaForm =FacturaForm(request.POST or None, instance=factura)
        if facturaForm.is_valid():
            facturaForm.save()
            return redirect('r_factura')
        else:
            facturaForm = FacturaForm(instance=factura)
    else: #Get
        factura = get_object_or_404(Factura, pk=id)
        facturaForm =FacturaForm(request.POST or None, instance=factura)
    return render(request,"factura/u_factura.html",{'facturaForm':facturaForm})


def d_factura(request, id):
    if request.method =="POST":
        factura = get_object_or_404(Factura,pk=id)
        facturaForm = FacturaForm(request.POST or None, instance= factura)
        if facturaForm.is_valid():
            factura.estado = 0
            factura.save()
            return redirect('r_factura')
    else: #get
        factura = get_object_or_404(Factura, pk=id)
        facturaForm = FacturaForm(request.POST or None, instance=factura)

    return render(request,"factura/d_factura.html",{'facturaForm': facturaForm})














