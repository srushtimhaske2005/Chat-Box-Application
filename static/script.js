body{
  font-family: Arial;
  background: #fef6f9;
  max-width: 900px;
  margin: 20px auto;
  padding: 0 10px;
}

.title{
  text-align: center;
  color: #7a5ca6;
}

.container{
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

#users{
  width: 180px;
  border: 1px solid #d7cfe7;
  border-radius: 10px;
  padding: 10px;
  background: #f5f0fa;
  height: 380px;
  overflow-y: auto;
}

.main{
  flex:1;
  min-width: 250px;
}

#chat{
  border:1px solid #d7cfe7;
  border-radius:10px;
  padding:10px;
  background:white;
  height:300px;
  overflow-y:auto;
}

.system{
  color:#888;
  font-style:italic;
  font-size:13px;
  margin:4px 0;
}

.input-area{
  margin-top:8px;
  display:flex;
  gap:5px;
}

textarea{
  flex:1;
  border-radius:6px;
  border:1px solid #d7cfe7;
  padding:6px;
}

button{
  background:#bda0cb;
  border:none;
  color:white;
  padding:6px 10px;
  border-radius:6px;
  cursor:pointer;
}

button:hover{
  background:#a98db8;
}

.emoji-bar{
  margin-top:6px;
}

.emoji{
  cursor:pointer;
  font-size:20px;
  margin-right:5px;
}

.delete-btn{
  margin-top:8px;
  background:#e27d60;
}

.delete-btn:hover{
  background:#d45d40;
}

/* Mobile Responsive */
@media screen and (max-width: 600px){
  .container{flex-direction: column;}
  #users{width:100%; height:150px;}
  #chat{height:250px;}
}
