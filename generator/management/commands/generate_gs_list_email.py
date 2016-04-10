import sys
import os
import errno
import zipfile

from django.core.management.base import BaseCommand, CommandError
import django_settings

from django.template.loader import get_template
from django.template import Template, Context

sys.path.append(django_settings.get('generator_gs_tools_path'))

from generator.models import GoldStandard, ActiveGoldStandard
from gs_tools import gs_collab_sheet
from gs_tools.reportlab_goldstandard import generate
import gs_tools.pdf_to_png



def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

class Command(BaseCommand):
    help = "Generates files that are suitible for use as an email body to" +\
           " the gold standard collaborators list to kick off work on the GS."

    def handle(self, *args, **options):

        #
        # Get the list of active Goldstandards and generate each one
        #
        #Directory=django_settings.get('generator_output_directory',\
        #  default='/tmp')
        #mkdir_p(Directory)
        #os.chdir(Directory)



        for Active in ActiveGoldStandard.objects.all():

            GS_Dict={'House': Active.goldstandard.get_gen_court_house_display(),
                     'Date' : Active.goldstandard.session_date.strftime('%A, %B %-d, %Y'),
                     'sheet_url' : Active.goldstandard.google_sheet_url,
                     'calendar_url' : Active.goldstandard.gen_court_calendar_url}

            t=get_template('generator_gslist_email.txt.dt')
            email_body=t.render(Context({'gs':GS_Dict}))

            print email_body
