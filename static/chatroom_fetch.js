//const messageInput = document.getElementById("message-input")
const messageContainer = document.querySelector('.chat-messages')
var last_message_id = -1


async function fetchMessage() {
    console.log('requested_message!!!');
    var message_id = JSON.stringify({'last_message_id': last_message_id})
    var response = await fetch('/requestmessage', {method: 'FETCH',
                                                   body: message_id,
                                                   headers: {'Content-Type': 'application/json'}})
   var response_data = await response.json()
   console.log(response_data)

   response_data.forEach((element) => {last_message_id = Math.max(last_message_id, element.id)
   var msg = document.createElement('div')
   msg.classList.add('bot-message')
   msg.classList.add('message')
   msg.textContent = element.text
   messageContainer.appendChild(msg)})
   }

setInterval(fetchMessage, 1500)



//// Функция для отправки запроса на серверный эндпоинт
//function sendRequest() {
//  // Получаем текст сообщения из поля ввода
//  const messageInput = document.getElementById("message-input");
//  const messageText = messageInput.value;
//
//  // Отправляем запрос на серверный эндпоинт
//  fetch("/requestmessage", {
//    method: "POST",
//    headers: {
//      "Content-Type": "application/json"
//    },
//    body: JSON.stringify({
//      message: messageText
//    })
//  })
//  .then(response => response.json())
//  .then(data => {
//    // Обрабатываем ответ от сервера
//    const chatContainer = document.querySelector('.chat-messages');
//    const botMessage = document.createElement('div');
//    botMessage.classList.add('message', 'bot-message');
//    botMessage.textContent = data.message;
//    chatContainer.appendChild(botMessage);
//    chatContainer.scrollTop = chatContainer.scrollHeight;
//
//    // Очищаем поле ввода
//    messageInput.value = '';
//  })
//  .catch(error => {
//    console.error("Ошибка:", error);
//  });
//}
//
//// Получаем ссылки на элементы DOM
//const sendButton = document.getElementById("send-button");
//
//// Добавляем обработчик события на кнопку отправки сообщения
//sendButton.addEventListener("click", sendRequest);
