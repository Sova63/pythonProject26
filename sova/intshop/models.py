from django.db import models
class Category_product(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=100)

	def __str__(self):
		return self.category_name

class Product_movie(models.Model):
	movie_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	year = models.IntegerField()
	country = models.CharField(max_length=40)
	short_description = models.TextField()
	description = models.TextField()
	image = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	category = models.ForeignKey(Category_product, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Product_book(models.Model):
	book_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	year = models.IntegerField()
	genre = models.CharField(max_length=40)
	short_description = models.TextField()
	description = models.TextField()
	pages = models.IntegerField()
	image = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	category = models.ForeignKey(Category_product, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Product_music(models.Model):
	music_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	executor = models.CharField(max_length=100)
	year = models.IntegerField()
	genre = models.CharField(max_length=40)
	duration = models.IntegerField()
	country = models.CharField(max_length=40)
	short_description = models.TextField()
	description = models.TextField()
	image = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	category = models.ForeignKey(Category_product, on_delete=models.CASCADE)

	def __str__(self):
		return self.name