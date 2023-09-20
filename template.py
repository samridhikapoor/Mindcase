css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #c0cff0
}
.chat-message.bot {
    background-color: #c0cff0
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #000000;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user"> 
    <div class="message">{{MSG}}</div>
</div>
'''
