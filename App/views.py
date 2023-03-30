from django.shortcuts import render,redirect
from django.http import HttpResponse
import xmlrpc.client
import requests
url = 'http://localhost:8069'
db = 'Movies'
username = 'willycachon@hotmail.com'
password = 'Loveglam1'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username,password,{})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

def index(request):
    try:
        partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[('id','>',7)]])
        datos = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['id','name', 'company_name', 'mobile','picking_warn_msg']})
        
    except Exception as e:   
        return HttpResponse('ERROR')
    
    contexto = {"datos":datos}
    return render(request,"products.html",contexto)

def datos(request):
    try:
        partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[('id','>',7)]])
        datos = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['id','name']})
        return HttpResponse(str(datos))
    except Exception as e:   
        return HttpResponse('Error en los datos Pa')
    
def create(request,name,price,description,stock):
    try:
        id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': name, 'company_name':price, 'mobile':description, 'picking_warn_msg':stock}])
        return redirect ("http://127.0.0.1:8000/")
    except Exception as e:
        return HttpResponse('Error en el create Pa')

def delete(request,id):
    try:
        models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
        return redirect ("http://127.0.0.1:8000/")
    except Exception as e:
        return HttpResponse('Error en el delete Mejia UwU')

def update(request,id,name,price,description,stock):
    try:
        models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': name,'company_name':price, 'mobile':description, 'picking_warn_msg':stock}])
        return redirect ("http://127.0.0.1:8000/")
    except Exception as e:
        return HttpResponse('Error en el update UnU')

def formcreate(request):
    return render(request,'create.html')

def ver_producto(request, id):
    try:
        partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[('id','=',id)]])
        datos = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['id','name', 'company_name', 'mobile', 'picking_warn_msg']})
        
    except Exception as e:   
        return HttpResponse('ERROR')
    
    contexto = {"datos":datos}
    return render(request,"details.html",contexto)

def ver_producto_para_editar(request, id):
    try:
        partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[('id','=',id)]])
        datos = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['id','name', 'company_name', 'mobile', 'picking_warn_msg']})
        
    except Exception as e:   
        return HttpResponse('ERROR')
    
    contexto = {"datos":datos}
    return render(request,"update.html",contexto)
