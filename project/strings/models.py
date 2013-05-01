from django.db import models

COPY_SECTIONS = (
    ('nav', 'Nav Section'),
    ('home', 'Home Page'),
)


class String(models.Model):
    string_id = models.CharField(max_length=50, unique=True)
    section = models.CharField(max_length=50,
            choices=COPY_SECTIONS)
    description = models.CharField(max_length=150, blank=True)
    content = models.CharField(max_length=250, blank=True)
    pub_date = models.DateTimeField(verbose_name='date published',
            auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.string_id

    class Meta:
        ordering = ('pub_date',)
