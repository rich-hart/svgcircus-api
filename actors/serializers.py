from rest_framework import serializers
from .models import Actor, Color, Position


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'name',
            'shape',
            'diameter',
            'x_position',
            'y_position',
            'opacity',
            'fill_r',
            'fill_g',
            'fill_b',
            'fill_a', 
            'stroke_r',
            'stroke_g',
            'stroke_b',
            'stroke_a', 
            'stroke_width',
            'stroke_dash_size',
            'stroke_dash_gaps',
            )

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = (
            'red',
            'blue',
            'green',
            'alpha',
        )

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = (
            'x',
            'y'
        )
