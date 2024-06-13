from flask import Blueprint, render_template,redirect,url_for,request
from apps.app import db
from apps.crud.model import Chat


crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="statics",
)

@crud.route('/', methods=["GET","POST"])
def login():
    if request.method == "POST" :
        return redirect('friends')
    return render_template('crud/login.html')


@crud.route('/friends',methods=["GET","POST"])
def friends():
    return render_template('crud/friends.html')


@crud.route('/chats',methods=["GET","POST"])
def chats():
    return render_template('crud/chats.html')


@crud.route('/chat',methods=["GET"])
def chat():
    chatting = db.session.query(Chat.friend_chating).all()
    
    return render_template('crud/chat.html', chatting = chatting)





