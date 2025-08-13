document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const checkedRadio = document.querySelector('input[name="booth_category_id"]:checked');
        const checkboxes = document.querySelectorAll('input[name="event_booth_ids"]');

        if (!checkedRadio || checkboxes.length === 0) return;

        checkboxes.forEach(cb => cb.checked = false);
        checkboxes[0]?.click();
    }, 500);
});

function _isMember() {
    let membershipValue = parseInt(document.querySelector("#partner_membership_value")?.value || "0", 10);
    let isMemberInput = document.querySelector("#is_member_input");
    if (membershipValue !== 0) {
    console.log('js loaded', isMemberInput)
    isMemberInput.value = "yes";
    } else {
        isMemberInput.value = "no";
    }
}