from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(prefix="/like", tags=["Like"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def like(
    like: schemas.Like,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == like.post_id).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found!",
        )
    like_query = db.query(models.Like).filter(
        models.Like.post_id == like.post_id, models.Like.user_id == current_user.id
    )
    like_found = like_query.first()
    if like.dir == 1:
        if like_found is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="You have already liked this post",
            )
        new_like = models.Like(post_id=like.post_id, user_id=current_user.id)
        db.add(new_like)
        db.commit()
        return {"message": "Successfully added like!"}
    else:
        if like_found is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This post is not liked by you!",
            )
        like_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Successfully removed like!"}
