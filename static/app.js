var interval = 500; // 1000 = 1 second

function get_current_temperatures() {
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/current-temperatures/",
    success: function (data) {
      document.getElementById("Sera1").innerHTML = data["Sera1"];
      document.getElementById("Sera2").innerHTML = data["Sera2"];
      document.getElementById("Sera3").innerHTML = data["Sera3"];
      document.getElementById("Sera4").innerHTML = data["Sera4"];
    },
    complete: function (data) {
      setTimeout(get_current_temperatures, interval);
    },
  });
}

setTimeout(get_current_temperatures, interval);

function set_temperature(sera_name, temperature) {
  $.ajax({
    type: "POST",
    url: `http://127.0.0.1:5000/set-temperature/`,
    data: { sera_name: sera_name, temperature: temperature },
    success: function (data) {
      //
    },
    complete: function (data) {
      //
    },
  });
}

$("#formid").submit(function(event) {

  event.preventDefault();

  var $form = $(this);
  var url = $form.attr('action');

  var posting = $.post(url, {
    sera_name: $('#sera_name').val(),
    temperature: $('#temperature').val()
  });
});
