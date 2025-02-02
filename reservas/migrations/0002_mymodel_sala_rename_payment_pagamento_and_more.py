# Generated by Django X.Y on YYYY-MM-DD HH:MM
from django.db import migrations, models
import django.utils.timezone
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),  # Dependência da migração inicial
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),  # Dependência do modelo de usuário
    ]

    operations = [
        # Criar o modelo Sala
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('capacidade', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
        ),
        # Renomear o modelo Payment para Pagamento
        migrations.RenameModel(
            old_name='Payment',
            new_name='Pagamento',
        ),
        # Renomear campos no modelo Feedback
        migrations.RenameField(
            model_name='feedback',
            old_name='mensagem',
            new_name='comentario',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='criacao',
            new_name='data_feedback',
        ),
        # Renomear campo data para data_fim no modelo Reserva
        migrations.RenameField(
            model_name='reserva',
            old_name='data',
            new_name='data_fim',
        ),
        # Remover campos desnecessários
        migrations.RemoveField(
            model_name='reserva',
            name='ccriada_em',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='dduracao',
        ),
        # Adicionar novos campos ao modelo Feedback
        migrations.AddField(
            model_name='feedback',
            name='avaliacao',
            field=models.IntegerField(default=0),
        ),
        # Adicionar novos campos ao modelo Reserva
        migrations.AddField(
            model_name='reserva',
            name='data_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reserva',
            name='status',
            field=models.CharField(default='confirmada', max_length=20),
        ),
        # Adicionar um campo ForeignKey para Sala no modelo Reserva
        migrations.AddField(
            model_name='reserva',
            name='sala',
            field=models.ForeignKey(
                to='reservas.sala',
                on_delete=models.CASCADE,
                null=True,  # Permite que o campo seja nulo
            ),
        ),
    ]
