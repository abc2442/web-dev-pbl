function call_sw_alert_func(route, id, message){
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }

    function getCsrfToken() {
      return getCookie('csrftoken') || $('input[name="csrfmiddlewaretoken"]').first().val() || '';
    }
    
    swal({
      title: "Are you sure?",
      text: message,
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
        $.ajax({
            type: 'POST',
            url: route,
            headers: {'X-CSRFToken': getCsrfToken()},
            success : function(data) {
              if (route.includes('delete')) { 
                swal({
                  title: "Delete Done!",
                  text: data.message || "Item was deleted.",
                  icon: "success",
                  button: "Done",
                });
                $("#row_"+id).remove();
              }else if(route.includes('close')){
                swal({
                  title: "Done!",
                  text: data.message || "Your job was marked closed.",
                  icon: "success",
                  button: "Done",
                });
                $("#change_job_status_"+id).html('<a class="text-white btn btn-success btn-sm" role="button">Closed</a>')
              }
            },

            error : function (xhr) {
                const response = xhr.responseJSON || {};
                swal({
                    title: 'Action failed',
                    text: response.message || 'Please refresh the page and try again.',
                    icon: 'error',
                    button: 'OK'
                })
            }
        });
      } else {
        swal("Your Post Is Safe!");
      }
    });
  }
