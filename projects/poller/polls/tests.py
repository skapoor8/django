

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False for questions whose
		pub_date is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was published recently returns False for questions whose
		pub date is older than 1 day
		"""
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() returns True for question whose
		pub date is within thelast day
		"""
		one_second_over_yesterday = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		one_second_before_now = timezone.now() - datetime.timedelta(seconds=1)
		now = timezone.now()
		oldest_recent = Question(pub_date=one_second_over_yesterday)
		most_recent_minus_1sec = Question(pub_date=one_second_before_now)
		most_recent = Question(pub_date=now)
		self.assertIs(oldest_recent.was_published_recently(), True)
		self.assertIs(most_recent_minus_1sec.was_published_recently(), True)
		self.assertIs(most_recent.was_published_recently(), True)
