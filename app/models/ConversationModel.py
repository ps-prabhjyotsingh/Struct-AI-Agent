
from sqlalchemy.orm import Mapped
from sqlmodel import Relationship

from app.common.Database import Database
from app.interfaces.ConversationResponse import ConversationBase
from app.models.MessageModel import MessageModel
from app.services.DatabaseService import DatabaseService

class ConversationModel(ConversationBase, table=True):

    messages: Mapped[list["MessageModel"] | None] = Relationship(back_populates="conversation",sa_relationship_kwargs=dict(lazy="selectin"))
    def createMessage(self, entity: int, message: str|None = None):
        db: Database = DatabaseService.get()
        message = MessageModel(message=message, conversation_id=self.id, entity=entity)
        message.status = MessageModel.STATUS_SUCCESS
        db.save(message)  # save the reply
        return message

    def summarize(self, messages, new_messages):
        db: Database = DatabaseService.get()
        self.all_messages = messages
        self.new_messages = new_messages
        db.save(self)