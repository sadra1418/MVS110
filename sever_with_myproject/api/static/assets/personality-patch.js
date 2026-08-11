(function(){
  function patch(){
    // add ids to the two personality textareas if missing
    var areas = document.querySelectorAll('.f-1-1 textarea');
    if(areas.length >= 2){
      if(!areas[0].id) areas[0].id = 'personality_1';
      if(!areas[1].id) areas[1].id = 'personality_2';
    }
    // monkey-patch fetch to inject personalities into API body
    var origFetch = window.fetch;
    window.fetch = function(url, opts){
      try{
        if(opts && opts.method === 'POST' && typeof url === 'string' && url.indexOf('/api/') !== -1 && opts.body){
          var body = JSON.parse(opts.body);
          var p1 = (document.getElementById('personality_1')||{}).value || '';
          var p2 = (document.getElementById('personality_2')||{}).value || '';
          body.personality_1 = p1;
          body.personality_2 = p2;
          opts = Object.assign({}, opts, {body: JSON.stringify(body)});
        }
      }catch(e){}
      return origFetch.call(this, url, opts);
    };
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', patch);
  else patch();
})();
