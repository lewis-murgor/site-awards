from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.lewis=Profile(Bio='Lewis Murgor',contact='kiplagatlewis29@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lewis,Profile))

    # Testing Save Method
    def test_save_profile(self):
        self.lewis.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    # Testing Delete Method
    def test_delete_profile(self):
        self.lewis.save_profile()
        self.lewis.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.django=Project(title='django',description='A django project',link='django.com')

    def tearDown(self):
        Project.objects.all().delete()

    # Testing  instance
    def test_check_instance_variables(self):
        self.assertEqual(self.django.title, 'django')
        self.assertEqual(self.django.description, 'A django project')
        self.assertEqual(self.django.link, 'django.com')

    # Testing Save Method
    def test_save_project(self):
        self.django.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    # Testing Delete Method
    def test_delete_project(self):
        self.django.save_project()
        self.django.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

    def test_search_by_title(self):
        project = Project.search_by_title('django')
        self.assertEqual(len(project),0)



