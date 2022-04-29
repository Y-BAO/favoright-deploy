 
 
 
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import permissions
from .yelp_api import get_yelp_data
from .google_api import get_google_map_view
# from .yelp_api import response
# Create your views here.

# view handler for posts
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     if self.request.user:
    #         if self.request.method == "POST":
    #             return Post.objects.filter(creator=self.request.user.id)
    #         elif self.request.method == "DELETE":
    #             return Post.objects.filter(creator=self.request.user.id)
    #         elif self.request.method == "GET":
    #             return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)

# --------------------------------------------------------------------------
# view handler for comments
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_queryset(self):
    #     if self.request.user:
    #         if self.request.method == "POST":
    #             return Comment.objects.filter(creator=self.request.user.id)
    #         elif self.request.method == "DELETE":
    #             return Comment.objects.filter(creator=self.request.user.id)
    #         elif self.request.method == "GET":
    #             return Comment.objects.all()
        
                

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)




# ---------------------------------------------------------------------------
# view handler for SubComments
class SubCommentViewSet(ModelViewSet):
    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer
    
    # def get_queryset(self):
    #     if self.request.user:
    #         if self.request.method == "POST":
    #             return SubComment.objects.filter(creator=self.request.user.id)
    #         elif self.request.method == "DELETE":
    #             return SubComment.objects.filter(creator=self.request.user.id)
    #         elif self.request.method == "GET":
    #             return SubComment.objects.all()
 
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)

 



#----------------------------------------------------------------------------
class SolvedFavorViewSet(ModelViewSet):
    queryset = SolvedFavor.objects.all()
    serializer_class = SolvedFavorSerializer

    def perform_create(self, serializer):
        # print(self.request.data,"!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(self.request.data['favorSolver'], '!!!!!!!!!!!!!!!!!!!!!!!!')
        # print(User.objects.get(id=self.request.data['favorOwner']).id)
        # print(User.objects.get(id=self.request.data['favorSolver']).id)
        favorOwner=User.objects.get(id=self.request.data['favorOwner'])
        favorSolver=User.objects.get(id=self.request.data['favorSolver'])
        serializer.save(favorOwner=favorOwner, favorSolver=favorSolver)
       
        return super().perform_create(serializer)


# ----------------------------------------------------------------------------
# view handler for users
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return(permissions.AllowAny(),)
        return (permissions.IsAdminUser(),)



















# API Handlers 
#===========================================================================

def handle_yelp_api(request):
    if request.method == "GET":
        params = request.GET
       
        # return HttpResponse('hello from yelp')
        try:
            # params = request.GET
            location = params['location']
            term = params['term']
            radius = params['radius']
            print("params!!!!!!!!!!!!!", params)
            data = get_yelp_data(location=location, term=term, radius=radius)
            print(data)
            return HttpResponse(data,status = 200) 
        except Exception as e:
            return HttpResponse("Something went wrong on your yelp api call: ", e, status=400)


def hendle_google_map_api(request):
    if request.method == "GET":
        try:
            params = request.GET
            print(params)
            address = params["address"]

            data = get_google_map_view(address=address)
            print(data)
            return HttpResponse(data, status=200)
        except Exception as e:
            return HttpResponse("seomthing went wrong on your google map api call!!", e , status=400)



 



