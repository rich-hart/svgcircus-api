from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# FIXME: break up according to frontend conventions
class Actor(models.Model):
    CIRCLE = 'CI'
    SQUARE = 'SQ'
    POLYGON = 'PO'
    SHAPE_CHOICES = (
        (CIRCLE, 'Circle'),
        (SQUARE, 'Square'),
        (POLYGON, 'Polygon'),
    )

    name = models.CharField(max_length=255)
    shape = models.CharField( # this is 'type' in svgcircus front end
        max_length=2,
        choices=SHAPE_CHOICES,
        default=CIRCLE,
    )
    diameter = models.IntegerField(
        default = 10, 
        validators = [
            MinValueValidator(1), 
            MaxValueValidator(100),
        ]
    )
    x_position = models.IntegerField(
        default = 50, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(100),
        ]
    ) 
    y_position = models.IntegerField(
        default = 75, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(100),
        ]
    )
    opacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1.00,
        validators = [
            MinValueValidator(0.00), 
            MaxValueValidator(1.00),
        ]
    )
    fill_r = models.IntegerField(
        default = 166, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    ) 
    fill_b = models.IntegerField(
        default = 3, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    )
    fill_g = models.IntegerField(
        default = 17, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    )
    fill_a = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1.00,
        validators = [
            MinValueValidator(0.00), 
            MaxValueValidator(1.00),
        ]
    )
    stroke_r = models.IntegerField(
        default = 166, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    )
    stroke_b = models.IntegerField(
        default = 3, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    )
    stroke_g = models.IntegerField(
        default = 17, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    )

    stroke_a = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1.00,
        validators = [
            MinValueValidator(0.00), 
            MaxValueValidator(1.00),
        ]
    )

    stroke_width = models.IntegerField(
        default = 1, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(50),
        ]
    )

    stroke_dash_size = models.IntegerField(
        default = 0, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(100),
        ]
    )

    stroke_dash_gaps = models.IntegerField(
        default = 0, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(100),
        ]
    )

 
class Color(models.Model):
    red = models.IntegerField(
        default = 166, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    )
    blue = models.IntegerField(
        default = 3, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    ) 
    green = models.IntegerField(
        default = 17, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(255),
        ]
    )
    alpha = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1.00,
        validators = [
            MinValueValidator(0.00), 
            MaxValueValidator(1.00),
        ]
    )

class Position(models.Model):
    x =  models.IntegerField(
        default = 50, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(100),
        ]
    )
    y = models.IntegerField(
        default = 75, 
        validators = [
            MinValueValidator(0), 
            MaxValueValidator(100),
        ]
    )

