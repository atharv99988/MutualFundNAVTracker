from flask import Flask
from flask_apscheduler import APScheduler
from datetime import datetime
from controller import addNAVs

# Define a class for your scheduler configuration
class Config:
    SCHEDULER_API_ENABLED = True
def scheduled_task():
    addNAVs.getMutualFund()
    print(f"Task is running at: {datetime.now()}")
    
app = Flask(__name__)
scheduler = APScheduler()

# Setup Flask config
app.config.from_object(Config())
# Add the scheduled job
scheduler.add_job(
    id='daily_task',               # Unique ID for the job
    func=scheduled_task,           # Function to be run
    trigger='cron',                # Cron trigger for specific time scheduling
    hour=8,                        # Set to 8 AM daily
    minute=0
)

scheduler.init_app(app)  # Initialize the scheduler with Flask app
scheduler.start()        # Start the scheduler



@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    # Set a custom port, e.g., port 8080
    app.run(debug=False, port=8080)
