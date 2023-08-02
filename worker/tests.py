from django.test import TestCase
from .models import Worker, Resume

class WorkerTestCase(TestCase):
    def test_create_vacancy_should_success(self):
        my_data = {
            "name": "NameTest 1",
            "specialization": "SpecializationTest",
            "waiting_salary": "100",
            "is_searching": "True"
        }

        response = self.client.post('/workers/', my_data)
        self.assertEqual(response.status_code, 200)

        new_worker = Worker.objects.first()
        self.assertEqual(new_worker.name, my_data["NameTest 1"])
        self.assertEqual(new_worker.specialization, my_data["SpecializationTest"])
        self.assertEqual(new_worker.waiting_salary, int(my_data["100"]))
        self.assertEqual(new_worker.is_searching, bool(my_data["True"]))

        worker_name = my_data["NameTest 1"]
        response_worker = self.client.get("/")
        self.assertContains(response_worker, worker_name)

# class ResumeTestCase(TestCase):
#     def test_create_resume_should_success(self):
#         my_data = {
#             "worker": "nameTest 1",
#             "title": "titleTest1",
#             "created_at": "dateTest",
#             "profile_photo": "True"
#         }

