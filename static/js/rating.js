$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault()
        $('#id_design').val('')
        $("#id_usability").val('')
        $("#id_content").val('')
    }) // End of submit event
  
  }) // End of document ready function