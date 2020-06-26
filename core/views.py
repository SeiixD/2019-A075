from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from core.models import DelitoAbierto, Chart1, Chart2, Chart3, Chart4, Chart5, Chart6
import pyodbc

# Create your views here.
def portfolio(request):
    Http_Respone = "<h1>Portafolio</h1>"
    return HttpResponse(Http_Respone)

def base(request):
    
    return render(request, "core/base.html")

def base2(request):
    
    return render(request, "core/base2.html")

def home(request):
    return render(request,"core/home.html")

def premapa(request):
    return render(request,"core/premapa.html")

def dashboard(request):
    conn = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};'
        'Server= DESKTOP-LAI4LO7;'
        'Database=DelitosDatosAbiertos;'
        'UID= pruebas;'
        'PWD=123456;'
        'Trusted_Connection=yes;'
    )
    conn2 = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};'
        'Server= DESKTOP-LAI4LO7;'
        'Database=DelitosDatosNoticias;'
        'UID= pruebas;'
        'PWD=123456;'
        'Trusted_Connection=yes;'
    )
    #"select fct_delitos_noticias.idMunicipio as 'Municipio', DATENAME(MM,dim_fecha.fecha) as 'Mes', DATENAME(YY,dim_fecha.fecha) as 'Ano', COUNT('Mes') as 'Total' from fct_delitos_noticias inner join dim_fecha on dim_fecha.idFecha = fct_delitos_noticias.idFecha where year(dim_fecha.fecha) = 2019 group by DATENAME(MM,dim_fecha.fecha), cube (fct_delitos_noticias.idMunicipio, DATENAME(YY,dim_fecha.fecha)) order by 'Municipio','Mes','Ano' desc"
    cursor1 = conn.cursor()
    cursor1.execute("select top (9) dim_colonia.colonia as 'Colonia', dim_tipo_delito.delito as 'Delito', COUNT(fct_delitos.idTipoDelito) as 'Sumatoria' from fct_delitos inner join dim_colonia on dim_colonia.idColonia = fct_delitos.idColonia inner join dim_tipo_delito on dim_tipo_delito.idTipoDelito = fct_delitos.idTipoDelito where fct_delitos.idTipoDelito = 1 group by Delito, cube (colonia) order by Sumatoria desc")
    result1 = cursor1.fetchall()
    cursor2 = conn.cursor()
    cursor2.execute("select top (9) dim_colonia.colonia as 'Colonia', dim_tipo_delito.delito as 'Delito', COUNT(fct_delitos.idTipoDelito) as 'Sumatoria' from fct_delitos inner join dim_colonia on dim_colonia.idColonia = fct_delitos.idColonia inner join dim_tipo_delito on dim_tipo_delito.idTipoDelito = fct_delitos.idTipoDelito where fct_delitos.idTipoDelito = 3 group by Delito, cube (colonia) order by Sumatoria desc")
    result2 = cursor2.fetchall()
    cursor3 = conn.cursor()
    cursor3.execute("select top (7) fct_delitos.idMunicipio as 'Municipio', DATENAME(dw,dim_fecha.fecha) as 'Dia', COUNT('Dia') as 'Total' from fct_delitos inner join dim_fecha on dim_fecha.idFecha = fct_delitos.idFecha  where idMunicipio=1 group by DATENAME(dw,dim_fecha.fecha), cube (fct_delitos.idMunicipio) order by idMunicipio desc")
    result3 = cursor3.fetchall()
    cursor = conn.cursor()
    cursor.execute("select fct_delitos.idDelito , dim_fecha.fecha  AS 'Fecha', dim_municipio.municipio AS 'Municipio', dim_colonia.colonia AS 'Colonia',  dim_coordenada.latitud AS 'Latitud',  dim_coordenada.longitud AS 'Longitud', dim_tipo_delito.delito AS 'TipoDelito'  from fct_delitos INNER JOIN dim_fecha ON fct_delitos.idFecha = dim_fecha.idFecha INNER JOIN dim_municipio ON fct_delitos.idMunicipio = dim_municipio.idMunicipio INNER JOIN dim_colonia ON fct_delitos.idColonia = dim_colonia.idColonia INNER JOIN dim_coordenada ON fct_delitos.idCoordenada = dim_coordenada.idCoordenada INNER JOIN dim_tipo_delito ON fct_delitos.idTipoDelito = dim_tipo_delito.idTipoDelito")
    result = cursor.fetchall()
    cursor4 = conn2.cursor()
    cursor4.execute("select top (7) fct_delitos_noticias.idMunicipio as 'Municipio', DATENAME(dw,dim_fecha.fecha) as 'Dia', COUNT('Dia') as 'Total' from fct_delitos_noticias inner join dim_fecha on dim_fecha.idFecha = fct_delitos_noticias.idFecha  where idMunicipio=1 group by DATENAME(dw,dim_fecha.fecha), cube (fct_delitos_noticias.idMunicipio) order by idMunicipio desc")
    result4 = cursor4.fetchall()
    cursor5 = conn2.cursor()
    cursor5.execute("select palabraComun as 'Palabra', COUNT(palabraComun) as 'Conteo' from topic_modeling group by palabraComun order by 'Conteo' desc")
    result5 = cursor5.fetchall()
    cursor6 = conn2.cursor()
    cursor6.execute("select top (9) dim_colonia.colonia as 'Colonia', dim_tipo_delito.delito as 'Delito', COUNT(fct_delitos_noticias.idTipoDelito) as 'Sumatoria' from fct_delitos_noticias inner join dim_colonia on dim_colonia.idColonia = fct_delitos_noticias.idColonia inner join dim_tipo_delito on dim_tipo_delito.idTipoDelito = fct_delitos_noticias.idTipoDelito group by Delito, cube (colonia) order by Sumatoria desc")
    result6 = cursor6.fetchall()
    cursor7 = conn2.cursor()
    cursor7.execute("select fct_delitos_noticias.idMunicipio as 'Municipio', DATENAME(MM,dim_fecha.fecha) as 'Mes', DATENAME(YY,dim_fecha.fecha) as 'Ano', COUNT('Mes') as 'Total' from fct_delitos_noticias inner join dim_fecha on dim_fecha.idFecha = fct_delitos_noticias.idFecha where year(dim_fecha.fecha) = 2019 group by DATENAME(MM,dim_fecha.fecha), cube (fct_delitos_noticias.idMunicipio, DATENAME(YY,dim_fecha.fecha)) order by 'Municipio' desc")
    result7 = cursor7.fetchall()
    return render(request,"core/dashboard.html", {'Chart1':result1, 'Chart2':result2, 'Chart3':result3, 'DelitoAbierto':result,  'Chart4':result4, 'Chart5':result5, 'Chart6':result6, 'Chart7':result7 })

def mapa(request):
    conn = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};'
        'Server= DESKTOP-LAI4LO7;'
        'Database=DelitosDatosAbiertos;'
        'UID= pruebas;'
        'PWD=123456;'
        'Trusted_Connection=yes;'
    )
    conn2 = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};'
        'Server= DESKTOP-LAI4LO7;'
        'Database=DelitosDatosNoticias;'
        'UID= pruebas;'
        'PWD=123456;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    
    if(request.POST['Delito']=="4"):
        cursor = conn2.cursor()
        cursor.execute("select fct_delitos_noticias.idDelito , dim_fecha.fecha  AS 'Fecha', dim_municipio.municipio AS 'Municipio', dim_colonia.colonia AS 'Colonia',  dim_coordenada.latitud AS 'Latitud',  dim_coordenada.longitud AS 'Longitud', dim_tipo_delito.delito AS 'TipoDelito'  from fct_delitos_noticias INNER JOIN dim_fecha ON fct_delitos_noticias.idFecha = dim_fecha.idFecha INNER JOIN dim_municipio ON fct_delitos_noticias.idMunicipio = dim_municipio.idMunicipio INNER JOIN dim_colonia ON fct_delitos_noticias.idColonia = dim_colonia.idColonia INNER JOIN dim_coordenada ON fct_delitos_noticias.idCoordenada = dim_coordenada.idCoordenada INNER JOIN dim_tipo_delito ON fct_delitos_noticias.idTipoDelito = dim_tipo_delito.idTipoDelito")    
    else:
        cursor.execute("select fct_delitos.idDelito , dim_fecha.fecha  AS 'Fecha', dim_municipio.municipio AS 'Municipio', dim_colonia.colonia AS 'Colonia',  dim_coordenada.latitud AS 'Latitud',  dim_coordenada.longitud AS 'Longitud', dim_tipo_delito.delito AS 'TipoDelito'  from fct_delitos INNER JOIN dim_fecha ON fct_delitos.idFecha = dim_fecha.idFecha INNER JOIN dim_municipio ON fct_delitos.idMunicipio = dim_municipio.idMunicipio INNER JOIN dim_colonia ON fct_delitos.idColonia = dim_colonia.idColonia INNER JOIN dim_coordenada ON fct_delitos.idCoordenada = dim_coordenada.idCoordenada INNER JOIN dim_tipo_delito ON fct_delitos.idTipoDelito = dim_tipo_delito.idTipoDelito where fct_delitos.idTipoDelito="+request.POST['Delito'])
    result = cursor.fetchall()
    return render(request, "core/mapa.html", {'DelitoAbierto':result, 'getlatitud': request.POST['latitud'], 'getlongitud': request.POST['longitud']})

def extra(request):
    conn = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};'
        'Server= DESKTOP-LAI4LO7;'
        'Database=DelitosAbiertos;'
        'UID= pruebas;'
        'PWD=123456;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("select TOP (10) fct_delitos.idDelito , dim_fecha.fecha  AS 'Fecha', dim_municipio.municipio AS 'Municipio', dim_colonia.colonia AS 'Colonia',  dim_coordenada.latitud AS 'Latitud',  dim_coordenada.longitud AS 'Longitud', dim_tipo_delito.delito AS 'TipoDelito'  from fct_delitos INNER JOIN dim_fecha ON fct_delitos.idFecha = dim_fecha.idFecha INNER JOIN dim_municipio ON fct_delitos.idMunicipio = dim_municipio.idMunicipio INNER JOIN dim_colonia ON fct_delitos.idColonia = dim_colonia.idColonia INNER JOIN dim_coordenada ON fct_delitos.idCoordenada = dim_coordenada.idCoordenada INNER JOIN dim_tipo_delito ON fct_delitos.idTipoDelito = dim_tipo_delito.idTipoDelito")
    result = cursor.fetchall()
    return render(request, "core/extra.html", {'DelitoAbierto':result })