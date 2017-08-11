$(function(){
    $("#bform").submit(function(e){
        e.preventDefault();
        var muestra = $("#muestra");
        muestra.fadeOut(10);

        $.ajax({
            url:$(this).attr("action"),
            type:$(this).attr("method"),
            dataType :'json',
            data:$(this).serialize(),
            success: function(data){
                muestra.empty();
                $("#respuesta").html("<i>Se muestran " + data.length + " resultado(s)</i><br><br>").removeClass("btn-danger").addClass("btn-success");
                $.each(data, function(i, item) {
                    muestra.append(i+1," Nombre: " + item.fields.nombre + " - Cedula: " + item.fields.cedula + "<br>");
                });
                muestra.fadeIn(500);
            }
            
        });

    });
});