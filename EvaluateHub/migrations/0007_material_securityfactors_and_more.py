# Generated by Django 4.2 on 2023-04-17 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EvaluateHub', '0006_workersaffairs_negatives'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('increase', models.IntegerField(blank=True, null=True)),
                ('decrease', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityFactors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fire_line', models.CharField(blank=True, choices=[('صالح', 1), ('غير صالح', 0)], max_length=11, null=True)),
                ('tanks', models.CharField(blank=True, choices=[('صالح', 1), ('غير صالح', 0)], max_length=11, null=True)),
                ('buckets', models.CharField(blank=True, choices=[('صالح', 1), ('غير صالح', 0)], max_length=11, null=True)),
                ('fire_extinguishers', models.CharField(blank=True, choices=[('صالح', 1), ('غير صالح', 0)], max_length=11, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='evaluationform',
            name='school_type',
        ),
        migrations.AddField(
            model_name='administration',
            name='activities_activation',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='analysis',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='communication_system',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='execution_plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='obstacles',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='predicted_crisis',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='risks_indicators',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='team_building',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='training_on_plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='cooperative',
            name='drag_profits',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='cooperative',
            name='drag_running',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='cooperative',
            name='existing_authorized_items',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='decentralization',
            name='append',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='decentralization',
            name='board_of_trustees',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='decentralization',
            name='decentralization_committee',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='decentralization',
            name='exchange',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='decentralization',
            name='plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='decentralization',
            name='settlement',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='environmentpopulation',
            name='activities',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='environmentpopulation',
            name='check_health_plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='environmentpopulation',
            name='diagnosis_health_plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='environmentpopulation',
            name='health_file',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='environmentpopulation',
            name='labs_health_procedures',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='environmentpopulation',
            name='toilets_health_procedures',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='laboratories',
            name='computers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='laboratories',
            name='evaluation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='laboratories',
            name='networks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='laboratories',
            name='ory_association',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='laboratories',
            name='tilo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='laboratories',
            name='work_validity',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='daily_received',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='daily_served',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='disciplined_distribution',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='health_certificate',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='not_stored_periods',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='productionunit',
            name='activation',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='productionunit',
            name='certified',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='productionunit',
            name='profit_distribution',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='productionunit',
            name='supply',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='first_year_one',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='first_year_three',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='first_year_two',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='second_year_one',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='second_year_three',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='second_year_two',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='third_year_one',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='third_year_three',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='third_year_two',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='securitysafety',
            name='building',
            field=models.CharField(blank=True, choices=[('منضبط', 1), ('غير منضبط', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='securitysafety',
            name='cabins',
            field=models.CharField(blank=True, choices=[('منضبط', 1), ('غير منضبط', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='securitysafety',
            name='external_factors',
            field=models.CharField(blank=True, choices=[('منضبط', 1), ('غير منضبط', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='securitysafety',
            name='labs',
            field=models.CharField(blank=True, choices=[('منضبط', 1), ('غير منضبط', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='securitysafety',
            name='wall',
            field=models.CharField(blank=True, choices=[('منضبط', 1), ('غير منضبط', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='strategicplanning',
            name='analysis',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='strategicplanning',
            name='obstacles',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='strategicplanning',
            name='plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='strategicplanning',
            name='plan_activation',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='strategicplanning',
            name='team_building',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='teachers_training',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='training_plan',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='training_plan_activation',
            field=models.CharField(blank=True, choices=[('يوجد', 1), ('لا يوجد', 0)], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='securitysafety',
            name='security_factors',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='security_factors', to='EvaluateHub.securityfactors'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='material_five',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_five', to='EvaluateHub.material'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='material_four',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_four', to='EvaluateHub.material'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='material_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EvaluateHub.material'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='material_six',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_six', to='EvaluateHub.material'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='material_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_three', to='EvaluateHub.material'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='material_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_two', to='EvaluateHub.material'),
        ),
    ]