from flask import Flask, render_template


app=Flask(__name__)


@app.route("/<name>",methods=["GET"])
def start(name):
    return f'welcome {name}'

jobs = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Cairo',
        'company': 'Tech Company'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Alexandria',
        'company': 'Data Corp'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'Zagazig',
        'company': 'Web Solutions'
    },
    {
        'id': 4,
        'title': 'Mobile Developer',
        'location': 'Cairo',
        'company': 'App Innovations'
    },
    {
        'id': 5,
        'title': 'DevOps Engineer',
        'location': 'Giza',
        'company': 'Cloud Services'
    }
]

companies = [
    {
        'id': 1,
        'name': 'Tech Company',
        'location': 'Cairo',
        'industry': 'Information Technology',
        'employees_count': 500
    },
    {
        'id': 2,
        'name': 'Data Corp',
        'location': 'Alexandria',
        'industry': 'Big Data',
        'employees_count': 250
    },
    {
        'id': 3,
        'name': 'Web Solutions',
        'location': 'Zagazig',
        'industry': 'Web Development',
        'employees_count': 100
    },
    {
        'id': 4,
        'name': 'App Innovations',
        'location': 'Cairo',
        'industry': 'Mobile Development',
        'employees_count': 75
    },
    {
        'id': 5,
        'name': 'Cloud Services',
        'location': 'Giza',
        'industry': 'Cloud Computing',
        'employees_count': 300
    }
]

@app.route("/jobs/<int:id>",methods=['GET'])
def list_jobs(id):
        job = next((job for job in jobs if job['id'] == id))
        return render_template('jobs_list.html',jobs=jobs)


@app.route("/companies/list",methods=["GET"])
def list_company():
    return render_template('company_list.html',companies=companies)


@app.route("/companies/<int:id>",methods=['GET'])
def show_company(id):
        company = next((company for company in companies if company['id'] == id))
        
        return render_template('company_details.html',companies=companies)