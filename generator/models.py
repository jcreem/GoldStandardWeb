from django.db import models

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

    class Meta:
        unique_together = ('session_date', 'gen_court_house',)

class ActiveGoldStandard(models.Model):
    goldstandard = models.OneToOneField(GoldStandard, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.goldstandard.__unicode__()
