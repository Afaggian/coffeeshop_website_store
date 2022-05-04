function show_pwd(button) {
    document.getElementById( 'id_password').setAttribute( 'type', 'text');
    document.getElementById("__action__id_password__show_button")
        .style.display="none";
    document.getElementById("__action__id_password__hide_button")
        .style.display=null;
;
}

function hide_pwd(button) {
    document.getElementById( 'id_password').setAttribute( 'type', 'password');
    document.getElementById("__action__id_password__hide_button")
        .style.display="none";
    document.getElementById("__action__id_password__show_button")
        .style.display=null;

}