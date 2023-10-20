from rest_framework import serializers
from .models import Profile, Project, CertifyingInstitution


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "github", "linkedin", "bio"]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # essa linha, server para fazer a API receber no campo profile apenas o ID
    # do perfil correspondente
    profile = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        ]


class CertifyingInstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url"]
