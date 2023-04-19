// Now When the page is ready the function will call
let prevValue = null
let table = null
let addBtn = null
$(document).ready(function () {
    prevValue = document.getElementById("id_event").value
    table = document.getElementsByClassName('table')
    clean()
    addBtn = document.getElementsByClassName('btn btn-sm btn-default float-right')


// This is will listen whenever the select option is change
    document.addEventListener("selectionchange", function (event) {
        let value = document.getElementById("id_event").value

        addBtn[0].addEventListener("click", function () {
            change(prevValue)
        });

        if (prevValue !== value) {
            prevValue = value
            change(value)
        }
    });


// Select Change Function On Add Page
    function change(value) {
        let error = false
        if (value) {
            let url = '/tickets/?event=' + value // Your API URL
            fetch(url, {
                method: 'GET',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                    'Content-Type': 'application/json'
                },
            }).then(async response => {
                if (!response.ok) {
                    error = true
                }
                return response.json();
            })
                .then(data => {
                        if (!error) {
                            let html = $.map(data, function (data) {
                                return '<option value="' + data.id + '">' + data.type + '</option>'
                            }).join('');
                            html = '<option value selected>---------</option>' + html
                            for (let i = 0; i < table[0].rows.length - 3; i++) {
                                let elementId = "id_orderticket_set-" + i + "-ticket"
                                document.getElementById(elementId).innerHTML = html // this will change the ticket options
                            }
                        } else {
                            clean()
                        }
                    }
                )
        } else {
            clean()
        }

    }

    function clean() {
        for (let i = 0; i < table[0].rows.length - 3; i++) {
            let elementId = "id_orderticket_set-" + i + "-ticket"
            document.getElementById(elementId).innerHTML = '<option value selected>---------</option>'
        }
    }


})
