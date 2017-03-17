function ContentXBlockEditor(runtime, element) {
  $(element).find('.save-button').bind('click', function() {
    var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
    var data = {
      subtopic: $(element).find('input[name=subtopic]').val(),
      subtopic_desc: $(element).find('input[name=subtopic_desc]').val(),
      image_url: $(element).find('input[name=image_url]').val(),
      image_desc: $(element).find('input[name=image_desc]').val(),
      sim_url: $(element).find('input[name=sim_url]').val(),
      sim_desc: $(element).find('input[name=sim_desc]').val(),
      anim_url: $(element).find('input[name=anim_url]').val(),
      anim_desc: $(element).find('input[name=anim_desc]').val(),
      vid_url: $(element).find('input[name=vid_url]').val(),
      vid_desc: $(element).find('input[name=vid_desc]').val(),
      game_url: $(element).find('input[name=game_url]').val(),
      game_desc: $(element).find('input[name=game_desc]').val()
    };
    runtime.notify('save', {state: 'start'});
    $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
      runtime.notify('save', {state: 'end'});
    });
  });

  $(element).find('.cancel-button').bind('click', function() {
    runtime.notify('cancel', {});
  });
}