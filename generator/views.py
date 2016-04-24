from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.core.management import call_command
from generator.models import GoldStandard, ActiveGoldStandard
from urllib import quote
from constance import config

#def index(request):
#    return HttpResponse("Hello, world. You're at the Generator index.")

def index(request):
    #
    # Build a list of tuples for the active Gold Standards to be expanded
    # by the template
    #
    ActiveStandardList=[]
    for Active in ActiveGoldStandard.objects.all():
        The_House=Active.goldstandard.get_gen_court_house_display()
        if The_House == "House":
            Copies=config.generator_House_GS_Print_Copies
        elif The_House == "Senate":
            Copies=config.generator_Senate_GS_Print_Copies

        The_Date=Active.goldstandard.session_date
        Simple_Date=The_Date.strftime('%m/%d')
        Day_Name=Active.goldstandard.session_date.strftime("%A")

        GS_Dict={'Copies':Copies,
                'Date_String':Active.goldstandard.session_date.strftime('%A, %B %-d'),
                'Pick_Up_Time':config.generator_Printer_Pickup_Time,
                'Requestor_Name':config.generator_Requestor_Name}

        t=get_template('generator_print_order_email.txt.dt')
        Printer_Email_Body=t.render({'gs':GS_Dict})

        Printer_Email_Subject=str(Copies) + " copies for pick-up " + Day_Name + " morning"

        GS_Dict={'House': The_House,
                 'Date' : The_Date.strftime('%A, %B %-d, %Y'),
		         'sheet_url' : Active.goldstandard.google_sheet_url,
                 'Gold_PDF'  : Active.Gold_PDF_Server_Name,
                 'White_PDF' : Active.White_PDF_Server_Name,
                 'ZIP_File'  : Active.ZIP_File_Server_Name,
 		         'regen_url' : 'do_generate_active',
                 'printer_email_to' : config.generator_gs_production_email_to,
                 'printer_email_cc' : config.generator_gs_production_email_cc,
                 'printer_email_subject' : quote(Printer_Email_Subject),
                 'printer_email_body' : quote(Printer_Email_Body),}
        ActiveStandardList.append(GS_Dict)


    t=get_template('generator_index.html.dt')
    html=t.render({'ActiveStandardList':ActiveStandardList})
    return HttpResponse(html)

def do_generate_active(request):
    call_command('generate_active')

    return index(request)
