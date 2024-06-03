from django.db import models


# Create your models here.
class TbDestructura(models.Model):
    id_estructura = models.IntegerField(primary_key=True)
    id_tipo_estructura = models.ForeignKey('TbNtipoEstructura', models.DO_NOTHING, db_column='id_tipo_estructura', blank=True, null=True)
    id_estructura_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='id_estructura_padre', blank=True, null=True)
    nombre_estructura = models.CharField(max_length=255)
    codigo_externo = models.CharField(max_length=255)
    codigo_area = models.CharField(max_length=255)
    siglas = models.TextField(blank=True, null=True)
    estructura_consejo = models.BooleanField(blank=True, null=True)
    estructura_credencial = models.BooleanField(blank=True, null=True)
    guardia = models.BooleanField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_destructura'


class TbDinmueble(models.Model):
    id_inmueble = models.IntegerField(primary_key=True)
    id_inmueble_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='id_inmueble_padre', blank=True, null=True)
    id_tipo_inmueble = models.ForeignKey('TbNtipoInmueble', models.DO_NOTHING, db_column='id_tipo_inmueble', blank=True, null=True)
    nombre_inmueble = models.CharField(max_length=255)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_dinmueble'


class TbDpersona(models.Model):
    id_persona = models.CharField(primary_key=True, max_length=255)
    id_sexo = models.ForeignKey('TbNsexo', models.DO_NOTHING, db_column='id_sexo', blank=True, null=True)
    id_municipio = models.ForeignKey('TbNmunicipio', models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_estructura = models.ForeignKey(TbDestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    nombre_completo = models.CharField(max_length=255)
    carne_identidad = models.CharField(max_length=255)
    solapin = models.CharField(max_length=255, blank=True, null=True)
    id_expediente = models.CharField(max_length=255, blank=True, null=True)
    residente = models.BooleanField()
    id_categoria = models.ForeignKey('TbNcategoria', models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    activo = models.BooleanField()
    baja = models.BooleanField()
    a_busqueda = models.CharField(max_length=255, blank=True, null=True)
    id_estructura_credencial = models.ForeignKey(TbDestructura, models.DO_NOTHING, db_column='id_estructura_credencial', related_name='tbdpersona_id_estructura_credencial_set', blank=True, null=True)
    usuario = models.TextField(blank=True, null=True)
    id_persona_foto = models.ForeignKey('TbDpersonaFoto', models.DO_NOTHING, db_column='id_persona_foto', blank=True, null=True)
    segundo_nombre = models.CharField(blank=True, null=True)
    primer_apellido = models.CharField(blank=True, null=True)
    segundo_apellido = models.CharField(blank=True, null=True)
    edificio = models.CharField(blank=True, null=True)
    apartamento = models.CharField(blank=True, null=True)
    primer_nombre = models.CharField(blank=True, null=True)
    id_estructura_consejo_direccion = models.ForeignKey(TbDestructura, models.DO_NOTHING, db_column='id_estructura_consejo_direccion', related_name='tbdpersona_id_estructura_consejo_direccion_set', blank=True, null=True)
    id_cargo = models.ForeignKey('TbNcargo', models.DO_NOTHING, db_column='id_cargo', blank=True, null=True)
    id_ano_academico = models.IntegerField(blank=True, null=True)
    id_parentesco = models.IntegerField(blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    id_persona_familiar = models.CharField(max_length=255, blank=True, null=True, db_comment='En este campo se guarda el id_persona de la persona que le reserva al familiar,')
    id_ano_academico_profesor = models.CharField(max_length=255, blank=True, null=True)
    trans_reservado = models.BooleanField(blank=True, null=True)
    trans_distribuido = models.BooleanField(blank=True, null=True)
    trans_cancelado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dpersona'


class TbDpersonaFoto(models.Model):
    foto = models.BinaryField(blank=True, null=True)
    color_foto = models.CharField(max_length=50, blank=True, null=True)
    id_persona_foto = models.AutoField(primary_key=True)
    id_foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dpersona_foto'


class TbNanoAcademico(models.Model):
    activo = models.BooleanField(blank=True, null=True)
    id_ano_academico = models.IntegerField(primary_key=True)
    nombre_ano_academico = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion_ano_academico = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_nano_academico'


class TbNcaracteristicaPersona(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    method_service = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_ncaracteristica_persona'


class TbNcargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ncargo'


class TbNcategoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    fecha_registro_categoria = models.DateTimeField()
    descripcion_categoria = models.TextField()
    activo_categoria = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_ncategoria'


class TbNmunicipio(models.Model):
    id_municipio = models.IntegerField(primary_key=True)
    id_provincia = models.ForeignKey('TbNprovincia', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)
    nombre_municipio = models.CharField(max_length=255)
    fecha_registro_municipio = models.DateTimeField()
    descripcion_municipio = models.TextField()
    codigo_oficial_municipio = models.CharField(unique=True, max_length=255)
    activo_municipio = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_nmunicipio'


class TbNparentesco(models.Model):
    activo = models.BooleanField(blank=True, null=True)
    id_parentesco = models.IntegerField(primary_key=True)
    nombre_parentesco = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion_parentesco = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_nparentesco'


class TbNprovincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre_provincia = models.CharField(max_length=255)
    fecha_registro_provincia = models.DateTimeField()
    descripcion_provincia = models.TextField()
    codigo_oficial_provincia = models.CharField(max_length=255)
    activo_provincia = models.BooleanField()
    abreviatura = models.CharField(max_length=255, blank=True, null=True)
    codigo_pais = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_nprovincia'


class TbNsexo(models.Model):
    id_sexo = models.IntegerField(primary_key=True)
    nombre_sexo = models.CharField(max_length=255)
    fecha_registro_sexo = models.DateTimeField()
    descripcion_sexo = models.TextField()
    activo_sexo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_nsexo'


class TbNtipoEstructura(models.Model):
    id_tipo_estructura = models.IntegerField(primary_key=True)
    id_tipo_estructura_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='id_tipo_estructura_padre', blank=True, null=True)
    nombre_tipo_estructura = models.CharField(max_length=255)
    fecha_registro_tipo_estructura = models.DateTimeField()
    descripcion_tipo_estructura = models.TextField(blank=True, null=True)
    activo_tipo_estructura = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_ntipo_estructura'


class TbNtipoInmueble(models.Model):
    id_tipo_inmueble = models.IntegerField(primary_key=True)
    nombre_tipo_inmueble = models.CharField(max_length=255)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_ntipo_inmueble'


class TbRinmueblePersona(models.Model):
    id = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_inmueble_persona = models.ForeignKey(TbDinmueble, models.DO_NOTHING, db_column='id_inmueble_persona', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rinmueble_persona'


class TbRpersonaFamiliar(models.Model):
    id_persona_familiar = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_familiar = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_familiar', related_name='tbrpersonafamiliar_id_familiar_set', blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_parentesco = models.ForeignKey(TbNparentesco, models.DO_NOTHING, db_column='id_parentesco', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rpersona_familiar'