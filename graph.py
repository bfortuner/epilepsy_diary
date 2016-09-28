from diary_app.charts import chart_manager
from diary_app.users.constants import ADMIN_USERNAME

if __name__ == "__main__":
    print chart_manager.get_chart(ADMIN_USERNAME)
