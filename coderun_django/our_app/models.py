from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Instruction(models.Model):
    # Choices for the direction dropdown
    DIRECTION_CHOICES = [
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West'),
        ('NE', 'North-East'),
        ('NW', 'North-West'),
        ('SE', 'South-East'),
        ('SW', 'South-West'),
    ]

    direction = models.CharField(max_length=2, choices=DIRECTION_CHOICES)

    distance = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Distance in nautical miles"
    )

    description = models.TextField()

    previous_instruction = models.OneToOneField(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_instruction'
    )

    risk_level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.get_direction_display()} - {self.distance} miles"