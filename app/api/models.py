from django.db import models


# Create your models here.
class TbDasignacion(models.Model):
    id_asignacion = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey('TbDpersonaGuardia', models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_ejecucion = models.ForeignKey('TbDejecucionDePlanificacion', models.DO_NOTHING, db_column='id_ejecucion', blank=True, null=True)
    id_persona_registro = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    id_persona_cambio = models.OneToOneField('TbDpersonaGuardia', models.DO_NOTHING, db_column='id_persona_cambio', related_name='tbdasignacion_id_persona_cambio_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dasignacion'


class TbDasistencia(models.Model):
    id_asistencia = models.IntegerField(primary_key=True)
    id_asignacion = models.ForeignKey(TbDasignacion, models.DO_NOTHING, db_column='id_asignacion', blank=True, null=True)
    asistencia = models.BooleanField()
    fecha_hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_dasistencia'


class TbDasistenciaOg(models.Model):
    id_asistencia_og = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    id_persona_registro = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dasistencia_og'


class TbDconfiguracion(models.Model):
    id_configuracion = models.IntegerField(primary_key=True)
    nombre_configuracion = models.CharField(max_length=255)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    activo = models.BooleanField()
    id_region_guardia = models.ForeignKey('TbDregionGuardia', models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dconfiguracion'


class TbDdiasPersona(models.Model):
    id = models.IntegerField(primary_key=True)
    id_persona = models.CharField(max_length=255)
    id_planificacion = models.ForeignKey('TbDplanificacion', models.DO_NOTHING, db_column='id_planificacion')
    turnos = models.TextField(blank=True, null=True, db_comment='(DC2Type:array)')
    dias = models.TextField(blank=True, null=True, db_comment='(DC2Type:array)')

    class Meta:
        managed = False
        db_table = 'tb_ddias_persona'


class TbDejecucionDePlanificacion(models.Model):
    id_ejecucion_planificacion = models.IntegerField(primary_key=True)
    id_planificacion = models.ForeignKey('TbDplanificacion', models.DO_NOTHING, db_column='id_planificacion', blank=True, null=True)
    fecha = models.DateField()
    id_turno = models.ForeignKey('TbNturno', models.DO_NOTHING, db_column='id_turno', blank=True, null=True)
    id_posta = models.ForeignKey('TbDposta', models.DO_NOTHING, db_column='id_posta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dejecucion_de_planificacion'


class TbDequipo(models.Model):
    id_equipo = models.IntegerField(primary_key=True)
    responsable = models.OneToOneField('TbDpersonaGuardia', models.DO_NOTHING, db_column='responsable', blank=True, null=True)
    id_region_guardia = models.ForeignKey('TbDregionGuardia', models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)
    nombre_equipo = models.CharField(max_length=255)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_dequipo'


class TbDgrupoGuardia(models.Model):
    id_grupo_guardia = models.AutoField(primary_key=True)
    nombre_grupo_guardia = models.CharField(max_length=255)
    cantidad_personas_maxima = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_region_guardia = models.ForeignKey('TbDregionGuardia', models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)
    id_grupo_guardia_estructura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dgrupo_guardia'


class TbDincidencia(models.Model):
    id_incidencia = models.IntegerField(primary_key=True)
    id_tipo_incidencia = models.ForeignKey('TbNtipoIncidencia', models.DO_NOTHING, db_column='id_tipo_incidencia', blank=True, null=True)
    id_ejecucion_planificacion = models.ForeignKey(TbDejecucionDePlanificacion, models.DO_NOTHING, db_column='id_ejecucion_planificacion', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    activo = models.BooleanField()
    fecha_registro = models.DateField()
    id_persona_guardia = models.ForeignKey('TbDpersonaGuardia', models.DO_NOTHING, db_column='id_persona_guardia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dincidencia'


class TbDpatron(models.Model):
    id_patron = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=250)
    periodicidad = models.IntegerField()
    rotacion_turnos = models.TextField(db_comment='(DC2Type:array)')
    rotacion_dias = models.TextField(db_comment='(DC2Type:array)')
    activo = models.BooleanField()
    id_tipo_periodicidad = models.ForeignKey('TbNtipoPeriodicidad', models.DO_NOTHING, db_column='id_tipo_periodicidad', blank=True, null=True)
    id_region_guardia = models.ForeignKey('TbDregionGuardia', models.DO_NOTHING, db_column='id_region_guardia')

    class Meta:
        managed = False
        db_table = 'tb_dpatron'


class TbDpersonaGuardia(models.Model):
    id_persona = models.CharField(primary_key=True, max_length=255)
    id_grupo_guardia = models.ForeignKey(TbDgrupoGuardia, models.DO_NOTHING, db_column='id_grupo_guardia', blank=True, null=True)
    id_equipo = models.ForeignKey(TbDequipo, models.DO_NOTHING, db_column='id_equipo', blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dpersona_guardia'


class TbDplanificacion(models.Model):
    id_planificacion = models.IntegerField(primary_key=True)
    id_region_guardia = models.ForeignKey('TbDregionGuardia', models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)
    id_estado_plan = models.ForeignKey('TbNestadoPlan', models.DO_NOTHING, db_column='id_estado_plan', blank=True, null=True)
    nombre_planificacion = models.CharField(unique=True, max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_persona_publicacion = models.CharField(max_length=255, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dplanificacion'


class TbDposta(models.Model):
    id_posta = models.IntegerField(primary_key=True)
    id_region_guardia = models.ForeignKey('TbDregionGuardia', models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)
    nombre_posta = models.CharField(max_length=255)
    localizacion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField()
    cantidad_personas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_dposta'


class TbDrecurso(models.Model):
    id_recurso = models.IntegerField(primary_key=True)
    id_tipo_recurso = models.ForeignKey('TbNtipoRecurso', models.DO_NOTHING, db_column='id_tipo_recurso', blank=True, null=True)
    id_posta = models.ForeignKey(TbDposta, models.DO_NOTHING, db_column='id_posta', blank=True, null=True)
    nombre_recurso = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tb_drecurso'


class TbDregionGuardia(models.Model):
    id_region_guardia = models.IntegerField(primary_key=True)
    nombre_region_guardia = models.CharField(max_length=255)
    activo = models.BooleanField()
    id_responsable = models.CharField(unique=True, max_length=255, blank=True, null=True)
    id_planificador = models.CharField(unique=True, max_length=255, blank=True, null=True)
    id_estructura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dregion_guardia'


class TbDsincronizacion(models.Model):
    id_sincronizacion = models.AutoField(primary_key=True)
    host = models.TextField(blank=True, null=True)
    puerto = models.TextField()
    usuario = models.TextField()
    contrasena = models.TextField()
    nombre_bd = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dsincronizacion'


class TbDsolicitudCambio(models.Model):
    id_solicitud_cambio = models.IntegerField(primary_key=True)
    id_asignacion_solicitante = models.ForeignKey(TbDasignacion, models.DO_NOTHING, db_column='id_asignacion_solicitante', blank=True, null=True)
    id_asignacion_cambiador = models.ForeignKey(TbDasignacion, models.DO_NOTHING, db_column='id_asignacion_cambiador', related_name='tbdsolicitudcambio_id_asignacion_cambiador_set', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    motivo = models.TextField()
    aprobadacambiador = models.BooleanField(blank=True, null=True)
    aprobadaplanificador = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dsolicitud_cambio'


class TbDvariable(models.Model):
    id_variable = models.IntegerField(primary_key=True)
    nombre_variable = models.CharField(unique=True, max_length=250)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    activo = models.BooleanField()
    id_metodo = models.ForeignKey('TbNmetodo', models.DO_NOTHING, db_column='id_metodo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dvariable'


class TbNdiaFestivo(models.Model):
    id_dia_festivo = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    todos_anhos = models.BooleanField()
    nombre_dia_festivo = models.CharField(max_length=250)
    dia_semana_mes = models.CharField(max_length=20, blank=True, null=True)
    metodo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ndia_festivo'


class TbNdias(models.Model):
    id_dias = models.IntegerField(primary_key=True)
    id_horario = models.ForeignKey('TbNhorario', models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_ndias'


class TbNdiasAMostrar(models.Model):
    id_dias_a_mostrar = models.IntegerField(primary_key=True)
    nombre_dias_a_mostrar = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_ndias_a_mostrar'


class TbNestadoPlan(models.Model):
    id_estado_plan = models.IntegerField(primary_key=True)
    nombre_estado_plan = models.CharField(unique=True, max_length=250)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    fecharegistro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_nestado_plan'


class TbNhorario(models.Model):
    id_horario = models.IntegerField(primary_key=True)
    nombre_horario = models.CharField(unique=True, max_length=250)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_nhorario'


class TbNmetodo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField()
    entity = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    method_service = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_nmetodo'


class TbNtipoIncidencia(models.Model):
    id_tipo_incidencia = models.IntegerField(primary_key=True)
    nombre_tipo_incidencia = models.CharField(unique=True, max_length=250)
    color = models.CharField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    activo = models.BooleanField()
    fecha_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_ntipo_incidencia'


class TbNtipoPeriodicidad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_ntipo_periodicidad'


class TbNtipoPlanificacion(models.Model):
    id_tipo_planificacion = models.IntegerField(primary_key=True)
    nombre_tipo_planificacion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_ntipo_planificacion'


class TbNtipoRecurso(models.Model):
    id_tipo_recurso = models.IntegerField(primary_key=True)
    nombre_tipo_recurso = models.CharField(unique=True, max_length=250)
    fecha_registro_tipo_recurso = models.DateTimeField()
    descripcion_tipo_recurso = models.TextField(blank=True, null=True)
    activo_tipo_recurso = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_ntipo_recurso'


class TbNturno(models.Model):
    id_turno = models.IntegerField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    nombre_turno = models.CharField(max_length=250)
    activo = models.BooleanField()
    nombre_notificacion = models.CharField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_nturno'


class TbNultimasGuardias(models.Model):
    id_ultimas_guardias = models.IntegerField(primary_key=True)
    nombre_ultimas_guardias = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_nultimas_guardias'


class TbRgrupoGuardiaEstructura(models.Model):
    id_grupo_guardia_estructura = models.AutoField(primary_key=True)
    id_grupo_guardia = models.ForeignKey(TbDgrupoGuardia, models.DO_NOTHING, db_column='id_grupo_guardia', blank=True, null=True)
    id_estructura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rgrupo_guardia_estructura'


class TbRgrupoGuardiaPersona(models.Model):
    id_grupo_guardia_persona = models.AutoField(primary_key=True)
    id_persona = models.TextField()
    id_grupo_guardia = models.ForeignKey(TbDgrupoGuardia, models.DO_NOTHING, db_column='id_grupo_guardia')
    id_estructura_credencial = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rgrupo_guardia_persona'


class TbRhorarioTurno(models.Model):
    id_horario = models.OneToOneField(TbNhorario, models.DO_NOTHING, db_column='id_horario', primary_key=True)  # The composite primary key (id_horario, id_turno) found, that is not supported. The first column is selected.
    id_turno = models.ForeignKey(TbNturno, models.DO_NOTHING, db_column='id_turno')

    class Meta:
        managed = False
        db_table = 'tb_rhorario_turno'
        unique_together = (('id_horario', 'id_turno'),)


class TbRpersonaGuardiaDiaFestivo(models.Model):
    id_persona_guardia_dia_festivo = models.AutoField(primary_key=True)
    id_persona_guardia = models.ForeignKey(TbDpersonaGuardia, models.DO_NOTHING, db_column='id_persona_guardia', blank=True, null=True)
    id_dia_festivo = models.ForeignKey(TbNdiaFestivo, models.DO_NOTHING, db_column='id_dia_festivo', blank=True, null=True)
    anho = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rpersona_guardia_dia_festivo'


class TbRpersonaGuardiaVariable(models.Model):
    id_persona_guardia = models.CharField(primary_key=True, max_length=255)  # The composite primary key (id_persona_guardia, id_variable) found, that is not supported. The first column is selected.
    id_variable = models.ForeignKey(TbDvariable, models.DO_NOTHING, db_column='id_variable')

    class Meta:
        managed = False
        db_table = 'tb_rpersona_guardia_variable'
        unique_together = (('id_persona_guardia', 'id_variable'),)


class TbRpersonaPatron(models.Model):
    id_rpersona_patron = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersonaGuardia, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_patron = models.ForeignKey(TbDpatron, models.DO_NOTHING, db_column='id_patron', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rpersona_patron'


class TbRpersonaVariable(models.Model):
    id_rpersona_variable = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersonaGuardia, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_variable = models.ForeignKey(TbDvariable, models.DO_NOTHING, db_column='id_variable', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rpersona_variable'


class TbRregionHorario(models.Model):
    id_rregion_horario = models.IntegerField(primary_key=True)
    id_region_guardia = models.ForeignKey(TbDregionGuardia, models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)
    id_horario = models.ForeignKey(TbNhorario, models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
    arreglo = models.TextField(blank=True, null=True, db_comment='(DC2Type:array)')

    class Meta:
        managed = False
        db_table = 'tb_rregion_horario'


class TbRregionHorarioDia2(models.Model):
    id_region_horario_dia = models.AutoField(primary_key=True)
    id_region_guardia = models.ForeignKey(TbDregionGuardia, models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)
    id_horario = models.ForeignKey(TbNhorario, models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True, db_comment='no esta referianciado por no existir una tabla que registre los dias de la semana, los posibles valores serian: 0-1-2-3-4-5-6-7, siendo 0 == domingo')
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rregion_horario_dia2'


class TbRregionHorarioTurno(models.Model):
    id_region_horario_turno = models.IntegerField(primary_key=True)
    id_rregion_horario = models.ForeignKey(TbRregionHorario, models.DO_NOTHING, db_column='id_rregion_horario', blank=True, null=True)
    turnos = models.TextField(db_comment='(DC2Type:array)')

    class Meta:
        managed = False
        db_table = 'tb_rregion_horario_turno'


class TbRregionHorarioTurno2(models.Model):
    id_region_horario_turno = models.AutoField(primary_key=True)
    id_region_guardia = models.ForeignKey(TbDregionGuardia, models.DO_NOTHING, db_column='id_region_guardia', blank=True, null=True)
    id_horario = models.ForeignKey(TbNhorario, models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
    id_turno = models.ForeignKey(TbNturno, models.DO_NOTHING, db_column='id_turno', blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rregion_horario_turno2'


class TbRtipoRecursoPosta(models.Model):
    id_rtipo_recurso_posta = models.IntegerField(primary_key=True)
    id_posta = models.ForeignKey(TbDposta, models.DO_NOTHING, db_column='id_posta', blank=True, null=True)
    id_tipo_recurso = models.ForeignKey(TbNtipoRecurso, models.DO_NOTHING, db_column='id_tipo_recurso', blank=True, null=True)
    valor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_rtipo_recurso_posta'


class TbRvariableConfiguracion(models.Model):
    id = models.IntegerField(primary_key=True)
    id_configuracion = models.ForeignKey(TbDconfiguracion, models.DO_NOTHING, db_column='id_configuracion', blank=True, null=True)
    id_variable = models.ForeignKey(TbDvariable, models.DO_NOTHING, db_column='id_variable', blank=True, null=True)
    negacion = models.BooleanField()
    tipo_atributo = models.CharField(max_length=255)
    arreglo = models.TextField(db_comment='(DC2Type:array)')

    class Meta:
        managed = False
        db_table = 'tb_rvariable_configuracion'
