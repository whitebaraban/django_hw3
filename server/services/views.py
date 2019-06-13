from django.shortcuts import render
import openpyxl
from .models import Service

def read_price():
    file = openpyxl.load_workbook(filename = 'services/fixtures/file.xlsx')
    sheet = file['Лист1']
    services = []
    for i in range(1, 5):
        for j in range(1, 5):
            val = {'name': sheet['A'+str(i)].value, 'price': sheet['B'+str(i)].value}
        services.append(val)
    return services


def services_list(request):
    # return render(request, 'services/services.html', {'services': read_price()})
    return render(
        request,
        'services/services.html',
        {'services': Service.objects.all()}
    )


def service_page(request, pk):
    #return render(request, 'services/service_page.html', {'service': read_price()[pk]})
    return render(
        request,
        'services/service_page.html',
        {'service': Service.objects.get(pk=pk)}
    )