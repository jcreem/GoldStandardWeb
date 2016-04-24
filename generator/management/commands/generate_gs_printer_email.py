import sys
import os
import errno
import zipfile

from django.core.management.base import BaseCommand, CommandError

from constance import config

sys.path.append(config.generator_gs_tools_path)

from django.template.loader import get_template
from django.template import Template, Context


from generator.models import GoldStandard, ActiveGoldStandard
#from gs_tools import gs_collab_sheet
#from gs_tools.reportlab_goldstandard import generate
#import gs_tools.pdf_to_png



def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

class Command(BaseCommand):
    help = "Generates email body for email message requesting that the " +\
           "the printer print goldstandards."

    def handle(self, *args, **options):

        #
        # Get the list of active Goldstandards and generate each one
        #
        #Directory=django_settings.get('generator_output_directory',\
        #  default='/tmp')
        #mkdir_p(Directory)
        #os.chdir(Directory)



        for Active in ActiveGoldStandard.objects.all():
            GS_House = Active.goldstandard.get_gen_court_house_display()
            if GS_House == "House":
              Copies=config.generator_House_GS_Print_Copies
            elif GS_House == "Senate":
              Copies=config.generator_Senate_GS_Print_Copies

            GS_Dict={'Copies':Copies,
                     'Date_String':Active.goldstandard.session_date.strftime('%A, %B %-d'),
                     'Pick_Up_Time':config.generator_Printer_Pickup_Time,
                     'Requestor_Name':config.generator_Requestor_Name}


            t=get_template('generator_print_order_email.txt.dt')
            email_body=t.render({'gs':GS_Dict})

            print email_body
