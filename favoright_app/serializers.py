 
 
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "category","title", "description", "comments", "primaryAddress", "secondaryAddress", "is_helped", "is_paid", "creator"]
         
 
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    creator = serializers.PrimaryKeyRelatedField(read_only=True)

# ------------------------------------------------------------------------------------

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "post" , "creator", "subcomments"]
       

    subcomments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    creator = serializers.PrimaryKeyRelatedField( read_only=True)



# ---------------------------------------------------------------------------------

class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = ["id", "content", "comment", "creator"]
    
    creator = serializers.PrimaryKeyRelatedField( read_only=True)
    
    
#------------------------------------------------------------------------------------
class SolvedFavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolvedFavor
        fields = ["id", "favorOwner", "title", "description","primaryAddress","secondaryAddress", "favorSolver" ]
    

    favorOwner = serializers.PrimaryKeyRelatedField( read_only = True )
    favorSolver = serializers.PrimaryKeyRelatedField( read_only = True )
# -----------------------------------------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "posts", "comments", "subcomments", "solvedFavorOwner", "solvedFavorSolver" ]

    password = serializers.CharField(write_only = True)
    posts = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    subcomments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    solvedFavorOwner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    solvedFavorSolver = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self,validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)