from django.test import TestCase
from core.models import Program, Excercises, Rounds
from django.contrib.auth.models import User


class ModelProgramTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="Mike",
                                   password="MikeMegaMan",
                                   email="mike@example.com")
        Program.objects.create(name="Less reps", author=user,
                               continuity=6, source="internet")

    def test_name_lable(self):
        program = Program.objects.get(id=1)
        field_label = program._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
        self.assertEqual(type(program.name), str)
        self.assertEqual(program.name, 'Less reps')

    def test_author_label(self):
        program = Program.objects.get(id=1)
        field_label = program._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')
        self.assertEqual(program.author.id, 1)

    def test_continuity_lable(self):
        program = Program.objects.get(id=1)
        field_label = program._meta.get_field('continuity').verbose_name
        self.assertEqual(field_label, 'continuity')
        self.assertEqual(type(program.continuity), int)
        self.assertEqual(program.continuity, 6)

    def test_source_label(self):
        program = Program.objects.get(id=1)
        field_label = program._meta.get_field('source').verbose_name
        self.assertEqual(field_label, 'source')
        self.assertEqual(type(program.source), str)
        self.assertEqual(program.source, "internet")


class ModelExcercisesTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="Mike",
                                   password="MikeMegaMan",
                                   email="mike@example.com")
        program = Program.objects.create(name="Less reps", author=user,
                                         continuity=6, source="internet")
        Excercises.objects.create(
            program=program, name="Sit Ups",
            weight=90, rounds_count=1, max_rep=20)
        Excercises.objects.create(
            program=program, name="bench press",
            weight=65, rounds_count=3, max_rep=12)

    def test_program_label(self):
        excercise1 = Excercises.objects.get(id=1)
        excercise2 = Excercises.objects.get(id=2)
        self.assertEqual(excercise1.program.name, 'Less reps')
        self.assertEqual(excercise2.program.name, 'Less reps')
        self.assertEqual(excercise1.program.author.username, "Mike")
        self.assertEqual(excercise2.program.author.username, "Mike")

    def test_name_label(self):
        excercise1 = Excercises.objects.get(id=1)
        excercise2 = Excercises.objects.get(id=2)
        field_label1 = excercise1._meta.get_field('name').verbose_name
        field_label2 = excercise2._meta.get_field('name').verbose_name
        self.assertEqual(field_label1, 'name')
        self.assertEqual(field_label2, 'name')
        self.assertEqual(type(excercise1.name), str)
        self.assertEqual(type(excercise2.name), str)
        self.assertEqual(excercise1.name, 'Sit Ups')
        self.assertEqual(excercise2.name, 'bench press')

    def test_weight_label(self):
        excercise1 = Excercises.objects.get(id=1)
        excercise2 = Excercises.objects.get(id=2)
        field_label1 = excercise1._meta.get_field('weight').verbose_name
        field_label2 = excercise2._meta.get_field('weight').verbose_name
        self.assertEqual(field_label1, 'weight')
        self.assertEqual(field_label2, 'weight')
        self.assertEqual(type(excercise1.weight), int)
        self.assertEqual(type(excercise2.weight), int)
        self.assertEqual(excercise1.weight, 90)
        self.assertEqual(excercise2.weight, 65)

    def test_rounds_count_label(self):
        excercise1 = Excercises.objects.get(id=1)
        excercise2 = Excercises.objects.get(id=2)
        field_label1 = excercise1._meta.get_field('rounds_count').verbose_name
        field_label2 = excercise2._meta.get_field('rounds_count').verbose_name
        self.assertEqual(field_label1, 'rounds count')
        self.assertEqual(field_label2, 'rounds count')
        self.assertEqual(type(excercise1.rounds_count), int)
        self.assertEqual(type(excercise2.rounds_count), int)
        self.assertEqual(excercise1.rounds_count, 1)
        self.assertEqual(excercise2.rounds_count, 3)

    def test_max_rep_label(self):
        excercise1 = Excercises.objects.get(id=1)
        excercise2 = Excercises.objects.get(id=2)
        field_label1 = excercise1._meta.get_field('max_rep').verbose_name
        field_label2 = excercise2._meta.get_field('max_rep').verbose_name
        self.assertEqual(field_label1, 'max rep')
        self.assertEqual(field_label2, 'max rep')
        self.assertEqual(type(excercise1.max_rep), int)
        self.assertEqual(type(excercise2.max_rep), int)
        self.assertEqual(excercise1.max_rep, 20)
        self.assertEqual(excercise2.max_rep, 12)


class ModelRoundsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="Mike",
                                   password="MikeMegaMan",
                                   email="mike@example.com")
        program = Program.objects.create(name="Less reps", author=user,
                                         continuity=6, source="internet")
        excercise1 = Excercises.objects.create(
            program=program, name="Sit Ups", weight=90,
            rounds_count=1, max_rep=20)
        excercise2 = Excercises.objects.create(
            program=program, name="bench press", weight=65,
            rounds_count=3, max_rep=12)

        Rounds.objects.create(excercise=excercise1, current_rep=20)
        Rounds.objects.create(excercise=excercise2, current_rep=12)
        Rounds.objects.create(excercise=excercise2, current_rep=10)
        Rounds.objects.create(excercise=excercise2, current_rep=8)

    def test_current_rep_label(self):
        round1 = Rounds.objects.get(id=1)
        round2 = Rounds.objects.get(id=2)
        round3 = Rounds.objects.get(id=3)
        round4 = Rounds.objects.get(id=4)
        field_label1 = round1._meta.get_field('current_rep').verbose_name
        field_label2 = round2._meta.get_field('current_rep').verbose_name
        field_label3 = round3._meta.get_field('current_rep').verbose_name
        field_label4 = round4._meta.get_field('current_rep').verbose_name
        self.assertEqual(field_label1, 'current rep')
        self.assertEqual(field_label2, 'current rep')
        self.assertEqual(field_label3, 'current rep')
        self.assertEqual(field_label4, 'current rep')
        self.assertEqual(type(round1.current_rep), int)
        self.assertEqual(type(round2.current_rep), int)
        self.assertEqual(type(round3.current_rep), int)
        self.assertEqual(type(round4.current_rep), int)
        self.assertEqual(round1.current_rep, 20)
        self.assertEqual(round2.current_rep, 12)
        self.assertEqual(round3.current_rep, 10)
        self.assertEqual(round4.current_rep, 8)

    def test_excercise_label(self):
        round1 = Rounds.objects.get(id=1)
        round2 = Rounds.objects.get(id=2)
        round3 = Rounds.objects.get(id=3)
        round4 = Rounds.objects.get(id=4)
        self.assertEqual(round1.excercise.name, "Sit Ups")
        self.assertEqual(round2.excercise.name, "bench press")
        self.assertEqual(round3.excercise.name, "bench press")
        self.assertEqual(round4.excercise.name, "bench press")
        self.assertEqual(round1.excercise.program.author.username, "Mike")
        self.assertNotEqual(round1.excercise.program.author.username, "John")
