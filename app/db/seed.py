import logging
from app.db.session import SessionLocal
from app.db.models import User
from app.core.security import get_password_hash

logger = logging.getLogger(__name__)


def seed_db():
    """Populates the database with initial dummy data."""
    db = SessionLocal()
    try:
        if db.query(User).first():
            logger.info("Database already contains users. Skipping seed.")
            return

        logger.info("Seeding database with dummy users...")

        test_user = User(
            email="test@example.com",
            hashed_password=get_password_hash("password123"),
            is_active=True,
        )

        admin_user = User(
            email="admin@example.com",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
        )

        db.add(test_user)
        db.add(admin_user)
        db.commit()
        logger.info("Database seeded successfully!")

    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()