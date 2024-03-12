from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
def root():
    return {"message": "Welcome to the JoyEnergy "}


@router.get("/health")
def health():
    return True
