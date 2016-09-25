from diary_app.database import db, init_db
from diary_app.events.models import Event
from diary_app.users.models import User


"""
DO NOT RUN THIS SCRIPT IN ''PROD'' IF DATABASE ALREADY HAS LIVE DATA!
"""

# Drop and recreate DB
init_db()

print "DB tables created"

# # Load Default Users
# admin_user = User(ADMIN_EMAIL, ADMIN_IAM_USER)
# default_user = User(DEFAULT_EMAIL, DEFAULT_IAM_USER)
# db.add(admin_user)
# db.add(default_user)
# db.commit()

# print "User table loaded"

# # Load Job Status Types
# for status_str in JOB_STATUS_TYPES:
# 	job_status = JobStatus(status_str)
# 	db.add(job_status)
# db.commit()

# print "JobStatusType table loaded"

# # Load Job Item Status Types
# for status_str in JOB_ITEM_STATUS_TYPES:
# 	job_item_status = JobItemStatus(status_str)
# 	db.add(job_item_status)
# db.commit()

# print "JobItemStatusType table loaded"

# # Insert Test Job
# job = Job(User.query.filter_by(iam_username=DEFAULT_IAM_USER).first().id, 1, 
# 		'testjob1', VAA3D_DEFAULT_PLUGIN, VAA3D_DEFAULT_FUNC, 1, OUTPUT_FILE_SUFFIXES[VAA3D_DEFAULT_PLUGIN])
# db.add(job)
# db.commit()

# print "Loaded test job data"

# # Insert Test Job Items
# job = Job.query.first()
