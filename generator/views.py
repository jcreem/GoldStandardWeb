"""
This module handles generation of non-admin views for the Gold Standard
generator application.

"""

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
    """
    This function handles the default 'index' page generation for the
    Gold Standard generator application
    """

    Num_Copies_Dict={'House' :config.generator_House_GS_Print_Copies, \
                     'Senate':config.generator_Senate_GS_Print_Copies, \
                     'JOINT' :config.generator_House_GS_Print_Copies + config.generator_Senate_GS_Print_Copies}

    #
    # Build a list of tuples for the active Gold Standards to be expanded
    # by the template
    #
    ActiveStandardList=[]
    for Active in ActiveGoldStandard.objects.all():
        #
        # The_House gets set to which house of the general court this
        # particular Gold Standard is for
        #
        The_House=Active.goldstandard.get_gen_court_house_display()

        The_Date=Active.goldstandard.session_date
        Simple_Date=The_Date.strftime('%m/%d')
        Day_Name=Active.goldstandard.session_date.strftime("%A")


        #
        # Generate the data that will be used for the mailto: link for
        # requesting collaborators for the Gold Standard
        #
        GS_Dict={'House': The_House,
                 'Date' : Active.goldstandard.session_date.strftime('%A, %B %-d, %Y'),
                 'sheet_url' : Active.goldstandard.google_sheet_url,
                 'calendar_url' : Active.goldstandard.gen_court_calendar_url}

        t=get_template('generator_gslist_email.txt.dt')
        Collaborators_Email_Body=t.render({'gs':GS_Dict})
        Collaborators_Email_Subject=The_House + " Gold Standard for " +\
          Active.goldstandard.session_date.strftime('%B %-d, %Y')


        GS_Dict={'Copies'       : Num_Copies_Dict[The_House],
                'Date_String'   : Active.goldstandard.session_date.strftime(
                   '%A, %B %-d'),
                'Pick_Up_Time'  : config.generator_Printer_Pickup_Time,
                'Requestor_Name': config.generator_Requestor_Name}

        t=get_template('generator_print_order_email.txt.dt')
        Printer_Email_Body=t.render({'gs':GS_Dict})
        Printer_Email_Subject=str(Num_Copies_Dict[The_House]) + \
          " copies for pick-up " + Day_Name + " morning"

        #
        # Generate the data that will be used for the mailto: link for
        # requesting production (printing) of the Gold Standard
        #
        GS_Dict={'Copies'       : Num_Copies_Dict[The_House],
                'Date_String'   : Active.goldstandard.session_date.strftime(
                   '%A, %B %-d'),
                'Pick_Up_Time'  : config.generator_Printer_Pickup_Time,
                'Requestor_Name': config.generator_Requestor_Name}

        t=get_template('generator_print_order_email.txt.dt')
        Printer_Email_Body=t.render({'gs':GS_Dict})

        Printer_Email_Subject=str(Num_Copies_Dict[The_House]) + \
          " copies for pick-up " + Day_Name + " morning"


        #
        # Create a dictionary that will be used to support 'this' gold
        # standard when we generate the final temlate that will represent this
        # page.
        #
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
                 'printer_email_body' : quote(Printer_Email_Body),
                 'collab_email_to'  : config.generator_gs_collab_email_to,
                 'collab_email_subject' : quote(Collaborators_Email_Subject),
                 'collab_email_body'    : quote(Collaborators_Email_Body)}
        ActiveStandardList.append(GS_Dict)


    t=get_template('generator_index.html.dt')
    html=t.render({'ActiveStandardList':ActiveStandardList})
    return HttpResponse(html)

def do_generate_active(request):
    call_command('generate_active')

    return index(request)
