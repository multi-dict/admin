if (!$) {
    $ = django.jQuery;
}
console.log($("#id_languages"));


$( document ).ready(function() {
    console.log( "ready!" );
    setLanguage()
    $('#id_languages').change(function(){
        setLanguage();
    });
});
function setLanguage(){
    languages = []
    $("#id_languages").parent().find('option:selected').each(function(){
        languages.push({ 'lang' : $(this).html(), 'val' : '<option value="'+$(this).val()+'">'+$(this).html()+'</option>'});
    })
    console.log(languages);
    $('.grp-related-widget-wrapper').each(function(){
        var select = $($(this)).find('select');
        if (select.attr('id') != 'id_languages'){
            var selected = select.find('option:selected');        
            select.html('')
            select.append('<option value="">---------</option>');
            for(var i = 0;i<languages.length;i++){
                if(languages[i].lang == selected.html()){
                    select.append(selected);
                } else {
                    select.append(languages[i].val);
                }
            }
        }
    })
}