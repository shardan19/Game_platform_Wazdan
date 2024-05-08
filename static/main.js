function changeMaintananceMode(mode){
    console.log("changing Maintanance mode...")
    const url = window.location.origin
    data=fetch(url+'/admin', {
        method: 'post',
        body: JSON.stringify({maintanance:mode})}).then((r) => r.json())
    .then((response)=>{
      console.log("response:",response);
    }).then(()=>{
        location.reload();
    })
}

function launchGame(id){
    console.log("launching game...",id)
    $('#gameModal').modal("show");
    console.log(games[id])
    console.log(games)
    const url = window.location.origin
    sendData={"id":id,"game":games[id]["name"],"token":games[id]["token"],"license":games[id]["licence"],"format":""}
    data=fetch(url+'/launch', {
        method: 'post',
        body: JSON.stringify(sendData)}).then((r) => r.text())
        .then((response)=>{
            console.log("response:",response);
            $('#gameContent').html(response);
            var scriptElement = document.createElement('script');
            scriptElement.src = response;
            document.head.appendChild(scriptElement);
          })
}

