from django.db import models
from domain.models import User
from intshop.models import Product_movie, Product_book, Product_music, Category_product


class Order(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	movie_id = models.ForeignKey(Product_movie, on_delete=models.CASCADE,null=True)
	book_id = models.ForeignKey(Product_book, on_delete=models.CASCADE,null=True)
	music_id = models.ForeignKey(Product_music, on_delete=models.CASCADE,null=True)
	category = models.ForeignKey(Category_product, on_delete=models.CASCADE,null=True)
	date = models.DateTimeField()

	def __str__(self):
		return self.name