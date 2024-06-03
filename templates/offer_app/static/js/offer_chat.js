$(document).ready(function() {
    var scrolledToBottom = true;
    var offerId = document.getElementById('chat-container').getAttribute('data-offer-id');

    function refreshMessages(lastDisplayedMessageId) {
        var lastDisplayedMessageId = $('.message-box:last').attr('message-id') || 0;
        $.ajax({
            url: `/api/get-message/${offerId}/`,
            type: 'GET',
            data: { last_displayed_message: lastDisplayedMessageId }, 
            success: function(data) {
                data.messages.forEach(function(message) {
                    if (message.id > lastDisplayedMessageId) {
                        var image_url;
                        if (message.from_user.image == ''){
                            image_url='/static/img/user-profile.svg'
                        }
                        else{
                            image_url=message.image
                        }
                        var messageHtml = `
                            <div class="message-box chat-box-message__left" message-id="${message.id}">
                                <div class='message-box-header left'>
                                    <div class="message-box-header__image">
                                        <img src="${image_url}" alt="">
                                    </div>
                                    <div class="message-box-header__name">
                                        <span>${message.from_user.first_name} ${message.from_user.last_name}</span>
                                    </div>
                                </div>
                                <div class="message-box-body">
                                    <span>${message.message}</span>
                                </div>
                                <div class="message-box-footer">
                                    <div class="message-box-footer">
                                        <span class="timestamp">${message.date_sent}</span>
                                    </div>
                                </div>
                            </div>`;
                        $('.chat-messages').append(messageHtml);
                        lastDisplayedMessageId = message.id;
                        //$('.chat-messages').scrollTop($('.chat-messages')[0].scrollHeight);
                        if (scrolledToBottom) {
                            $('.chat-messages').scrollTop($('.chat-messages')[0].scrollHeight);
                        } else {
                            $('.scroll-down-btn').show();
                        }
                    }
                });
            }
        });
    }

    setInterval(function() {
        refreshMessages();
    }, 1000);
    
    $('.chat-messages').scroll(function() {
        var scrollTop = $(this).scrollTop();
        var scrollHeight = $(this)[0].scrollHeight;
        var windowHeight = $(this).outerHeight();
        scrolledToBottom = scrollTop + windowHeight >= scrollHeight;
        if (scrolledToBottom) {
            $('.scroll-down-btn').hide();
        }
    });

    $('.scroll-down-btn').click(function() {
        $('.chat-messages').scrollTop($('.chat-messages')[0].scrollHeight);
        $(this).hide();
    });
});

$(document).ready(function() {
    $('.chat-messages').scrollTop($('.chat-messages')[0].scrollHeight);
});