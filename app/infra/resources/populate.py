from app.infra.db.connector import AppSession

if __name__ == "__main__":
    AppSession().create_tables()