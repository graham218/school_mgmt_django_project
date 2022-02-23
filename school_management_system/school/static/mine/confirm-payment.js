function confirmPayment(pk){
    $.ajax({
        method: 'POST',
        url: '/api/simulate',
        data: {
            'booking_id':pk,
        },
        success: function (data) {
            let message = data['message'];
            let response_code = data['response_code'];
            if (response_code === 0){
                alert('payment successful');
            }else{
                let container = $('#alert-container');
                let content = `
                    <div class="alert alert-warning text-center alert-dismissible fade show" id="home-alert" role="alert">
                    <p id="home-alert-text">${message}</p>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                    </div>
                    `;
                container.html(content);
            }
        }
    });

}