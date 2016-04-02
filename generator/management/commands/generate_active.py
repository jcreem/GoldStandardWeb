from django.core.management.base import BaseCommand, CommandError
from generator.models import GoldStandard, ActiveGoldStandard
from gs_tools import gs_collab_sheet
import generate
import os

class Command(BaseCommand):
    def handle(self, *args, **options):

        #
        # Get the list of active Goldstandards and generate each one
        #
        os.chdir('/tmp')

        for Active in ActiveGoldStandard.objects.all():
            GS_Filename_Date=Active.goldstandard.session_date.strftime('%m-%d-%y')
            GS_Title_Date=Active.goldstandard.session_date.strftime('%A, %B %-d, %Y')
            GS_House=Active.goldstandard.get_gen_court_house_display()

            gs_collab_sheet.Create_Goldstandard_From_Sheet(
                Sheet_URL=Active.goldstandard.google_sheet_url,
                GS_Title= GS_House +
                ' SESSION - ' + GS_Title_Date,
                Filename='/tmp/goldstandard-'+ GS_Filename_Date + '-' +
                 GS_House[0] + '.pdf',
                JSON_Key_File='/home/jcreem/nhla/gs_tools/NHLAGS-e8b3911072d5.json',
                Background_Color=generate.White,
                )

            gs_collab_sheet.Create_Goldstandard_From_Sheet(
                Sheet_URL=Active.goldstandard.google_sheet_url,
                GS_Title= GS_House +
                ' SESSION - ' + GS_Title_Date,
                Filename='/tmp/goldstandard-'+ GS_Filename_Date + '-' +
                 GS_House[0] + '-y.pdf',
                JSON_Key_File='/home/jcreem/nhla/gs_tools/NHLAGS-e8b3911072d5.json',
                Background_Color=generate.Gold,
                )
