
from fastapi import APIRouter, HTTPException
from pydantic_ai.messages import ModelMessagesTypeAdapter

from app.interfaces.APIError import APIError

from app.interfaces.ConversationInterface import Conversation as ConversationType
from app.interfaces.ConversationReplyType import ConversationReplyType
from app.interfaces.ConversationResponse import ConversationResponse
from app.models.ConversationModel import ConversationModel
from app.models.MessageModel import MessageModel
from app.services.DatabaseService import DatabaseService
from app.services.GeneralAIService import GeneralAIService
from sqlmodel import select

router = APIRouter()
@router.post('/ai/conversation',response_model=ConversationResponse)
# You can extend the type Conversation to create your own specific kind of Conversations
def createConversation(conversation:ConversationType):
    #create conversation and add message
    conversationModel = ConversationModel(referenced_by=conversation.referencedBy)
    db = DatabaseService.get()
    db.save(conversationModel)

    conversationModel.createMessage(0, conversation.message)

    #now for the AI's reply
    message = conversationModel.createMessage(1)

    aiService = GeneralAIService.getInstance()
    #aiService.becomeSomeone()
    try:
        response = aiService.query(conversation.message)
        message.message = response.data
        message.request_tokens = response.usage().request_tokens
        message.response_tokens = response.usage().response_tokens
        conversationModel.summarize(response.all_messages_json(), response.new_messages_json())
    except Exception as e:
        message.status = 0
        message.error = str(e)
    db.save(message)
    if message.status == 0:
        #failed
        return APIError(message=message.error)
    #fetch conversation again
    db.refresh(conversationModel)
    return conversationModel

@router.get("/ai/conversation/{conversationID}",response_model=ConversationResponse)
def getConversation(conversationID: int):
    statement = (select(ConversationModel)
                 .where(ConversationModel.id == conversationID))
    db = DatabaseService.get()

    conversation = db.exec(statement).first()
    if conversation is None:
        raise HTTPException(404,"Unable to find the requested conversation.")
    return conversation

@router.patch("/ai/conversation/{conversationID}")
def replyConversation(reply: ConversationReplyType,conversationID: int):
    statement = select(ConversationModel).where(ConversationModel.id == conversationID)
    db = DatabaseService.get()

    conversation = db.exec(statement).first()
    if conversation is None:
        raise HTTPException(404,"Unable to find the requested conversation.")
    # add user message
    conversation.createMessage(0, reply.message)
    # compose a reply
    message = conversation.createMessage(1)
    aiService = GeneralAIService.getInstance()
    history = ModelMessagesTypeAdapter.validate_json(conversation.all_messages)
    try:
        response = aiService.query(reply.message, history)
        message.message = response.data
        message.request_tokens = response.usage().request_tokens
        message.response_tokens = response.usage().response_tokens
        conversation.summarize(response.all_messages_json(), response.new_messages_json())

    except Exception as e:
        message.status = 0
        message.error = str(e)
    db.save(message)
    if message.status == 0:
        #failed
        return APIError(message=message.error)
    return message
