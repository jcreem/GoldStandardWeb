from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context

from generator.models import GoldStandard, ActiveGoldStandard


#def index(request):
#    return HttpResponse("Hello, world. You're at the Generator index.")

def index(request):

    #
    # Build a list of tuples for the active Gold Standards to be expanded
    # by the template
    #
    ActiveStandardList=[]
    for Active in ActiveGoldStandard.objects.all():
        ActiveStandardList.append(
            (Active.goldstandard.get_gen_court_house_display(),
             Active.goldstandard.session_date.strftime('%A, %B %-d, %Y'),
             Active.Gold_PDF_Server_Name,
             Active.White_PDF_Server_Name,
             Active.ZIP_File_Server_Name))
    t=get_template('generator_index.html.dt')
    html=t.render(Context({'ActiveStandardList':ActiveStandardList}))
    return HttpResponse(html)
