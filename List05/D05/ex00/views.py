from django.shortcuts import render
from django.views.generic import TemplateView 
import psycopg2
# Create your views here.
class Ex00_movies(TemplateView):
    def get(self, request, **kargs):
        try:
            conn = psycopg2.connect(user="llima-ce", password="l1u2i3z4")
        except Exception as e:
            return render(request, 'ex00/ex00.html', {"message": "ERROR to connect the db"})
        cur = conn.cursor()
        try:
            cur.execute("CREATE DATABASE ex00_movies;")
            cur.execute("CREATE TABLE title (data varchar(64) NOT NULL UNIQUE;")
            cur.execute('CREATE TABLE episode_nb (id serial PRIMARY KEY);')
            cur.execute('CREATE TABLE opening_crawl (data text);')
            cur.execute('CREATE TABLE director (data varchar(32) NOT NULL);')
            cur.execute('CREATE TABLE producer (data varchar(128) NOT NULL);')
            cur.execute('CREATE TABLE release_date (data date);')
            return render(request, 'ex00/ex00.html', {"message": "OK"})
        except Exception as e:
            return render(request, 'ex00/ex00.html', {"message": str(e)})
