# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Betankande(models.Model):
    isbn = models.CharField(u"ISBN-nummer", max_length=20, blank=True, help_text='Utan bindestreck, t.ex. 9138133938')
    number = models.CharField(u"SOU-nummer", max_length=20, help_text=u'T.ex. 1993:21')
    title = models.TextField(u"Titel", help_text=u'Ökat personval : betänkande')
    pdf_url = models.URLField(u"Länk till PDF-fil", blank=True)
    txtfile = models.CharField(u"Filnamn råtext", max_length=255)
    libris_bib_id = models.CharField(u"Bib-id i Libris", max_length=50, blank=True, help_text=u'T.ex. 7265056' )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def ocr_text(self):
        #open ocr textfile
        with open(settings.SOUTXTPATH + self.txtfile, 'rb') as f:
            return f.read()


    class Meta:
        verbose_name = u"Betänkande"
        verbose_name_plural = u"Betänkanden"
        ordering = ['number']
