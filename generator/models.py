from django.db import models
import django_settings

class Text(django_settings.db.Model):
    value=models.TextField()
    class Meta:
        abstract= True


class GoldStandard(models.Model):
    HOUSE='Hou'
    SENATE='Sen'
    GEN_COURT_HOUSE_CHOICES = ((HOUSE,'House'),
                               (SENATE,'Senate'))

    session_date = models.DateField('session date')
    google_sheet_url = models.URLField('google sheet url')
    gen_court_house = models.CharField(max_length=3,
                                       choices=GEN_COURT_HOUSE_CHOICES,
                                       default=HOUSE)

    def __unicode__(self):

        return u'%s - %s' % (self.get_gen_court_house_display(), self.session_date.strftime('%B %d, %Y'))

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
    Gold_PDF_Server_Name = models.CharField(
      max_length=180,
      default='')

    White_PDF_Server_Name = models.CharField(
      max_length=180,
      default='')
    ZIP_File_Server_Name  = models.CharField(
      max_length=180,
      default='')

    def __unicode__(self):
        return self.goldstandard.__unicode__()

django_settings.register(Text)
