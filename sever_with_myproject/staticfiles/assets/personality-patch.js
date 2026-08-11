// Runtime patch: ensure personality textareas have ids and Send_data includes them
(function() {
  function ensureIds() {
    // Find textareas in navbar that look like personality inputs
    const textareas = document.querySelectorAll('textarea');
    let p1 = null, p2 = null;
    textareas.forEach(ta => {
      const ph = (ta.placeholder || '').toLowerCase();
      if (ph.includes('ai-1') || ph.includes('ai1') || ph === 'ai-1') {
        ta.id = 'personality_1';
        p1 = ta;
      } else if (ph.includes('ai-2') || ph.includes('ai2') || ph === 'ai-2') {
        ta.id = 'personality_2';
        p2 = ta;
      }
    });
    // Fallback: first two textareas in .f-1 or .navbar
    if (!p1 || !p2) {
      const candidates = document.querySelectorAll('.f-1 textarea, .navbar textarea, .f textarea');
      if (candidates[0] && !candidates[0].id) candidates[0].id = 'personality_1';
      if (candidates[1] && !candidates[1].id) candidates[1].id = 'personality_2';
    }
  }

  // Monkey-patch fetch to inject personalities into POST bodies that look like the AI chat API
  const originalFetch = window.fetch;
  window.fetch = async function(input, init) {
    try {
      if (init && init.method && init.method.toUpperCase() === 'POST' && init.body) {
        let body = init.body;
        if (typeof body === 'string') {
          try {
            const data = JSON.parse(body);
            if (data && (data.hasOwnProperty('dafee') || data.hasOwnProperty('text_tag_input') || data.hasOwnProperty('url_1'))) {
              ensureIds();
              data.personality_1 = (document.getElementById('personality_1') || {}).value || data.personality_1 || '';
              data.personality_2 = (document.getElementById('personality_2') || {}).value || data.personality_2 || '';
              init = Object.assign({}, init, { body: JSON.stringify(data) });
            }
          } catch (e) {}
        }
      }
    } catch (e) {}
    return originalFetch.call(this, input, init);
  };

  // Also ensure ids after DOM load / React render
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => setTimeout(ensureIds, 500));
  } else {
    setTimeout(ensureIds, 500);
  }
  // Re-run periodically in case React re-renders
  setInterval(ensureIds, 2000);
})();
