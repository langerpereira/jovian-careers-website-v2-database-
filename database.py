from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://sql6688646:NkiN2SXTNm@sql6.freesqldatabase.com/sql6688646?charset=utf8mb4")

def load_jobs_fromdb():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      result_dicts = []
      for row in result.all():
          row_dict = {}
          for column in result.keys():
              row_dict[column] = getattr(row, column)
          result_dicts.append(row_dict)
  return result_dicts

def load_job_fromdb(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]) 

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, {
                 'job_id': job_id, 
                 'full_name': data['full_name'],
                 'email': data['email'],
                 'linkedin_url': data['linkedin_url'],
                 'education': data['education'],
                 'work_experience': data['work_experience'],
                 'resume_url': data['resume_url']
    })
       

