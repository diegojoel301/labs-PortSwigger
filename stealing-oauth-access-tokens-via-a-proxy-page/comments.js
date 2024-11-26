
window.addEventListener('message', function(e) {
    if (e.data.type === 'oncomment') {
        e.data.content['csrf'] = '6f5PrHj8CtH8lvrJaLHictG3rIFFa8uU';
        const body = decodeURIComponent(new URLSearchParams(e.data.content).toString());
        fetch("/post/comment",
            {
                method: "POST",
                body: body
            }
        ).then(r => window.location.reload());
    }
}, false)