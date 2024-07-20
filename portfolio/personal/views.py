from django.shortcuts import render
from .models import PersonalInfo, Education, Experience, Project, Skill, Certification, Achievement, Activity, Referee

def home(request):
    personal_info = PersonalInfo.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    achievements = Achievement.objects.all()
    activities = Activity.objects.all()
    referees = Referee.objects.all()

    context = {
                                                'personal_info': personal_info,
                                                        'education': education,
                                                                'experience': experience,
                                                                        'projects': projects,
                                                                                'skills': skills,
                                                                                        'certifications': certifications,
                                                                                                'achievements': achievements,
                                                                                                        'activities': activities,
                                                                                                                'referees': referees,
                                                                                                                    }
    return render(request, 'personal/home.html', context)
