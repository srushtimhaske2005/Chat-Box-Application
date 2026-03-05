const socket = io();

// ===== Username =====
let username = localStorage.getItem("chatUser") || "";
while(!username){
  username = prompt("Enter your name:");
  if(username){
    localStorage.setItem("chatUser", username);
  }
}

socket.emit("join", username);

// ===== Elements =====
const chat = document.getElementById("chat");
const users = document.getElementById("users");
const msg = document.getElementById("msg");
const sendBtn = document.getElementById("send-btn");
const deleteBtn = document.getElementById("delete-btn");

// ===== Render Chat History =====
function render(history){
  chat.innerHTML = "";
  history.forEach(m => {
    if(m.type === "system"){
      chat.innerHTML += `<div class="system">${m.message}</div>`;
    } else {
      chat.innerHTML += `<b>${m.username}</b> [${m.time}]<br>${m.message}<br><br>`;
    }
  });
  chat.scrollTop = chat.scrollHeight;
}

// ===== Send Message =====
sendBtn.onclick = () => {
  if(msg.value.trim()){
    socket.emit("send_message",{username, message: msg.value});
    msg.value = "";
  }
};

// Enter key sends message
msg.addEventListener("keypress", e => {
  if(e.key === "Enter" && !e.shiftKey){
    e.preventDefault();
    sendBtn.click();
  }
});

// ===== Delete Chat =====
deleteBtn.onclick = () => {
  if(confirm("Delete entire chat?")){
    socket.emit("delete_all");
  }
};

// ===== Receive Chat History =====
socket.on("chat_history", render);

// ===== System Message =====
socket.on("system_message", text => {
  chat.innerHTML += `<div class="system">${text}</div>`;
  chat.scrollTop = chat.scrollHeight;
});

// ===== Online Users =====
socket.on("user_list", list => {
  users.innerHTML = "<b>Online Users</b><hr>" + list.join("<br>");
});

// ===== Emoji Click =====
document.querySelectorAll(".emoji").forEach(e => {
  e.onclick = () => msg.value += e.innerText;
});
