//const messageInput = document.getElementById("message-input")

function fetchMessage() {
    console.log('requested_message')
    fetch('/requestmessage', {method: 'FETCH', headers: {
      "Content-Type": "application/json"}, body: JSON.stringify({
      message: messageText
    })})
                        }

setInterval(fetchMessage, 1000)



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
