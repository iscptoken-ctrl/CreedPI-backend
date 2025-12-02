from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

router = APIRouter(prefix="/wallet", tags=["Wallet"])

def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/update")
def update_wallet(telegram_id: int, wallet: str, db: Session = Depends(db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if user:
        user.wallet = wallet
        db.commit()
    return {"status": "ok"}
