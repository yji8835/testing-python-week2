from fastapi import APIRouter, File, Form, UploadFile
from app.models.user import UserResponse

router = APIRouter()


@router.post("/users/register", response_model=UserResponse)
async def register(user_id: str = Form(...), image: UploadFile = File(...)):
    """회원 등록 엔드포인트"""
    pass


@router.post("/users/authenticate")
async def authenticate(image: UploadFile = File(...)):
    """회원 인증 엔드포인트"""
    pass


@router.get("/users/{user_id}")
def get_user_info(user_id: str):
    """회원 정보 조회 엔드포인트"""
    pass


@router.delete("/users/{user_id}")
def delete_user_info(user_id: str):
    """회원 삭제 엔드포인트"""
    pass
