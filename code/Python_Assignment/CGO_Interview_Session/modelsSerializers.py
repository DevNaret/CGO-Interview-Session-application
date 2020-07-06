from rest_framework import serializers
from django.contrib.postgres.fields import ArrayField
from django.core.validators import int_list_validator
from CGO_Interview_Session.models import Frog


class FrogSerializer(serializers.ModelSerializer):
    X = serializers.IntegerField()
    A = ArrayField(serializers.IntegerField())
    class Meta:
        model = Frog
        fields = ['X', 'A']

    def validate_X(self, value):
        """
        Check X cannot less than 1 and over than 100,000
        """
        if value not in range(1, 100001):
            raise serializers.ValidationError(f"X: without [1-100000] ")
        return value

    def validate(self, data):
        """
        Check element of array A within [1-X]
        """
        if max(data['A']) > data['X']:
            _x = data['X']
            raise serializers.ValidationError(f"A: without [1-{_x}]")
        return data
