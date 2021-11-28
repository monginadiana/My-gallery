function shareImage(image_url) {
    navigator.clipboard.writeText(image_url)
        .then(function onSuccess() {
            alert('Successfully copied image url to clipboard');
        })
        .catch(function onError() {
            alert('unable to paste to clipboard')
        })
}
