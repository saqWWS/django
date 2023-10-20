from django.db import models


class Atalanta(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Atalanta BC"
        verbose_name_plural = "Atalanta BC"


class Cagliari(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Cagliari Calcio"
        verbose_name_plural = "Cagliari Calcio"


class Bologna(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Bologna FC 1909"
        verbose_name_plural = "Bologna FC 1909"


class Empoli(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "FC Empoli"
        verbose_name_plural = "FC Empoli"


class Fiorentina(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "ACF Fiorentina"
        verbose_name_plural = "ACF Fiorentina"


class Frosinone(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Frosinone Calcio"
        verbose_name_plural = "Frosinone Calcio"


class Genoa(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Genoa CFC"
        verbose_name_plural = "Genoa CFC"


class HellasVerona(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Hellas Verona"
        verbose_name_plural = "Hellas Verona"


class Inter(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Inter Milan"
        verbose_name_plural = "Inter Milan"


class Juventus(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    birth_of_date = models.DateTimeField()
    age = models.PositiveIntegerField(default=15)
    citizenship = models.CharField(max_length=50)
    POSITION = (
        ("G", "Goalkeeper"),
        ("D", "Defender"),
        ("M", "Midfielder"),
        ("F", "Forward"),
    )
    position = models.CharField(max_length=1, choices=POSITION)
    number = models.PositiveIntegerField()
    FOOT = (
        ("R", "Right"),
        ("L", "Left"),
        ("B", "Both")
    )
    foot = models.CharField(max_length=1, choices=FOOT)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Juventus FC"
        verbose_name_plural = "Juventus FC"
