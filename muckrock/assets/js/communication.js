/* communication.js
**
** This handles the logic on the communication pattern.
** It toggles the display of forms on the commmunication when targeted by the URL.
*/

function showCommForm(id) {
    if (!id) {
        return;
    }
    var form = $(id);
    $('.options.dropdown').removeClass('visible');
    $('.communication-actions').show();
    form.addClass('visible').siblings().removeClass('visible');
    form.find('button.cancel').click(function(e){
        e.preventDefault();
        $(id).removeClass('visible');
        $('.communication-actions').hide();
    });
}

var actions = $('.communication-action').map(function() {
    return '#' + $(this).attr('id');
}).get();

// Bind to hashchange event
$(window).on('hashchange', function () {
    // check if the hash is a target
    var hash = location.hash;
    if (actions.indexOf(hash) !== -1) {
        showCommForm(hash);
    }
});

showCommForm(actions.indexOf(location.hash) !== -1 ? location.hash : '');
