from rest_framework import serializers
from .models import Profile, Project, CertifyingInstitution, Certificate


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


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "certifying_institution",
            "timestamp",
            "profiles",
        ]


class NestedCertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name", "timestamp"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificatesSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        new_certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        new_certificate = {}
        for certificate in certificates_data:
            new_certificate = {
                "name": certificate["name"],
                "certifying_institution": new_certifying_institution,
            }
            CertificateSerializer().create(new_certificate)
        return new_certifying_institution
