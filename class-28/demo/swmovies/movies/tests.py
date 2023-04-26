from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Movie


class MovieTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.movie = Movie.objects.create(
            name="star wars", description="description test", owner=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.movie), "star wars")

    def test_movie_content(self):
        self.assertEqual(f"{self.movie.name}", "star wars")
        self.assertEqual(f"{self.movie.owner}", "tester")
        self.assertEqual(f"{self.movie.description}", "description test")

    def test_movie_list_view(self):
        response = self.client.get(reverse("list_view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "star wars")
        self.assertTemplateUsed(response, "movie-list.html")

    def test_movie_detail_view(self):
        response = self.client.get(reverse("detail_view", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Owner: tester")
        self.assertTemplateUsed(response, "movie-detail.html")

    def test_movie_create_view(self):
        response = self.client.post(
            reverse("create_view"),
            {
                "name": "Raker",
                "description": "test",
                "owner": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("detail_view", args="2"))
        self.assertContains(response, "Details about Raker")

    def test_movie_update_view_redirect(self):
        response = self.client.post(
            reverse("update_view", args="1"),
            {"name": "Updated name", "description": "new description", "owner":self.user.id}
        )
        self.assertRedirects(response, reverse("detail_view", args="1"))

    def test_movie_delete_view(self):
        response = self.client.get(reverse("delete_view", args="1"))
        self.assertEqual(response.status_code, 200)
