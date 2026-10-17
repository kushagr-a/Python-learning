from pydantic import BaseModel  # type: ignore[reportMissingImports]
from typing import List, Optional


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None  # self-referencing model


Comment.model_rebuild()  # This is necessary to resolve the forward reference

comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(
            id=2,
            content="This is a reply to the comment",
            replies=[Comment(id=3, content="This is a reply to the reply")],
        )
    ],
)

print("This is the comment data with self-referencing model:", comment)

commnet_data = {
    "id": 4,
    "content": "This is another comment",
    "replies": [
        {
            "id": 5,
            "content": "This is a reply to another comment",
            "replies": [
                {"id": 6, "content": "This is a reply to the reply to another comment"}
            ],
        }
    ],
}

cmt = Comment(**commnet_data)
print("This is the comment data with self-referencing model:", cmt)