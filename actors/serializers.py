from rest_framework import serializers
from .models import Actor


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = (
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
