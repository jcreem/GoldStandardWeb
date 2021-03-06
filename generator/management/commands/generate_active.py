import sys
import datetime
import os
import errno
import zipfile

from django.core.management.base import BaseCommand, CommandError
from constance import config

#
# We add to to python path here the path of the folder that contains
# the gs_tools gold standard generation package. Another option would have been
# have to include this info in the WGSI configuration files. The line that
# adds config.generator_gs_tools_path makes sense and is a reasonable choice
# for path management. The part where we add /gs_tools below seems a bit
# broken to me. What happens withtout it is that we find the items we
# explicitly import below (gs_collab_sheet, etc) but they fail to find
# 'colocated' items within the python package like the generator specific
# bill.py file. Presumably this is a lack of understanding on my part about
# WGSI interaction with things like the python package system.
#
sys.path.append(config.generator_gs_tools_path + '/gs_tools')
sys.path.append(config.generator_gs_tools_path)

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
    help = 'Generates all active goldstandards'

    def handle(self, *args, **options):

        #
        # Get the list of active Goldstandards and generate each one
        #
        Directory=config.generator_output_directory
        mkdir_p(Directory)
        os.chdir(Directory)
        Contributors_Filename = 'contributors.txt'


        JSON_Key_File=config.generator_JSON_key_file

        for Active in ActiveGoldStandard.objects.all():

            GS_Title_Date=Active.goldstandard.session_date.strftime('%A, %B %-d, %Y')
            GS_House=Active.goldstandard.get_gen_court_house_display()

            gs_collab_sheet.Create_Goldstandard_From_Sheet(
                Sheet_URL=Active.goldstandard.google_sheet_url,
                GS_Title= GS_House +
                ' SESSION - ' + GS_Title_Date,
                Filename=Active.goldstandard.get_pdf_name(Gold_Background = False),
                JSON_Key_File=JSON_Key_File,
                Background_Color=generate.White,
                Right_Side_Font_Size=Active.Right_Side_Recommend_Font_Size,
                )



            GS_Info = gs_collab_sheet.Create_Goldstandard_From_Sheet(
                Sheet_URL=Active.goldstandard.google_sheet_url,
                GS_Title= GS_House +
                ' SESSION - ' + GS_Title_Date,
                Filename=Active.goldstandard.get_pdf_name(Gold_Background = True),
                JSON_Key_File=JSON_Key_File,
                Background_Color=generate.Gold,
                Right_Side_Font_Size=Active.Right_Side_Recommend_Font_Size,
                )

            #
            # For the 'yellow' version of the goldstandard, we also generate
            # individual PNG images of the pages for use on things like
            # Facebook posts and mailing list emails
            #
            Image_List = gs_tools.pdf_to_png.Convert(
              Active.goldstandard.get_pdf_name(Gold_Background = True))


            #
            # Put the list of contributors in a file
            #
            with open (Contributors_Filename, "w") as f:
                for Sheet_Contributor in GS_Info['Contributors']:
                    print >> f, Sheet_Contributor + ", "
            #
            # Put the images into a zip file and then delete the individual
            # images
            #
            Zip_Name, Discard = os.path.splitext(
              Active.goldstandard.get_pdf_name(Gold_Background = True))
            Zip_Name=Zip_Name + ".zip"
            with zipfile.ZipFile(Zip_Name, 'w') as myzip:
                myzip.write(Contributors_Filename)
                for Image in Image_List:
                    myzip.write(Image)

            os.remove(Contributors_Filename)
            for Image_File in Image_List:
                os.remove(Image_File)



            #
            # Put the path info (web server relative) into the database
            #
            Server_Relative_Prefix=Directory=config.generator_http_server_relative_directory

            Active.Gold_PDF_Server_Name = Server_Relative_Prefix + '/' + \
                Active.goldstandard.get_pdf_name(Gold_Background = True)

            Active.White_PDF_Server_Name = Server_Relative_Prefix + '/' + \
                Active.goldstandard.get_pdf_name(Gold_Background = False)

            Active.ZIP_File_Server_Name = Server_Relative_Prefix + '/' + \
                Zip_Name

            Active.goldstandard.contributors=",".join(str(i) \
              for i in GS_Info['Contributors'])
            Active.goldstandard.save()
            Active.save()
