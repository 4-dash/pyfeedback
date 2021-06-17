# coding=utf-8

from django.db import models
from feedback.models import Fragebogen, Ergebnis

class Fragebogen2016(Fragebogen):
    fach = models.CharField(max_length=5, choices=Fragebogen.FACH_CHOICES, blank=True)
    abschluss = models.CharField(max_length=5, choices=Fragebogen.ABSCHLUSS_CHOICES, blank=True)
    semester = models.CharField(max_length=4, choices=Fragebogen.SEMESTER_CHOICES16, blank=True)
    geschlecht = models.CharField(max_length=1, choices=Fragebogen.GESCHLECHT_CHOICES, blank=True)
    studienberechtigung = models.CharField(max_length=1, choices=Fragebogen.STUDIENBERECHTIGUNG_CHOICES, blank=True)
    pflichveranstaltung = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)
    male_veranstaltung_gehoert = models.CharField(max_length=1, choices=Fragebogen.VERANSTALTUNG_GEHOERT, blank=True)
    pruefung_angetreten = models.CharField(max_length=1, choices=Fragebogen.KLAUSUR_ANGETRETEN, blank=True)

    v_wie_oft_besucht = models.PositiveSmallIntegerField(blank=True, null=True)
    v_besuch_ueberschneidung = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)
    v_besuch_qualitaet = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)
    v_besuch_verhaeltnisse = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)
    v_besuch_privat = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)
    v_besuch_elearning = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)
    v_besuch_zufrueh = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)
    v_besuch_sonstiges = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)

    v_3_1 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_2 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_3 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_4 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_5 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_6 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_7 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_8 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_9 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_10 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_11 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_12 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_3_13 = models.PositiveSmallIntegerField(blank=True, null=True)

    v_4_1 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_2 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_3 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_4 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_5 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_6 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_7 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_8 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_4_9 = models.PositiveSmallIntegerField(blank=True, null=True)

    v_5_1 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_5_2 = models.PositiveSmallIntegerField(blank=True, null=True)

    v_6_1 = models.CharField(max_length=1, choices=Fragebogen.STUNDEN_NACHBEARBEITUNG, blank=True)

    v_6_2 = models.CharField(max_length=3, blank=True)
    v_6_3 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_6_4 = models.PositiveSmallIntegerField(blank=True, null=True)
    v_6_5 = models.PositiveSmallIntegerField(blank=True, null=True)

    v_6_8 = models.CharField(max_length=1, choices=Fragebogen.BOOLEAN_CHOICES, blank=True)

    class Meta:
        verbose_name = 'Fragebogen 2016'
        verbose_name_plural = 'Fragebögen 2016'
        ordering = ['semester', 'veranstaltung']
        app_label = 'feedback'


class Ergebnis2016(Ergebnis):
    parts_vl = [
             ['v_6_5', 'Vorlesung: Gesamtnote',
              ['6.5 Welche Gesamtnote würdest Du der Vorlesung (ohne Übungen) geben?']],
             ['v_didaktik', 'Vorlesung: Didaktik',
              ['3.3 Die Lernziele der Veranstaltung sind mir klar geworden.',
               '3.4 Der Stoff wurde anhand von Beispielen verdeutlicht.',
               '3.9 Ich habe durch diese Veranstaltung viel gelernt.',
               '3.10 Mein Vorwissen war ausreichend, um der Vorlesung folgen zu können.',
               '3.11 Ich kann abschätzen, was in der Prüfung von mir erwartet wird.',
               '4.1 Die Lehrkraft hat Kompliziertes verständlich dargelegt.',
               '4.3 Die Lehrkraft hat die Vorlesung rhetorisch gut gestaltet.',
               '4.4 Die Lehrkraft hat die Vorlesung didaktisch gut gestaltet.',
               '4.6 Der Lehrende regte gezielt zur eigenen Mitarbeit / zum Mitdenken in der Vorlesung an.',
               '4.7 Die Lehrkraft hat elektronische Plattformen sinnvoll und hilfreich eingesetzt.']],
             ['v_organisation', 'Vorlesung: Organisation',
              ['3.1 Die Vorlesung war inhaltlich gut strukturiert, ein roter Faden war erkennbar.',
               '3.2 Die Organisation der Vorlesung war gut.',
               '3.6 Die (Zwischen-)Fragen der Studierenden wurden angemessen beantwortet.',
               '4.2 Die Lehrkraft zeigte sich gut vorbereitet.',
               '4.5 Der Lehrende war auch außerhalb der Vorlesung ansprechbar.',
               '4.8 Die Sprachkenntnisse der Lehrkraft in der Vorlesungssprache waren gut.',
               '4.9 Die Lehrkraft hielt die Vorlesung größtenteils selbst.']],
             ['v_praxisbezug_motivation', 'Vorlesung: Praxisbezug und Motivation',
              ['3.5 Der Bezug zwischen Theorie und praktischem Arbeiten / praktischen Anwendungen wurde hergestellt.',
               '3.8 Die Vorlesung motivierte dazu, sich außerhalb der Veranstaltung selbstständig mit den behandelten Themen auseinanderzusetzen.']],
            ]

    parts_ue = [
                ['ue_didaktik', 'Übung: Didaktik',
                 ['4.1 Die Übung war inhaltlich gut strukturiert.',
                  '4.2 Die Lernziele der Übung sind mir klar geworden.',
                  '5.2 Der*Die Tutor*in hat gut und verständlich erklärt.',
                  '5.3 Der*Die Tutor*in hat die Gruppe motiviert.',
                  '5.4 Der*Die Tutor*in war fachlich kompetent.',
                  '5.5 Der*Die Tutor*in zeigte sich gut vorbereitet.',
                  '5.6 Der*Die Tutor*in hat die Übungstunde gut strukturiert.',
                  '5.7 Der*Die Tutor*in war engagiert.',
                  '5.8 Der*Die Tutor*in stellte wesentliche Punkte zur Bearbeitung der Aufgaben vor.',
                  '5.9 Der*Die Tutor*in regte mich gezielt zum Mitdenken und zu eigener Mitarbeit an.',
                  '5.10 Der*Die Tutor*in setzte verfügbare Medien (z. B. Tafel, Projektor, Beamer) sinnvoll ein.',
                  '5.11 Der*Die Tutor*in hat elektronische Plattformen sinnvoll und hilfreich eingesetzt.',
                  '5.15 Der*Die Tutor*in hat konstruktives bzw. gutes Feedback gegeben.']],
                ['ue_organisation', 'Übung: Organisation',
                 ['3.3 Die Aufgabenstellungen waren verständlich.',
                  '3.4 Die Übungsaufgaben hatten inhaltlich eine klare Struktur.',
                  '3.5 Die Übungsaufgaben waren motivierend.',
                  '3.6 Es wurden ausreichend Lösungsvorschläge bereitgestellt bzw. präsentiert.',
                  '3.7 Der Stoff der Vorlesung war gut auf die Übungen abgestimmt.',
                  '3.8 Mein Vorwissen war ausreichend, um die Übungsaufgaben bearbeiten zu können.',
                  '4.3 Die Organisation des Übungsbetriebs war gut.',
                  '4.4 Es wurde genug Übungsmaterial (Aufgaben, etc.) zur Verfügung gestellt.',
                  '4.5 Es stand genug Zeit für die Bearbeitung der Aufgaben zur Verfügung.',
                  '4.6 Die Abgaben waren gut vereinbar mit anderen Veranstaltungen laut Regelstudienplan.']],
                ['ue_arbeitsbedingungen', 'Übung: Arbeitsbedingungen',
                 ['4.7 Die Auswahlmöglichkeiten der Termine waren angemessen bzw. der Übungszeitpunkt war passend.',
                  '4.8 Die Gruppengröße war zufriedenstellend.',
                  '4.9 Der Raum für die Übungen war zum Arbeiten und Lernen geeignet.']],
                ['ue_umgang', 'Übung: Umgang',
                 ['5.12 Der*Die Tutor*in erschien pünktlich.',
                  '5.13 Der*Die Tutor*in behandelte alle Studierenden respektvoll.',
                  '5.14 Der*Die Tutor*in teilte die Zeit zwischen den Studierenden angemessen auf.',
                  '5.16 Der*Die Tutor*in hat nachvollziehbar bewertet bzw. benotet.']],
                ['ue_lernerfolg', 'Übung: Lernerfolg',
                 ['3.1 Durch die Aufgaben und den Übungsbetrieb habe ich viel gelernt.',
                  '3.2 Die Übungen haben mir geholfen, den Stoff der Vorlesung besser zu verstehen.']],
            ]

    parts = parts_vl + parts_ue
    hidden_parts = [
             ['v_feedbackpreis', 'Feedbackpreis: Beste Vorlesung',
              ['2.4 Die Vorlesung war inhaltlich gut strukturiert, ein roter Faden war erkennbar.',
               '2.5 Die Lernziele der Veranstaltung sind mir klar geworden.',
               '2.6 Die Lehrkraft hat Kompliziertes verständlich dargelegt.',
               '2.7 Der Stoff wurde anhand von Beispielen verdeutlicht.',
               '2.8 Die Lehrkraft zeigte Bezüge zur aktuellen Forschung auf.',
               '2.9 Der Bezug zwischen Theorie und praktischem Arbeiten / praktischen Anwendungen wurde hergestellt.',
               '2.10 Das Tempo der Vorlesung war angemessen.',
               '2.11 Die Lehrkraft zeigte sich gut vorbereitet.',
               '2.12 Die (Zwischen-)Fragen der Studierenden wurden angemessen beantwortet.',
               '2.13 Der Lehrende war auch außerhalb der Veranstaltung ansprechbar.',
               '2.14 Der Lehrende regte gezielt zur eigenen Mitarbeit / zum Mitdenken in der Veranstaltung an.',
               '3.8 Die Vorlesung motivierte dazu, sich außerhalb der Veranstaltungselbstständig mit den behandelten Themen auseinander zu setzen.',
               '3.7 Die Vorlesungsmaterialien (Folien, Skripte, Tafelanschrieb, Lehrbücher,e-Learning, etc.) haben das Lernen wirkungsvoll unterstützt.',
               '6.5 Welche Gesamtnote würdest Du der Vorlesung (ohne Übungen) geben?']],
             ['ue_feedbackpreis', 'Feedbackpreis: Beste Übung',
              ['3.1 Durch die Aufgaben und den Übungsbetrieb habe ich viel gelernt.',
               '3.2 Die Übungen haben mir geholfen, den Stoff der Vorlesung besser zu verstehen.',
               '3.3 Die Aufgabenstellungen waren verständlich.',
               '3.4 Die Übungsaufgaben hatten inhaltlich eine klare Struktur.',
               '3.5 Die Übungsaufgaben waren motivierend.',
               '3.7 Der Stoff der Vorlesung war gut auf die Übungen abgestimmt.',
               '4.1 Die Übung war inhaltlich gut strukturiert.',
               '4.2 Die Lernziele der Übung sind mir klar geworden.',
               '4.3 Die Organisation des Übungsbetriebs war gut.',
               '4.4 Es wurde genug Übungsmaterial (Aufgaben, etc.) zur Verfügung gestellt.',
               '4.5 Es stand genug Zeit für die Bearbeitung der Aufgaben zur Verfügung.',
               '6.3 Welche Gesamtnote gibst du der Übung?']],
            ]
    weight = {
              'v_feedbackpreis': [1] * 13 + [13],
              'ue_feedbackpreis': [1] * 10 + [10],
             }

    #TODO: decimal statt float benutzen
    v_didaktik = models.FloatField(blank=True, null=True)
    v_didaktik_count = models.PositiveIntegerField(default=0)
    v_didaktik_parts = ['v_3_3', 'v_3_4', 'v_3_9', 'v_3_10', 'v_4_1', 'v_4_3', 'v_4_4', 'v_4_6', 'v_4_7']
    v_organisation = models.FloatField(blank=True, null=True)
    v_organisation_count = models.PositiveIntegerField(default=0)
    v_organisation_parts = ['v_3_1', 'v_3_2', 'v_3_6', 'v_4_2', 'v_4_5', 'v_4_7', 'v_4_8', 'v_4_9']
    v_praxisbezug_motivation = models.FloatField(blank=True, null=True)
    v_praxisbezug_motivation_count = models.PositiveIntegerField(default=0)
    v_praxisbezug_motivation_parts = ['v_3_5', 'v_4_8']
    v_6_5 = models.FloatField(blank=True, null=True)
    v_6_5_count = models.PositiveIntegerField(default=0)

    v_feedbackpreis = models.FloatField(blank=True, null=True)
    v_feedbackpreis_count = models.PositiveIntegerField(default=0)
    v_feedbackpreis_parts = ['v_3_1', 'v_3_2', 'v_3_3', 'v_3_4', 'v_3_5', 'v_3_6', 'v_3_7', 'v_3_8', 'v_3_9', 'v_4_1', 'v_4_2', 'v_4_3', 'v_4_4',
    'v_4_5', 'v_4_6', 'v_4_9', 'v_6_2', 'v_6_5', 'v_gesamt']

    ue_didaktik = models.FloatField(blank=True, null=True)
    ue_didaktik_count = models.PositiveIntegerField(default=0)
    ue_didaktik_parts = ['ue_4_1', 'ue_4_2', 'ue_5_2', 'ue_5_3', 'ue_5_4', 'ue_5_5', 'ue_5_6', 'ue_5_7', 'ue_5_8', 'ue_5_9', 'ue_5_10', 'ue_5_11', 'ue_5_15']
    ue_organisation = models.FloatField(blank=True, null=True)
    ue_organisation_count = models.PositiveIntegerField(default=0)
    ue_organisation_parts = ['ue_3_3', 'ue_3_4', 'ue_3_5', 'ue_3_6', 'ue_3_7', 'ue_3_8', 'ue_4_3', 'ue_4_4', 'ue_4_5', 'ue_4_6']
    ue_arbeitsbedingungen = models.FloatField(blank=True, null=True)
    ue_arbeitsbedingungen_count = models.PositiveIntegerField(default=0)
    ue_arbeitsbedingungen_parts = ['ue_4_7', 'ue_4_8', 'ue_4_9']
    ue_umgang = models.FloatField(blank=True, null=True)
    ue_umgang_count = models.PositiveIntegerField(default=0)
    ue_umgang_parts = ['ue_5_12', 'ue_5_13', 'ue_5_14', 'ue_5_16']
    ue_lernerfolg = models.FloatField(blank=True, null=True)
    ue_lernerfolg_count = models.PositiveIntegerField(default=0)
    ue_lernerfolg_parts = ['ue_3_1', 'ue_3_2']

    ue_feedbackpreis = models.FloatField(blank=True, null=True)
    ue_feedbackpreis_count = models.PositiveIntegerField(default=0)
    ue_feedbackpreis_parts = ['ue_3_1', 'ue_3_2', 'ue_3_3', 'ue_3_4', 'ue_3_5', 'ue_3_7', 'ue_4_1', 'ue_4_2', 'ue_4_3', 'ue_4_4', 'ue_4_5', 'ue_6_3']


    gesamt = models.FloatField(blank=True, null=True)
    gesamt_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Ergebnis 2016'
        verbose_name_plural = 'Ergebnisse 2016'
        ordering = ['veranstaltung']
        app_label = 'feedback'
