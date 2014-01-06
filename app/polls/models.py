from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date_published')

    def __unicode__(self):
        return u"%s: %s: %s" % (self.pk, self.question, self.pub_date)
