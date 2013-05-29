jQuery.noConflict()

jQuery(window).load( function () {
    var userId = null, postsUri = null;

    userId = jQuery('.vcard').attr('data-userid');
    postsUri = '/s/search.ajax?a=' + userId + '&t=0&p=1';
    jQuery('#latestPosts').load(postsUri);
});
