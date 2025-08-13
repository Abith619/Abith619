function _boothChange() {
    let checkedRadio = document.querySelector('input[name="booth_category_id"]:checked');
    let checkboxes = document.querySelectorAll('input[name="event_booth_ids"]');

    if (!checkedRadio || checkboxes.length === 0) return;

    setTimeout(() => {
        function processCheckboxes() {
            setTimeout(() => {
                let checkboxes = document.querySelectorAll('input[name="event_booth_ids"]');

                if (checkboxes.length > 0) {
                    checkboxes.forEach(checkbox => (checkbox.checked = false));

                    checkboxes[0]?.click();
                }
            }, 500);
        }
        if (checkboxes.length > 0) {
            processCheckboxes();
            return;
        }
    });

    setTimeout(() => {
        checkboxes[0].click();
    }, 500);
}

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