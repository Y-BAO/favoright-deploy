   

 
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ------------------------------------------------------------------------------------------
class Post(models.Model):
    class CategoryOpetions(models.IntegerChoices):
        Delivery = 1
        Repair = 2
        Other = 3

    category = models.IntegerField(choices=CategoryOpetions.choices)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    primaryAddress = models.CharField(max_length=255)
    secondaryAddress = models.CharField(max_length=255, blank=True, null=True)
    is_helped = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts")
    #comments
    #subcomments
 


    def __str__(self):
        return f"Post:{self.title}/ id: {self.id}"
# ------------------------------------------------------------------------------------------

class Comment(models.Model):
    content = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") 
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
     
    def __str__(self):
        return f"Content:{self.content}"

# ------------------------------------------------------------------------------------------
class SubComment(models.Model):
    content = models.CharField(max_length=255)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="subcomments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subcomments")

    def __str__(self):
        return f"SubComment: {self.content}; Creator: {self.creator}"

# ------------------------------------------------------------------------------------------
 

class SolvedFavor(models.Model):
    favorOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solvedFavorOwner")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    primaryAddress = models.CharField(max_length=255, blank=True, null=True)
    secondaryAddress = models.CharField(max_length=255, blank=True, null=True)
    favorSolver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solvedFavorSolver")

    def __str__(self):
        return f"favor solved by: {self.favorOwner}, favorinfo:{self.favorOwner}, {self.title}"
    

 







 