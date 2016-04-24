"""
This module implements a django manage.py command that allows for the
generation of email content intended to go to the printer to support the
printing of the GoldStandard.

"""
import sys
import os
import errno

from django.core.management.base import BaseCommand, CommandError

from constance import config

sys.path.append(config.generator_gs_tools_path)

from django.template.loader import get_template
from django.template import Template, Context
from generator.models import GoldStandard, ActiveGoldStandard



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
           "the printer print goldstandard."

    def add_arguments(self, parser):
        parser.add_argument('--house', help="Set to House or Senate to " +
          "specify which house of the general court we are working with.")
        parser.add_argument('--date', help="Set to MM/DD of the date of the" +
          " Gold Standard.")

    def handle(self, *args, **options):
        email_body=''
        #
        # Get the list of active Goldstandards and generate each one
        #
        for Active in ActiveGoldStandard.objects.all():
            GS_House = Active.goldstandard.get_gen_court_house_display()
            GS_Simple_Date=Active.goldstandard.session_date.strftime('%m/%d')
            GS_Day_Name=Active.goldstandard.session_date.strftime("%A")
            if (not options['house'] or options['house'] == GS_House) and \
               (not options['date'] or options['date'] == GS_Simple_Date):

                if GS_House == "House":
                    Copies=config.generator_House_GS_Print_Copies
                elif GS_House == "Senate":
                    Copies=config.generator_Senate_GS_Print_Copies

                GS_Dict={'Copies':Copies,
                     'Date_String':Active.goldstandard.session_date.strftime('%A, %B %-d'),
                     'Pick_Up_Time':config.generator_Printer_Pickup_Time,
                     'Requestor_Name':config.generator_Requestor_Name}


                t=get_template('generator_print_order_email.txt.dt')
                email_body=email_body + '\n' + t.render({'gs':GS_Dict})

        return email_body
