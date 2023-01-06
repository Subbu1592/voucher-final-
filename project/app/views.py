from django.shortcuts import render,redirect
from .models import  Voucher
from .forms import*
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
# Create your views here.

def home(request):
    voucher = Voucher.objects.all()
    
    context = {
        'voucher': voucher
    }
    return render(request, 'home.html', context)

def add(request):
    form = VoucherForm()
    if request.method == 'POST':
        form = VoucherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form,
    }
    
    return render(request, 'add.html', context)





def soft(request, paid_to):
    voucher = Voucher.objects.filter(id=paid_to)
    template_path = 'soft.html'
    context = {'voucher': voucher}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, )
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response






