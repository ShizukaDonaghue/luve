let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', 'var(--placeholder-grey)');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', 'var(--placeholder-grey)');
    } else {
        $(this).css('color', 'var(--grey)');
    }
});