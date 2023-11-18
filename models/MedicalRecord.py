""" MedicalRecord Model """
from masoniteorm.models import Model
from masoniteorm.relationships import has_many
from .Medication import Medication


class MedicalRecord(Model):
    @has_many("id", "medicalrecord_id")
    def medications(self):
        return Medication
