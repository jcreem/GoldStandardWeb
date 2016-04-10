from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.core.management import call_command
from generator.models import GoldStandard, ActiveGoldStandard
#def index(request):
#    return HttpResponse("Hello, world. You're at the Generator index.")

def index(request):
    f=open('/tmp/gen/view.log','w')
    f.write('alive\n')
    #
    # Build a list of tuples for the active Gold Standards to be expanded
    # by the template
    #
    ActiveStandardList=[]
    for Active in ActiveGoldStandard.objects.all():
        GS_Dict={'House': Active.goldstandard.get_gen_court_house_display(),
                 'Date' : Active.goldstandard.session_date.strftime('%A, %B %-d, %Y'),
		 'sheet_url' : Active.goldstandard.google_sheet_url,
                 'Gold_PDF'  : Active.Gold_PDF_Server_Name,
                 'White_PDF' : Active.White_PDF_Server_Name,
                 'ZIP_File'  : Active.ZIP_File_Server_Name,
 		 'regen_url' : 'do_generate_active'}
        ActiveStandardList.append(GS_Dict)

    f.write( Active.goldstandard.google_sheet_url)
    t=get_template('generator_index.html.dt')
    html=t.render({'ActiveStandardList':ActiveStandardList})
    f.close()
    return HttpResponse(html)

def do_generate_active(request):
    call_command('generate_active')

    return index(request)
