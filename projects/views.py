from rest_framework import viewsets
from django.shortcuts import get_object_or_404, render
from .models import Profile, Project, CertifyingInstitution
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile_id = kwargs.get("pk")
            profile = get_object_or_404(Profile, pk=profile_id)
            projects = profile.projects.all()
            context = {
                "profile": profile,
                "projects": projects,
            }
            return render(
                request,
                "profile_detail.html",
                context=context,
            )
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
