from django.db import models
import datetime
from django.utils.timezone import utc, now
class GoldStandard(models.Model):
    HOUSE='Hou'
    SENATE='Sen'
    GEN_COURT_HOUSE_CHOICES = ((HOUSE,'House'),
                               (SENATE,'Senate'))

    session_date = models.DateField('session date')
    google_sheet_url = models.URLField('google sheet url')
    gen_court_calendar_url = models.URLField(
        'NH General Court Calendar URL',\
        default="http://www.gencourt.state.nh.us/")

    gen_court_house = models.CharField(max_length=3,
                                       choices=GEN_COURT_HOUSE_CHOICES,
                                       default=HOUSE)

    contributors = models.TextField(default='', blank=True)

    def __unicode__(self):

        return u'%s - %s' % (self.get_gen_court_house_display(), \
            self.session_date.strftime('%B %d, %Y'))

    def get_pdf_name(self, Gold_Background = True):
        GS_Filename_Date=self.session_date.strftime('%m-%d-%y')

        GS_House=str(self.get_gen_court_house_display())
        if Gold_Background:
            suffix='-y'
        else:
            suffix=''

        Filename='goldstandard-'
        Filename=Filename + GS_Filename_Date + '-' + \
          GS_House[0] + suffix + '.pdf'
        return Filename

    class Meta:
        unique_together = ('session_date', 'gen_court_house',)



class ActiveGoldStandard(models.Model):
    goldstandard = models.OneToOneField(GoldStandard, on_delete=models.CASCADE)

    Draft_Number = models.IntegerField(default=1)

    #
    # User does not fill in any of these. They get set when we actually
    # generate a goldstandard
    #
    Gold_PDF_Server_Name = models.CharField(
      max_length=180,
      default='', blank=True)
    White_PDF_Server_Name = models.CharField(
      max_length=180,
      default='', blank=True)
    ZIP_File_Server_Name  = models.CharField(
      max_length=180,
      default='', blank=True)

    def __unicode__(self):
        return self.goldstandard.__unicode__()
