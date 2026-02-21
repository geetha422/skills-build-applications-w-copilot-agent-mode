from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@stark.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@rogers.com', team=marvel)
        bruce = User.objects.create(name='Bruce Banner', email='bruce@banner.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@kent.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@prince.com', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        yoga = Workout.objects.create(name='Yoga', description='Flexibility', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=tony, type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Yoga', duration=40, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Pushups', duration=25, date=timezone.now().date())
        Activity.objects.create(user=diana, type='Running', duration=35, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=80)
        Leaderboard.objects.create(user=clark, score=95)
        Leaderboard.objects.create(user=diana, score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
