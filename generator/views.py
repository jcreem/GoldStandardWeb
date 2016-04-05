from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context

from generator.models import GoldStandard, ActiveGoldStandard


#def index(request):
#    return HttpResponse("Hello, world. You're at the Generator index.")

def index(request):
    ActiveStandardList=[]
    for Active in ActiveGoldStandard.objects.all():
        ActiveStandardList.append(
            (Active.goldstandard.get_gen_court_house_display(),
             Active.goldstandard.session_date.strftime('%A, %B %-d, %Y'),
             Active.goldstandard.get_pdf_name(Gold_Background = True)))
    t=get_template('generator_index.html.dt')
    html=t.render(Context({'ActiveStandardList':ActiveStandardList}))
    return HttpResponse(html)
#     fp=open('/home/jcreem/nhla/GoldStandardWeb/generator/generator_index.html.dt')
#     t=Template(fp.read())
#     fp.close()
#     html=t.render(Context({'ActiveGS':}))
#     return HttpResponse(html)
