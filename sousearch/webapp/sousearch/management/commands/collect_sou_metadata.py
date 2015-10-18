# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from sousearch.models import *
from django.conf import settings
import os, fnmatch
import requests


class Command(BaseCommand):
    help = u"Importerar metadata för SOU:er i databasen från kb:s webbplats."

    def handle(self, *args, **options):

        souer = Betankande.objects.all()

        self.stdout.write(u"Hittade %s SOU:er. Slår upp metadata från http://regina.kb.se/sou/" % len(souer))

        # Load data
        url = "http://regina.kb.se/sou/"

        r = requests.get(url)
        soudata = dict()


        #Make dict of sou numbers and bib ids
        for line in r.text.split("\n"):
            if "urn:nbn:se:kb:sou" in line and "</a>" in line:
                no, urn = line.split("</a>")
                no = no.split("</a>")[0].replace(">","").replace("\"","").strip()
                urn = urn.split("urn=")[1].split("\"")[0].strip()
                soudata[no] = urn

        self.stdout.write(u"Hittade %s urn:er" % len(soudata))

        # Uppdatera databasen

        count = 0
        for sou in souer:
            if sou.number in soudata:
                sou.libris_bib_id = soudata[sou.number].split("sou-")[1]
                sou.save()
                count += 1

        self.stdout.write(u"Uppdaterade %s sou:er med libris-id" % count)
