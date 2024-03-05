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
    result = conn.execute(text("select * from jobs where id = :val"), val=id)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])  