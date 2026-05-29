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
    
    swal({
      title: "Are you sure?",
      text: message,
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
        // var CSRF_TOKEN = `{{ csrf_token() }}`;
        // console.log(CSRF_TOKEN);
        $.ajax({
            type: 'POST',
            url: route,
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            // data : {'_method' : 'DELETE', '_token' : CSRF_TOKEN },
            success : function(data) {
              if (route.includes('delete')) { 
                swal({
                  title: "Delete Done!",
                  text: "Your Job Was Deleted!",
                  icon: "success",
                  button: "Done",
                });
                $("#row_"+id).remove();
              }else if(route.includes('close')){
                swal({
                  title: "Done!",
                  text: "Your Job was marked closed!",
                  icon: "success",
                  button: "Done",
                });
                $("#change_job_status_"+id).html('<a class="text-white btn btn-success btn-sm" role="button">Closed</a>')
              }
            },

            error : function () {
                swal({
                    title: 'Something went wrong !',
                    // text: data.message,
                    timer: '1500'
                })
            }
        });
      } else {
        swal("Your Post Is Safe!");
      }
    });
  }
