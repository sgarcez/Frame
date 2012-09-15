from django.db import models

DEVICE_TYPES = (
    ('m', 'Mobile'),
    ('t', 'Tablet'),
    ('d', 'Desktop'),
)

class Device(models.Model):
    name = models.CharField(max_length=200, unique=True)
    section = models.CharField(max_length=50,
            choices=DEVICE_TYPES)
    description = models.TextField(max_length=500, blank=False)
    screen_width = models.IntegerField(blank=False)
    screen_height = models.IntegerField(blank=False)
    screen_x = models.IntegerField(blank=False)
    screen_y = models.IntegerField(blank=False)
    overlay_image = models.ImageField(upload_to='overlays', help_text="Only jpg-Images allowed.", blank=False, null=False)
    pub_date = models.DateTimeField(verbose_name='date published',
            auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('pub_date',)
