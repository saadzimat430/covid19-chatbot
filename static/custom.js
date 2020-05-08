function submit_message(message) {
    $.post( "/send_message", {
        message: message
    }, handle_response);

    function handle_response(data) {
      // append the bot repsonse to the div
      $('#chat-container').append(`
            <div class="chat-message col-md-5 offset-md-7 bot-message" id="response">
                ${data.message}
            </div>
      `).animate({scrollTop: $('#chat-container').prop("scrollHeight")}, 500)

      // remove the loading indicator
      $( "#loading" ).remove();
    }
}

$('#target').on('submit', function(e){
    e.preventDefault();
    const input_message = $('#input_message').val()
    // return if the user does not enter any text
    if (!input_message) {
      return
    }

    $('#chat-container').append(`
        <div class="chat-message col-md-5 human-message">
            ${input_message} 
        </div>
    `).animate({scrollTop: $('#chat-container').prop("scrollHeight")}, 500)

    // loading
    $('#chat-container').append(`
        <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
        <span id="wait">.</span>
        <script>
            const dots = window.setInterval( function() {
                const wait = document.getElementById("wait");
                if(wait != null){
                    if ( wait.innerHTML.length > 3 ) 
                        wait.innerHTML = "";
                    else 
                        wait.innerHTML += ".";
                } }, 400);
        </script>
        </div>
    `).animate({scrollTop: $('#chat-container').prop("scrollHeight")}, 500)

    // clear the text input
    $('#input_message').val('')

    // send the message
    submit_message(input_message)
});

var scroll_to_bottom = function(element){
    let new_height;
    var tries = 0, old_height = new_height = element.height();
    var intervalId = setInterval(function() {
        if( old_height !== new_height ){
            // Env loaded
            clearInterval(intervalId);
            element.animate({ scrollTop: new_height }, 'slow');
        }else if(tries >= 30){
            // Give up and scroll anyway
            clearInterval(intervalId);
            element.animate({ scrollTop: new_height }, 'slow');
        }else{
        }
    }, 100);
}

scroll_to_bottom($('#response'));