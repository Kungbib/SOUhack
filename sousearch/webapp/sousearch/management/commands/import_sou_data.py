# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from sousearch.models import *
from django.conf import settings
import os, fnmatch


class Command(BaseCommand):
    help = 'Importerar SOU-textfiler'

    def handle(self, *args, **options):

        self.stdout.write("Letar SOU-textfiler i %s" % settings.SOUTXTPATH)

        count = 0


        try:
            for txtfile in os.listdir(settings.SOUTXTPATH):
                if txtfile.endswith(".txt"):

                    title, number = txtfile.split(" - SOU ")
                    number = number.replace(".txt","")

                    try:
                        #update
                        b = Betankande.objects.get(number=number)
                        b.title = title
                        b.txtfile = txtfile
                    except Betankande.DoesNotExist:
                        # create it
                        b = Betankande(title=title, number=number, txtfile=txtfile)

                    b.save()
                    count += 1

        except ValueError:
            self.stdout.write(u'Fel vid import av %s. Hoppade över.' % txtfile)


        self.stdout.write('Importerade %s filer' % count)
